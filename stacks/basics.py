testcases = int(input())
for i in range(0,testcases):
    arr = list(map(int, input().split()))
    print(arr)
    stack = []
    output = []
    for j in arr:
        if j>0:
            stack.append(j)
        else:
            if len(stack) == 0:
                pass
            else: 
                print(stack.pop() , end="")
