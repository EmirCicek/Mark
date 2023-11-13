import functions


while True:
    try:
        tetikleyici_komut = str(functions.sesi_metne_cevir())
        if 'Mark'.lower() in tetikleyici_komut.lower() or 'Mark 1'.lower() in tetikleyici_komut.lower() or 'Hey Mark'.lower() in tetikleyici_komut.lower() or 'Hey Mark 1'.lower() in tetikleyici_komut.lower(): 
            print('Input :',tetikleyici_komut)
            functions.text_to_speech('Sizi Dinliyorum')

            try: # Program tetiklendikten sonra komut alma
                komut = str(functions.sesi_metne_cevir())
                if 'hava durumu' in komut.lower() or 'hava durumunu aç' in komut.lower():
                    functions.open_weather_website()
                    functions.text_to_speech('Hava Durumu Açıldı')
                elif 'beyaz ekran' in komut.lower():
                    functions.update_file('source.txt','index.html','beyaz-ekran-html-start','beyaz-ekran-html-end')
                    functions.refresh()
                    functions.text_to_speech('Beyaz Ekran Açıldı')
                elif 'programı sonlandır' in tetikleyici_komut.lower():
                    functions.text_to_speech('Program Sonlandırılıyor')
                    break
            except:
                print('Komut Almaya Çalışılırken Bir Hata Oluştu')


    except Exception as error:
        print('Bir Hata Oluştu')
        print('Error',error)
