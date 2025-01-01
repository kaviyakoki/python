from tkinter import font
import webbrowser as wb
import speech_recognition as sr
import pyttsx3
def main1():
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("sayy...")
        audio=r.listen(source)
    try:
        print("Recognizing now...")
        text=str(r.recognize_google(audio))
        label_font=font.Font(weight="bold",family="Times New Roman",size=10)
        Label(r1,text=text,font=label_font).place(relx=0.5,rely=0.35)
    except Exception as e:
         print("Error:"+str(e))
def main2():
    r=sr.Recognizer()
    url="https://WWW.google.co.in/search?q="
    with sr.Microphone()as source:
        print("speak...,It is google search...,what do you want to search..")
        audio=r.listen(source)
    try:
        get=r.recognize_google(audio)
        print(get)
        label_font=font.Font(weight="bold",family='Times New Roman',size=10)
        Label(r1,text=get,font=label_font).place(relx=0.5,rely=0.45)
        wb.get().open_new(url+get)
    except sr.UnknownValueError:
        print("error")
    except sr.RequestError as e:
        print('failed'.format(e))
    except:
        print("Microphone not detected")
def main3():
    r=sr.Recognizer()
    url="https://WWW.youtube.com/results?search_query="
    with sr.Microphone()as source:
        print("speak..,It is the youtube search..,what do you want to search..")
        audio=r.listen(source)
    try:
        get=r.recongnize_google(audio)
        print(get)
        label_font=font.Font(weight="bold",family='Times New Roman',size=10)
        Label(r1,text=get,font=label_font).place(relx=0.5,rely=0.55)
        wb.get().open_new(url+get)
    except sr.UnknownValueError:
        print("error")
    except sr.RequestError as e:
        print('failed'.format(e))
    except:
        print("Microphone not detected")
def main4():
    speech=pyttsx3.init()
    speech.setProperty('rate',200)
    speech.setProperty('volume',1.0)
    voices=speech.getProperty('voices')
    speech.setProperty('voice',voices[1].id)#0 to 1
    speech.say(a1.get("1.0",END))
    speech.runAndWait()
    speech.stop()
#end
from tkinter import*
r1=Tk()
r1.geometry("600x400")
label_font=font.Font(weight="bold",family='Helvietica',size=30)
l1=Label(r1,text="speech Recognition",font=label_font,bg='#0052cc',fg='#ffffff')
l1.place(anchor="center",relx=0.5,rely=0.1)

label_font=font.Font(weight="bold",family='Times New Roman',size=20)
l2=Label(r1,text="This is example of speech Recognition and GUI",font=label_font,bg='orange',fg='#ffffff')
l2.place(anchor="center",relx=0.5,rely=0.25)

label_font=font.Font(weight="bold",family='Times New Roman',size=10)
b=Button(r1,text="Its just a print what you say",command=lambda:main1(),font=label_font)
b.place(relx=0.1,rely=0.35)

label_font=font.Font(weight="bold",family='Times New Roman',size=10)
b=Button(r1,text="Its google search what you say",command=lambda:main2(),font=label_font)
b.place(relx=0.1,rely=0.45)

label_font=font.Font(weight="bold",family="Times New Roman",size=10)
b=Button(r1,text="Its youtube search what you say",command=lambda:main3(),font=label_font)
b.place(relx=0.1,rely=0.55)

a1=Text(r1,height=2,width=30)
a1.place(relx=0.1,rely=0.65)

label_font=font.Font(weight="bold",family='Times New Roman',size=10)
b=Button(r1,text="Text to speak",command=lambda:main4(),font=label_font)
b.place(relx=0.55,rely=0.65)

r1.mainloop()


        


    
