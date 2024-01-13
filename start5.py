import time

name = input("Adınız nedir? ")
age = int(input("Yaşınız kaç? "))

if age >= 12:
    print("Başlıyoruz...\n")
    time.sleep(1)  # Ekstra etki için gecikmeler ekleniyor
    print("Lütfen bekleyin!")
    time.sleep(1)
    count = 0
    while count != 5:
        print(".", end="")
        time.sleep(2 / 5)
        count += 1

    print("\nMerhaba", name, "! Bu maceraya hoş geldiniz! 🏕️🏝️🏖️🏕")

    answer = input("\nBir toprak yoldasınız, yolun sonuna geldiniz ve sola veya sağa gidebilirsiniz. Hangi yolu seçmek istersiniz (sol/sağ)?: ").lower()

    if answer == "sol":
        count = 0
        while count != 5:
            print(".", end="")
            time.sleep(2 / 5)
            count += 1
        answer = input("\nBir nehirle karşılaştınız, etrafından yürüyerek geçebilir veya yüzerek geçebilirsiniz? Yürümek için Y'yi, yüzmek için S'yi tuşlayın: ").upper()

        if answer == "S":
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2 / 5)
                count += 1
            print("\nYüzerek geçtiniz ve bir timsah tarafından yenildiniz.")
        elif answer == "Y":
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2 / 5)
                count += 1
            print("\nÇok mil yürüdünüz, suyunuz bitti ve oyunu kaybettiniz.")
        else:
            print('Geçerli bir seçenek değil. Kaybettiniz.')

    elif answer == "sağ":
        count = 0
        while count != 5:
            print(".", end="")
            time.sleep(2 / 5)
            count += 1
        answer = input("\nWobbly görünen bir köprüye geldiniz, üzerinden geçmek mi istersiniz yoksa geri mi dönmek (geç/geri)? ").lower()

        if answer == "geri":
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2 / 5)
                count += 1
            print("\nGeri döndünüz ve kaybettiniz.")
        elif answer == "geç":
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2 / 5)
                count += 1
            answer = input("\nKöprüyü geçtiniz ve bir yabancıyla karşılaştınız. Onunla konuşacak mısınız (evet/hayır)? ").lower()

            if answer == "evet":
                count = 0
                while count != 5:
                    print(".", end="")
                    time.sleep(2 / 5)
                    count += 1
                print("\nYabancıyla konuştunuz ve size altın verdiler. Kazandınız!")
            elif answer == "hayır":
                count = 0
                while count != 5:
                    print(".", end="")
                    time.sleep(2 / 5)
                    count += 1
                print("\nYabancıyı görmezden geldiniz ve onlar kırıldı, Kaybettiniz!.")
            else:
                print('Geçerli bir seçenek değil. Kaybettiniz.')
        else:
            print('Geçerli bir seçenek değil. Kaybettiniz.')

    else:
        print('Geçerli bir seçenek değil. Kaybettiniz.')

    print("Deneyim için teşekkürler", name, ":)")
else:
    print("\nÜzgünüm :( Oynamak için yeterince yaşta değilsiniz...")
    print("\nÇıkılıyor...")
    count = 0
    while count != 5:
        print(".", end="")
        time.sleep(2/5)
        count += 1
    print()

if __name__ == "__main__":
    print()
import time

name = input("Adınız nedir? ")
age = int(input("Yaşınız kaç? "))

if age >= 12:
    print("Başlıyoruz...\n")
    time.sleep(1)  # Ekstra etki için gecikmeler ekleniyor
    print("Lütfen bekleyin!")
    time.sleep(1)
    count = 0
    while count != 5:
        print(".", end="")
        time.sleep(2 / 5)
        count += 1

    print("\nMerhaba", name, "! Bu maceraya hoş geldiniz! 🏕️🏝️🏖️🏕")

    answer = input("\nBir toprak yoldasınız, yolun sonuna geldiniz ve sola veya sağa gidebilirsiniz. Hangi yolu seçmek istersiniz (sol/sağ)?: ").lower()

    if answer == "sol":
        count = 0
        while count != 5:
            print(".", end="")
            time.sleep(2 / 5)
            count += 1
        answer = input("\nBir nehirle karşılaştınız, etrafından yürüyerek geçebilir veya yüzerek geçebilirsiniz? Yürümek için Y'yi, yüzmek için S'yi tuşlayın: ").upper()

        if answer == "S":
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2 / 5)
                count += 1
            print("\nYüzerek geçtiniz ve bir timsah tarafından yenildiniz.")
        elif answer == "Y":
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2 / 5)
                count += 1
            print("\nÇok mil yürüdünüz, suyunuz bitti ve oyunu kaybettiniz.")
        else:
            print('Geçerli bir seçenek değil. Kaybettiniz.')

    elif answer == "sağ":
        count = 0
        while count != 5:
            print(".", end="")
            time.sleep(2 / 5)
            count += 1
        answer = input("\nWobbly görünen bir köprüye geldiniz, üzerinden geçmek mi istersiniz yoksa geri mi dönmek (geç/geri)? ").lower()

        if answer == "geri":
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2 / 5)
                count += 1
            print("\nGeri döndünüz ve kaybettiniz.")
        elif answer == "geç":
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2 / 5)
                count += 1
            answer = input("\nKöprüyü geçtiniz ve bir yabancıyla karşılaştınız. Onunla konuşacak mısınız (evet/hayır)? ").lower()

            if answer == "evet":
                count = 0
                while count != 5:
                    print(".", end="")
                    time.sleep(2 / 5)
                    count += 1
                print("\nYabancıyla konuştunuz ve size altın verdiler. Kazandınız!")
            elif answer == "hayır":
                count = 0
                while count != 5:
                    print(".", end="")
                    time.sleep(2 / 5)
                    count += 1
                print("\nYabancıyı görmezden geldiniz ve onlar kırıldı, Kaybettiniz!.")
            else:
                print('Geçerli bir seçenek değil. Kaybettiniz.')
        else:
            print('Geçerli bir seçenek değil. Kaybettiniz.')

    else:
        print('Geçerli bir seçenek değil. Kaybettiniz.')

    print("Deneyim için teşekkürler", name, ":)")
else:
    print("\nÜzgünüm :( Oynamak için yeterince yaşta değilsiniz...")
    print("\nÇıkılıyor...")
    count = 0
    while count != 5:
        print(".", end="")
        time.sleep(2/5)
        count += 1
    print()

if __name__ == "__main__":
    print()
