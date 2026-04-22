string1= input("Enter numbers separated by comma")
l1=string1.split(',')
l2=[]
for x in l1:
    l2.append(int(x))
l1=l2
print(l1)


