def IntArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a n: "))
            l1.append(n)
        except Exception as e:
            return l1
def ReverseArr(arr):
    i=0
    j=len(arr)-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i=i+1
        j-=1
arr=IntArr()
print("the original array is :",arr)
res=ReverseArr(arr)
print("The reversed array is : ",arr)

# FINDING MISSING NUMBER

def IntArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a num: "))
            l1.append(n)
        except Exception as e:
            return l1
def MissingNum(arr):
    n=len(arr)+1
    actual_sum=n*(n+1)//2
    current_sum=0
    for i in range(len(arr)):
        current_sum=current_sum+arr[i]
    return actual_sum - current_sum
arr=IntArr()
print("the original array is : ",arr)
res=MissingNum(arr)
print("the missed number is: ",res)