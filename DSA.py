# Write a Python program to merge two dictionaries and sum the values of common keys.


def merge(dict1, dict2):
    dic1 = dict1.copy()
    
    for key , val in dict2.items():
        if key in dic1:
            dic1[key] = dic1[key] + val;
        else:
            dic1[key] = val
            
    return dic1

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}

mergedDict = merge(dict1, dict2)

print(mergedDict)