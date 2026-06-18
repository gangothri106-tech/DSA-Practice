def IntArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a num: "))
            l1.append(n)
        except Exception as e:
            return l1
def Running_Sum(arr):
    sum=0
    for i in range(0,len(arr)):
        sum=sum+arr[i]
        arr[i]=sum
    return arr
arr=IntArr()
print("The original arr:",arr)
res=Running_Sum(arr)
print("the Running sum: ",res)