# Write a Python program to read the range and display the numbers that are divisible by 3 and 5 within the range 
x = int(input())
y = int(input())
for  i  in range(x,y+1):
  if (i%3 == 0) and (i%5 == 0):
    print(i)
