import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import subprocess

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)

def takeCommand():
	#It takes microphone input from the user and returns string output

	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 0.5
		audio = r.listen(source)

		try:
			print("Recognizing...")

			Query = r.recognize_google(audio, language='id-ID')
			print("the command is printed=", Query)

		except Exception as e:
			print(e)
			return "None"

		return Query

def tellDay():
    
	day = datetime.datetime.today().weekday() + 1
 
	Day_dict = {1: 'Monday', 2: 'Tuesday',
				3: 'Wednesday', 4: 'Thursday',
				5: 'Friday', 6: 'Saturday',
				7: 'Sunday'}

	if day in Day_dict.keys():
		day_of_the_week = Day_dict[day]
		speak("The day is" + day_of_the_week)
  
def tellTime(perintah:str="") -> str:

	time = str(datetime.datetime.now())

	hour = time[11:13]
	min = time[14:16]
	if not perintah:
		speak("The time is " + hour + "Hours and" + min + "Minutes")

	return hour
def speak(audio):

	engine.say(audio)

	engine.runAndWait()
 
def Hello():
    hour = int(tellTime("Peintah"))
    waktu = ""
    if hour < 10:
        waktu = "Good Morning"
    elif hour < 14:
        waktu = "Good Afternoon"
    elif hour < 18:
        waktu = "Good Evening"
    else: 
        waktu = "Good Night"
        
    speak(f"Hello Sir, {waktu}. I am your desktop Assistant. How can I help you ?")
    
def Take_query():
    
	Hello()
 
	while(True):
	
		query = takeCommand().lower()
		
		if "hari apa" in query:
			tellDay()
			continue

		elif "jam berapa" in query:	
			tellTime()
			continue

		elif "apa itu" in query:
			speak("searching wikipedia")
			query = query.replace("apa itu", "")
			results = wikipedia.summary(query, sentences=2)
			speak("According to wikipedia, " + results)
			continue

		elif "tolong" in query:
			if "buka" in query:
				if "youtube" in query:
					webbrowser.open("www.youtube.com")
					speak("Opening YouTube")
				elif "google" in query:
					webbrowser.open("www.google.com")
					speak("Opening Google")
				elif "chrome" in query:
					speak("what should i search ?")
					search = takeCommand().lower()
					if "tidak ada" not in search:
						webbrowser.open(f"www.google.com/search?q={search}")
					subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
					speak("Chrome Opened")
				elif "visual studio code" in query:
					subprocess.Popen("C:\\Users\\young\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
					speak("Opening Visual Studio Code")
				elif "permainan" in query:
					subprocess.Popen("C:\\Riot Games\\Riot Client\\RiotClientServices.exe")
					speak("Opening Riot Client")
			if "tutup" in query:
				if "chrome" in query:
					subprocess.Popen("taskkill /f /im chrome.exe")
					speak("Chrome Closed")
				elif "visual studio code" in query:
					subprocess.Popen("taskkill /f /im code.exe")
					speak("Visual Studio Code Closed")
				elif "permainan" in query:
					subprocess.Popen("taskkill /f /im RiotClientServices.exe")
					speak("Riot Client Closed")
			continue
		
		elif "matikan sistem" or "nonaktif" in query:
			speak("system will shutdown in. 3")
			speak("2")
			speak("1")
			break
    
if __name__ == '__main__':

	Take_query()