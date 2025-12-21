import unittest

from smart_home import AkilliEv, Isik, Klima, Televizyon


class TestSmartHome(unittest.TestCase):
    def test_polymorphic_report(self) -> None:
        ev = AkilliEv()
        ev.cihaz_ekle(Isik("I1", parlaklik=10))
        ev.cihaz_ekle(Klima("K1", sicaklik=30, mod="isit"))
        ev.cihaz_ekle(Televizyon("T1", kanal=2, ses=50))

        rapor = ev.rapor()
        self.assertIn("Isik('I1')", rapor)
        self.assertIn("Klima('K1')", rapor)
        self.assertIn("Televizyon('T1')", rapor)

    def test_common_off(self) -> None:
        ev = AkilliEv()
        i = Isik("Salon")
        k = Klima("Klima")
        t = Televizyon("TV")
        for c in (i, k, t):
            c.ac()
            ev.cihaz_ekle(c)

        ev.hepsini_kapat()
        self.assertFalse(i.acik)
        self.assertFalse(k.acik)
        self.assertFalse(t.acik)


if __name__ == "__main__":
    unittest.main()
