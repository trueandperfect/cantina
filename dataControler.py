import json,sys,csv
from collections import defaultdict

variable = sys.argv[1]
obj = json.load(sys.stdin)

def find(key, dictionary):
    for k, v in dictionary.items():
        if k == key and variable in str(v):
            yield v
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                if isinstance(d, dict):
                    for result in find(key, d):
                        yield result
                        


print(" ")
print("class Results:")
print(list(find("class", obj)))
print(" ")

print("classNames Results:")
print(list(find("classNames", obj)))
print(" ")


print("identifier Results:")
print(list(find("identifier", obj)))
print(" ")

