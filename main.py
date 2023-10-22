#----Numerical Analysis Dersi için Python genel tekrar Notları----

#Değişkenler ve Veri Türleri:

x = 5  # Bir tamsayı (int) değişkeni tanımlama
y = 3.14  # Bir ondalık sayı (float) değişkeni tanımlama
ad = "Bedirhan"  # Bir metin (string) değişkeni tanımlama.

#Koşullu İfadeler:
if x > 0:
    print("x pozitif")
elif x < 0:
    print("x negatif")
else:
    print("x sıfır")

#Döngüler
for i in range(5):
    print(i)  # 0'dan 4'e kadar sayıları yazdırır.

while x > 0:
    print(x)
    x -= 1

#Liste
my_list = [1, 2, 3, 4, 5]

#Fonksiyon
def toplama(a, b):
    return a + b

sonuc = toplama(3, 4)  # 3 ile 4'ü toplar ve sonucu döndürür

#Modül
import math
x = math.sqrt(25)  # 25'in karekökünü hesaplar.

