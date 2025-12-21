from __future__ import annotations

from dataclasses import dataclass, field
from abc import ABC, abstractmethod


def _clamp(value: int, low: int, high: int) -> int:
    return max(low, min(high, value))


@dataclass
class Cihaz(ABC):
    """Akıllı evdeki tüm cihazlar için temel sınıf.

    Ortak özellikler:
      - ad
      - durum (açık/kapalı)

    Ortak davranış:
      - ac()
      - kapat()
      - bilgi_ver()  -> polymorphism: alt sınıflar detay üretir
    """
    ad: str
    acik: bool = field(default=False, init=False)

    def ac(self) -> None:
        self.acik = True

    def kapat(self) -> None:
        self.acik = False

    def durum_metni(self) -> str:
        return "açık" if self.acik else "kapalı"

    def bilgi_ver(self) -> str:
        return (
            f"{self.__class__.__name__}('{self.ad}') -> {self.durum_metni()} | "
            f"{self._detay_bilgisi()}"
        )

    @abstractmethod
    def _detay_bilgisi(self) -> str:
        """Alt sınıflar kendi özel durumunu burada döndürür."""


@dataclass
class Isik(Cihaz):
    parlaklik: int = 50

    def __post_init__(self) -> None:
        self.parlaklik = _clamp(self.parlaklik, 0, 100)

    def parlaklik_ayarla(self, deger: int) -> None:
        self.parlaklik = _clamp(deger, 0, 100)

    def parlaklik_artir(self, artis: int = 10) -> None:
        self.parlaklik_ayarla(self.parlaklik + artis)

    def parlaklik_azalt(self, azalis: int = 10) -> None:
        self.parlaklik_ayarla(self.parlaklik - azalis)

    def _detay_bilgisi(self) -> str:
        return f"parlaklık=%{self.parlaklik}"


@dataclass
class Klima(Cihaz):
    sicaklik: int = 24
    mod: str = "otomatik"

    def __post_init__(self) -> None:
        self.sicaklik = _clamp(self.sicaklik, 16, 30)
        self.mod_ayarla(self.mod)

    def mod_ayarla(self, mod: str) -> None:
        mod = mod.strip().lower()
        izinli = {"sogut", "isit", "otomatik"}
        if mod not in izinli:
            raise ValueError(
                f"Geçersiz klima modu: '{mod}'. İzinli: {sorted(izinli)}"
            )
        self.mod = mod

    def sicaklik_ayarla(self, deger: int) -> None:
        self.sicaklik = _clamp(deger, 16, 30)

    def sicaklik_artir(self, artis: int = 1) -> None:
        self.sicaklik_ayarla(self.sicaklik + artis)

    def sicaklik_azalt(self, azalis: int = 1) -> None:
        self.sicaklik_ayarla(self.sicaklik - azalis)

    def _detay_bilgisi(self) -> str:
        return f"sıcaklık={self.sicaklik}°C, mod={self.mod}"


@dataclass
class Televizyon(Cihaz):
    kanal: int = 1
    ses: int = 20
    _sessizde: bool = field(default=False, init=False)

    def __post_init__(self) -> None:
        if self.kanal < 1:
            raise ValueError("Kanal 1'den küçük olamaz.")
        self.ses = _clamp(self.ses, 0, 100)

    def kanal_degistir(self, kanal: int) -> None:
        if kanal < 1:
            raise ValueError("Kanal 1'den küçük olamaz.")
        self.kanal = kanal

    def kanal_artir(self) -> None:
        self.kanal += 1

    def kanal_azalt(self) -> None:
        if self.kanal > 1:
            self.kanal -= 1

    def ses_ayarla(self, deger: int) -> None:
        self.ses = _clamp(deger, 0, 100)
        if self.ses > 0:
            self._sessizde = False

    def ses_artir(self, artis: int = 5) -> None:
        self.ses_ayarla(self.ses + artis)

    def ses_azalt(self, azalis: int = 5) -> None:
        self.ses_ayarla(self.ses - azalis)
        if self.ses == 0:
            self._sessizde = True

    def sessize_al(self) -> None:
        self._sessizde = True

    def sessizden_cik(self) -> None:
        if self.ses == 0:
            self.ses = 10
        self._sessizde = False

    def _detay_bilgisi(self) -> str:
        sessiz = "evet" if self._sessizde else "hayır"
        return f"kanal={self.kanal}, ses={self.ses}, sessizde={sessiz}"
