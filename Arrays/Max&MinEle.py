#MAXIMUM ELEMENT OF AN ARRAY

def IntArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a num: "))
            l1.append(n)
        except Exception as e:
            return l1
def Max_ele(arr):
    MaxEle=-2**32
    MaxEleIndx=-1
    for i in range(0,len(arr)):
        if arr[i]>MaxEle:
            MaxEle=arr[i]
            MaxEleIndx=i
    return  MaxEle,MaxEleIndx   
arr=IntArr()
print("The original arr: ",arr)
MaxEle,MaxEleIndx=Max_ele(arr)
print(f"the maximum element of a given array is {MaxEle} at the index {MaxEleIndx}")

#MINIMUM ELEMENT OF AN ARRAY

def IntArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a num: "))
            l1.append(n)
        except Exception as e:
            return l1
def Min_ele(arr):
    MinEle,MinEleIndx=2**32,-1
    for i in range(0,len(arr)):
        if arr[i]<MinEle:
            MinEle=arr[i]
            MinEleIndx=i
    return MinEle,MinEleIndx

arr=IntArr()
print("The original array is: ",arr)
MinEle,MinEleIndx=Min_ele(arr)
print(f" Minimum Element:{MinEle} at Index: {MinEleIndx} ")