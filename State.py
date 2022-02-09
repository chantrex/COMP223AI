'''
@author: Devangini Patel
'''

from GraphData import *

class State:
    '''
    This class retrieves state information for social connection feature
    '''
    
    def __init__(self, name = None, name2 = None):
        if name == None:
            #create initial state
            self.name = self.getInitialState()
            self.name2 = self.getInitialState()
        else:
            self.name = name
            self.name2 = name2
    
    def getInitialState(self):
        """
        This method returns me.
        """
        #initialState = "Christopher"
        return initialState


    def successorFunction(self):
        """
        This is the successor function. It finds all the persons connected to the
        current person
        """
        return connections[self.name]
        
        
    def checkGoalState(self):
        """
        This method checks whether the person is Jill.
        """ 
        #check if the person's name is Jill
        return finalState
        #return self.name == "Frank"