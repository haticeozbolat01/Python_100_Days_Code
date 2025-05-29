#Hey kodlama meraklısı! 👋 Bugün Python'ın en temel ama bir o kadar da güçlü iki fonksiyonuyla tanışacağız. Hazır mısın? İşte sihirli değneklerimiz:

# ✨ print() - Ekrana Yazdırma Sihri
# Bu fonksiyon Python'un megafonu gibi! Ona ne söylersen, direk ekrana bağırıyor:

print("Merhaba Dünya!")  # Klasikleşmiş başlangıç
print(42)  # Sayılar da yazdırabiliriz
print("🐍 Python harika!")  # Emojiler bile kullanabiliriz!

# 🎤 input() - Kullanıcıyla Sohbet
#Kullanıcıdan bilgi almak için mükemmel bir araç:

isim = input("Adınız nedir? ")  # Kullanıcıya soru soruyoruz
print(f"Hoş geldin {isim}!")  # Aldığımız cevabı kullanıyoruz

# f-string, başına f veya F eklenmiş stringlerdir ve içine değişkenleri doğrudan yerleştirebiliriz


print("🏆 Müthiş Takım İsmi Oluşturucu 🏆")
print("Merhaba,Hoş Geldiniz")

# Kullanıcıdan bilgileri alalım
sehir = input("Yaşadığınız şehir: ")
hayvan = input("En sevdiğiniz hayvan: ")
renk = input("Göz renginiz: ")

# Takım ismini oluşturalım
takim_adi = f"{sehir} {renk} {hayvan}leri"
print(f"\n⭐ Takımınızın ismi: {takim_adi} ⭐")

#İpucu: Bu projeyi geliştirmek istersen:
# Kullanıcının verdiği cevapları büyük harfe çevirebilirsin
#Rastgele renkler/hayvanlar önerebilirsin



# ENG Version
# 🐍 Python Basics: Print and Input Functions
#Hey coding enthusiast! 👋 Today we'll explore Python's two most fundamental yet powerful functions. Ready? Here are our magic wands:

# ✨ print() - The Display Magic
# This function is like Python's megaphone! Whatever you tell it, it shouts directly to the screen:

print("Hello World!")  # The classic starter
print(42)  # We can print numbers too
print("🐍 Python is awesome!")  # We can even use emojis!

#🎤 input() - Chatting with Users
# A perfect tool for getting user input:
name = input("What's your name? ")  # Asking the user a question
print(f"Welcome {name}!")  # Using the response we got

# 🎉 Fun Project: Team Name Generator
# Now let's use these two functions to create a cool team name:

print("🏆 Awesome Team Name Generator 🏆")
print("Hello and Welcome!")

# Get user information
city = input("Your city: ")
animal = input("Your favorite animal: ")
color = input("Your eye color: ")

# Create the team name
team_name = f"{city} {color} {animal}s"
print(f"\n⭐ Your team name: {team_name} ⭐")


# Bonus Tip: You can enhance this project by:
#Capitalizing user inputs automaticall
#Suggesting random colors/animals

#Now it's your turn! I can't wait to see what you'll create with these basic functions 😊
#"The journey of a thousand codes begins with a single print() statement!" 🚀