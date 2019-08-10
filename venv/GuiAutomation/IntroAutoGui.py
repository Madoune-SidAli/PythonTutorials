import pyautogui


print(pyautogui.size())                   # current screen resolution width and height
print(pyautogui.position())               # current mouse x and y
print(pyautogui.onScreen(500, 500))       # True if x & y are within the screen.
pyautogui.PAUSE = 2                       # Set up a 2 second pause after each PyAutoGUI call:

#Mouse Functions:
pyautogui.moveTo(x, y, duration=num_seconds)  # move mouse to XY coordinates over num_second seconds
pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)  # move mouse relative to its current position

pyautogui.dragTo(x, y, duration=num_seconds)  # drag mouse to XY
pyautogui.dragRel(xOffset, yOffset, duration=num_seconds)  # drag mouse relative to its current position

pyautogui.rightClick(x=moveToX, y=moveToY)    #go to XY and rightClick
pyautogui.middleClick(x=moveToX, y=moveToY)
pyautogui.doubleClick(x=moveToX, y=moveToY)
pyautogui.tripleClick(x=moveToX, y=moveToY)

pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY)
print(pyautogui.position())
pyautogui.click(1341,331)
pyautogui.scroll(10)                # scroll up 10 "clicks"
pyautogui.scroll(-10)      # scroll down 10 "clicks"

pyautogui.scroll(10, x=1341, y=331)  # move mouse cursor to 100, 200, then scroll up 10 "clicks"

pyautogui.hscroll(10)    # scroll right 10 "clicks"
pyautogui.hscroll(-10)   # scroll left 10 "clicks"

pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')
pyautogui.mouseUp(x=moveToX, y=moveToY, button='left')

#Keyboard Functions
pyautogui.typewrite('Hello world!\n', interval=1.0)  #write message with 1 sec between keys
pyautogui.hotkey('ctrl', 'c')       # ctrl-c to copy
pyautogui.hotkey('ctrl', 'v')       # ctrl-v to paste
pyautogui.keyDown(key_name)
pyautogui.keyUp(key_name)

#The press() Functions
pyautogui.press('enter')  # press the Enter key
pyautogui.press('f1')     # press the F1 key
pyautogui.press('left')   # press the left arrow key

#Message Box Functions
pyautogui.alert('This displays some text with an OK button.')
pyautogui.confirm('This displays text and has an OK and Cancel button.')
pyautogui.prompt('This lets the user type in a string and press OK.')

#Screenshot Functions
pyautogui.screenshot()             # returns a Pillow/PIL Image object
pyautogui.screenshot('foo.png')      #returns a Pillow/PIL Image object, and saves it to a file


