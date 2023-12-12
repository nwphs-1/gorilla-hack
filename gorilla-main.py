import math
from pynput import keyboard

def on_press(key):
try:
print('alphanumeric key {0} pressed'.format(
key.char))
except AttributeError:
print('special key {0} pressed'.format(
key))

def on_release(key):
print('{0} released'.format(
key))
if key == keyboard.Key.esc:
# Stop listener
return False

Collect events until released
with keyboard.Listener(
on_press=on_press,
on_release=on_release) as listener:
listener.join()

stats = {}
def phase(curPhase):
if curPhase == "start":
stats = {lv, cc, vg, dx, ig, hp, ac, t}
gorillaClass = input("Chose your class: \n[1]Silverback\n[2]Youngling\n[3]Innovator\n")
lv = 1
cc = input("Chose difficulty (1-5)\n")
if gorillaClass == 1:
vg = math.random(1,12)
dx = math.random(1,8)
ig = math.random(1,6)
elif gorillaClass == 2:
vg = math.random(1,8)
dx = math.random(1,12)
ig = math.random(1,6)
elif gorillaClass == 3:
vg = math.random(1,6)
dx = math.random(1,8)
ig = math.random(1,12)
hp = 10
ac = 10
t = 0
return

def move(dir):
print('a')

def controls():
on_Press(key):
if key == "Key.up":
move(up)
elif key == "Key.left":
move(left)
elif key == "Key.right":
move(right)
elif key == "Key.down":
move(down)