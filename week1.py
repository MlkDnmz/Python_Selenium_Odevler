# Python'da Değişkenler :
# Python değişkenleri üzerinde veri depolamak için tanımladığımız sembolik isimler olarak adlandırabiliriz. 
# Python'da tanımlayacağımız değişken yapısının veri tipini belirtmemize gerek yoktur.
# Bizim yerimize python yorumlayıcısı (interpreter) tanımlamış olduğumuz değişkenin veri tipini algılıyor ve ona göre işlemlerimizi 
# gerçekleştirmemize yardımcı oluyor.

# Python projemizde değişken tanımlamak istediğimiz zaman vereceğimiz isimde sayı ile başlayamaz, boşluk bırakamaz ve özel karakter kullanamayız.
# Python diline ait özel anahtar kelimeler (keyword) yapıları kullanılarak değişken ismi belirtilemez.
# İsimlendirme esnasında küçük harfle başlanarak isimlendirilme yapılması önerilir.

# VERİ TİPLERİ 
# String (metin) veri tipleri → str
# Numerik (sayısal) veri tipleri → int, float, complex
# Sequence (sıralama) veri tipleri → list, tuple, range
# Mapping (haritalama) veri tipleri → dict
# Set veri tipleri → set, frozenset
# Boolean veri tipleri → bool

# type() fonksiyonu kullanarak herhangi bir değişkenin veri tipi öğrenilebilir.

a= "Merhaba "  #str
b= 86          #int
c= 98.85       #float
d= 42j         #complex
e= ["Melike" , "Zeynep" , "Kübra"]  #list
f= ("Melike" , "Zeynep" , "Kübra")  #tuple
g= range(25)                        #range
h= {"Adi" : "Melike","Yas" : 18 }   #dict
j= {"Melike" , "Zeynep" , "Kübra"}  #set
k= frozenset({"Melike" , "Zeynep" , "Kübra"})  #frozenset
m= True  #bool

# Int veya tamsayı veri tipi, sınırsız uzunlukta pozitif veya negatif tam sayıları ifade etmektedir.
# Float veya ondalıklı sayı veri tipi, noktadan sonra bir veya daha fazla ondalık sayı içeren pozitif veya negatif sayıları ifade etmektedir. 
# Float, ayrıca içinde e veya E barındıran tüm bilimsel sayıları tanımlarken kullanılır.
# Integer ya da float veri tipinde " " kullanılmaz , kullanılırsa pyhton bunu metin zanneder.
# Python'daki string değerler tek tırnak işareti veya çift tırnak işareti içinde ifade edilmektedir. 
# Diğer bir ifade ile 'Merhaba' ve "Merhaba" Python için aynıdır.
# Birden fazla satırda ifade edilecek bir string değer varsa değer üç çift tırnak (""") veya üç tek tırnak (''') içine alınır.
# Boolean tanımlanan değişkenler iki değerden birini döndürür: True (Doğru) veya False (Yanlış).
# Boolean karar verme aşamasında kullanılır. İlk hafleri büyük olmak zorundadır.

# String (Metin) Veri Tipleri :
# Değişkenlerimiz üzerinde char yapıların birleşmesinden meydana gelen metinsel verileri saklamak istediğimiz zaman " String " veri tipine ihtiyaç duyarız.
# strDegisken = "String Bir Metin" 
# pythonString = "Merhaba Python!"

# Numerik (Sayısal) Veri Tipleri
# Integer: Belek üzerinde 4 Byte yer kaplar. İçerisinde -2³¹ ile 2³¹-1 arasında yer alan tamsayı değerlerini barındırır.
# Float: Uzunluğu 32 bittir. Ondalıklı sayı türünde -3.4*10³⁸ ile 3.4*10³⁸ arasında değerler alır.
# Complex: Karmaşık sayılar olarak bilinen bu tipler diğer veri tiplerinden daha büyük sayıları içerisinde barındırır. 
# Bu değerler o kadar büyüktür ki iki parçadan oluşur. Reel (gerçek) ve imajiner (sanal) isimli iki kısımdan oluşur.

# integerDegisken = 100 
# floatDegisken = 128.65 
# complexDegisken = 42j 

# Sequence (Sıralama) Veri Tipleri :
# List: Python’da bileşik veri tiplerinin bir arada toplanarak çok yönlü işlemlere imkan vermesi sonucu oluşur. 
# İçerisindeki veriler virgülle ayrılır ve köşeli parantez kullanılarak tanımlanır.
# Öge koleksiyonları oluşturmamıza olanak sağlar. Güncellenebilir olmaları sebebiyle oldukça kullanışlıdır. 
# İçerisine karışık olarak her türlü veriyi bir çok kere alabilir. 

# Tuple: Liste yapılarından farklı olarak parantez kullanılarak tanımlanır. Tuple, ayrıca sadece read-only yani sadece verilerin okunmasına izin verir.
# Onun dışında listelerle aynı özellikleri taşır. İçerisine farklı türde ögeler alabilir.
# Her öge virgülle ayrılmalıdır. Düzenli yapıya sahiptir. Aynı ögeden birden fazla alabilir.
# Listelerden onu ayıran en büyük özelliği güncellenemez oluşudur.Tuple'lar ilk yapıldığı şekilde kalır.
# Listeden daha hızlı çalıştırılır.

# Set : Süslü parantezle oluşturulan öge koleksiyonlarıdır. Her ögeden yalnızca bir tane kullanılmasına izin verir.
# Tanımlanan öge tanımlanan yerde bulunmaz karışık olarak çıktı verir. 
# Değiştirilemez yapıya sahiptir. Yalnızca öge silinebilir ya da eklenebilir.

# Dict: Süslü parantezle oluşturulan öge koleksiyonlarıdır.
# Key ya da value kısmındaki metinler tırnak içerisinde yazılır.
# Key ve value arasına " : " işaretini koyarak key value arasındaki köprüyü oluştururuz.
# İçerisindeki yer alan verileri, anahtar ve bu anahtarın karşılığına gelen değerler olarak tutar. 
# Python üzerinde Dictionary olarak bilinen bu veri tipinde tanımlamalar küme parantez kullanılarak ve değer atamaları köşeli parantezler ile gerçekleştirilir.

# pyhonListe = ['Emre', 'Çelen', 23, 3.14]   #list
# pythonTuple = ('Sadece', 'Okunabilir', 'Bir', 'Yapım Var')  #tuple
# pythonDict['ad'] = "Emre"
# pythonDict['soyisim'] = "Çelen"
# Dictionary yapımıza veri eklemek istediğimiz zaman köşeli parantez kullanarak değer atamaları gerçekleştirebiliriz.
# dictValue = {'ad' : 'Muhiddin', 'soyisim' : 'Dalveren', 'yas' : 36}  #dict

#****************************************************************************************************************************************************

# Kodlama.io sitesinde yer alan metinsel ifadeler string veri tipine örnektir. --> Kurs isimleri, açıklamaları, eğitmen isimleri
# Kodlama.io sitesinde yer alan tüm tam sayılar integer veri tipine örnektir. --> Yıllar, kursların tamamlanma oranı
# Kodlama.io sitesinde yer alan ondalıklı sayılar float veri tipine örnektir. --> Kursların ne kadar süreceği 1.5 ay,2.5 ay vb
# Kodlama.io sitesinde yer alan karar verme / seçme / seçenek kısımları boolean veri tipine örnektir. --> Butonlar

tikla = "Bitir ve devam et"  #string
kullaniciTikla = "Bitir ve devam et"  #string
if kullaniciTikla == tikla :
    print("Bir sonraki bölüme yönlendiriliyorsunuz..\nLütfen bekleyiniz..")
else :
    print("Lütfen bölümü bitirdikten sonra diğer bölüme geçiniz !")


gmail = input("Gmail : ")
password = input("Password: ")

kaydedilen_gmail = "Kodlama.io@gmail.com"  #string
kaydedilen_password = "12345"              #string

entry_requirement1=  gmail == kaydedilen_gmail       #bool
entry_requirement2=  password == kaydedilen_password #bool

if entry_requirement1 :  
    if  entry_requirement2 : 
        print("Giriş başarılı\nSayfaya yönlendiriliyorsunuz..")
    else:
        print("Hatalı şifre girişi !")
else:
    print("Girilen gmaile ait kayıtlı kullanıcı bulunamadı !")

    
courses = ( "Yazılım Geliştirici Yetiştirme Kampı (JAVA + REACT)",
            "(2022) Yazılım Geliştirici Yetiştirme Kampı -JAVA",
            "Yazılım Geliştirici Yetiştirme Kampı (JavaScript)",
            "Yazılım Geliştirici Yetiştirme Kampı (C# + ANGULAR)",
            "(2023) Yazılım Geliştirici Yetiştirme Kampı - Python & Selenium",
            "Senior Yazılım Geliştirici Yetiştirme Kampı (.NET)",
            "Programlamaya Giriş İçin Temel Kurs"                              )#tuple

for course in courses:
     print(course)

Egitmen1 = "Halit Kalaycı"  #string
Egitmen2 = "Engin Demiroğ"  #string

Egitmenler = ["Engin Demiroğ","Halit Kalaycı"]  #list

for i in Egitmenler:
    print(i)
