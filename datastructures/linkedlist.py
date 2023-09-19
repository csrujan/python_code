# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.length = 1
#         self.head = new_node
#         self.tail = new_node
#
#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1
#
#     def print_node_value(self):
#         i = self.head
#         while i:
#             print(i.value, end=" ")
#             i = i.next
#
#     def prepend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.length += 1
#
#     def insert(self, pos, val):
#         new_node = Node(val)
#         if self.length == 0 and pos == 0:
#             self.head = self.tail = new_node
#         elif 0 < pos < self.length:
#             temp = self.head
#             for _ in range(pos-1):
#                 temp = temp.next
#             post = temp.next
#             temp.next = new_node
#             new_node.next = post
#             if pos == 0:
#                 self.head = new_node
#         self.length += 1
#
#
# l1 = LinkedList(3)
# l1.append(1)
# l1.append(2)
# l1.prepend(5)
# l1.insert(0, 5)
# l1.print_node_value()
#
#
class Student:
    def __init__(self,name,id,age):
        self.name = name;
        self.id = id;
        self.age = age
    def display_details(self):
        print("Name:%s, ID:%d, age:%d"%(self.name,self.id))
s = Student("John",101,22)
print(s.__doc__)
print(s.__dict__)
print(s.__module__)