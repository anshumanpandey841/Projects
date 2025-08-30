arr = tuple(map(int, input().split()))
temp=0 
i=0
while i > len(arr):
    for j in range(len(arr)):
        if arr[i]==arr[j]:
            print("False")
            break
        
        else:
            j=+1    
        i=+1
        print("True")
        
