import pyautogui
from responsive_voice import ResponsiveVoice
import speech_recognition as sr

ENGINE = ResponsiveVoice()
ENGINE = ResponsiveVoice(lang=ResponsiveVoice.TURKISH)

def sesi_metne_cevir():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Dinleme başlatıldı.")
        recognizer.adjust_for_ambient_noise(source)
        ses = recognizer.listen(source, timeout=5)

    try:
        metin = recognizer.recognize_google(ses, language="tr-TR")
        return metin
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

def open_weather_website():
    update_file('source.txt','script.js','hava-durumu-js-start','hava-durumu-js-end')
    update_file('source.txt','index.html','hava-durumu-html-start','hava-durumu-html-end')
    refresh()


def text_to_speech(text):
    print(text)
    ENGINE.say(text.encode('utf-8'))

