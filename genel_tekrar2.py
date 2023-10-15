

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








































































































