def IntArr():
    l=[]
    while True:
        try:
            n=int(input("Enter a num: "))
            l.append(n)
        except Exception as e:
            return l
def selectionSort(arr):
    n=len(arr)
    for i in range(0,n-1):
        max_ele,curr_max_indx=-2**32,-1
        actual_indx=(n-1)-i
        for j in range(0,n-i):
            if arr[j]>max_ele:
                max_ele=arr[j]
                curr_max_indx=j
        arr[curr_max_indx],arr[actual_indx]=arr[actual_indx],arr[curr_max_indx]
arr=IntArr()
print("The original array is: ",arr)
selectionSort(arr)
print("sorted array of: ",arr)

