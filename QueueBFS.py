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

    #you can print the content of the queue
    while len(queue) > 0:
        
        #get first item in queue
        currentNode = queue.popleft()

        #check if this is goal state :: return 1
        if currentNode.state.name == person2:
            print ("reached goal state")
            print ("----------------------")
            print ("This is the Path that tou need to follow for mmeeting too ", person2)
            currentNode.printPath()
            print ("----------------------")
            print ("Tree")
            root.printTree()
            return 1
            break
        
        # Try to find if friend exists
        try:
            childStates = currentNode.state.successorFunction()
        except:
            # Does not exist the first friend :: return 2
            print ("Frien does not exist")
            print ("----------------------")
            print ("Tree")
            root.printTree()            
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
    #Does not exist relation to goal frined :: return 3
    print ("Tree")
    root.printTree()  
    return 3

graphX = "Graph"
option = 0
while option != 1:
    person1 = input("Please, Introduce your origin person : ")
    person2 = input("Please, Introduce your goal person : ")
    option = BFS_christopher(graphX, person1, person2)
    if option == 1:
            print ("You find the way to meet :", person2)
    if option == 2:
            print ("Sorry. we can't find :", person1)
    if option == 3:
            print ("Sorry. no one knows ", person2)

print("Thank you..")


    
