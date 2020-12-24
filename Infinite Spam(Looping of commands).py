import pyautogui
import time
# pyautogui is importing commands (pyautogui.write) and (pyautogui.press) its library.
#def Neverendingspam(): is the function that the spamming script is in.
def Neverendingspam():
    time.sleep(5)
    #time.sleep value amount ->(5) is the duration before the script starts running this amount can be changed.
    Set= 1
    #while Set == 1: Below is saying that while the value of the Set variable is equal to 1 then it runs the code after
    while Set == 1:
     pyautogui.write("Sentence 1 ")
     pyautogui.press('enter')
     pyautogui.write("Sentence 2")
     pyautogui.press('enter')
     pyautogui.write("Sentence 3")
     pyautogui.press('enter')
     pyautogui.write("Sentence 4")
     pyautogui.press('enter')
     pyautogui.write("Sentence 5")
     pyautogui.press('enter')
     # The text thats between the ("") after each pyautogui.write  command can be changed to anything aslong as its between ("").
Neverendingspam()