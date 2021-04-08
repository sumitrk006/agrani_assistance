#AGRANI
#Developed By Debalikh Chatterjee and Sumit Kumar Mondal
#From UEM Kolkata

import os
import pyttsx3
import datetime
import getpass
import random
import speech_recognition as sr
import psutil
import json
import requests
from urllib.request import urlopen
import pyjokes
import time
import smtplib
import pyautogui
import wolframalpha
import wikipedia

import webbrowser as wb


username = getpass.getuser()
firs_name = username.split()
name = firs_name[0]



application_msword_path = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007' 
#please choose your microsoft office word file directory here . This path will not run for you as it belongs to my computer    

screen_shot= 'C:\\Users\\' + username + '\\Pictures\\screenshot1.png' 
#Change the directory of the screenshot saves if you want to....(not mandatory-will not give errors if left unchanged.It will work)


choose_your_songs_directory = "E:\\Desktop Playable"

your_email = ""
#enter your email here


your_gmail_generated_app_password_here = ""
#Step 1 -> Open your gmail inbox -> on the top right corner click on your cirlce profile pic and then click 'Manage your google account'
#Step 2 -> Go to security -> scroll down and turn on 'less secure app access'
#step 3 -> In security page turn on 2-step verification
#step 4 -> Now generate an app password from 'App Password' in security page
#step 5 -> Copy and paste this generated password in the above variable. Done ! . Now you can send email from here.
# Make sure not to share that generated passsword with anyone.

news_api_id = ""

wolframalpha_api_id = ""



def speak(command , rate = None):
    engine = pyttsx3.init()
    voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty("voice" , voice_id)
    if(rate != None):
        engine.setProperty("rate" , rate)
    else:
        engine.setProperty("rate" , 150)
    
    engine.say(command)
    engine.runAndWait()


def date():
    date = datetime.datetime.now().date()
    speak("The date is :")
    speak(date)
   

def greeting():
    hour = datetime.datetime.now().hour
    if(hour >=0 and hour<12):
        speak("Good Morning " + name  +  " I am at your service and  How may i help you")
    
    
    elif(hour >=12 and hour < 17):
        speak("Good Afternoon " + name)
        speak("I am  Agrani and always at your service" , 125)
        speak("How may I help you ?")
    elif(hour >= 17 and hour < 20):
        speak("Good Evening" + name)
        speak("I am  Agrani and always at your service", 125)
        speak("How may I help you ?")
    else :
        speak("Good Night" + name) 
   
        speak("I am  Agrani and always at your service" , 125)
        speak("How may I help you ?")


def  tellJoke():
    speak(pyjokes.get_joke() , 130)
    
def takeAudio():
        r = sr.Recognizer()
    

        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold = 2
            audio = r.listen(source , phrase_time_limit= 5)
    
       
        try:
            print("Recognising....")
            text = r.recognize_google(audio , language= "en-US")
            print(text)
        except Exception as e:
            print(e)
            print("i didnt recognize what you said")
            return 'None'
        return text 


def cpuPercentageAndBattery():
    cpu = str(psutil.cpu_percent())
    speak("Cpu is utilising its" + cpu + "percentage right now")

    battery = psutil.sensors_battery()
    speak("And currently the battery is ")
    speak(str(battery.percent) + "percent")


def takeScreenshot():

    image = pyautogui.screenshot() 
    image.save(screen_shot)


def sendMail():
    email = smtplib.SMTP('smtp.gmail.com' , 587 )
    email.starttls()
    email.ehlo()
    speak("Enter the email address of your recipent in terminal :" , 130)
    to_email = input("Enter recipent address :")
    speak("Tell me the subject of your email")
    subject = takeAudio()
    speak("Now tell me the message which i will send")
    message = takeAudio()
    msg = "Subject:{}\n\n{}".format(subject, message)
    email.login(your_email , your_gmail_generated_app_password_here)
    email.sendmail(your_email , to_email , msg)
    email.quit()
    speak("Email sent successfully sir")




   


 



greeting()


while True:

    query = takeAudio().lower()

    if 'what is my name' in query:
        speak("Your name is " + username , 120)

    elif 'my name' in query:
        speak("Your name is " + username , 120)

    elif 'there' in query:
        speak("I am here sir")

    elif 'agrani' in query:
        speak("yes sir")

    elif "date" in query:
        date()
    
    elif 'time' in query:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(time)

    elif 'created' in query:
        speak("Thanks to two of the students of uem kolkata that i took birth on this world" , 120)

    elif 'creator' in query:
           speak("Thanks to two of the students of uem kolkata that i took birth on this world" , 120)
        

    elif "good morning" in query:
        speak("Good Morning Sir")
    
    elif "good afternoon" in query:
        speak("Good afternoon Sir")

    elif "good evening" in query:
        speak("Good evening Sir")

    elif "good night" in query:
        speak("Good night Sir")

    elif "how are you" in query:
        speak("I am fine Sir and I hope you are well too")
    
    elif 'who i am' in query:
        speak("You can speak so i guess you are a human being")

    elif 'who am i' in query:
        speak("You can speak so i guess you are a human being")

    elif 'thank you' in query:
        speak("Welcome Sir")
    
    elif 'hello' in query:
        speak("hi sir how are you ?")

    elif 'i am fine' in query:
        speak("Thats great sir")

    elif 'welcome' in query:
        speak("wish you good luck sir")

    
    elif "what is your name" in query:
        speak("My Name is Agrani" , 130)
        speak("in sanskrit meaning always first" , 130)

    elif "what you do" in query:
        speak("I help people to solve their problem at first")

    elif "wikipedia" in query:
        
        speak("wait a few seconds sir")
        query = query.replace('wikipedia' , '')
        result = wikipedia.summary(query , sentences = 3)
        speak("According to wikipedia:")
        print(result)
        speak(result)

    elif "great" in query:
        speak("Thank U sir")

    elif "well done" in query:
        speak("Thank You Sir")

    elif "that's great" in query:
        speak("Thank U sir")

    elif "good" in query:
        speak("Thank You Sir")
    
    elif "do you have a girlfriend" in query:
        speak("No Sir I am single right now")

    elif 'search chrome' in query:
        chromePath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        speak("Just tell me the site name - the domain name   example  google")
        search_query = takeAudio().lower()
        wb.get(chromePath).open_new_tab(search_query + '.com')
        speak("Opening Sir")

    elif 'open youtube' in query :
        speak('Opening Sir')
        wb.open('https://www.youtube.com/')

    elif 'search youtube' in query :
        speak("What should i search in youtube sir")
        searchYoutube = takeAudio().lower()
        wb.open('https://www.youtube.com/results?search_query='+ searchYoutube)
        speak("Opening Sir")

    elif 'search google' in query :
        speak("What should i search in Google sir")
        searchGoogle = takeAudio().lower()
        wb.open('https://www.google.com/search?q='+ searchGoogle)
        speak("Opening Sir")

    elif 'cpu' in query:
        cpuPercentageAndBattery()
    
    
    elif 'shutdown' in query:
        speak("Shutting down sir")
        quit()

    elif 'quit' in query:
        speak("Shutting down sir")
        quit()

    elif 'exit' in query:
        speak("Shutting down sir")
        quit()

    elif 'log out' in query:
        speak("Logging you out")
        os.system("shutdown -l")

    elif 'turn off computer' in query:
        speak("Logging you out")
        os.system("shutdown /s /t 1")

    elif 'turn of pc' in query:
        speak("Logging you out")
        os.system("shutdown /s /t 1")

    elif 'restart' in query:
        speak("Restarting")
        os.system("shutdown /r /t 1")

    elif 'you can go now' in query:
        speak("Ok Shutting down sir")
        quit()

    elif 'go offline' in query:
        speak("Shutting down sir")
        quit()

    elif 'open word' in query:
        speak("Here we go sir")
        os.startfile(application_msword_path) 

    elif 'screenshot' in query :
        takeScreenshot()
        speak("Screenshot Taken and saved sir") 

    elif 'songs' in query:

        list_songs = os.listdir(choose_your_songs_directory)
        number_of_songs_in_dir = len(list_songs)
        speak("There are " + str(number_of_songs_in_dir ) + " songs in your folder sir" , 120)
        print("****************************************************************************************")
        i =0
        for song in list_songs:
            print("-->" + song + " (number -> "+ str(i) + " )")
            i = i+1
        print("****************************************************************************************")
        speak("I have listed the songs for you in the terminal")
        
        speak("Choose a number between 0 and " + str(number_of_songs_in_dir-1) + " or say random or say choose yourself" , 130)
        speak("I will wait for 10 seconds" , 140)
        time.sleep(10)
        speak("now tell me  sir" , 130)
        song_number = takeAudio().lower()
        while('number' not in song_number and song_number != 'random' and song_number != 'choose yourself'):
            print("Please say , 'random' or 'choose yourself' or 'number [any]' ")
            speak("I am sorry    unable to recognise your query Sir")
            song_number = takeAudio().lower()
        
        if 'number' in song_number and  'zero' not in song_number:
            song_number = int(song_number.replace('number', ''))
            while(song_number > (number_of_songs_in_dir -1)):
                speak("You are telling an out of limit number sir , say it again")
                song_number = takeAudio().lower()
            os.startfile(os.path.join(choose_your_songs_directory, list_songs[song_number]))

        elif 'zero' in song_number:
            os.startfile(os.path.join(choose_your_songs_directory, list_songs[0]))
            
            
        elif 'random' in song_number:
            random_number = random.randint(0 , number_of_songs_in_dir)
            os.startfile(os.path.join(choose_your_songs_directory, list_songs[random_number]))
        elif 'choose yourself' in song_number:
            random_number = random.randint(0 , number_of_songs_in_dir)
            os.startfile(os.path.join(choose_your_songs_directory, list_songs[random_number]))


    elif 'music' in query:

        list_songs = os.listdir(choose_your_songs_directory)
        number_of_songs_in_dir = len(list_songs)
        speak("There are " + str(number_of_songs_in_dir ) + " songs in your folder sir" , 120)
        i = 0
        print("****************************************************************************************")
        for song in list_songs:
            print("-->" + song+ " (number -> "+ str(i)+ " )")
            i = i+1
        print("****************************************************************************************")
        speak("I have listed the songs for you in the terminal")
        
        speak("Choose a number between 0 and " + str(number_of_songs_in_dir-1) + " or say random or say choose yourself" , 130)
        speak("I will wait for 10 seconds" , 140)
        time.sleep(10)
        speak("now tell me  sir" , 130)
        song_number = takeAudio().lower()
        while('number' not in song_number and song_number != 'random' and song_number != 'choose yourself'):
            print("Please say , 'random' or 'choose yourself' or 'number [any]' ")
            speak("I am sorry    unable to recognise your query Sir")
            song_number = takeAudio().lower()
        
        if 'number' in song_number and  'zero' not in song_number:
            song_number = int(song_number.replace('number', ''))
            while(song_number > (number_of_songs_in_dir -1)):
                speak("You are telling an out of limit number sir , say it again")
                song_number = takeAudio().lower()
            os.startfile(os.path.join(choose_your_songs_directory, list_songs[song_number]))

        elif 'zero' in song_number:
            os.startfile(os.path.join(choose_your_songs_directory, list_songs[0]))
            
            
        elif 'random' in song_number:
            random_number = random.randint(0 , number_of_songs_in_dir)
            os.startfile(os.path.join(choose_your_songs_directory, list_songs[random_number]))
        elif 'choose yourself' in song_number:
            random_number = random.randint(0 , number_of_songs_in_dir)
            os.startfile(os.path.join(choose_your_songs_directory, list_songs[random_number]))
        

    elif 'where is' in query:
        
        location = query.replace("where is" , "")
        speak("Searching the location of " + location)
        wb.open_new_tab("https://www.google.com/maps/place/" + location)
        time.sleep(4)
        speak("Location found")

    elif 'who is' in query:
        
        location = query.replace("where is" , "")
        speak("Searching the location of " + location)
        wb.open_new_tab("https://www.google.com/maps/place/" + location)
        time.sleep(4)
        speak("Location found")

    elif 'remember' in query:
        speak("Please tell what to remember Sir:")
        remember = takeAudio()
        remember_file = open("remember.txt", mode='w')
        remember_file.write(remember)
        speak("I will remember this Sir Listen")
        time.sleep(2.3)
        speak(remember)
        remember_file.close()

    elif 'my note' in query:
        file_remember = open("remember.txt" , mode='r')
        speak("ok sir, you said earlier")
        remembered = file_remember.read()
        speak(remembered)
        remember_file.close()

    elif 'stop listening' in query:
        speak("For how much seconds sir" , 120)
        speak("Please tell me only the number" , 120)
        audio = takeAudio()
        timer = int(audio)
        time.sleep(timer)
        speak("I am back again sir")

    elif 'joke' in query:
        speak("Ok listen sir ", 140)
        time.sleep(2)
        tellJoke()
        time.sleep(2)
        speak("Hope you like it")
    
    elif 'like it' in query:
        speak("I will again say it for you if you wish for", 130)

    elif 'what is' in query:
        user = wolframalpha.Client(wolframalpha_api_id)
        res = user.query(query)
        try:
            speak(next(res.results).text)
            print(next(res.results).text)
        except:
            speak("I could not get it sir")
            

    elif 'email' in query:
        sendMail()

    elif 'news' in query:
        try:
            jsonObject = urlopen("https://newsapi.org/v2/top-headlines?country=in&apiKey=" + news_api_id)
            data = json.load(jsonObject)
            i = 1
            speak("Here are some news about India" , 125)
            print("********************HEADLINES*********************\n")

            for news in data['articles']:
                print(str(i)+"."+" " + news['title'] + "\n")
                print(news['description'])
                print("\n\n")
                speak(news['title'] , 130)
                i += 1

        except Exception as e:
            print(e)

    elif 'calculate' in query :
        user = wolframalpha.Client(wolframalpha_api_id)
        indx = query.lower().split().index('calculate')
        query = query.split()[indx + 1:]
        res = user.query(''.join(query))
        result = next(res.results).text
        speak("Your answer is")
        time.sleep(1)
        speak(result)

    



        

        

    
 
    

        
        


    






    
  
    




         


