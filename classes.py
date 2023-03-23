# class'lar referans tiptir.
# Soyutlama teknikleriyle veya inheritance gibi tekniklerle yazılımda sürdürülebilirliği sağlar.
# Pythonda diğer dillere göre daha sınırlıdır.
# class = obje
# obje : İçinde özellik barındırır. Operasyon tutucudur.

def selamVer() :
    print("Merhaba")

# Fonksiyon : İş yapan kod bloğu..

def krediHesapla() :
    print("Hesaplar yapıldı..")

krediHesapla()
krediHesapla()
krediHesapla()

# Kodlarımızı daha verimli yönetmek için classlardan yararlanıyoruz.

class Banka :
    def krediBasvur(self) :
        print("Kredi başvurusu yapıldı..")

    def krediHesapla(self) :
        print("Hesaplar yapıldı..")

# class'lar referans tiplerdir. Yazılımda sürdürülebilirliği sağlamak için çok önemlidir.
# self = this  --> Parametre olarak geçilmeli..

banka = Banka()
banka.krediBasvur()

# class Matematik :

#     def __init__(self) : 
#         print("Matematik başladı (referansı oluştu.)")
        
#     def topla(self,sayi1,sayi2) :
#         return sayi1 + sayi2 
    
#     def cikar(self,sayi1,sayi2) :
#         return sayi2 - sayi1
    
#     def carp(self,sayi1,sayi2) :
#         return sayi1 * sayi2 
    
#     def bol(self,sayi1,sayi2) :
#         return sayi2 / sayi1

# matematik = Matematik () 
# sonuc = matematik.topla(3,5)
# print("Sonuc : " + str(sonuc))

# self i kullanmak zorunlu..

class Matematik :

    def __init__(self,sayi1,sayi2) : # constructor-yapıcı
        self.sayi1 = sayi1
        self.sayi2 = sayi2
        print("Matematik başladı (referansı oluştu.)")
        
    def topla(self) :
        return self.sayi1 + self.sayi2 
    
    def cikar(self) :
        return self.sayi2 - self.sayi1
    
    def carp(self) :
        return self.sayi1 * self.sayi2 
    
    def bol(self) :
        return self.sayi2 / self.sayi1

matematik = Matematik (7,8) #instance
# referans oluşturuldu..
sonuc = matematik.topla()
print("Sonuc : " + str(sonuc))


class Person :

    def __init__(self,name,lastName) :
        self.name = name
        self.lastName = lastName

musteri1 = Person("Ahmet","Demiroğ")
musteri2 = Person("Kerem","Demiroğ")
musteri3 = Person("İlker","Demiroğ")

print(musteri1.name)
