# PageRank Engine

This is for our Discrete Mathematics Project!
We are basically explaining how and why Discete Mathematics is used for pagerank and is presented in such a way so that that is covers many discrete mathematics topics, such as graph theory, linear algebra, probability, and more.

A comprehensive PageRank analysis tool with interactive visualization capabilities. This project implements the PageRank algorithm from scratch using NumPy and provides both command-line analysis and graphical visualization using Tkinter.

## What is PageRank?

PageRank is the algorithm originally developed by Google founders to rank web pages in search results. It works by:
- Analyzing the link structure of a graph (web pages and their connections)
- Calculating the probability that a random walker will visit each node
- Assigning higher scores to nodes that are linked to by important nodes

## Features

- **Custom PageRank Implementation**: Built from scratch using NumPy matrix operations
- **Interactive Visualizer**: Beautiful graph visualization with colorful nodes and edges
- **Multiple Graph Types**: Default, custom, chain, star, and complete graphs
- **Menu-driven Interface**: Easy-to-use command-line interface
- **Modular Architecture**: Clean separation of concerns across multiple modules
- **Dynamic Visualization**: Visualizer updates based on currently loaded graph

## Project Structure

```
pagerank/
├── main.py                 # Menu-driven interface
├── src/
│   ├── pagerank.py        # Core PageRank algorithm
│   ├── graph_loader.py    # Graph creation and loading functions
│   ├── utils.py           # Helper functions for visualization and formatting
│   └── pagerank_visualizer.py  # Tkinter-based graph visualizer
├── README.md
└── requirements.txt
```

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup with Virtual Environment

1. **Clone or download the project**
   ```bash
   cd pagerank
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   **Linux/Mac:**
   ```bash
   source venv/bin/activate
   ```
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python3 main.py
   ```

## Usage

### Main Menu Options

1. **Calculate PageRank (Raw Values)** - Display numerical results with rankings
2. **Launch Graph Visualizer** - Open interactive graphical visualization
3. **Load Different Graph** - Choose from various graph types:
   - Default Graph (A→B→C→D structure)
   - Create Custom Graph (user input)
   - Sample Graphs (chain, star, complete)
4. **Show Current Graph Info** - Display graph statistics
5. **Advanced Options** - Modify iterations and damping factor
6. **Exit** - Close the application

### Graph Types

- **Default Graph**: The original A→B→C→D structure from the research
- **Chain Graph**: Simple linear connection A→B→C→D
- **Star Graph**: Central node connected to all others
- **Complete Graph**: Every node connects to every other node
- **Custom Graph**: Create your own by entering edges

### Visualizer Features

- **Color-coded nodes**: Red (low PageRank) to Green (high PageRank)
- **Size-based importance**: Larger nodes have higher PageRank scores
- **Directed edges**: Arrows show link direction
- **Score display**: PageRank values shown on each node
- **Interactive controls**: Adjust iterations and refresh visualization

## Example Output

```
==================================================
PAGERANK RESULTS
==================================================
Rank   Node     Score        Percentage  
------------------------------------------------
1      C        0.387298     38.73      %
2      A        0.331196     33.12      %
3      D        0.211327     21.13      %
4      B        0.070179     7.02       %
------------------------------------------------
Total: 1.000000
==================================================
```

## Technical Details

- **Algorithm**: Implements the power iteration method for PageRank calculation
- **Damping Factor**: Default 0.85 (configurable)
- **Convergence**: Iterative approach with configurable iteration count
- **Visualization**: Circular layout with HSV color mapping
- **Architecture**: Modular design with separation of concerns

## Dependencies

- `numpy`: Matrix operations and numerical computing
- `networkx`: Graph data structures and algorithms
- `scipy`: Scientific computing utilities
- `tkinter`: GUI framework (included with Python)
- `colorsys`: Color space conversions
- `math`: Mathematical functions

## Deactivating Virtual Environment

When you're done working:
```bash
deactivate
```

## Contributing

This is an educational project demonstrating PageRank implementation and graph visualization. Feel free to extend it with additional features like:
- Export functionality for results
- More graph layout algorithms
- Web interface
- Larger graph support
- Performance optimizations



