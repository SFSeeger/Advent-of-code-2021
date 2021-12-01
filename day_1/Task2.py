data = []
depth = 0
with open("input") as f:
    data = f.readlines()
for index, d in enumerate(data):
    try:
        tri_1 = int(d.replace('\n',''))+int(data[index+1].replace('\n',''))+int(data[index+2].replace('\n',''))
        tri_2 = int(data[index+1].replace('\n',''))+int(data[index+2].replace('\n',''))+int(data[index+3].replace('\n',''))
        depth += 1 if tri_2-tri_1 > 0 else 0
    except Exception:
        pass
print(depth)
