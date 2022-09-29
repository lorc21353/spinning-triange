# spinning-triange
python code for a spinning triangle 





----------------------------------------------------------------------------------------------
explaination of the radian maths and my thought process behind it 
----------------------------------------------------------------------------------------------

polygon[0] = (70.711*cos(i))+centerx
polygon[1] = (70.711*sin(i))+centery
polygon[2] = (70.711*cos(i+((pi*2)/3)))+centerx
polygon[3] = (70.711*sin(i+((pi*2)/3)))+centery
polygon[4] = (70.711*cos((i+(pi*4)/3)))+centerx
polygon[5] = (70.711*sin((i+(pi*4)/3)))+centery

firstly the theory behind it 
polygon is the name of an array which contains the x and y coords of the polygon which i am rotating, therefore i have to move the coords inside of it in order to draw a polygon in the correct new position. in order to find the new position i use the formula for tracing the edge of a circle, the foruma is as follows:
x = radius*sin(radians)+offset
y = radius*cos(radians)+offset
in my code the sin and cos are flipped, all that this does is change the rotation between clockwise and anti-clockwise, in other-words it doesnt really matter
the offset is just how far away the circle is from x=0, y=0  


secondly why it is written like that
the reason it was written like that is because it makes more sense to read, i could have made the code a few lines shorter by doing all of the math entirely based off of the center-point and radius with a nested for loop but that would not have been worth the tradeoff in terms of time investment to results


thirdly what is going on with the radians section
the radians section of the maths may look very complicated or very simple depending on how much you know about radians already 
basically a radian is a way of measuring rotations similar to degrees, the main difference is that radians use π as their unit and 2π is a full rotation 
i is just the inital radians, it is equivalent to the degrees variable just in radians form 
2π/3 is just a third of a rotation 
4π/3 is two thirds of a rotation 
so what i am doing in the radians section is placing the initial point and then in the points after it adding a third of a rotation and then two thirds of a rotation respectively
this leads to the effect of creating an equilateral triangle as all of the points are a third of a rotation away from eachother on the imaginary circle surrounding the triangle 


fourthly putting it all together 
take the first value from polygon which is an x, then set it to the next point on the circumfrence of the circle by finding the point on the circle using the formula from earlier
then take the next value from polygon which is a y, get the next value on the circumfrence using the formula and set the value in the list to it 
repeat these steps for the remaining amount of points adding the rotation between them each time until you reach the end of the array/polygon 


i hope this made at least some sense and i didnt make the explaination too complex 
