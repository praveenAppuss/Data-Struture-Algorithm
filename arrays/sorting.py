def merge_sorting(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sorting(arr[:mid])
    right=merge_sorting(arr[mid:])
    return merging(left,right)
def merging(left,right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]>right[j]:
            result.append(right[j])
        else:
            result.append(left[i])
    result.extend(left[i:])
    result.extend(right[j:])
    return result
arr=[3,2,5,6,77,4,55,12]
print(merge_sorting(arr))


def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]
        print(left_arr)
        print(right_arr)
        # recursion
        merge_sort(left_arr)
        merge_sort(right_arr)
        i = 0  # left array idx
        j = 0  # right array idx
        k = 0  # merged array idx
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


arr = [3, 2, 5, 6, 77, 4, 55, 12]
merge_sort(arr)
print(arr)