# Anagram

def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    if len(s1) == 0:
        return True
    m1 = min(s1)
    m2 = min(s2)
    if m1 != m2:
        return False
    s1 = s1.replace(m1, '')
    s2 = s2.replace(m2, '')
    return anagram(s1, s2)

print(anagram('hello', 'oellh'))

# FInd the second largest element

arr = [1, 2, 3, 4, 5, 6, 7, 88, 44, 33, 56, 66]


def sec_largest(arr, index=0, large=0, sec=0):
    if index == len(arr):
        return sec
    if arr[index] > large:
        sec = large
        large = arr[index]
    elif arr[index] > sec and arr[index] != large:
        sec = arr[index]
    return sec_largest(arr, index + 1, large, sec)


print(sec_largest(arr))

# Find large element

arr = [1, 2, 3, 4, 5, 6, 7, 88, 44, 33, 56, 66]


def largerst_element(arr, index=0, large=0):
    if index == len(arr):
        return large
    if arr[index] > large:
        large = arr[index]
    return largerst_element(arr, index + 1, large)


print(largerst_element(arr))