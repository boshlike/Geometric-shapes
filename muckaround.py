values = [(1,2,3), (4,5,6)]
values = [item for sublist in values for item in sublist] # List comprehenstion thats flattens
print(values)