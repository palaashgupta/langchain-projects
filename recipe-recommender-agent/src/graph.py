from langgraph.graph import StateGraph

from src.nodes.normalize import run as normalize
from src.nodes.retrieve import run as retrieve
from src.nodes.format import run as format_output

def build_graph():
    g = StateGraph(dict)

    g.add_node("normalize", normalize)
    g.add_node("retrieve", retrieve)
    g.add_node("format", format_output)

    g.set_entry_point("normalize")
    g.add_edge("normalize", "retrieve")
    g.add_edge("retrieve", "format")

    return g.compile()
