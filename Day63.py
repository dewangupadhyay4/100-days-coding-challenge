list=[12,34,543,3,3,323,232,12,121,344]

def find_lar_small(list):
    largest=max(list)
    smallest=min(list)
    return largest, smallest

print(find_lar_small(list))