import partition as p
import sys
numbers = []
for i in range(1 , len(sys.argv)):
    numbers.append(int(sys.argv[i]))
p.partition_array(numbers)