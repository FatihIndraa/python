MARS_RADIUS = 3396.2 # in kilometres
PI = 3.1415927
MILES_RATIO = 1.609344 # one mile is equal to 1.609344 kilometres

print("Mars Circumference Calculation")
marsCirc = 2 * MARS_RADIUS * PI

print("The equatorial circumference of Mars is", str(round(marsCirc,3)), "km")
print("The equatorial circumference of Mars is",

str(round(marsCirc/MILES_RATIO,3)), "miles")
print("The End")