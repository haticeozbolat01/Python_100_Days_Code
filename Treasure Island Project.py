# -------------------------------------------------------
# 🏴‍☠️ Treasure Island Oyunu | Türkçe Versiyon
# -------------------------------------------------------

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_ 
*******************************************************************************
''')

print("\n🎉 Hazine Adasına Hoş Geldin!")
print("🎯 Görevin: Hazineyi bulmak!\n")

yol = input("🛤️ Bir yol ayrımındasın. Hangi yöne gitmek istersin? (sol/sağ): ").lower()

if yol == "sol":
    print("\n🌊 Bir göle geldin. Ortada bir ada var.")
    gol = input("⛵ Bir tekne beklemek için 'bekle' yaz. Yüzmek için 'yüz' yaz: ").lower()

    if gol == "bekle":
        print("\n🏝️ Adaya güvenli şekilde ulaştın. Üç kapılı bir ev var.")
        kapi = input("🚪 Kırmızı, sarı ve mavi kapılar var. Hangi kapıyı seçiyorsun? ").lower()

        if kapi == "sarı":
            print("🎉 Kazandın! Hazine senin!")
        elif kapi == "kırmızı":
            print("🔥 Alevler tarafından yakıldın. Oyun Bitti.")
        elif kapi == "mavi":
            print("👹 Canavarlar tarafından yenildin. Oyun Bitti.")
        else:
            print("🚪 Geçersiz seçim. Oyun Bitti.")
    else:
        print("🐟 Alabalıklar tarafından saldırıya uğradın. Oyun Bitti.")
else:
    print("🕳️ Bir çukura düştün. Oyun Bitti.")

# -------------------------------------------------------
# 🏴‍☠️ Treasure Island Game | English Version
# -------------------------------------------------------

print("\nWelcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

road = input("You're at a crossroad. Where do you want to go? (left/right): ").lower()

if road == "left":
    print("\nYou've come to a lake. There is an island in the middle of the lake.")
    lake = input("Type 'wait' to wait for a boat or 'swim' to swim across: ").lower()

    if lake == "wait":
        print("\nYou arrive at the island unharmed. There is a house with 3 doors.")
        door = input("One red, one yellow, and one blue. Which color do you choose? ").lower()

        if door == "yellow":
            print("🎉 You win!")
        elif door == "red":
            print("🔥 Burned by fire. Game Over.")
        elif door == "blue":
            print("👹 Eaten by beasts. Game Over.")
        else:
            print("🚪 Invalid choice. Game Over.")
    else:
        print("🐟 Attacked by trout. Game Over.")
else:
    print("🕳️ You fell into a hole. Game Over.")
