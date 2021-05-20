''' for speech recognization'''
import speech_recognition as sr
''' for text to speech version x3 use package'''
import pyttsx3
import pywhatkit as kit
import datetime
import wikipedia


listener=sr.Recognizer()
engine=pyttsx3.init() #to initialize pyttsx3

#for female voice set voice id =1
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    #engine.say('hi i am alexa')
    engine.say(text)
    engine.runAndWait()


def control_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'dell' in command:
                command=command.replace('dell',"")
                print(command)
                #talk(command)

    except:
        pass
    return command


def run_alexa():
    command=control_command()
    print(command)
    if 'play' in command:
        song=command.replace('play'," ")
        talk('playing '+ song)
        print("playing....")
        kit.playonyt(song)

    elif 'send' in command:
        send=command.replace('send','')
        talk('send a message'+send)
        print("sending....")
        kit.sendwhatmsg("+919766596335","hi this is me",18,3)

    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is'+time)

    elif 'wh' in command:
        person= command.replace('wh'," ")
        info=wikipedia.summary(person,2)
        print(info)
        talk(info)

    else:
        talk('plz repeat the command')

while True:
    run_alexa()