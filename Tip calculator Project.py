# 🧮 Python'da Matematiksel İşlemler ve Tip Dönüşümleri
# Merhaba Python severler! Bugün tip hesaplayıcı projemiz üzerinden Python'da matematik işlemleri, veri tipleri ve tip dönüşümlerini öğreneceğiz. 🚀

# 🔍 Veri Tipi Kontrolü (type())
# Hangi veri tipinde olduğunu kontrol etmek için type() fonksiyonunu kullanabiliriz:


print(type(2.5))  # <class 'float'>
print(type(5))   # <class 'int'>
print(type("hatice")) # <class 'str'>

#Tip Dönüşümleri (Type Conversion)
# Python'da veri tipleri arasında dönüşüm yapmak çok önemlidir:

#int(): Tam sayıya dönüştürür
#float(): Ondalıklı sayıya dönüştürür
#str(): String'e dönüştürür

# String -> Sayı dönüşümü
num_str = "15"
num_int = int(num_str)  # 15 (tam sayı)
num_float = float(num_str)  # 15.0 (ondalıklı)

# Sayı -> String dönüşümü
text = str(42)  # "42"

#Projemizde çeşitli matematiksel işlemler yapıyoruz Hadi Başlayalım:

#Başlangıç ekranında kullanıcıyı selamladıktan sonra, hesaplama yapabilmek için gerekli verileri alıyoruz.
print("Bahşiş Hesaplayıcıya Hoş Geldiniz!")
fatura = float(input("Toplam fatura tutarı ne kadar? ₺"))
bahsis = int(input("Yüzde olarak ne kadar bahşiş vermek istersiniz? 10, 12 veya 15 "))
kisi = int(input("Faturayı kaç kişi bölüşeceksiniz? "))

# Hesaplamalar
bahsis_yuzdesi = bahsis / 100 # Yüzdeyi ondalığa çevirme
toplam_bahsis = fatura * bahsis_yuzdesi # Çarpma işlemi
toplam_tutar = fatura + toplam_bahsis # Toplama işlemi
kisi_basi = toplam_tutar / kisi # Bölme işlemi

# Yuvarlama İşlemi (round()): Para hesaplamalarında genellikle 2 ondalık basamak kullanırız.
son_tutar = round(kisi_basi, 2)

# String Formatlama (f-string) Sonucu güzel bir şekilde göstermek için:
print(f"\nHer bir kişi ödemesi gereken tutar: ₺{son_tutar}")

# Ekstra Bilgiler
# 📏 String Uzunluğu (len()). Bir string'in uzunluğunu ölçmek için:
message = "Hello"
print(len(message))  # 5

# 🧮 Mathematical Operations and Type Conversions in Python
# Hello Python enthusiasts! Today, we'll learn about mathematical operations, data types, and type conversions through our tip calculator project. 🚀

# 🔍 Checking Data Types (type())
# We can use the type() function to check data types:

print(type(2.5))  # <class 'float'>
print(type(5))   # <class 'int'>
print(type("hatice")) # <class 'str'>

# Type Conversion
# Converting between data types is very important in Python:

# int(): Converts to integer
# float(): Converts to floating-point number
# str(): Converts to string

# String -> Number conversion
num_str = "15"
num_int = int(num_str)  # 15 (integer)
num_float = float(num_str)  # 15.0 (float)

# Number -> String conversion
text = str(42)  # "42"

# Let's Begin Our Project Calculations:

# First we greet the user and collect necessary data for calculations
print("Welcome to the Tip Calculator!")
bill = float(input("What's the total bill amount? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15 "))
people = int(input("How many people to split the bill? "))

# Calculations
tip_percent = tip / 100 # Convert percentage to decimal
total_tip = bill * tip_percent # Multiplication
total_amount = bill + total_tip # Addition
per_person = total_amount / people # Division

# Rounding (round()): We typically use 2 decimal places for money calculations
final_amount = round(per_person, 2)

# String Formatting (f-string) To display the result nicely:
print(f"\nEach person should pay: ${final_amount}")

# Additional Information
# 📏 String Length (len()): To measure string length:
message = "Hello"
print(len(message))  # 5


