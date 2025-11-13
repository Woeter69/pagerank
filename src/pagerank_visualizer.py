import tkinter as tk
import math
from pagerank import pagerank
from graph_loader import load_default_graph
from utils import calculate_layout, get_node_color, get_node_size, format_scores_for_display

# Global variables
canvas = None
info_label = None
iterations_var = None
graph = None
scores = None
node_positions = {}

def set_graph(input_graph):
    """Set the graph to visualize"""
    global graph
    graph = input_graph

def calculate_node_layout():
    """Calculate node positions using utils function"""
    global graph, canvas
    
    # Get canvas dimensions
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    
    if canvas_width <= 1 or canvas_height <= 1:
        canvas_width, canvas_height = 800, 600
    
    return calculate_layout(graph, canvas_width, canvas_height)



def draw_edge(start_pos, end_pos, color='#666666', width=2):
    """Draw an edge with arrow"""
    global canvas
    x1, y1 = start_pos
    x2, y2 = end_pos
    
    # Calculate arrow position (slightly before the end node)
    dx = x2 - x1
    dy = y2 - y1
    length = math.sqrt(dx*dx + dy*dy)
    
    if length > 0:
        # Shorten the line to not overlap with nodes
        factor = (length - 35) / length
        x2_adj = x1 + dx * factor
        y2_adj = y1 + dy * factor
        
        # Draw main line
        canvas.create_line(x1, y1, x2_adj, y2_adj, fill=color, width=width, smooth=True)
        
        # Draw arrowhead
        arrow_length = 15
        arrow_angle = math.pi / 6
        
        angle = math.atan2(dy, dx)
        
        # Arrow points
        ax1 = x2_adj - arrow_length * math.cos(angle - arrow_angle)
        ay1 = y2_adj - arrow_length * math.sin(angle - arrow_angle)
        ax2 = x2_adj - arrow_length * math.cos(angle + arrow_angle)
        ay2 = y2_adj - arrow_length * math.sin(angle + arrow_angle)
        
        canvas.create_polygon([x2_adj, y2_adj, ax1, ay1, ax2, ay2], 
                             fill=color, outline=color)

def visualize_graph():
    """Main visualization function"""
    global graph, canvas, scores, node_positions, iterations_var, info_label
    
    if not graph:
        return
    
    # Clear canvas
    canvas.delete("all")
    
    # Calculate PageRank scores
    try:
        iterations = int(iterations_var.get())
    except ValueError:
        iterations = 100
        
    scores = pagerank(graph, iterations)
    
    if not scores:
        return
    
    # Calculate positions
    node_positions = calculate_node_layout()
    
    # Get score statistics
    scores_values = list(scores.values())
    max_score = max(scores_values)
    min_score = min(scores_values)
    
    # Draw edges first (so they appear behind nodes)
    for edge in graph.edges():
        start_node, end_node = edge
        if start_node in node_positions and end_node in node_positions:
            start_pos = node_positions[start_node]
            end_pos = node_positions[end_node]
            draw_edge(start_pos, end_pos, '#4CAF50', 2)
    
    # Draw nodes
    for node, score in scores.items():
        if node not in node_positions:
            continue
            
        x, y = node_positions[node]
        
        # Calculate node properties
        color = get_node_color(score, max_score, min_score)
        size = get_node_size(score, max_score, min_score)
        
        # Draw node shadow
        canvas.create_oval(x - size//2 + 3, y - size//2 + 3, 
                          x + size//2 + 3, y + size//2 + 3, 
                          fill='#000000', outline='', stipple='gray50')
        
        # Draw node
        canvas.create_oval(x - size//2, y - size//2, 
                          x + size//2, y + size//2, 
                          fill=color, outline='#ffffff', width=3)
        
        # Draw node label
        canvas.create_text(x, y - 8, text=node, fill='#000000', 
                          font=('Arial', 12, 'bold'))
        
        # Draw score label (smaller and positioned inside the circle)
        score_text = f"{score:.3f}"
        canvas.create_text(x, y + 6, text=score_text, fill='#000000', 
                          font=('Arial', 7))
    
    # Update info label
    info_text = format_scores_for_display(scores)
    info_label.config(text=info_text)

def on_canvas_resize(event):
    """Handle canvas resize event"""
    # Recalculate layout and redraw after small delay
    event.widget.after(100, visualize_graph)

def create_gui():
    """Create the GUI"""
    global canvas, info_label, iterations_var
    
    root = tk.Tk()
    root.title("PageRank Graph Visualizer")
    root.geometry("1000x700")
    root.configure(bg='#1e1e1e')
    
    # Create main frame
    main_frame = tk.Frame(root, bg='#1e1e1e')
    main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Create title
    title_label = tk.Label(main_frame, text="PageRank Graph Visualization", 
                          font=('Arial', 18, 'bold'), fg='#ffffff', bg='#1e1e1e')
    title_label.pack(pady=(0, 10))
    
    # Create canvas frame
    canvas_frame = tk.Frame(main_frame, bg='#2d2d2d', relief=tk.RAISED, bd=2)
    canvas_frame.pack(fill=tk.BOTH, expand=True)
    
    # Create canvas
    canvas = tk.Canvas(canvas_frame, bg='#2d2d2d', highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    # Create info frame
    info_frame = tk.Frame(main_frame, bg='#1e1e1e')
    info_frame.pack(fill=tk.X, pady=(10, 0))
    
    # Create info label
    info_label = tk.Label(info_frame, text="", font=('Arial', 10), 
                         fg='#cccccc', bg='#1e1e1e', justify=tk.LEFT)
    info_label.pack(anchor=tk.W)
    
    # Control frame
    control_frame = tk.Frame(main_frame, bg='#1e1e1e')
    control_frame.pack(fill=tk.X, pady=(5, 0))
    
    # Refresh button
    refresh_btn = tk.Button(control_frame, text="Refresh Visualization", 
                           command=visualize_graph, bg='#4CAF50', fg='white',
                           font=('Arial', 10, 'bold'), relief=tk.FLAT, padx=20)
    refresh_btn.pack(side=tk.LEFT)
    
    # Iterations entry
    tk.Label(control_frame, text="Iterations:", fg='#cccccc', bg='#1e1e1e').pack(side=tk.LEFT, padx=(20, 5))
    iterations_var = tk.StringVar(value="100")
    iterations_entry = tk.Entry(control_frame, textvariable=iterations_var, width=10)
    iterations_entry.pack(side=tk.LEFT)
    
    # Bind canvas resize event
    canvas.bind('<Configure>', on_canvas_resize)
    
    return root, canvas

def main(input_graph=None):
    """Main function"""
    global canvas
    
    # Set the graph (use default if none provided)
    if input_graph is None:
        input_graph = load_default_graph()
    set_graph(input_graph)
    
    # Create GUI
    root, canvas = create_gui()
    
    # Initial visualization
    root.after(100, visualize_graph)  # Small delay to ensure canvas is ready
    
    # Start the GUI
    root.mainloop()

if __name__ == "__main__":
    main()
