from llm import generate_graph
from graph import visualize_knowledge_graph

if __name__ == "__main__":
    graph = generate_graph("Teach me about supply side economics")
    visualize_knowledge_graph(graph)
