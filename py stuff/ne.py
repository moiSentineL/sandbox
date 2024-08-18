import random
with open("new", "w") as f: 
    for _ in random.sample([file for file in open("py stuff/needs_work.txt", "r")], 20): f.write(_) 