import time
import random

def slow_print(text, delay=0.03):
    for character in text:
        print(character, end='', flush=True)
        time.sleep(delay)
    print()

def start_adventure():
    slow_print("Uzak bir galakside, bilinmeyen bir gezegende, bir uzaylı medeniyeti keşfettin.")
    slow_print("Bu medeniyetin teknolojisi ve kültürü seni büyüledi.")
    slow_print("Ancak bir sorun var: Gezegenin lideri seni bir yabancı olarak görüyor ve güvenmiyor.")
    slow_print("Seni evine, Dünya'ya geri göndermek için bir uzay gemisi yapman gerekiyor.")
    slow_print("Ancak bunun için yerel halkın güvenini kazanman ve gerekli malzemeleri toplaman lazım.")
    slow_print("Macera başlıyor...\n")

    first_choice()

def first_choice():
    slow_print("Bir kavşakta duruyorsun. Sol yoldan gitmek, yerel bir köye gider. Sağ yoldan gitmek, eski bir uzay limanına gider.")
    choice = input("Hangi yolu seçmek istersin? (sol/sağ): ").lower()

    if choice == "sol":
        village_path()
    elif choice == "sağ":
        spaceport_path()
    else:
        slow_print("Anlaşılmayan bir seçim yaptın. Lütfen tekrar dene.")
        first_choice()

def village_path():
    slow_print("\nKöye doğru yola çıkıyorsun. Köylüler başlangıçta seni şüpheyle karşılıyor.")
    slow_print("Ancak, onlara yardım etmeye karar veriyorsun.")
    slow_print("Bir köylü, ekinlerin zarar gördüğünü ve yardıma ihtiyacı olduğunu söylüyor.")
    help_choice = input("Yardım edecek misin? (evet/hayır): ").lower()

    if help_choice == "evet":
        slow_print("\nKöylüye yardım ediyorsun ve ekinleri kurtarıyorsun.")
        slow_print("Köylüler senin iyi niyetini görüyor ve sana güvenmeye başlıyorlar.")
        slow_print("Bir köylü, uzay gemisi yapımında kullanabileceğin bazı malzemeleri veriyor.")
        slow_print("Artık uzay limanına gitme zamanı geldi.")
        spaceport_path()
    elif help_choice == "hayır":
        slow_print("\nKöylülere yardım etmeyi reddediyorsun ve onların güvenini kazanamıyorsun.")
        slow_print("Bu yüzden, uzay gemisi yapmak için gerekli malzemeleri bulamıyorsun.")
        slow_print("Tekrar denemek için uzay limanına gitmeye karar veriyorsun.")
        spaceport_path()
    else:
        slow_print("Anlaşılmayan bir seçim yaptın. Lütfen tekrar dene.")
        village_path()

def spaceport_path():
    slow_print("\nEski uzay limanına varıyorsun. Burası terk edilmiş ve harabelerle dolu.")
    slow_print("Ancak, eski bir uzay gemisi gövdesi buluyorsun ki bu senin için mükemmel bir başlangıç.")
    slow_print("Gemiye yakından bakıyorsun ve onarılması gerektiğini fark ediyorsun.")
    repair_choice = input("Gemiye zarar vermeden onarmaya çalışacak mısın? (evet/hayır): ").lower()

    if repair_choice == "evet":
        slow_print("\nBüyük bir dikkat ve özenle gemiyi onarıyorsun.")
        slow_print("Gemi yavaş yavaş eski ihtişamına kavuşuyor.")
        slow_print("Artık Dünya'ya dönüş yolculuğuna başlayabilirsin.")
        end_game(True)
    elif repair_choice == "hayır":
        slow_print("\nGemiye zarar veriyorsun ve onarılamaz hale geliyor.")
        slow_print("Artık Dünya'ya dönmenin başka bir yolunu bulman gerekecek.")
        end_game(False)
    else:
        slow_print("Anlaşılmayan bir seçim yaptın. Lütfen tekrar dene.")
        spaceport_path()

def end_game(success):
    if success:
        slow_print("\nTebrikler! Uzay gemisini başarıyla onardın ve Dünya'ya dönüş yolculuğuna çıkıyorsun.")
        slow_print("Yeni uzaylı dostlarınla vedalaşıyorsun ve evrenin derinliklerine doğru yol alıyorsun.")
    else:
        slow_print("\nMaalesef, Dünya'ya dönüş yolculuğunu başlatamadın.")
        slow_print("Ancak, bu gezegende yeni bir hayat kurmaya karar veriyorsun.")
        slow_print("Belki bir gün, Dünya'ya dönmenin başka bir yolunu bulursun.")
    slow_print("Oyun bitti. Teşekkürler oynadığın için!")

# Oyunu başlat
start_adventure()
