#   a113_numeric_comparison.py
#   Predict what the following code will do.
import turtle as trtl

painter = trtl.Turtle()

# your code is here
for num in range(4):
  painter.forward(50)
  painter.right(90)

for num in range(8):
  painter.forward(80)
  painter.right(45)

wn = trtl.Screen()
wn.mainloop()


