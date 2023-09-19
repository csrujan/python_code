a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]


def insertionSort(list1):
    for i in range(1, len(list1)):
        for j in range(i, 0, -1):
            if list1[j - 1] < list1[j]:
                break
            print(list1)
            print(list1[j - 1], list1[j])
            print("-----------")
            list1[j - 1], list1[j] = list1[j], list1[j - 1]
    return list1

if __name__ == "__main__":
    k = insertionSort([9, 7, 3, 1, 89, 0])
    print(k)
