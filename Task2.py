def task2(x):
    with open(x) as f:
        return json.load(f)
