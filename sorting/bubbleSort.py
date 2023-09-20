#        0,
def bubbleSort(list1):
    for i in range((a := len(list1)) - 1):
        for j in range(a - i - 1):
            if list1[j] > list1[j + 1]:
                #print(list1)
                #print(list1[j], list1[j + 1])
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    return list1


print(bubbleSort([9, 4, 32, 1]))
