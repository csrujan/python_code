#pickle dump
# import pickle
# a = int(input("enter number of values"))
# data=[]
# for i in range(a):
#     raw = input("enter string "+str(i)+" :")
#     data.append(raw)
#
# file1 = open("file1", "wb")
# pickle.dump(data, file1)

#pickle load
# import pickle
# file1 = open("file1", "rb")
# a = pickle.load(file1)
# print(a)

# import pickle
# data = []
# no_of_inputs = int(input("Enter Number of Inputs: "))
# for i in range(no_of_inputs):
#     data.append(input(f"Enter {i+1} value: "))
#
# file1 = open("file1", "wb")
# pickle.dump(data, file1)

import pickle
a = open("file1", "rb")
b = pickle.load(a)
print(b)















