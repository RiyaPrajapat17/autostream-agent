from langgraph.graph import StateGraph
from agent.intents import detect_intent
from agent.rag import KnowledgeBase
from agent.tools import mock_lead_capture
from agent.state import AgentState

kb = KnowledgeBase()

def agent_node(state: AgentState):
    user_msg = state["messages"][-1]

    # =====================================================
    # 🔒 LEAD CAPTURE MODE (DO NOT RE-DETECT INTENT)
    # =====================================================
    if state.get("intent") == "HIGH_INTENT_LEAD":

        if not state.get("name"):
            state["name"] = user_msg
            return {
                "messages": state["messages"] + [
                    "Thanks! Could you share your email address?"
                ]
            }

        if not state.get("email"):
            state["email"] = user_msg
            return {
                "messages": state["messages"] + [
                    "Which platform do you create content on? (YouTube, Instagram, etc.)"
                ]
            }

        if not state.get("platform"):
            state["platform"] = user_msg
            mock_lead_capture(
                state["name"],
                state["email"],
                state["platform"]
            )
            return {
                "messages": state["messages"] + [
                    "🎉 You're all set! Our team will contact you shortly."
                ]
            }

    # =====================================================
    # 🔍 NORMAL INTENT DETECTION
    # =====================================================
    intent = detect_intent(user_msg)
    state["intent"] = intent

    if intent == "CASUAL_GREETING":
        return {
            "messages": state["messages"] + [
                "Hi! How can I help you with AutoStream today?"
            ]
        }

    if intent == "PRODUCT_INQUIRY":
        answer = kb.retrieve(user_msg)
        return {
            "messages": state["messages"] + [answer]
        }

    if intent == "HIGH_INTENT_LEAD":
        return {
            "messages": state["messages"] + [
                "Great! May I have your name?"
            ]
        }

    return {
        "messages": state["messages"] + [
            "I can help with AutoStream pricing, plans, refunds, or support. What would you like to know?"
        ]
    }

graph = StateGraph(AgentState)
graph.add_node("agent", agent_node)
graph.set_entry_point("agent")
graph.set_finish_point("agent")

app = graph.compile()
