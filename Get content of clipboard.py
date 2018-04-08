from tkinter import Tk
import time

starttime=time.time()
time_delta = 1 #in seconds 
current_clip_content = " "

while True:
	r = Tk()
	
	new_clip_content = r.selection_get(selection = "CLIPBOARD")
	if current_clip_content != new_clip_content:
		current_clip_content = new_clip_content
		print(new_clip_content)
		file = open('clip_text.txt','a+')
		file.write(new_clip_content)
		file.close()

	
	time.sleep(time_delta - ((time.time() - starttime) % time_delta))



