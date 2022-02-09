'''
@author: Christopher Chantres

Reference: https://www.python.org/doc/essays/graphs/
'''

#create a dictionary with all the mappings
connections = {}
connections["Christopher"] = {"George", "Frank", "Adam"}
connections["George"] = {"Christopher"}
connections["Frank"] = {"Christopher"}
connections["Adam"] = {"Christopher", "Ema", "Bob"}
connections["Ema"] = {"Adam", "Bob", "Dolly"}
connections["Bob"] = {"Adam", "Ema", "Dolly"}
connections["Dolly"] = {"Ema", "Bob"}
