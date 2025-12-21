from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

from .devices import Cihaz


@dataclass
class AkilliEv:
    """Cihazları bir arada yöneten sınıf.

    Burada polymorphism şovu:
      - Aynı listede farklı alt sınıflar durur (Isik/Klima/Televizyon)
      - tek tip arayüzle (kapat(), bilgi_ver()) yönetilir
    """
    cihazlar: List[Cihaz] = field(default_factory=list)

    def cihaz_ekle(self, cihaz: Cihaz) -> None:
        self.cihazlar.append(cihaz)

    def cihaz_bul(self, ad: str) -> Optional[Cihaz]:
        ad_kucuk = ad.strip().lower()
        for c in self.cihazlar:
            if c.ad.strip().lower() == ad_kucuk:
                return c
        return None

    def hepsini_kapat(self) -> None:
        for c in self.cihazlar:
            c.kapat()

    def rapor(self) -> str:
        if not self.cihazlar:
            return "Evde cihaz yok. (Koskoca akıllı ev, bomboş bir evren.)"
        satirlar = ["Akıllı Ev Durum Raporu:"]
        for c in self.cihazlar:
            satirlar.append(f" - {c.bilgi_ver()}")
        return "\n".join(satirlar)
