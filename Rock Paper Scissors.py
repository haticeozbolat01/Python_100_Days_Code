import random  # Rastgele sayı üretmek için gerekli / For generating random numbers

# Taş görseli / Rock ASCII art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Kağıt görseli / Paper ASCII art
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

# Makas görseli / Scissors ASCII art
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Seçenekleri liste halinde tutuyoruz / Store the options in a list
game_images = [rock, paper, scissors]

# Kullanıcıya seçim yapması için mesaj göster / Show message to the user
print("Ne seçiyorsun? (0 = Taş / Rock, 1 = Kağıt / Paper, 2 = Makas / Scissors)")

# Kullanıcının girişini al / Take input from the user
user_input = input("Seçiminizi yazın (0, 1, 2):\nEnter your choice (0, 1, or 2): ")

# Girilen verinin rakam olup olmadığını kontrol et / Check if input is a digit
if user_input.isdigit():  # e.g. "1", "2" gibi string sayı mı?
    user_choice = int(user_input)  # Sayıya çevir / Convert input to integer

    # Girilen sayı geçerli aralıkta mı (0,1,2)? / Is it in valid range?
    if user_choice >= 0 and user_choice <= 2:
        # Oyuncunun seçtiği şekli yazdır / Show the user's choice
        print("\nSenin seçimin / Your choice:")
        print(game_images[user_choice])  # Seçime göre taş/kağıt/makas ASCII çizimi

        # Bilgisayarın seçimi / Computer randomly selects 0, 1 or 2
        computer_choice = random.randint(0, 2)

        # Bilgisayarın seçimini yazdır / Show computer's choice
        print("Bilgisayarın seçimi / Computer chose:")
        print(game_images[computer_choice])

        # Oyun sonuçlarını kontrol et / Compare choices and determine result
        if user_choice == computer_choice:
            print("Berabere! 🤝\nIt's a draw! 🤝")
        elif user_choice == 0 and computer_choice == 2:
            print("Kazandın! 🏆 Taş makası yener.\nYou win! 🏆 Rock beats scissors.")
        elif user_choice == 2 and computer_choice == 0:
            print("Kaybettin! 😢 Taş makası yener.\nYou lose! 😢 Rock beats scissors.")
        elif user_choice > computer_choice:
            print("Kazandın! 🥳\nYou win! 🥳")  # Örn: Kağıt (1) makası (2) yener
        else:
            print("Kaybettin! 😔\nYou lose! 😔")  # Diğer tüm kaybetme durumları

    else:
        # Kullanıcı 0,1,2 dışında bir sayı girdiyse / If input is a number but not 0–2
        print("Geçersiz sayı girdiniz. Lütfen 0, 1 veya 2 girin.\nInvalid number. Please enter 0, 1, or 2.")
else:
    # Kullanıcı harf veya sembol girdiyse / If input is not a number at all
    print("Geçersiz giriş. Lütfen sadece rakam girin.\nInvalid input. Please enter only numbers.")

