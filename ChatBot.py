
# coding: utf-8

# In[1]:

import speech_recognition as sr

r=sr.Recognizer()
def talk():
    
    
    with sr.Microphone() as source:
        
        
        audio=r.listen(source)
        user=r.recognize_google(audio)

    try:
        
        print('Google recognised your speech as: \n' + user)
        
    except:
        
        pass
    return user


# In[2]:

from translate import Translator 
import pyttsx3
#chatbot = ChatBot('Harper', trainer = 'chatterbot.trainers.ListTrainer')
def main():

    try:
        
        engine = pyttsx3.init()
        print("Welcome")
        engine.say("Welcome to my Translator")
        engine.setProperty('rate',120)
        engine.setProperty('volume', 0.9)
        engine.runAndWait()
        
        
        
        print("What language would you like your text translated to?")
        engine.say("What language would you like your text translated to?")
        engine.setProperty('rate',120)
        engine.setProperty('volume', 0.9)
        engine.runAndWait()  
        lang_2 = talk()
        
        print("From what language you want your text translated to?")
        engine.say("From what language you want your text translated to?")
        engine.setProperty('rate',120)
        engine.setProperty('volume', 0.9)
        engine.runAndWait()
        lang_1=talk()
        
        
        print('So What statement you want to convert?')
        engine.say('So What statement you want to convert')
        engine.setProperty('rate',120)
        engine.setProperty('volume', 0.9)
        engine.runAndWait()
        request=talk()
        
        translator= Translator(from_lang=lang_1,to_lang= lang_2)
        translation = translator.translate(request)
        print (translation)
        engine.say(translation)
        engine.setProperty('rate',120)
        engine.setProperty('volume', 0.9)
        engine.runAndWait()
        
            
    except KeyboardInterrupt:
        
        print("Program Interrupted")
main()


# In[ ]:




# In[ ]:




# In[ ]:



