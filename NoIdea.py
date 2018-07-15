n, m = (map(int, raw_input().split()))
list_of_numbers = (map(int, raw_input().split()))
setA = set(map(int, raw_input().split()))
setB = set(map(int, raw_input().split()))
happ = 0
for elem in list_of_numbers:
    if elem in setA:
        happ = happ + 1
    if elem in setB:
        happ = happ - 1
print(happ)