
def ref_demo(a, x):
    v = [t for t in a if t >= x]
    s = sum(v)
    return s

v = [2, 5, 3]
print(ref_demo(v, 3))