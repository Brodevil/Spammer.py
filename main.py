import pyautogui
import time


data = input("Enter the sentance which you want to spam :\t")
times = int(input("Enter The number or times you want to spam: \t"))
if times > 500:
	conform = input(f"Make sure this is a very big number this will spam more are you conform to spame {times} times Enter [y/n] :\t")
	if conform.lower() == "y":
		print("Make sure that you have 10 sec. Put your coursor where you want to spam Okay")
		time.sleep(13)
    s = 0
		while s <= times:
		    pyautogui.typewrite(data)
		    pyautogui.press("enter")
		    s += 1
	else:
		print("Okay you had conform that you want to quite :\t")
else:
	print("Make sure that you have 10 sec. Put your coursor where you want to spam Okay")
	time.sleep(13)
	while s <= times:
	    pyautogui.typewrite(data)
	    pyautogui.press("enter")
	    s += 1
	   
