#ITERATIVE VERSION
def binarySearch(array,x,low,high):
    #repeat until the pointers low and high meet each other
    while low <=high:
        mid = low+(high-low)//2
        if array[mid]==x:
            return mid
        elif array[mid] < x:
            low =mid +1

        else:
            high=mid-1

    return -1

def binary_search(arr,low,high,x):
    #check base case
    if high>=low:
        mid =(high+low)//2

        #if element is present at the middle itself
        if arr[mid] ==x:
            return mid

        #if element is smaller than mid,then it can only
        #be present in left subarray
        elif arr[mid]>x:
            return binary_search(arr,mid-1,high,x)

        #else the element can only be present in right subarray
        else:
            return binary_search(arr,mid+1,high,x)

    else:
        #element is not present in binary
        return -1