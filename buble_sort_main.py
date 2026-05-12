import bubble_sort as b
elements=[]
n=int(input("Enter number of elements"))
for i in range(n):
    ele=int(input())
    elements.append(ele)
b.buble_sort(n , elements)

b.optimized_buble_sort(n , elements)

