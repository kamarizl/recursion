import csv

dataList = []

with open('export.csv','r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        dataList.append(row)

# list of the ids
id = [ x['PID'] for x in dataList ]

# unique list of parent id
pid = list(set([x['Parent PID'] for x in dataList ]))

nodes = [ x['Parent PID'] for x in dataList if x['Parent PID'] not in id ]
parents = [ x for x in dataList if x['Parent PID'] in nodes ]

# recursive function
def get_child(parent, indent=0):
    if parent['PID'] not in pid:
        # base condition is when the id is not parent to any ids
        return
    
    else:
        # recursive case
        childs = [x for x in dataList if x['Parent PID'] == parent['PID']]
        for child in childs:
            print("-" * indent + ":", child['Process Name'], child['Command Line'])
            get_child(child, indent + 2)

            
for parent in parents:
    print(">",parent['Process Name'], parent['Command Line'])
    get_child(parent, indent=2)
