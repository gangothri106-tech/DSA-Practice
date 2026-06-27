def IntArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a num: "))
            l1.append(n)
        except Exception as e:
            return l1
def SecMax(arr):
    maxEle,maxEleIndx=-2**32,-1
    secmaxEle,secmaxEleIndx=-2**32,-1
    for i in range(len(arr)):
        if arr[i]>maxEle:
            secmaxEle,secmaxEleIndx=maxEle,maxEleIndx
            maxEle=arr[i]
            maxEleIndx=i
        elif maxEle!=arr[i]and secmaxEle<arr[i]:
            secmaxEle=arr[i]
            secmaxEleIndx=i
    return[maxEle,maxEleIndx,secmaxEle,secmaxEleIndx]
arr=IntArr()
print("The original Array is :",arr)
res=SecMax(arr)
print(f"The Maximum Element is {res[0]} at the index  {res[1]}")
print(f"The Second Largest Ele from Array is {res[2]} at the index  {res[3]}")