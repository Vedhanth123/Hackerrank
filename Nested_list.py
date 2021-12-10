
"""
Python Program to create list of list using nested for loop and add some
number to all elements
case:
Enter n1 :3
Enter n2 :2
Enter no to add :5
Enter list elements
1
2
3
4
5
6
[[6, 7], [8, 9], [10, 11]]
"""

n1 = int(input("enter n1 :"))
n2 = int(input("enter n2 :"))
n3 = int(input("enter no to add :"))
list1 = []
for i in range(n1):
    list2 = []
    for j in range(n2):
        n4 = int(input())
        list2.append(n4 + n3)
    list1.append(list2)
print(list1)