import pyttsx3
import os

print()
pyttsx3.speak("Hello! Shivam, what can I do for you.")
pyttsx3.speak("You can type help for options supported.")
pyttsx3.speak("You can type exit, to leave the terminal.")

while True:
	print("Hello! Shivam, what can I do for you: ", end='')
	p = input()

	if("help" in p):
	  print("*******************************************************************")
	  print("        You can launch following apps using this interface:        ")
	  print("                           1. Notepad                              ")
	  print("                           2. Chrome                               ")
	  print("                           3. Internet Explorer                    ")
	  print("                           4. Media Player                         ")
	  print("                           5. Visual studio code                   ")
	  print("                           6. Microsoft Word                       ")
	  print("                           7. Microsoft Excel                      ")
	  print("                           8. Microsoft Power Point                ")
	  print("                           9. Sublime text                         ")
	  print("                          10. GitBash                              ")
	  print("                          11. Music Player                         ")
	  print("                          12. Camera                               ")
	  print("                          13. Map                                  ")
	  print("                          14. Calculator                           ")
	  print("                          15. Calander                             ")
	  print("                          16. Time & Date                          ")
	  print("                          17. Alarm                                ")
	  print("*******************************************************************")
	  continue;
	if (("notepad" in p) or ("editor" in p) or ("Notepad" in p)) and (("run" in p) or ("execute" in p)):
	  pyttsx3.speak("Notepad opened.")
	  os.system("notepad")
	elif (("chrome" in p) or ("browser" in p) or ("Chrome" in p)) and (("run" in p) or ("execute" in p)):
	  pyttsx3.speak("Chrome opened.")
	  os.system("chrome")
	elif (("explorer" in p) or ("edge" in p) or ("internet" in p)) and (("run" in p) or ("execute" in p)):
	  pyttsx3.speak("Internet explorer opened.")
	  os.system("start microsoft-edge:")
	elif (("media" in p) or ("player" in p) or ("Player" in p) or ("Media" in p)) and (("run" in p) or ("execute" in p)):
	  pyttsx3.speak("Media player opened.")
	  os.system("wmplayer")
	elif (("code" in p) or ("visual" in p) or ("studio" in p) or ("Visual" in p) or ("Studio" in p)) and (("run" in p) or ("execute" in p)):
	  pyttsx3.speak("Visual studio code opened.")
	  os.system("code")
	elif (("microsoft" in p) or ("word" in p)or ("Word" in p)) and (("run" in p) or ("execute" in p)):
	  pyttsx3.speak("Microsoft word opened.")
	  os.system("EXCEL.EXE")
	elif (("microsoft" in p) or ("excel" in p)or ("Excel" in p)) and (("run" in p) or ("execute" in p)):
	  pyttsx3.speak("Microsoft excel opened.")
	  os.system("WINWORD.EXE")
	elif (("microsoft" in p) or ("powerpoint" in p) or ("ppt" in p) or ("PowerPoint" in p)) and (("run" in p) or ("execute" in p)):
	  pyttsx3.speak("Microsoft power point opened.")
	  os.system("POWERPNT.EXE")
	elif (("sublime" in p) or ("text" in p) or ("SublimeText" in p)) and (("run" in p) or ("execute" in p)):
	  pyttsx3.speak("Sublime text opened.")
	  os.system("sublime_text")
	elif (("bash" in p) or ("git" in p) or ("GitBash" in p)) and (("run" in p) or ("execute" in p)):
	  pyttsx3.speak("GitBash opened.")
	  pyttsx3.speak("Type exit, to close git bash terminal.")
	  os.system("bash")
	elif (("music" in p) or ("song" in p) or ("Music" in p)) and (("run" in p) or ("execute" in p) or ("play" in p)):
	  pyttsx3.speak("Music player opened.")
	  os.system("start mswindowsmusic:")
	elif ("camera" in p) and (("run" in p) or ("execute" in p) or ("show" in p)):
	  pyttsx3.speak("Camera opened.")
	  os.system("start microsoft.windows.camera:")
	elif (("map" in p) or ("location" in p)) and (("run" in p) or ("execute" in p) or ("show" in p)):
	  pyttsx3.speak("Map opened.")
	  os.system("start bingmaps:")
	elif (("calculator" in p) or ("Calculator" in p)) and (("run" in p) or ("execute" in p)):
	  pyttsx3.speak("Calculator opened.")
	  os.system("start calculator:")
	elif (("calender" in p) or ("Calender" in p)) and (("run" in p) or ("execute" in p) or ("show" in p)):
	  pyttsx3.speak("Show calender.")
	  os.system("start outlookcal:")
	elif (("time" in p) or ("date" in p) or ("Time" in p) or ("Date" in p)) and (("run" in p) or ("execute" in p) or ("show" in p)):
	  pyttsx3.speak("Show time & date.")
	  os.system("timedate.cpl")
	elif (("alarm" in p) or ("clock" in p))and (("run" in p) or ("execute" in p) or ("show" in p) or ("set" in p)):
	  pyttsx3.speak("Set alarm")
	  os.system("start ms-clock:")
	elif ("exit" in p) or ("quit" in p):
	  pyttsx3.speak(" Thanks for using. Program exited.")
	  break
	else:
          pyttsx3.speak("Option not available.")
          print("Option not available.")
