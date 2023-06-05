def task6(x):
    with open(x) as f:
        return xmltodict.parse(f.read())
