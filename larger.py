def largest_number_by_two_times(nums):
    return (2*nums)
x=[]
n=int(input('enter a number:'))
for i in range(1,n+1):
    a=int(input('enter the element:'))
    x.append(a)
x.sort()
print('The elements of the list:')
print(x)
y=largest_number_by_two_times(x[-2])
if(x[-1]<y):
    print('False')
else:
    print('True')