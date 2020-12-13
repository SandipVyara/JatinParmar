list1= [56,89,12,3,4,2,84]
def swaplist(list1):
    first= list1.pop(0)
    last= list1.pop(-1)
    list1.insert(0,last)
    list1.append(first)
    return list1
print(swaplist(list1))
