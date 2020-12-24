import pyautogui
import time
# pyautogui is importing commands (pyautogui.write) and (pyautogui.press) its library.
def Tempspam():
    #def Tempspam(): is the function that the spamming script is in.
    time(10)
    #time.sleep value amount ->(10) is the duration before the script starts running this amount can be changed.
    Counter = 1
     #for Counter in range(2): Below is saying that the value of the (Counter)=> 1 then range(2) will loop or send it the amount specified which is (2).
for Counter in range(2):
    pyautogui.write("Sentence 1")
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
