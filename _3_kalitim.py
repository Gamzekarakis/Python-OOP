"""

Ana Sınıf (Base Class)
    - Alt Sınıf 1 (Child Class)
    - Alt Sınıf 2 (Child Class)

"""


class AnaSinif:
    # Ana Sınıfın Özellikleri
    pass


class AltSinif1(AnaSinif):
    # Ana Sınıfın Özellikleri
    # Alt Sınıf 1 'in Özellikleri
    pass


class AltSinif2(AnaSinif):
    # Ana Sınıfın Özellikleri
    # Alt Sınıf 2 'in Özellikleri
    pass


# Örnek -> Şekil

import math


# super class
class Sekil(object):
    """Şekiller için super class"""
    def __init__(self, renk='kırmızı'):
        self.renk = renk


# sub class -> Daire
class Daire(Sekil):
    """Daire sınıfı, Şekil sınıfından kalıtım alır."""
    def __init__(self, yaricap, renk='mavi'):
        super().__init__(renk=renk)
        self.yaricap = yaricap

    def alan(self):
        return math.pi ** self.yaricap**2


# sub class -> Dikdörtgen
class Dikdortgen(Sekil):
    """Dikdörtgen sınıfı"""
    def __init__(self, kisa=1.0, uzun=1.0, renk='turuncu'):
        super().__init__(renk=renk)
        self.kisa = kisa
        self.uzun = uzun

    def alan(self):
        return self.kisa * self.uzun


# sub class -> Kare
class Kare(Sekil):
    """Kare sınıfı"""
    def __init__(self, kenar=1.0, renk='beyaz'):
        super().__init__(renk=renk)
        self.kenar = kenar

    def alan(self):
        return self.kenar**2


# nesneler yarat

# Sekil
se = Sekil('mor')
print("Sekil nesnesi olan se'nin rengi: ", se.renk)

# Daire
da = Daire(yaricap=5)
print("Daire nesnesi olan da'nin yaricap: ", da.yaricap)

# Dairenin rengi
print("Daire nesnesi olan da'nin rengi: ", da.renk)
# AttributeError: 'Daire' object has no attribute 'renk'
# Daireyi yaratırken -> super().__init__() metodunu çağırmadık -> self.renk oluşmadı
# super().__init__() -> renk vermediğim için -> kırmızı
# super().__init__(renk=renk) -> renk mavi

# Dikdörtgen
dk = Dikdortgen(kisa=2, uzun=8, renk='sarı')
print("Dikdortgen nesnesi olan dk'nin rengi: ", dk.renk)

print('Dikdörtgenin alanı: ', dk.alan())


"""
object Class'ı:
Python'da bütün class'ların atası, 'object' class'ıdır.
Tüm sınıflar 'object' sınıfından gelir.
"""

# class Sekil:   =>   class Sekil(object):

print("Sekil sınıfı, object sınıfının alt sınıfı mı?: ", isinstance(se, object))


# issubclass()
# Kare, Sekil'in alt sınıfı mı?
print("Kare, Sekil'in alt sınıfı mı?: ", issubclass(Kare, Sekil))











