 '''
@author: Devangini Patel
'''
import os
from Node import Node
from State import State
from collections import deque

def BFS_christopher(graphX, person1, person2):
    """
    This function performs BFS search using a queue
    """
    #create queue
    queue = deque([]) 
    #since it is a graph, we create visited list
    visited = [] 
    #create root node
    initialState = State(person1)
#--------------------------------------------------------    
    root = Node(initialState)
    #add to queue and visited list
    queue.append(root)    
    visited.append(root.state.name)
    # check if there is something in queue to dequeue
    while len(queue) > 0:
        
        #get first item in queue
        currentNode = queue.popleft()
        
        #print (("-- dequeue --"), currentNode.state.name)
        
        #check if this is goal state
        if currentNode.state.name == person2:
            print ("reached goal state")
            #print the path
            print ("----------------------")
            print ("This is the Path that tou need to follow for mmeeting too ", person2)
            currentNode.printPath()
            bestPath = currentNode
            return False
            break
        try:
            childStates = currentNode.state.successorFunction()
        except:
            print ("Frien does not exist")
            return 2
            continue

        for childState in childStates:
            
            childNode = Node(State(childState))
            
            #check if node is not visited
            if childNode.state.name not in visited:
                
                #add this node to visited nodes
                visited.append(childNode.state.name)
                
                
                #add to tree and queue
                currentNode.addChild(childNode)
                queue.append(childNode)                        
    #print tree
    print ("----------------------")
    print ("Tree")
    root.printTree()
    return bestPath

print ("Get")
graphX = "Graph"
person1 = input("Please, Introduce your origin person : ")
person2 = input("Please, Introduce your goal person : ")
option = 0
option = BFS_christopher(graphX, person1, person2)
option


    
