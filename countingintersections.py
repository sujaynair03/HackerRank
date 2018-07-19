c= int(raw_input())
list_n =  raw_input().split()
d= int(raw_input())
list_b = raw_input().split()
def counter(n, b):
    count = 0
    for elem in n:
        if elem in b:
            count += 1
    return count
print (counter(list_n, list_b))
	
	