# Class tanımlayalım
# docstring -> class

class Araba:
    """
    Bu araba classıdır.
    """
    marka = 'BMW'

    def calisma(self):
        print('Bu araba çalışıyor')


# marka attribute'una erişmek için
# nesne yaratmadan -> direk class ile eriştik
# print(Araba.marka)

"""
dunder (doubel underscore):
iki alt tire (__) metodalara ve attribute'lara 'dunder' adı verilir.
"""

# tanımladığımız Araba class'ının docstring'ine erişelim
# print(Araba.__doc__)

# calisma metodunun özelliği
# print(Araba.calisma)

# calisma() çağırsak ne olcaktı?
# print(Araba.calisma())

# nesne yaratmadan çağırdığmız için -> TypeError: calisma() missing 1 required positional argument: 'self'

yeni_araba = Araba()
# print(yeni_araba.marka)

# calisma() metodu çalışabilir -> nesne var
# yeni_araba.calisma()

"""
Soru 'self' parametresi nerde?
yeni_araba.calisma()

Cevap:
'self' parametresi yeni_araba'nın kendisi.
"""

# yeni_araba.calisma()

# ilk parametre 'self' ise -> Araba.calisma(yeni_araba)
# Araba.calisma(yeni_araba)


# Örnek
import math

class Cember:

    def __init__(self, yaricap):
        self.__yaricap = yaricap

    def get_yaricap(self):
        return self.__yaricap

    def set_yaricap(self, yeni_yaricap):
        if yeni_yaricap > 0:
            self.__yaricap = yeni_yaricap
        else:
            print('Yarıçap pozitif olmalı.')

    def cevre(self):
        return math.pi * self.__yaricap**2


# cember_1 = Cember(10)
# print(cember_1.get_yaricap())
# cevre = cember_1.cevre()
# print(cevre)
#
# print("------- set --------")
#
# cember_1.set_yaricap(20)
# cevre = cember_1.cevre()
# print(cevre)


# Yeni bir sınıf
class Ogrenci:
    def __init__(self, isim, yas, sinif):
        self.isim = isim
        self.yas = yas
        self.sinif = sinif


ogr = Ogrenci('Cin Ali', 8, '3-A')
print(ogr.isim)
print(ogr.yas)
print(ogr.sinif)

print("------ silme ------")

# Nesnelerin attribute'larını silelim -> del
del ogr.yas
# print(ogr.yas)

"""
Attribute Silme:
del nesne.attribute

Nesnenin Kendisini Silmek:
del nesne
"""

# Öğrenci nesnesi -> ogr -> sil
del ogr

print(ogr.ad)















