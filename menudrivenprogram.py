import pyttsx3
import os
import webbrowser as wb
import wikipedia
import psutil


while True:
    print("How may I help you Ma'am ?")
    pyttsx3.speak("How may I help you Ma'am ?")
    query = input("")

    # Below Conditions open chrome browser we can open any website with TLDs as .com
    if ("chrome" in query) or ("browser" in query):
        Chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        print("What do you want to open in chrome browser?")
        pyttsx3.speak("What do you want to open in chrome browser?")
        requirement = input("")
        print("Opened successfully...")
        wb.get(Chromepath).open_new_tab(requirement + '.com')
        pyttsx3.speak("Opened successfully")



    # It opens playlist. and plays the 1st song of the playlist.
    elif ("play" in query) or ("song" in query) or ("music" in query):
        song_dir = "C:/Users/chavan aarti/Music"
        song = os.listdir(song_dir)
        os.startfile(os.path.join(song_dir, song[1]))
        print("Task executed")
        pyttsx3.speak("Task executed")
        
        

    # It open the wikipedia and give option to search particuler topic
    elif "wikipedia" in query:
        print("What do you want to search ?")
        pyttsx3.speak("What do you want to search ?")
        query = input("")
        print("Searching...")
        pyttsx3.speak("Searching...")
        result = wikipedia.summary(query, sentences=1)
        print(result)
        pyttsx3.speak(result)



    # This shuts down the computer when you run it
    # By setting timeout period before the shutdown. The default is 30 seconds
    elif "shutdown" in query:
        os.system("shutdown /s /t 1")
        
        

    # Shuts down the computer, and restarts it afterwards.
    # By setting timeout period before the shutdown. The default is 30 seconds
    elif "restart" in query:
        os.system("shutdown /r /t 1")
        


    elif ("cpu" in query) or ("useage" in query) or ("battery" in query):
        # It tells about the CPU Useage.
        cpu_usage = str(psutil.cpu_percent())
        pyttsx3.speak("CPU is at" + cpu_usage)

        # It tells about the battery.
        battery = psutil.sensors_battery()
        pyttsx3.speak("Battery is at")
        pyttsx3.speak(battery.percent)



    # It exit from the program.
    elif ("exit" in query) or ("offline" in query) or ("terminate" in query):
        print("Program Terminated.")
        pyttsx3.speak("Program Terminated.")
        quit()



