import numpy as np
import scipy
import networkx as nx
import pprint # Just prints a map better

'''
'g' is the passed graph (the grpah containing the internet),

'rounds' are the number of iterations the the processing is gonna go through as we we don't what depends on what

'd' is the damping factor just a suggested value by the pagerank founders i won't fuck with it niether should you.
'''

def pagerank(g,rounds,d = 0.85):
    all_nodes = []

    for node in g.nodes():
        all_nodes.append(node) # Gets the nodes from our graph (internet) and adds it to a list

    
    n = len(all_nodes) # Basically getting hte number of nodes present

    initial_rank = 1/n # All of the nodes get the same rank using this

    if not n:
        return {} # If there are no nodes return nothing

    pagerank = {} # A map to store {node_name: rank}

    base_score = (1-d)/n # Just a calculated guess what if the user gets bored and don't go through one of the links and rather jumps to a random page (Its a escape route that also helps in completing the probability equation)
    
    for node in all_nodes:

        pagerank[node] = initial_rank # Assigning all nodes the same rank

    pprint.pprint(pagerank) # Checking if it worked

    prev_pagerank = pagerank # As we have to keep track of the previous state of our ranks

    print (f"\nDoing {rounds} interations\n")

    for i in range(rounds): # The reason we go through multiple iterations is because its like the what comes first egg or chicken puzzle The score of A depend of C and score of C depend on A so as we go thorugh many iteration the value gets closer and closer to to the value it is supposed to be. Also a quick note as soon as the score start not to change by very much we should stop the iterations.

        new_pagerank = {} # Resetting the map to store new values

        for node in all_nodes:
            links_score_total = 0 # Starting scores given by nodes will be 0 


            for link in g.predecessors(node): # Gets the nodes that are connected to our current node 
                link_rank = prev_pagerank[link] # Gets which node is it?

                out_edges = g.out_degree(link) # Gets how many edges comes to our current node

                given_score = (link_rank / out_edges) # Formula derived by the pagerank founders (A way to calculate the Link score a number represting how often a person would stumble on a page going through by links)

                links_score_total += given_score # We sum it up as there could be multiple nodes connnected to our current node

            new_pagerank[node] = (base_score + d * (links_score_total)) # Using the main formula dervied by the founders of pagerank again the base score is just a number for the probability a person would come to a page NOT through by links

        prev_pagerank =  pagerank # Giving the current data for the next iteration as current will be past for next iteration
        pagerank = new_pagerank # Given our main map 'pagerank' the scores we collected


    print("Complete! The interations are done!\n")

    return pagerank 
    

g = nx.DiGraph()

g.add_edge('A', 'B')
g.add_edge('A', 'C')

g.add_edge('B', 'C')

g.add_edge('C', 'A')
g.add_edge('C', 'D')

g.add_edge('D', 'C')


print(list(g.edges()), "\n")

final_scores = pagerank(g,100)

print(final_scores)

# Many improvements are still remaining will make the final version in numpy because the calculation was some kind of matrix multiplication (which i don't understand yet so can't work on it) This is a very premitive version using maps. Though it is premitive it still works as a pagerank but not on a higher scale. 

# As for the concepts of discrete mathematics it covers graph theory, linear algebra, and probability













