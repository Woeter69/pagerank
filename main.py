#!/usr/bin/env python3
"""
PageRank Engine - Main Menu Interface
A comprehensive PageRank analysis tool with visualization capabilities
"""

import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from pagerank import pagerank
import graph_loader as gl
import utils
from pagerank_visualizer import main as run_visualizer

def print_banner():
    """Print the application banner"""
    print("\n" + "="*60)
    print("PAGERANK ENGINE - Graph Analysis Tool")
    print("="*60)
    print("Analyze web graphs and visualize PageRank scores")
    print("Built with NetworkX, NumPy, and Tkinter")
    print("="*60)

def print_main_menu():
    """Print the main menu options"""
    print("\nMAIN MENU")
    print("-" * 30)
    print("1. Calculate PageRank (Raw Values)")
    print("2. Launch Graph Visualizer")
    print("3. Load Different Graph")
    print("4. Show Current Graph Info")
    print("5. Advanced Options")
    print("6. Exit")
    print("-" * 30)

def print_graph_menu():
    """Print the graph selection menu"""
    print("\nGRAPH SELECTION")
    print("-" * 30)
    print("1. Default Graph (Original)")
    print("2. Create Custom Graph")
    print("3. Load Sample Graphs")
    print("4. Back to Main Menu")
    print("-" * 30)

def print_advanced_menu():
    """Print the advanced options menu"""
    print("\nADVANCED OPTIONS")
    print("-" * 30)
    print("1. Change Iteration Count")
    print("2. Change Damping Factor")
    print("3. Export Results to File")
    print("4. Back to Main Menu")
    print("-" * 30)

def calculate_and_display_pagerank(graph, iterations=100, damping=0.85):
    """Calculate and display PageRank results"""
    print(f"\nCalculating PageRank...")
    print(f"Iterations: {iterations}, Damping Factor: {damping}")
    
    try:
        scores = pagerank(graph, iterations, damping)
        utils.print_pagerank_results(scores)
        return scores
    except Exception as e:
        print(f"Error calculating PageRank: {e}")
        return None

def handle_graph_selection():
    """Handle graph selection menu"""
    while True:
        print_graph_menu()
        choice = input("Select option (1-4): ").strip()
        
        if choice == "1":
            graph = gl.load_default_graph()
            print("Default graph loaded")
            return graph
        elif choice == "2":
            graph = gl.load_custom_graph()
            if len(graph.nodes()) > 0:
                print("Custom graph created")
                return graph
            else:
                print("Empty graph created, loading default instead")
                return gl.load_default_graph()
        elif choice == "3":
            graph = gl.load_sample_graphs()
            return graph
        elif choice == "4":
            return None
        else:
            print("Invalid choice. Please try again.")

def handle_advanced_options(iterations, damping):
    """Handle advanced options menu"""
    while True:
        print_advanced_menu()
        choice = input("Select option (1-4): ").strip()
        
        if choice == "1":
            try:
                new_iterations = int(input(f"Enter iteration count (current: {iterations}): "))
                if new_iterations > 0:
                    iterations = new_iterations
                    print(f"Iterations set to {iterations}")
                else:
                    print("Invalid iteration count")
            except ValueError:
                print("Invalid number format")
        
        elif choice == "2":
            try:
                new_damping = float(input(f"Enter damping factor (current: {damping}): "))
                if 0 < new_damping < 1:
                    damping = new_damping
                    print(f"Damping factor set to {damping}")
                else:
                    print("Damping factor must be between 0 and 1")
            except ValueError:
                print("Invalid number format")
        
        elif choice == "3":
            print("Export feature coming soon!")
        
        elif choice == "4":
            break
        
        else:
            print("Invalid choice. Please try again.")
    
    return iterations, damping

def main():
    """Main application loop"""
    # Initialize default settings
    current_graph = gl.load_default_graph()
    iterations = 100
    damping_factor = 0.85
    
    print_banner()
    
    while True:
        print_main_menu()
        choice = input("Select option (1-6): ").strip()
        
        if choice == "1":
            # Calculate PageRank with raw values
            calculate_and_display_pagerank(current_graph, iterations, damping_factor)
        
        elif choice == "2":
            # Launch visualizer
            print("\nLaunching Graph Visualizer...")
            print("Close the visualizer window to return to menu")
            try:
                run_visualizer(current_graph)
            except Exception as e:
                print(f"Error launching visualizer: {e}")
        
        elif choice == "3":
            # Load different graph
            new_graph = handle_graph_selection()
            if new_graph is not None:
                current_graph = new_graph
                gl.display_graph_info(current_graph)
        
        elif choice == "4":
            # Show current graph info
            print("\nCURRENT GRAPH INFORMATION")
            gl.display_graph_info(current_graph)
        
        elif choice == "5":
            # Advanced options
            iterations, damping_factor = handle_advanced_options(iterations, damping_factor)
        
        elif choice == "6":
            # Exit
            print("\nThank you for using PageRank Engine!")
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select 1-6.")
        
        # Wait for user to continue
        if choice in ["1", "4"]:
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        print("Please report this issue.")


