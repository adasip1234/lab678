def xmlwjs(x, y):
    data = task6(x)
    donejson(y, data)
    print("utworzono nowy plik .json")

def ymlwjs(x, y):
    data = task4(x)
    donejson(y, data)
    print("utworzono nowy plik .json")

def donejson(x, data):
    with open(x, "w") as f:
        f.write(json.dumps(data))
