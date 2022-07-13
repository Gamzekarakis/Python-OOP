"""
Çek Seviyeli Kalıtım:
Anneanne -> Anne -> Çocuk
"""

class AnneAnne(object):
    # AnneAnne'nin özellikleri
    pass

class Anne(AnneAnne):
    # AnneAnne'nin özellikleri
    # Anne'nin kendi özellikleri
    pass

class Cocuk(Anne):
    # AnneAnne'nin özellikleri
    # Anne'nin özellikleri
    # Çocuğun özellikleri
    pass


# Örnek:
# Saat de KumSaati'nden kalıtım alsın
# Saat ve Takvim -> SaatliTakvim ikisinden kalıtım alan alt sınıf

# Kum Saati
class KumSaati(object):
    def __init__(self):
        self.kum_saati_baslasin()

    def kum_saati_baslasin(self):
        print('Kum Saati başladı')



# Saat Sınıfı
class Saat(KumSaati):
    """Saat'i simule eder."""
    def __init__(self, saat, dakika, saniye):
        super().__init__()
        self.saati_kur(saat, dakika, saniye)

    def saati_kur(self, saat, dakika, saniye):
        self.__saat = saat
        self.__dakika = dakika
        self.__saniye = saniye

    def saat_kac(self):
        return '{0}:{1}:{2}'.format(self.__saat, self.__dakika, self.__saniye)

    def kum_saati_baslasin(self):
        print('Kum Saati başladı - Saatinden içinden')


# Takvim Class'ı
class Takvim(object):
    """Takvimi simule eder."""
    def __init__(self, d, m, y):
        self.takvim_kur(d, m, y)

    def takvim_kur(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    def bugun_ne(self):
        return '{d}:{m}:{y}'.format(d=self.d, m=self.m, y=self.y)


# Saatli Takvim
class SaatliTakvim(Saat, Takvim):
    def __init__(self, gun, ay, yil, saat, dakika, saniye):
        Saat.__init__(self, saat, dakika, saniye)
        Takvim.__init__(self, gun, ay, yil)


# SaatliTakvim
saatli_takvim = SaatliTakvim(12, 1, 2020, 13, 25, 48)
saatli_takvim.kum_saati_baslasin()

"""
Soru: Eğer aynı metod bir kaç atada varsa, hangisini çalıştırır?
Cevap: En yakın atasından başlayarak çağırır.
Method Resolution Order -> MRO
"""

# Class'ların Method Resolution Order -> MRO
print("MRO:", SaatliTakvim.__mro__)
for m in SaatliTakvim.__mro__:
    print(m)
