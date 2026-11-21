list1 = input().split()
list2 = input().split()

set1 = set(list1)
set2 = set(list2)

common_elements = set1 & set2
print(len(common_elements))

