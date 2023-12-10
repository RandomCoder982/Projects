import pyautogui
import time
import math

# print(pyautogui.size()) Size(width=1920, height=1200)

dur = 0.001
sleep = 0
x = 50
y = x/3


# Uncomment To Draw Cube #
# #Distance Between Squares
# DBS = (x, y)

# time.sleep(sleep)

# #Make Initial Square
# py.dragRel(1, 0, duration=dur)
# py.dragRel(100, 0, duration=dur)
# py.dragRel(0, 100, duration=dur)
# py.dragRel(-100, 0, duration=dur)
# py.dragRel(0, -100, duration=dur)

# #Move Position to slightly infront
# py.moveRel(DBS[0], DBS[1])

# #Make Second Square
# py.dragRel(1, 0, duration=dur)
# py.dragRel(100, 0, duration=dur)
# py.dragRel(0, 100, duration=dur)
# py.dragRel(-100, 0, duration=dur)
# py.dragRel(0, -100, duration=dur)

# #Connect The Squares To Make A 3D Image
# py.dragRel(-DBS[0],-DBS[1], duration=dur)
# py.moveRel(0,100, duration=dur)
# py.dragRel(DBS[0], DBS[1], duration=dur)
# py.moveRel(100, 0, duration=dur)
# py.dragRel(-DBS[0], -DBS[1], duration=dur)
# py.moveRel(0,-100, duration=dur)
# py.dragRel(DBS[0], DBS[1], duration=dur)


# Set the center and radius of the circle
mx, my = pyautogui.position()
radius = 50  # Change this radius as needed

# Calculate points along the circumference of the circle
num_points = 5
points = [(mx + int(radius * math.cos(2 * math.pi * i / num_points)),
           my + int(radius * math.sin(2 * math.pi * i / num_points)))
          for i in range(num_points)]

# Move the mouse to the starting point
pyautogui.moveTo(points[0])

# Draw the circle by moving the mouse to each point
for point in points:
    pyautogui.dragTo(point, duration=0.0000000000000000001)  # Adjust duration as needed

# Optional: Keep the window open for some time
time.sleep(5)