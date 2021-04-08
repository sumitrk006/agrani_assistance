# agrani_assistance
![agrani](https://github.com/Debalikh25/agrani_assistance/blob/master/giticon.png)

An AI based speech recognition assistance created with the help of python. Though it is availabe in the market but we added some extra functionalities onto it. We named
our assistance 'agrani' , in sanskrit meaning 'always first'. We used windows 10's inbuilt female voice 'Zira' as the main voice of our assistance.
Some of the external as well as in-bulit python modules used with this project -> json , os , requests ,smtplib , pyjokes , wikipedia , urllib , speech_recognition , pyautogui etc.
Agrani can help you with :
- Reading and listening to news about India.(from wolframalpha API).
- Sending email without opening gmail.
- Taking Screenshots.
- Informing the cpu usage and battery percentage of your pc.
- Inform you anything from Wikipedia
- Search youtube and google
- Locate places from google maps.
- Date and time info.
- Taking a single note.
- Telling Jokes
- Mathematical calculations
- Play music from your favourites directory
- Etc
---

### Steps to setup : ###
1. Clone this repository using : `git clone https://github.com/Debalikh25/agrani_assistance.git` in your local directory(create the local directory first).
2. Install the requirmnets using : `pip install -r requirements.txt` in the terminal.
3. Open the script: `agrani.py` with your prefered code editor.
4. Type the paths for the variables : `application_msword_path = ""(where your ms word is installed) , screen_shot = ""(for saving screenshots) , choose_your_songs_directory=""`.
5. Type your email : `your_email = ""`. Generate a gmail app password(steps commented inside script) for your email and type that password in `your_gmail_generated_app_password_here = "" ` variable.
6. Go to `https://newsapi.org/` and `https://products.wolframalpha.com/api/` , sign in and generate your API key  for both.
7. Paste your API keys inside the `news_api_id=""` and `wolframalpha_api_id = ""` variables. 
8. Done !(You are ready to go)
---
 ### Note: ### 
 if you face error while installing PyAudio package then we have provided the file for PyAudio in the repo:
  first -> pipwin -> `pip install pipwin`.
 Install it using : `pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl` or `pipwin install PyAudio-0.2.11-cp39-cp39-win_amd64.whl`.

---

After all the steps mentioned above you can create a windows executable file from the script so as to not open your editor again and again.
1. install pyinstaller - > `pip install pyinstaller`
2. Navigate to your agrani directory  , then  -> `pyinstaller agrani.py`
3. An .exe file will be created.
 
