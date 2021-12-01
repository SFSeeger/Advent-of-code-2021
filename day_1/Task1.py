data = []
depth = 0
with open("input") as f:
    data = f.readlines()
for index, d in enumerate(data):
    try:
        depth += 1 if int(d.replace('\n', ''))-int(data[index-1].replace('\n','')) > 0 else 0
    except Exeption:
        pass
print(depth)
