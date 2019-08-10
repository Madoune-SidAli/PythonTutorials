import pyautogui

# print(pyautogui.size())                   # current screen resolution width and height
# print(pyautogui.position())               # current mouse x and y
# print(pyautogui.onScreen(500, 500))       # True if x & y are within the screen.
# pyautogui.PAUSE = 2                       # Set up a 2 second pause after each PyAutoGUI call:
#
# #Mouse Functions:
#
# pyautogui.moveTo(x, y, duration=num_seconds)  # move mouse to XY coordinates over num_second seconds
# pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)  # move mouse relative to its current position
#
# pyautogui.dragTo(x, y, duration=num_seconds)  # drag mouse to XY
# pyautogui.dragRel(xOffset, yOffset, duration=num_seconds)  # drag mouse relative to its current position

pyautogui.rightClick(x=200, y=300)