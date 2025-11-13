import numpy as np
import math
import colorsys

def calculate_layout(graph, canvas_width=800, canvas_height=600):
    """Calculate node positions using a circular layout"""
    nodes = list(graph.nodes())
    n = len(nodes)
    
    if n == 0:
        return {}
    
    # Calculate center and radius
    center_x = canvas_width // 2
    center_y = canvas_height // 2
    radius = min(canvas_width, canvas_height) * 0.3
    
    positions = {}
    
    if n == 1:
        positions[nodes[0]] = (center_x, center_y)
    else:
        for i, node in enumerate(nodes):
            angle = 2 * math.pi * i / n - math.pi / 2  # Start from top
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            positions[node] = (x, y)
    
    return positions

def get_node_color(score, max_score, min_score):
    """Generate color based on PageRank score"""
    if max_score == min_score:
        normalized_score = 0.5
    else:
        normalized_score = (score - min_score) / (max_score - min_score)
    
    # Use HSV color space for beautiful gradient
    # Hue from red (0) to green (0.33) based on score
    hue = normalized_score * 0.33
    saturation = 0.8
    value = 0.9
    
    rgb = colorsys.hsv_to_rgb(hue, saturation, value)
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))

def get_node_size(score, max_score, min_score):
    """Calculate node size based on PageRank score"""
    if max_score == min_score:
        normalized_score = 0.5
    else:
        normalized_score = (score - min_score) / (max_score - min_score)
    
    min_size = 40
    max_size = 80
    return min_size + (max_size - min_size) * normalized_score

def format_scores_for_display(scores, precision=4):
    """Format PageRank scores for display"""
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    info_text = "PageRank Scores (Ranked): "
    for i, (node, score) in enumerate(sorted_scores):
        info_text += f"{node}: {score:.{precision}f}"
        if i < len(sorted_scores) - 1:
            info_text += " | "
    return info_text

def print_pagerank_results(scores):
    """Print PageRank results in a formatted way"""
    print("\n" + "="*50)
    print("PAGERANK RESULTS")
    print("="*50)
    
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    print(f"{'Rank':<6} {'Node':<8} {'Score':<12} {'Percentage':<12}")
    print("-" * 48)
    
    total_score = sum(scores.values())
    for i, (node, score) in enumerate(sorted_scores, 1):
        percentage = (score / total_score) * 100
        print(f"{i:<6} {node:<8} {score:<12.6f} {percentage:<11.2f}%")
    
    print("-" * 48)
    print(f"Total: {total_score:.6f}")
    print("="*50)
