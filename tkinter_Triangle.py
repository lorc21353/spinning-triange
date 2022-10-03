# import the GUI library, the time library, and the maths library
from tkinter import * 
from time import * 
from math import *

divisions = 3 # set the number of vertices in the regular polygon
polygon = [] # declare list of points of polygon

root = Tk() # create window 
root.geometry("500x300") # set window size
root.title("Spinning Polygon") # set window title 

d = 0 # degrees of rotation
for count in range(divisions):
  polygon.append(0)
  polygon.append(0)
  
centerx = 200 #center of polygon
centery = 150
canvas = Canvas(root, width = 500, height = 300) # declare canvas
center = canvas.create_polygon([centerx,centery], outline='blue', width=5) # create initial window 
poly = canvas.create_polygon(polygon, outline='gray', fill='gray', width=1) # create inital polygon
canvas.pack() # basically just finishing making the canvas, it submits the options inside to the compiler for this code im not using any optional bits 

# if i were going to make multiple spinning objects i would make this a class and then put copies inside of an array but that is way too much work for such a small project 
while True:
  sleep(0.02)
  canvas.delete(poly) # remove the old polygon
  canvas.delete(center)
  d+=1 # increment degrees
  if d == 360: # there is no point making the degrees really large so ill include a reset for it 
    d = 0
  i = d*(pi/180) # turning degrees into radians

  # improved radian maths with for loop, old one in readme file, the logic remains the same
  for count in range(len(polygon)):
    if(count % 2 != 0):
      continue
    polygon[count] = (70.711*cos(i+((pi*count)/divisions)))+centerx
    polygon[count+1] = (70.711*sin(i+((pi*count)/divisions)))+centery

  print(polygon) # print the array of points on the polygon 
  poly = canvas.create_polygon(polygon, outline='gray', fill='gray', width=1) # add the new polygon
  center = canvas.create_polygon([centerx,centery], outline='blue', width=5) # draw center point overtop of the polygon
  canvas.update() # update the canvas to draw the new pixels 
