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
    
    node_map = {}
    
    i = 0

    for node in all_nodes:
        node_map[node] = i
        i+=1


    if not n:
        return {} # If there are no nodes return nothing
    
    voteMatrix = np.zeros((n, n))

    for j_node in g.nodes():
        out_degree = g.out_degree(j_node)
        
        if out_degree > 0:
            for i_node in g.successors(j_node):

                i = node_map[i_node]
                j = node_map[j_node]

                voteMatrix[i,j] = 1.0 / out_degree


    print("Vote Matrix")
    print(voteMatrix, '\n')



    scoreMatrix = np.ones(n)/n


    baseRankVector = np.ones(n) * ((1-d)/n) # Just a calculated guess what if the user gets bored and don't go through one of the links and rather jumps to a random page (Its a escape route that also helps in completing the probability equation)
    

    print (f"\nDoing {rounds} interations\n")

    for i in range(rounds): # The reason we go through multiple iterations is because its like the what comes first egg or chicken puzzle The score of A depend of C and score of C depend on A so as we go thorugh many iteration the value gets closer and closer to to the value it is supposed to be. Also a quick note as soon as the score start not to change by very much we should stop the iterations.

        scoreMatrix = baseRankVector + d * (voteMatrix @ scoreMatrix)

    print("Complete! The interations are done!\n")

    pagerank = {}

    for node in node_map:
        i = node_map[node]

        score = scoreMatrix[i]

        pagerank[node] = score

    return pagerank













