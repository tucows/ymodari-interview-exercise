import math
sum = 0

## open the file and read each line
with open('input.txt') as f:
    for line in f:
        #each astronomical unit, divide by 3, round down and subtract 2
        line1 = math.floor(int(line)/3.0) - 2
        # add the calculated fuel required to the total sum
        sum = sum + line1

print("The sum of the fuel requirements for all astronomical units between wormholes is",sum)

f.close()
