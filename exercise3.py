import math;

#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
"""
age = 10
height = 179.9
complex = 1j

base = input("Enter base:")
height = input("Enter Height:")
area = 0.5 * int(base) *  int(height)
print("The area of triangle is ",math.ceil(area))
"""
#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
"""
side_a = int(input("Enter side a:"))
side_b = int(input("Enter side b:"))
side_c = int(input("Enter side c:"))
perimeter = side_a + side_b + side_c
print("The perimeter of the triange is ",perimeter);
"""

#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
"""
length = int(input("Enter length:"))
width = int(input("Enter Width:"))
area = length * width
perimeter = (2 * (length + width))
print("The area of the rectangle is ",area);
print("The perirmeter of the rectangle is ",perimeter)
"""

"""
#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r = int(input("Enter radius:"))
area = (math.pi) * r * r
circumference = 2 * (math.pi) * r

print("Area of the circle is ",area);
print("Circumference of the circle is ",circumference)
"""

"""
#Calculate the slope, x-intercept and y-intercept of y = 2x -2

#we need to find
#the slope
#the x intercept 
#the y intercept

#y = 2x -2 -> given equation form
#y = mx + b -> converted
#so mx = 2x and b = -2


#in this problem slope is 2 (the number near the x)
mx = 2 #slope
b = -2


#we put it inside the parenthesis so that
y_intercept = (0,mx)

#just reverses the sign of b from -2 turns it into 2
#! BY default the result of division in python is double
x_value = -b / mx
x_intercept  = (x_value,0)

print("Slope = ",mx)
print("Y Intercept = ", y_intercept)
print("x Intercept =",x_intercept)
#-b means flip the sign of whatever b is from positive to negative
print(-b)
print(b)
"""

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

"""
x1 = 2
y1 = 3
x2 = 6
y2  = 6

#solution for slope problem
up_down = y2 - y1
left_right  = x2 - x1
slope = up_down / left_right

#solution for euclidean distance problem
euclidean = math.sqrt((x2 - x1 ) ** 2  + (y2 - y1) ** 2);

print("Slope is ",math.ceil(slope))
print("Euclidean distance is ", math.ceil(euclidean))
"""

#Compare the slopes in tasks 8 and 9.
"""
task_8_slope  = 2;
task_9_slope = 2;

print("(Task 8 Slope : ",task_8_slope,")-"," (Task 9 Slope : ",task_9_slope,") = ",(task_8_slope - task_9_slope))
"""


#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = -3
y = x**2 + ((6*x) + 9)
print("To Zero = ",y);


