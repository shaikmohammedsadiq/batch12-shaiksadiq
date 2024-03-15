"""
i = 20
while i<31:
    if i==27:
        print(i)
        break
        i+=2
i = 20
while i<65:
    if i==33:
        i=i+1
        continue
    break
total_sum=0
for num in range(12, 23):
    total_sum += num
    print("the sum of numbers from 12 to 22 is:", total_sum)

i =12
sum=0
while i<=22:
    sum=sum+1
    print(sum)
    i+=1
"""
"""   
i = 20
while i<26:
    i=i+1
    print(i)

i = 20
sum=0
while i<=25:
    sum=sum+1
    print(sum)
    i+=1

i = 20
sum = 0
count = 0
while i<=30:
    sum = sum+i
    count+=1
    i+=1
    print(sum/count)
"""
rows = int(input("enter the rows:"))
cols = int(input("enter the cols:"))

for row in range(rows):
    for col in range(cols):
        print("*", end=" ")
        print()

    
      

     
