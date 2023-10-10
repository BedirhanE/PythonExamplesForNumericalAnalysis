
#pythonda bir önceki örneğe göre daha kapsamlı ve daha karmaşık bir örnek


import random

# Bir sınıf tanımladım
class Ogrenci:
    # Sınıfın özelliklerini belirme yaptığım kısım
    def __init__(self, isim, soyisim, numara):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.notlar = [] # Boş bir liste oluşturuyoruz

    # Sınıfın metodlarını tanımladım
    def not_ekle(self, notu):
        # Bir hata yakalama bloğu kullanıyoruz
        try:
            # Notun sayısal bir değer olduğunu kontrol ediyoruz
            assert isinstance(notu, int) or isinstance(notu, float)
            # Notun 0 ile 100 arasında olduğunu kontrol ediyoruz
            assert 0 <= notu <= 100
            # Notu listeye ekliyoruz
            self.notlar.append(notu)
        except AssertionError:
            # Hata mesajı veriyoruz
            print("Not geçerli bir değer değil!")

    def ortalama_hesapla(self):
        # Notların ortalamasını hesaplıyoruz
        toplam = sum(self.notlar)
        adet = len(self.notlar)
        if adet > 0:
            ortalama = toplam / adet
            return ortalama
        else:
            return 0

    def __str__(self):
        # Sınıfın string temsilini döndürüyoruz
        return f"{self.isim} {self.soyisim} ({self.numara})"

# Bir fonksiyon tanımladım
def ogrenci_olustur():
    # Rastgele isim ve soyisim seçiyoruz
    isimler = ["Ali", "Ayşe", "Mehmet", "Fatma", "Ahmet", "Zeynep"]
    soyisimler = ["Yılmaz", "Demir", "Kaya", "Çelik", "Öztürk", "Şahin"]
    isim = random.choice(isimler)
    soyisim = random.choice(soyisimler)
    # Rastgele bir numara oluşturuyoruz
    numara = random.randint(1000, 9999)
    # Bir öğrenci nesnesi oluşturuyoruz
    ogrenci = Ogrenci(isim, soyisim, numara)
    return ogrenci

# Bir sözlük oluşturdum
ogrenciler = {}

# Bir dosya açıyoruz
with open("ogrenciler.txt", "w") as dosya:
    # Dosyaya başlık yazıyoruz
    dosya.write("İsim\tSoyisim\tNumara\tOrtalama\n")
    # 10 tane öğrenci oluşturuyoruz ve sözlüğe ekliyoruz
    for i in range(10):
        ogrenci = ogrenci_olustur()
        ogrenciler[ogrenci.numara] = ogrenci
        # Her öğrenciye rastgele 3 tane not veriyoruz
        for j in range(3):
            notu = random.randint(0, 100)
            ogrenci.not_ekle(notu)
        # Öğrencinin bilgilerini ve ortalamasını dosyaya yazıyoruz
        dosya.write(f"{ogrenci.isim}\t{ogrenci.soyisim}\t{ogrenci.numara}\t{ogrenci.ortalama_hesapla()}\n")

# Sözlükteki öğrencileri ekrana yazdırıyoruz
for numara, ogrenci in ogrenciler.items():
    print(f"{numara}: {ogrenci}")