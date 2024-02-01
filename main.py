from llm import generate_graph    
from graph import visualize_knowledge_graph

graph = generate_graph("Teach me about quantum mechanics")
visualize_knowledge_graph(graph)
