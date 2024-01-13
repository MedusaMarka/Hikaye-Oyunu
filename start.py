import time
import random

class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} maalesef hayatını kaybetti.")
            time.sleep(2)
            print("Oyun bitti.")
            exit()

    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def use_item(self, item):
        if item in self.inventory:
            if item == "medkit":
                self.heal(50)
                self.inventory.remove(item)
                print(f"{self.name} bir medkit kullandı ve 50 sağlık puanı kazandı.")
                return True
        return False

def print_slow(str):
    for letter in str:
        print(letter, end='', flush=True)
        time.sleep(0.02)
    print()

def ask_question(question, options):
    print_slow(question)
    for i, option in enumerate(options, 1):
        print_slow(f"{i}. {option}")
    while True:
        choice = input("> ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        else:
            print_slow("Lütfen geçerli bir seçenek girin.")

def encounter_zombies(player):
    print_slow("Bir grup zombiyle karşılaştınız!")
    while True:
        action = ask_question(
            "Ne yapacaksın?",
            ["Savaş", "Kaç", "Envanteri kullan"]
        )
        if action == 1:
            if fight_zombies(player):
                return True
            else:
                return False
        elif action == 2:
            if run_away(player):
                return True
            else:
                return False
        elif action == 3:
            if use_inventory(player):
                continue
            else:
                print_slow("Envanterinde kullanılabilir bir şey yok.")

def fight_zombies(player):
    zombie_health = random.randint(50, 100)
    while zombie_health > 0 and player.is_alive():
        player_damage = random.randint(5, 15)
        zombie_damage = random.randint(5, 10)
        zombie_health -= player_damage
        player.take_damage(zombie_damage)
        print_slow(f"Zombiye {player_damage} hasar verdin. Zombi sağlığı: {zombie_health}")
        print_slow(f"Zombi sana {zombie_damage} hasar verdi. Sağlığın: {player.health}")
        time.sleep(1)
    return player.is_alive()

def run_away(player):
    if random.choice([True, False]):
        print_slow("Başarıyla kaçtın!")
        return True
    else:
        print_slow("Kaçarken zombiler tarafından yakalandın!")
        player.take_damage(random.randint(10, 30))
        return player.is_alive()

def use_inventory(player):
    if "medkit" in player.inventory:
        player.use_item("medkit")
        return True
    return False

def main():
    print_slow("Dünya zombiler tarafından istila edildi ve hayatta kalmak için mücadele ediyorsun.")
    name = input("Karakterinin adı ne?: ").strip()
    player = Character(name)
    player.add_to_inventory("medkit")  # Oyuncuya başlangıçta bir medkit ver
    print_slow(f"Merhaba {player.name}, zorlu bir maceraya başlıyorsun...")

    # Hikaye ve kararlar burada başlar
    # Örnek olarak sadece birkaç senaryo eklenmiştir
    # Gerçek bir oyun için çok daha fazla içerik ve dallanma gerekecektir

    first_choice = ask_question(
        "Ne yapmak istersin?",
        ["Keşif ekibiyle dışarı çık ve kaynak ara", "Sığınağı güçlendir ve savunmayı organize et"]
    )

    if first_choice == 1:
        print_slow("Keşif ekibine katıldın ve dışarı çıktın...")
        if encounter_zombies(player):
            print_slow("Zombilerle karşılaştın ve hayatta kalmayı başardın.")
            # Burada oyuncunun bulduğu kaynaklar ve diğer etkileşimler eklenebilir
        else:
            return
    elif first_choice == 2:
        print_slow("Sığınağı güçlendirmeye karar verdin...")
        # Sığınağı güçlendirme senaryosu burada devam eder
        # Oyuncu sığınağı güçlendirmek için kaynak toplama ve tuzak kurma gibi etkinlikler yapabilir

    # Oyunun devamı için daha fazla senaryo ve karar noktası eklenebilir

    print_slow("Hayatta kalmak için verdiğin mücadele devam ediyor...")

if __name__ == "__main__":
    main()
