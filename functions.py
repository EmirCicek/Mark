import pyautogui
from responsive_voice import ResponsiveVoice
import speech_recognition as sr
from datetime import datetime


ENGINE = ResponsiveVoice()
ENGINE = ResponsiveVoice(lang=ResponsiveVoice.TURKISH)

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Dinleme başlatıldı.")
        recognizer.adjust_for_ambient_noise(source)
        ses = recognizer.listen(source, timeout=5)

    try:
        text = recognizer.recognize_google(ses, language="tr-TR")
        return text
    except sr.UnknownValueError:
        print("Ses algılanamadı.")
    except sr.RequestError as e:
        print(f"Hata oluştu; {e}")
def clear_file(file,input): # This function clears the javascript file
    with open(file,'w') as fl:
        fl.write(input)

def update_file(r_file,w_file,start,finish): # This function updates the file
    with open(r_file,'r+') as fl:
        source_code = fl.readlines()
        clear_file(w_file,'\n')

        with open(w_file,'a') as file:
            started = False

            for line in source_code:
                if start == line.strip():
                    started = True
                    continue
                elif finish in line and started == True:
                    break
                elif started == True:
                    file.write(line)

def refresh():
    pyautogui.leftClick(50,100) # Clicking the browser for refresh
    pyautogui.hotkey('ctrl','f5') # Refreshing the browser

def full_screen():
    pyautogui.leftClick(50,100)
    pyautogui.hotkey('f11')

def open_weather_website():
    update_file('source.txt','script.js','hava-durumu-js-start','hava-durumu-js-end')
    update_file('source.txt','index.html','hava-durumu-html-start','hava-durumu-html-end')
    refresh()


def text_to_speech(text):
    print(text)
    ENGINE.say(text.encode('utf-8'))


def time():
    days = {
        'Monday' : 'Pazartesi',
        'Tuesday' : 'Salı',
        'Wednesday' : 'Çarşamba',
        'Thursday' : 'Perşembe',
        'Friday' : 'Cuma',
        'Saturday' : 'Cumartesi',
        'Sunday' : 'Pazar'
    }
    
    now = datetime.now()
    hour = now.strftime("%H:%M")
    # date = now.strftime("%Y-%m-%d")
    date = now.strftime("%d-%m-%Y")
    day = now.strftime("%A")

    result = [hour,date,days[day]]

    return result # [0] --> 12:38 [1] --> 25-11-2023 [2] --> Saturday(Cumartesi)


def open_time():
    update_file('source.txt','index.html','saat-html-start','saat-html-end')
    update_file('source.txt','script.js','saat-js-start','saat-js-end')
    refresh()

