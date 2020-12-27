import csv

data = []
with open('export.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

def get_child(node=None, processList=None, indent=None):
    
    # if return empty list, this is the last node
    hasChild = [ x for x in data if x['Parent PID'] == node]
    
    if len(hasChild) == 0:
        # base case
        return
    
    childs = [x for x in data if x['Parent PID'] == node ]
    
    for child in childs:
        print(" " * indent, child['Parent Name'], child['Process Name'], child['PID'], child['Parent PID'])
        pid = child['PID']
        get_child(node=pid, processList=list([child]), indent=indent+2)
    

get_child(node='8516', processList=data, indent=1)
