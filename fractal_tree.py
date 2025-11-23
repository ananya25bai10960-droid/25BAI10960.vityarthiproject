def fractal_tree(level, indent=0):
    if level == 0:
        return
    print(" " * indent + "*")
    fractal_tree(level - 1, indent + 2)
    fractal_tree(level - 1, indent + 2)
