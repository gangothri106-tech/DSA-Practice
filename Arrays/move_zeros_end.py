def IntArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a num: "))
            l1.append(n)
        except Exception as e:
            return l1
def move_zeros(arr):
    i=0
    j=0
    while i <=(len(arr)-1):
        if arr[i]!=0:
            arr[j]=arr[i]
            j+=1
        i+=1
    while j<=(len(arr)-1):
         arr[j]=0
         j+=1
    return arr
        
arr=IntArr()
print("The original array: ",arr)
print(move_zeros(arr))
