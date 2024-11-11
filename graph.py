from langgraph.graph import StateGraph, START, END
from state import State
from nodes import get_location, play_song, get_weather, find_hotels

graph_builder = StateGraph(State)

graph_builder.add_node("get_location", get_location)
graph_builder.add_node("play_song", play_song)
graph_builder.add_node("get_weather", get_weather)
graph_builder.add_node("find_hotels", find_hotels)

graph_builder.add_edge(START, "get_location")
graph_builder.add_edge("get_location", "play_song")
graph_builder.add_edge("play_song", "get_weather")
graph_builder.add_edge("get_weather", "find_hotels")
graph_builder.add_edge("find_hotels", END)

graph = graph_builder.build()
