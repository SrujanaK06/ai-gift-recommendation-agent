from langgraph.graph import StateGraph, START, END

from .state import GiftState
from .nodes import recommend_gifts


def build_gift_agent(client):
    def recommendation_node(state):
        return recommend_gifts(state, client)

    builder = StateGraph(GiftState)

    builder.add_node("recommend_gifts", recommendation_node)
    builder.add_edge(START, "recommend_gifts")
    builder.add_edge("recommend_gifts", END)

    return builder.compile()
