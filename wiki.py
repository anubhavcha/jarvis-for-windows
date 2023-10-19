from speak import speak
from wikipedia import wikipedia
def wiki_search(text):
    speak("Searching Wikipedia.....")
    text = text.replace("jarvis", "")
    text = text.replace("wikipedia", "")
    wiki = wikipedia.summary(text, 2)
    print(wiki)
    speak(f"According To Wikipedia : {wiki}")


wiki_search("who is carry minati")