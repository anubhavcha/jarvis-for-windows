from listen import Listen
from speak import speak
from playsound import playsound
from youtubesearch import listen_and_searchyt
import random
from alam import set_alarm
import pyautogui as gui
from timesp import check_time
from openlinkedin import open_linkedin
import webbrowser
from sendmassegeonwhatsapp import Send_massege_on_Whatsapp
from openCHAtGpt import chatgpt
from qna import load_qa_data
from openytstudio import open_ytstudio
from open_telegram import open_telegram
from open_youtube import open_youtube
from shutdown import shutdown
from shutdown import reboot
from open_mysql import open_MYSQL
from wish import greating
from sendmassegeonwhatsapp import Send_massege_on_Whatsapp2
from sendmassegeonwhatsapp import Send_massege_on_Whatsapp3
import pywhatkit
from wether_report import Temp
from wether_report import temcity
from switchdash import switch_dash_1
from switchdash import switch_dash_2
from switchdash import switch_dash_3
from switchdash import switch_dash_4
from switchdash import switch_dash_5
from switchdash import switch_dash_6
from switchdash import switch_dash_7
from switchdash import switch_dash_8
from opengoogleclassroom import open_googleclassroom
from batterypersent import battey_persentage
from check_in_sp import speedtest
from openVsCode import open_code
from set_reminder import set_reminder


qa_file_path = "/home/zeno/Desktop/Jarvis/qna_log.txt"
qa_dict = load_qa_data(qa_file_path)




def main():
    while True:
        pass_call = Listen().lower()
        if "jarvis" in pass_call or "wake up" in pass_call or "wakeup" in pass_call or "wake up jarvis" in pass_call or "wakeup jarvis" in pass_call:
            playsound(
                "/home/zeno/Desktop/Jarvis/mp3(data)/Jarvis On (mp3cut.net) (1).mp3")
            while True: 
                text = Listen().lower()
                text = text.replace("jarvis", "")

                if "wake up" in text or "wakeup" in text:
                   random_choice = random.choice(["speak", "playsound"])
                   if random_choice == "speak":
                     speak("Hello sir, I am here. How may I help you?")
                   else:
                    playsound("/home/mr_zenox/Desktop/Jarvis/mp3(data)/Jarvis Startup ! Jarvis tiktok pc sound.mp3")
                elif "set alarm" in text:
                  speak("Sir, this is my beta version and I can't set alarms using voice. Please enter the time:")
                  alarm_time = input()
                  set_alarm(alarm_time)

                elif "youtube search" in text:
                 speak("What should I search on YouTube, sir?")
                 listen_and_searchyt()

                elif text.startswith("play song "):
                 song_name = text.replace("play song", "")
                 song_name = song_name.replace("on youtube", "")
                 pywhatkit.playonyt(song_name)
                 speak(f'Playing {song_name} on YouTube.')
                 speak("enjoy sir")

                elif "check battery persentage" in text or "check battery power" in text or "check battery status" in text:
                 battey_persentage()

                elif "open google classroom" in text or "open classroom" in text or "open googleclassroom" in text:
                 open_googleclassroom()

                elif "close" in text or "close this window" in text or " close window" in text:
                 gui.hotkey('alt', 'f4')

                elif "stop" in text or "play" in text or "pause" in text:
                 gui.hotkey('space')

                elif "thanks" in text or "thank you" in text:
                  playsound("/home/zeno/Desktop/Jarvis/mp3(data)/Jarvis Confirm-male.mp3")

                elif "hello" in text:
                  responses = ["hello sir , how may i assist you",
                         "hello sir i am excited to assist you"]
                  response = random.choice(responses)
                  speak(response)

                elif "love you" in text or "i love you" in text:
                 responses = ["love you to sir ", "love you three thousent sir",
                         "love you four thousent sir", "i love you to sir"]
                 response = random.choice(responses)
                 speak(response)

                elif "minimise this window" in text or "minimise window" in text or "minimise" in text:
                 gui.hotkey('winleft', 'h')

                elif "open code" in text or "open vs code" in text or "open code editor" in text:
                 open_code()

                elif "what time" in text or "what is the time" in text or "what is the time jarvis" in text:
                 check_time()

                elif "mute" in text or "mute jarvis" in text:
                 gui.hotkey('f1')
  
                elif "open linkedin" in text:
                 open_linkedin()
   
                elif "open chatgpt" in text or "open chat gpt" in text or "chatgpt" in text or "open gpt" in text:
                  chatgpt()
        

                elif text.startswith("who is "):
                  if text in qa_dict:
                   speak(qa_dict[text])
                  else:
                   query = text.replace("who is ", "")
                   query = query.replace("search on google", "")
                   query = query.strip()
                   if query:
                    url = "https://www.google.com/search?q=" + query
                    webbrowser.open_new_tab(url)
                    speak("Here are the search results for " + query)
                   else:
                    speak("I didn't catch what you said")

                elif text.startswith("what is "):
                  if text in qa_dict:
                   speak(qa_dict[text])
                  else:
                   query = text.replace("what is ", "")
                   query = query.replace("search on google", "")
                   query = query.strip()
                   if query:
                    url = "https://www.google.com/search?q=" + query
                    webbrowser.open_new_tab(url)
                    speak("Here are the search results for " + query)
                   else:
                    speak("I dont know")

                elif text.startswith("how to "):
                  if text in qa_dict:
                   speak(qa_dict[text])
                  else:
                   query = text.replace("how to ", "HOW TO ")
                   query = query.replace("search on google", "")
                   query = query.strip()
                   if query:
                     url = "https://www.google.com/search?q=" + query
                     webbrowser.open_new_tab(url)
                     speak("Here are the search results for " + query)
                   else:
                    speak("I dont know")
 
                elif "send message on whatsapp" in text:
                 Send_massege_on_Whatsapp()

                elif "who are you" in text or "indroduse yourself" in text:
                 playsound("/home/zeno/Desktop/Jarvis/mp3(data)/Jarvis.mp3")

                elif text in qa_dict:
                 speak(qa_dict[text])

                elif "open youtube studio" in text or "open youtube studio" in text:
                 open_ytstudio()

                elif "open telegram" in text:
                 open_telegram()

                elif "open youtube" in text:
                 open_youtube()

                elif "shutdown my laptop" in text or "shutdown" in text:
                 shutdown()

                elif "restart" in text or "restart my laptop" in text:
                 reboot()

                elif "open mysql" in text or "open my sql" in text or "open database" in text:
                 open_MYSQL()

                elif "good morning" in text or "good afternoon" in text or "good evening" in text:
                 greating()

                elif "good night" in text or "happy night" in text or "sweet dream" in text:
                  responses = ["good night sir , sleep well sir", "good night sir ,sweet dreams",
                             "good night sir", "ok sir i will meet you new dream world"]
                  response = random.choice(responses)
                  speak(response)
                  speak("sir can i send good night to you special one and dad")
                  text = Listen().lower()
                  if "yes" in text or "yes please" in text:
                    Send_massege_on_Whatsapp2()
                    speak("GOOD NIGHT TO YOUR FATHER ! FUNCTION DONE")
                    Send_massege_on_Whatsapp3()
                    speak("GOOD NIGHT TO SOMEONE SPICIAL ALSO DONE")
                  elif "no" in text or "no thanks" in text or "no need" in text:
                   pass

                elif "check temperature outside" in text or "check temperature" in text:
                  Temp()

                elif "check temprature bangaluru" in text or "check temprature in banglore" in text or "temprature in banglore" in text:
                 temcity()

                elif "switch dash 1" in text or "switch dash one" in text:
                 switch_dash_1()

                elif "switch dash 2" in text or "switch dash two" in text or "switch dash to" in text:
                 switch_dash_2()

                elif "switch dash 3" in text or "switch dash three" in text:
                 switch_dash_3()

                elif "switch dash 4" in text or "switch dash four" in text:
                 switch_dash_4()

                elif "switch dash 5" in text or "switch dash five" in text:
                 switch_dash_5()

                elif "switch dash 6" in text or "switch dash six" in text:
                 switch_dash_6()

                elif "switch dash 7" in text or "switch dash seven" in text:
                  switch_dash_7()

                elif "switch dash 8" in text or "switch dash eight" in text:
                  switch_dash_8()

                elif "show dash" in text or "so dash" in text or "soo dash" in text:
                  gui.press('winleft')

                elif "check internet speed" in text or "internet speed" in text:
                 speedtest()    
                
                elif text.startswith("set reminder "):
                 text = text.replace("set reminder ","")
                 text = text.replace("for ", "")
                 text = text.replace(" seconds", "s")
                 text = text.replace(" minutes", "m") 
                 text = text.replace(" hours", "h") 
                 print(text)
                 
                 set_reminder(text)
                 speak(f"ok sir ! reminder set for {text}")


main()