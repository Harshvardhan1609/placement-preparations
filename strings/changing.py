strs  = "KALKI"
# string -> list
l1 = list(strs)
print(l1)
#['K', 'A', 'L', 'K', 'I']
l1[2] = 'P'
print(l1)
# ['K', 'A', 'P', 'K', 'I']
#list -> string
l2 = "".join(l1)
print(l2)
#KAPKI