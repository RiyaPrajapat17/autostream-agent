from agent.graph import app

state = {
    "messages": [],
    "name": None,
    "email": None,
    "platform": None
}

while True:
    user_input = input("User: ")
    state["messages"].append(user_input)
    state = app.invoke(state)
    print("Agent:", state["messages"][-1])
