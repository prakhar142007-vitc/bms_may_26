
def buble_sort(n , elements):
    for i in range(n-1):
        
        for j in range(n-1-i):
            if elements[j] > elements[j+1]:
                elements[j] , elements[j+1] = elements[j+1] , elements[j]
                
        
    print(elements)
def optimized_buble_sort(n , elements):
    for i in range(n-1):
        sorted = True   
        for j in range(n-1-i):
            if elements[j] > elements[j+1]:
                elements[j] , elements[j+1] = elements[j+1] , elements[j]
                sorted = False
        if sorted:
            break
    print(elements)

'''elements=[]
n=int(input("Enter number of elements"))
for i in range(n):
    ele=int(input())
    elements.append(ele)
buble_sort(n , elements)

optimized_buble_sort(n , elements)

'''

