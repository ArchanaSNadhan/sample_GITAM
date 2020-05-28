x=[]
n=int(input('enter a number:'))
for i in range(1,n+1):
    a=int(input('enter the element:'))
    x.append(a)
x.sort()
if(x[-1]<(2*x[-2])):
    print('False')
else:
    print('True') 