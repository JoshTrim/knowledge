from graphviz import Digraph

from model import KnowledgeGraph

from wiki import get_wikipedia_url

def visualize_knowledge_graph(kg: KnowledgeGraph):
    dot = Digraph(comment="Knowledge Graph")
    url = ''
    # Add nodes
    for node in kg.nodes:
        if node.label != None:
            print(f"> Getting url for {node.label}")
            url = get_wikipedia_url(node.label)
        dot.node(str(node.id), label=f"{node.label} url={url}", color=node.color)

    # Add edges
    for edge in kg.edges:
        dot.edge(str(edge.source), str(edge.target), label=edge.label, color=edge.color)

    # Render the graph
    dot.render("knowledge_graph.gv", view=True)


