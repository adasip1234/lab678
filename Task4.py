def task4(x):
    with open(x) as f:
        return {"root": yaml.safe_load(f)}
