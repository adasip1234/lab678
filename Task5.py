def jswyml(x, y):
    data = task2(x)
    doneyml(y, data)
    print("utworzono nowy plik .yml")

def xmlwyml(x, y):
    data = task6(x)
    doneyml(y, data)
    print("utworzono nowy plik .yml")

def doneyml(x, data):
    with open(x, 'w') as f:
        yaml.dump(data, f)
