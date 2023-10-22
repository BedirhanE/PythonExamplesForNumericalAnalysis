

#VERI YAPILARI

#Listeler  List()

Notlar=[90,80,50,40,65]
print(type(Notlar))

liste=["a",10.5,20]
Liste_genis=["a",10.5,20,Notlar]
print(Liste_genis)
print(len(Liste_genis))
print(type(Liste_genis))
print(type(Liste_genis[0]))
print(type(Liste_genis[3]))
print(type(Liste_genis[2]))
print(type(Liste_genis[1]))

#Liste Birleştirme işlemi.

tüm_list=[Notlar,liste,Liste_genis]
print(tüm_list)
print(len(tüm_list))
print(type(tüm_list))

#Liste elemanlarına erişmek
listem=[10,20,30,40,50]
print(listem[0])
print(listem[4])
print(listem[0:4:1])
print(listem[0:4:2])
print(listem[0:8:8])
print(tüm_list[1][1])#liste içindeki listedeki elemanı çağırma metodu

#listedeki elemanları değiştirme ,ekleme ,silme ,işlemi

örn_list=["bedirhan","büşra","ferhat","ali","fatma"]
print(örn_list)

örn_list[4]=["ayşe"] #liste içerisindeki veriyi değiştirme işlemi

print(örn_list) #yeni listeyi yazdırma

örn_list[0:3]="bedirhanın_babası","büşranın_babası","ferhatın_babası"  #örnek liste içerisindeki elemanları değiştirme
print(örn_list)

#listeye eleman ekleme işlemi

örn_list = örn_list+["kadir"] #kalıcı olarak ekleme
print(örn_list)

del örn_list[3]  #listeden eleman silme işlemi
print(örn_list)
#silme işlemini atama işlemi yaparak da yapabiliriz fakat del fonk. daha basit ve kolay



#Koşullu ifadeler

yas = 18

if yas >= 18:
    print("Ehliyet alabilirsiniz.")
else:
    print("Ehliyet alamazsınız.")
#***********************************

#Döngüler  "FOR DONGUSU"
meyveler = ["elma", "armut", "kiraz"]

for meyve in meyveler:
    print(meyve)


#"WHILE DONGUSU"

sayac = 0

while sayac < 5:
    print("Sayac:", sayac)
    sayac += 1

notlar=0
while notlar <100:
    print("sınavdan geçenler:",notlar)
    notlar+=10



#"FONKSIYON"
def toplama(a, b):
    return a + b

sonuc = toplama(5, 3)
print("Toplama Sonucu:", sonuc)


# CLASS İŞLEMLERİ
class Kitap:
    def __init__(self, baslik, yazar, sayfa_sayisi):
        self.baslik = baslik
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi

    def bilgileri_goster(self):
        print(f"Kitap Adı: {self.baslik}")
        print(f"Yazar: {self.yazar}")
        print(f"Sayfa Sayısı: {self.sayfa_sayisi}\n")


# Kitap sınıfından nesneler oluşturalım
kitap1 = Kitap("Python Programlama", "John Smith", 350)
kitap2 = Kitap("Veri Bilimi İçin Python", "Jane Doe", 450)

# Kitapların bilgilerini gösterelim
print("Kitap 1 Bilgileri:")
kitap1.bilgileri_goster()

print("Kitap 2 Bilgileri:")
kitap2.bilgileri_goster()


# /////////////////////////////////////////////////
# INHERITANCE (KALITIM)

# Üst sınıf (Soyut sınıf)
class EvcilHayvan:
    def __init__(self, isim, tur):
        self.isim = isim
        self.tur = tur

    def konus(self):
        pass


# Alt sınıf (Soyut sınıftan türetilmiş)
class Kedi(EvcilHayvan):
    def konus(self):
        return "Miyav!"


# Alt sınıf (Soyut sınıftan türetilmiş)
class Köpek(EvcilHayvan):
    def konus(self):
        return "Hav Hav!"


# Nesneleri oluştur
whiskers = Kedi("Whiskers", "Kedi")
fido = Köpek("Fido", "Köpek")

# Alt sınıfların metotlarını çağır
print(whiskers.konus())  # Kedi nesnesi, "Miyav!" çıktısı verir.
print(fido.konus())  # Köpek nesnesi, "Hav Hav!" çıktısı verir.

# iki farklı vektörel listenin çarpılmış hali

import numpy as np

# İki vektörü NumPy dizileri olarak tanımlayın
vektor1 = np.array([1, 2, 3])
vektor2 = np.array([4, 5, 6])

# Vektörlerin skalar çarpımını hesaplayın
skalar_carpim = np.dot(vektor1, vektor2)

# Sonucu yazdırın
print("Vektörlerin Skalar Çarpımı:", skalar_carpim)





























































































