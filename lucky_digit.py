import pdb
pdb.set_trace()
num=int(input("Enter a number:"))
sum=0
while num!=0:
    remainder=num%10
    num=num//10
    sum=sum+remainder
    if sum>9 and num==0:
        num=sum
        sum=0
print(sum)