import random 
def largestNumber(n1, n2, n3): 
 largestNum = n1 
 if (n2 > largestNum): 
    largestNum = n2 
 if (n3 > largestNum): 
    largestNum = n3 
 return largestNum 
 
print("Iteration n1 n2 n3 largestNum") 
for i in range(5): 
 # for each iteration generate 3 random float numbers 
 # in interval <0, 1000>, and find/print the largest number 
 a = random.random() * 1000 
 b = random.random() * 1000 
 c = random.random() * 1000 
 largest = largestNumber(a, b, c) 
 
 aStr = str(round(a,2)).rjust(10) 
 bStr = str(round(b,2)).rjust(10) 
 cStr = str(round(c,2)).rjust(10) 
 largestStr = str(round(largest,2)).rjust(10) 
 
 print (" ", (i+1), aStr, bStr, cStr, largestStr)