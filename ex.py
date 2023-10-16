def toplama(a, b):
    sonuc = a + b
    return sonuc

x = 5
y = 3
toplam = toplama(x, y)

print("Toplam:", toplam)

##################################################
def ardışık_toplam(n):
    toplam = 0
    for i in range(1, n + 1):
        toplam += i
    return toplam

sayı = 10
toplam = ardışık_toplam(sayı)
print(f"1'den {sayı}'e kadar olan sayıların toplamı: {toplam}")

############################################################
def asal_mı(sayı):
    if sayı <= 1:
        return False
    for i in range(2, int(sayı ** 0.5) + 1):
        if sayı % i == 0:
            return False
    return True

sayı = 17
if asal_mı(sayı):
    print(f"{sayı} bir asal sayıdır.")
else:
    print(f"{sayı} bir asal sayı değildir.")
