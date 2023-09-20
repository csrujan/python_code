# helper function
"""
iterate over both the sorted list and which item is less add it to the new list
"""

# my try
# def merge(a, b):
#     new_list = []
#     i = 0
#     j = 0
#     while True:
#         if a[i] > b[j]:
#             new_list.append(b[j])
#             j += 1
#         else:
#             new_list.append(a[i])
#             i += 1
#         if i == len(a):
#             new_list.extend(b[j:])
#             return new_list
#         elif j == len(b):
#             new_list.extend(a[i:])
#             return new_list

def merge(a,b):
    i=0
    j=0
    new_list = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            new_list.append(a[i])
            i += 1
        else:
            new_list.append(b[j])
            j += 1
    while i < len(a):
        new_list.append(a[i])
        i+=1
    while j < len(b):
        new_list.append(b[j])
        j+=1
    return new_list



# print(merge([1,2,7,8],[3,4,5,6]))
## merge helper is being used in mergeSort
def mergeSort(a):
    if len(a) == 1:
        return a
    mid_index = int(len(a) / 2)
    left = mergeSort(a[:mid_index])
    right = mergeSort(a[mid_index:])
    return merge(left, right)


print(mergeSort([11,0,3,2,5,1,9]))
