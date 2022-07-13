"""
Çoklu Kalıtım:
Bir sınıfın, birden fazla ana sınıftan kalıtım alması
"""

# Örnek:
class Ana_1:
    pass


class Ana_2:
    pass


class Alt(Ana_1, Ana_2):
    pass


# Örnek:
# Saat ve Takvim -> SaatliTakvim ikisinden kalıtım alan alt sınıf

# Saat Sınıfı
class Saat:
    """Saat'i simule eder."""

    def __init__(self, saat, dakika, saniye):
        self.__saat = saat
        self.__dakika = dakika
        self.__saniye = saniye


    def saati_kur(self, saat, dakika, saniye):
        self.__saat = saat
        self.__dakika = dakika
        self.__saniye = saniye

    def saat_kac(self):
        return '{0}:{1}:{2}'.format(self.__saat, self.__dakika, self.__saniye)


clock = Saat(0, 0, 0)
print(clock.saat_kac())
clock.saati_kur(10, 4, 28)
print(clock.saat_kac())


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


print('----- takvim ------')
takvim = Takvim(6, 11, 2019)
print(takvim.bugun_ne())
takvim.takvim_kur(16, 1, 2020)
print(takvim.bugun_ne())


# SaatliTakvim Class
class SaatliTakvim(Saat, Takvim):
    """
    Saat ve Takvimi beraber tutar.
    """
    def __init__(self, gun, ay, yil, saat, dakika, saniye):
        Saat.__init__(self, saat, dakika, saniye)
        Takvim.__init__(self, gun, ay, yil)


# bu kadar basit
print("-------------- saatli takvim --------------")
saatli_takvim = SaatliTakvim(8, 12, 2020, 16, 45, 7)
print(saatli_takvim)
print(saatli_takvim.saat_kac())
print(saatli_takvim.bugun_ne())
































