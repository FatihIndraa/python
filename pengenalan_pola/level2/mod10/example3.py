a = 0
b = a + 1
if a > 0 or b > 0:
 a = a + 1
 b = b + 1
 print("Trace1 a =", a, "b =",b)

if a > 0 and b > 0:
 a = a + 1
 b = b + 1
 print("Trace2 a =", a, "b =",b)

x = a + b
print("Value of x: ", x)