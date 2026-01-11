from typing import TypedDict, Optional

class AgentState(TypedDict):
    intent: str
    name: Optional[str]
    email: Optional[str]
    platform: Optional[str]
    messages: list
