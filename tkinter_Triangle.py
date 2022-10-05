# import the GUI library, the time library, and the maths library
from tkinter import * 
from time import * 
from math import *
polygon = [] # declare list of points of polygon

while True:
  try:
    divisions = int(input("Input the number of vertices: ")) # set the number of vertices in the regular polygon
    if divisions < 1:
      raise("invalid number of vertices")
    break

  except:
    print("Invalid value entered\n")

while True:
  try:
    polySize = int(input("Input the size: ")) # set the size of the circle around the polygon that the polygon is being drawn on the edge of 
    break

  except:
    print("Invalid value entered\n")
for count in range(divisions):
  polygon.append(0)
  polygon.append(0)

print ("WASD to move the polygon, Q,E to change the rotation speed")
centerx = 200 #center of polygon
centery = 150
sleeplen = 0.02

def onKeyPress(event):
  global centerx
  global centery
  global sleeplen
  #print(event.char)
  if event.char == "w":
    centery-=1
  elif event.char == "s":
    centery+=1
  elif event.char == "a":
    centerx-=1
  elif event.char == "d":
    centerx+=1
  elif event.char == "q":
    sleeplen -= 0.0001
    if sleeplen <= 0:
      sleeplen = 0
    print("rotation speed =", sleeplen)
  elif event.char == "e":
    sleeplen += 0.0001
    print("rotation speed =", sleeplen)


root = Tk() # create window 
root.geometry("500x300") # set window size
root.title("Spinning Regular Polygon") # set window title 
root.bind('<KeyPress>', onKeyPress)

d = 0 # degrees of rotation

canvas = Canvas(root, width = 500, height = 300) # declare canvas
center = canvas.create_polygon([centerx,centery], outline='blue', width=5) # create initial window 
poly = canvas.create_polygon(polygon, outline='gray', fill='gray', width=1) # create inital polygon
canvas.pack() # basically just finishing making the canvas, it submits the options inside to the compiler for this code im not using any optional bits 




# if i were going to make multiple spinning objects i would make this a class and then put copies inside of an array but that is way too much work for such a small project 
while True:
  sleep(sleeplen)
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
    polygon[count] = (polySize*cos(i+((pi*count)/divisions)))+centerx
    polygon[count+1] = (polySize*sin(i+((pi*count)/divisions)))+centery

  #print(polygon) # print the array of points on the polygon 
  poly = canvas.create_polygon(polygon, outline='gray', fill='gray', width=1) # add the new polygon
  center = canvas.create_polygon([centerx,centery], outline='blue', width=5) # draw center point overtop of the polygon
  canvas.update() # update the canvas to draw the new pixels 
