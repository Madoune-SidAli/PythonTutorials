#install pyautogui package
import pyautogui

print(pyautogui.position())          #get position of input
pyautogui.click(246,50)

#Tap in position hello world and click enter
pyautogui.write("hello world!")
pyautogui.write(["enter"])

#Copy the url of page and open new ongle and paste it there
pyautogui.hotkey("ctrl","c")
pyautogui.hotkey("ctrl","t")
pyautogui.click(246,5)
pyautogui.hotkey("ctrl","v")
pyautogui.write(["enter"])

# #Exercise:open the txt file that is in the following order: test \ testin \ testinin \ testininin \ text.txt
# #Point(x=577, y=25)
pyautogui.click(577,25)
pyautogui.write(["enter"])
pyautogui.write(["enter"])
# #file test open
# pyautogui.write(["down"])
# pyautogui.write(["enter"])
# #file testin open
# pyautogui.write(["down"])
# pyautogui.write(["enter"])
# #file testinin open
# pyautogui.write(["down"])
# pyautogui.write(["enter"])
# #file testininin open
# pyautogui.write(["down"])
# pyautogui.write(["enter"])
# #file testinininin open
# pyautogui.write(["down"])
# pyautogui.write(["enter"])
# #file text open
# pyautogui.write(["down"])
# pyautogui.write(["enter"])

#Sol with for loop
for i in range(5):
    pyautogui.write(["down"])
    pyautogui.write(["enter"])

