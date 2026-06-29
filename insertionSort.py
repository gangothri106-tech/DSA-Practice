def IntArr():
    l1=[]
    while True:
        try:
            n=int(input("Enter a num: "))
            l1.append(n)
        except Exception as e:
            return l1
def InsertionSort(arr):
    for i in range(0,len(arr)-1):
        for j in range(i+1,0,-1):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
            else:
                break
arr=IntArr()
print("The original array is: ",arr)
InsertionSort(arr)
print("the sorted array isd: ",arr)

    
        
        
        
        