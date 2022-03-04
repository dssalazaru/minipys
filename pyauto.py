import pyautogui as auto
from time import sleep

sleep(3)

# ss = pyautogui.screenshot()
# ss.save("ss.png")

# for i in range(0,20):
#     time.sleep(1)
#     ss = pyautogui.screenshot()
#     ss.save()
# for i in range(1,5):
    # auto.moveRel(200, 0, 1)

# Screen Size
# print(auto.size())
# print(auto.position())
#auto.displayMousePosition()

# auto.moveTo(200, 200)
 
# Move mouse in square form
# auto.moveRel(200, 0, .2)
# auto.moveRel(0, 200, .2)
# auto.moveRel(-200, 0, .2)
# auto.moveRel(0, -200, .2)

# Only move and click
# x, y, times, time between click, left or right, time to move
# auto.click(300, 300, 20, .1, 'left')
# auto.click(300, 500, 20, .1, 'left')
# auto.click(500, 500, 20, .1, 'left')
# auto.click(500, 300, 20, .1, 'left', 1)

# x, y, time between click, left or right, time to move
# auto.doubleClick(300, 300, 1, 'left', 2)
'''
auto.doubleClick()
auto.tripleClick()
auto.rightClick()
auto.leftClick()
'''

# auto.scroll(500) # scroll up
# sleep(1)
# auto.scroll(-500) # scroll down
# print(str(auto.position()).split(' '))


'''
auto.mouseDown(button='left')

# Cube on left screen
# auto.moveTo(300, 500, 2)
# auto.moveTo(500, 500, 1)
# auto.moveTo(500, 300, .5)
# auto.moveTo(300, 300, .25)

# Cube on mouse
auto.moveRel(200, 0, 2)
auto.moveRel(0, 200, 1)
auto.moveRel(-200, 0, 2)
auto.moveRel(0, -200, 1)

auto.mouseUp()
'''

# ===========================================
# Spiral exercise

# print(auto.position())
# exit()
# x = 0; y = 0
# print(auto.position())

# Clear workspace
auto.leftClick(115, 110, 0, .5)
sleep(.3)
auto.leftClick(70, 180, 0, .3)
auto.leftClick(220, 180, 0, .3)
sleep(.5)
auto.moveTo(60,200, .5)
auto.mouseDown(button='left')
auto.moveTo(600,670, .5)
sleep(.5)
auto.mouseUp()
auto.typewrite(['delete'])
sleep(.5)

# Select pen
auto.doubleClick(230, 120, .3, 'left', .5)
sleep(.5)

# Start Drawing
auto.moveTo(340,420, .5)
sleep(1)
auto.mouseDown(button='left')
x, y = auto.position()
i = 0
while(y >= 220 and y <= 650):
    x, y = auto.position()
    i += 1
    n = (i*10)*-1 if (i % 2) == 0 else i*10
    auto.moveRel(n, 0, .2)
    auto.moveRel(0, n, .2)
auto.mouseUp()