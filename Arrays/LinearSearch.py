def IntArr():
    l1=[]
    try:
        while True:
            n=int(input("Enter a num: "))
            l1.append(n)
    except Exception as e:
        return l1
def LinearSearch(arr,target):
    for i in range(0,len(arr)):
        if arr[i]==target:
            return True,i
    return False,-1

arr=IntArr()
target=int(input("Enter a target : "))
flag,index=LinearSearch(arr,target)
if flag:
    print(f"The {target} found at {index} ")
if not flag:
    print(f"the {target} not found")

    
    