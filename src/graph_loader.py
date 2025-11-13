import numpy as np
import networkx as nx

def load_default_graph():
    """Load the default graph from pagerank.py"""
    g = nx.DiGraph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'C')
    g.add_edge('C', 'A')
    g.add_edge('C', 'D')
    g.add_edge('D', 'C')
    return g

def load_custom_graph():
    """Load a custom graph by user input"""
    g = nx.DiGraph()
    
    print("\n" + "="*40)
    print("CREATE CUSTOM GRAPH")
    print("="*40)
    print("Enter edges in format: source destination")
    print("Type 'done' when finished")
    print("Example: A B")
    print("-" * 40)
    
    while True:
        edge_input = input("Enter edge (or 'done'): ").strip()
        
        if edge_input.lower() == 'done':
            break
            
        try:
            parts = edge_input.split()
            if len(parts) == 2:
                source, dest = parts
                g.add_edge(source, dest)
                print(f"Added edge: {source} -> {dest}")
            else:
                print("Invalid format. Use: source destination")
        except Exception as e:
            print(f"Error: {e}")
    
    print(f"\nGraph created with {len(g.nodes())} nodes and {len(g.edges())} edges")
    return g

def load_sample_graphs():
    """Load predefined sample graphs"""
    graphs = {
        "1": {
            "name": "Simple Chain (A->B->C)",
            "graph": create_chain_graph()
        },
        "2": {
            "name": "Star Graph (Center->All)",
            "graph": create_star_graph()
        },
        "3": {
            "name": "Complete Graph (All->All)",
            "graph": create_complete_graph()
        },
        "4": {
            "name": "Default Graph (Original)",
            "graph": load_default_graph()
        }
    }
    
    print("\n" + "="*40)
    print("SAMPLE GRAPHS")
    print("="*40)
    for key, value in graphs.items():
        print(f"{key}. {value['name']}")
    print("-" * 40)
    
    choice = input("Select a graph (1-4): ").strip()
    
    if choice in graphs:
        selected = graphs[choice]
        print(f"Loaded: {selected['name']}")
        return selected["graph"]
    else:
        print("Invalid choice, loading default graph")
        return load_default_graph()

def create_chain_graph():
    """Create a simple chain graph A->B->C->D"""
    g = nx.DiGraph()
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('C', 'D')
    return g

def create_star_graph():
    """Create a star graph with center node connecting to all others"""
    g = nx.DiGraph()
    center = 'CENTER'
    nodes = ['A', 'B', 'C', 'D']
    
    for node in nodes:
        g.add_edge(center, node)
        g.add_edge(node, center)  # Bidirectional
    
    return g

def create_complete_graph():
    """Create a complete directed graph where every node connects to every other"""
    g = nx.DiGraph()
    nodes = ['A', 'B', 'C', 'D']
    
    for source in nodes:
        for dest in nodes:
            if source != dest:
                g.add_edge(source, dest)
    
    return g

def display_graph_info(graph):
    """Display information about the graph"""
    print(f"\nGraph Information:")
    print(f"Nodes: {list(graph.nodes())}")
    print(f"Edges: {list(graph.edges())}")
    print(f"Number of nodes: {len(graph.nodes())}")
    print(f"Number of edges: {len(graph.edges())}")
    
    # Show out-degrees
    print("\nOut-degrees:")
    for node in graph.nodes():
        out_deg = graph.out_degree(node)
        print(f"  {node}: {out_deg}")
