from __future__ import annotations

from .home import AkilliEv
from .devices import Isik, Klima, Televizyon


def demo() -> None:
    ev = AkilliEv()

    salon_isik = Isik("Salon Işığı", parlaklik=70)
    klima = Klima("Salon Klima", sicaklik=23, mod="sogut")
    tv = Televizyon("Salon TV", kanal=5, ses=25)

    ev.cihaz_ekle(salon_isik)
    ev.cihaz_ekle(klima)
    ev.cihaz_ekle(tv)

    salon_isik.ac()
    klima.ac()
    tv.ac()

    salon_isik.parlaklik_artir(15)
    klima.sicaklik_azalt(2)
    tv.kanal_artir()
    tv.sessize_al()

    print(ev.rapor())

    print("\nHepsini kapatıyoruz...")
    ev.hepsini_kapat()
    print(ev.rapor())


if __name__ == "__main__":
    demo()
