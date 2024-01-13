import time
import random

class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = {'medkit': 2, 'ammo': 10}

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

    def heal(self):
        if self.inventory['medkit'] > 0:
            self.health += 50
            self.inventory['medkit'] -= 1
            if self.health > 100:
                self.health = 100
            print(f"{self.name} bir medkit kullandı ve 50 sağlık puanı kazandı.")
        else:
            print("Medkit'in kalmadı!")

    def attack(self):
        if self.inventory['ammo'] > 0:
            self.inventory['ammo'] -= 1
            return random.randint(5, 25)
        else:
            print("Mermi kalmadı!")
            return 0

    def search_for_items(self):
        found_item = random.choice(['medkit', 'ammo', 'food'])
        print(f"{self.name} bir {found_item} buldu!")
        if found_item in self.inventory:
            self.inventory[found_item] += 1
        else:
            self.inventory[found_item] = 1

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
            ["Savaş", "Kaç", "Medkit kullan", "Mermi ara"]
        )
        if action == 1:
            zombie_health = random.randint(30, 50)
            while zombie_health > 0 and player.is_alive():
                attack_damage = player.attack()
                if attack_damage:
                    print_slow(f"Zombiye {attack_damage} hasar verdin.")
                    zombie_health -= attack_damage
                if zombie_health <= 0:
                    print_slow("Zombiyi yendin!")
                    player.search_for_items()
                    break
                player.take_damage(random.randint(5, 15))
        elif action == 2:
            print_slow("Kaçmayı başardın!")
            break
        elif action == 3:
            player.heal()
        elif action == 4:
            player.search_for_items()

def main():
    print_slow("Dünya zombiler tarafından istila edildi ve hayatta kalmak için mücadele ediyorsun.")
    name = input("Karakterinin adı ne?: ").strip()
    player = Character(name)
    print_slow(f"Merhaba {player.name}, zorlu bir maceraya başlıyorsun...")

    while player.is_alive():
        print_slow("Bir sonraki hareketin ne olacak?")
        choice = ask_question(
            "Ne yapmak istersin?",
            ["Keşif yap", "Dinlen ve sağlık kazan", "Envanterini kontrol et", "Bölgeyi güçlendir"]
        )

        if choice == 1:
            encounter_zombies(player)
        elif choice == 2:
            player.heal()
        elif choice == 3:
            print(f"Envanterin: {player.inventory}")
        elif choice == 4:
            print_slow("Bölgenin savunmasını güçlendiriyorsun...")
            # Burada bölgeyi güçlendirmeyle ilgili ekstra mekanikler eklenebilir.

        time.sleep(1)

if __name__ == "__main__":
    main()
