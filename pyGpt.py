import gtts
import os
import speech_recognition as sr
from time import sleep
import playsound
import openai
openai.api_key = "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"


class pygpt:
    def __init__(self):
        return None
        


    def processing(self,query):
        if query:
            ans = openai.ChatCompletion.create(model='gpt-3.5-turbo',messages = [{'role':'system', 'content':'You are a helpful assistant'},
                                                                                {'role':'user','content':query}])
            
            return ans.choices[0].message["content"]
        
        return None
    
    def speak(self,text):
        tts = gtts.gTTS(text,lang='en-In',slow=False)
        filename = "voice.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)

    def get_audio(self):
        recognize = sr.Recognizer()

        # print(sr.Microphone().list_microphone_names())
        with sr.Microphone(device_index=1) as mic:
            print("Say Something......")
            recognize.adjust_for_ambient_noise(mic,duration=0.2)

            user_audio = recognize.listen(mic)
            print("Stop")

            try:
                user_audio_text_data = recognize.recognize_google(audio_data=user_audio, language="en-In")
                print(f"User :->> {user_audio_text_data}")
                return user_audio_text_data.lower()

            except ValueError:
                print("I did not get it please try again!")
                sleep(2)
                

        return 'None'
    

if __name__=="__main__":
    pg = pygpt()

    pg.speak("How May I help you?")

    while True:
        user_query = pg.get_audio()

        if 'exit' in user_query.lower():
            break
        gpt_reply = pg.processing(user_query)
        print("gpt:-->>",gpt_reply)
        pg.speak(gpt_reply)