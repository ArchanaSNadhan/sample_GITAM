def largest_number_by_two_times(nums):
    return (2*nums)
x=[]
n=int(input('enter a number:'))
for i in range(1,n+1):
    a=int(input('enter the element:'))
    x.append(a)
x.sort()
y=largest_number_by_two_times(x[-2])
if(x[-1]<y):
    print('False')
else:
    print('True') 