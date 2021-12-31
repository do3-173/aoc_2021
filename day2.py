def prvi_dio():
    f = open("input/2.txt", "r")
    depth=height=0
    for x in f:
      data=x.split()
      if(data[0]=="forward"):
          height+=int(data[1])
      if (data[0]=="down"):
          depth += int(data[1])
      if(data[0]=="up"):
          depth-=int(data[1])
    return (depth*height)

def drugi_dio():
    f = open("input/2.txt", "r")
    depth = height = poz = 0
    for x in f:
        data = x.split()
        if (data[0] == "forward"):
            height += int(data[1])
            depth += int(data[1]) * poz
        if (data[0] == "down"):
            poz += int(data[1])
        if (data[0] == "up"):
            poz -= int(data[1])
    return (depth * height)

print(prvi_dio())
print(drugi_dio())