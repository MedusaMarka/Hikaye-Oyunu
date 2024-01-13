def scene1():
    import time
    print("\n\tBU MACERA OYUNUNA HOŞ GELDİNİZ!\n"
          "\n\tHadi aksiyona başlayalım! ☆-🎬-☆\n"
          "\n\t\tLily gece yarısı yatak odasında uyanır. Evden dışarıda yüksek bir BANG sesi duyar."
          "\n\t\tŞimdi iki seçeneği var; odada kalabilir veya sesin ne olduğunu kontrol edebilir.")
    c1 = input("\n\n\tSeçiminizi yazın: Kal veya Kontrol Et? ")

    time.sleep(2)
    ans = 'yanlış'
    while (ans == 'yanlış'):
        if (c1.upper() == "KAL"):
            print(
                "\n\tLily odada kalmaya karar verir ve sonsuza kadar içeride kalır çünkü kimse ona yardım etmeye gelmez.")
            ans = 'doğru'
        elif (c1.upper() == "KONTROL ET"):
            print("\n\tLily sessizce odadan çıkar ve ana salona ulaşır.")
            ans = 'doğru'
            scene2()
        else:
            c1 = input("\tDOĞRU SEÇENEĞİ GİRİN! Kal veya Kontrol Et?: ")


def scene2():
    import time
    print("\n\t\tAna salonda, yerde garip ama sevimli bir oyuncak ayı bulur. "
          "\n\t\tAyıyı almak ister. "
          "\n\t\tAma almalı mı? Ona ait değil. (•˳̂•̆)")
    time.sleep(2)
    c1 = input("\n\n\tSeçiminizi yazın: Al veya Yok Say?: ")


    ans = 'yanlış'
    while (ans == 'yanlış'):
        if (c1.upper() == "AL"):
            print(
                "\n\t\tLily oyuncak ayıyı aldığı anda. Oyuncak ayı KONUŞMAYA başlar!"
                "\n\t\tAyı, Lily'nin büyük tehlikede olduğunu çünkü evde bir canavarın olduğunu söyler."
                "\n\t\tVe canavarın AİLESİNİ de yakaladığını!"
                "\n\t\tAma ona sarılarak korkmamasını söyler çünkü canavarı nasıl yeneceğini biliyor!")
            time.sleep(2)
            print("\n\tAyı, Lily'ye canavarı zayıflatabilecek ve kaçmasını sağlayacak sihirli bir iksir verir!"
                  "\n\t\tİksiri verir ve KAYBOLUR! Lily ilerlemeye devam eder.")
            ans = 'doğru'
            pick = "True"
        elif (c1.upper() == 'YOK SAY'):
            print("""\n\tLily ayıyı almayı reddeder ve ilerlemeye devam eder.""")
            ans = 'doğru'
            pick = "False"
        else:
            c1 = input("\tYanlış Giriş! Al veya Yok Say yazın?: ")
    time.sleep(2)
    scene3(pick)


def scene3(pick_value):
    import time
    print("\n\n\tBir süre yürüdükten sonra, Lily karşısında CANAVARI görür!"
    "\n\t\tKırmızı gözleri ve kötü bir görünüşü var. Çok korkar! ")
    time.sleep(2)
    if (pick_value == "True"):
        time.sleep(2)
        print("\n\tAma sonra hatırlar! Sihirli iksiri var ve onu canavara atar!"
              "\n\t\tKaybedecek bir şeyi yoktu!""")
        time.sleep(2)
        print("\n Canavar acı içinde ÇIĞLIK atar ama bir portal açmayı başarır ve Lily'yi yeni bir dünyaya iter!")
    elif (pick_value == "False"):
        print("\n\tCanavar Lily'ye saldırır ve onu yaralar! Daha sonra canavar tarafından yeni bir dünyaya atılır!")


if __name__ == "__main__":
    scene1()
print("\n\n")
print("=================================BÖLÜM 1'İN SONU=================================")

# Orijinal Kaynak: https://www.askpython.com/python/text-based-adventure-game
