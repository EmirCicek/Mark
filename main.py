import functions


while True:
    try:
        trigger_command = str(functions.speech_to_text())
        if 'Mark'.lower() in trigger_command.lower() or 'Mark 1'.lower() in trigger_command.lower() or 'Hey Mark'.lower() in trigger_command.lower() or 'Hey Mark 1'.lower() in trigger_command.lower(): 
            print('Input :',trigger_command)
            functions.text_to_speech('Sizi Dinliyorum')

            try:
                command = str(functions.speech_to_text())
                if 'hava durumu' in command.lower() or 'hava durumunu aç' in command.lower():
                    functions.open_weather_website()
                    functions.text_to_speech('Hava Durumu Açıldı')
                elif 'beyaz ekran' in command.lower():
                    functions.update_file('source.txt','index.html','beyaz-ekran-html-start','beyaz-ekran-html-end')
                    functions.refresh()
                    functions.text_to_speech('Beyaz Ekran Açıldı')
                elif 'saat' in command.lower():
                    functions.open_time()
                    functions.text_to_speech('Saat '+ functions.time()[0])
                elif 'tam ekran' in command.lower() or 'ekran modu' in command.lower()  :
                    functions.full_screen()
                elif 'programı sonlandır' in trigger_command.lower():
                    functions.text_to_speech('Program Sonlandırılıyor')
                    break
                else:
                    print(command)
            except:
                print('Komut Almaya Çalışılırken Bir Hata Oluştu')


    except Exception as error:
        print('Bir Hata Oluştu')
        print('Error',error)
