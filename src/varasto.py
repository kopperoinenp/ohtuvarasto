class Varasto:
    def __init__(self, tilavuus: float, alku_saldo: float = 0.0):
        # Tilavuus ei voi olla negatiivinen
        self.tilavuus = max(0.0, tilavuus)

        # Saldo ei voi olla negatiivinen eikä ylittää tilavuutta
        if alku_saldo < 0.0:
            self.saldo = 0.0
        else:
            self.saldo = min(alku_saldo, self.tilavuus)

    def paljonko_mahtuu(self) -> float:
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara: float) -> None:
        if maara < 0:
            # ei tehdä mitään
            return
        self.saldo = min(self.tilavuus, self.saldo + maara)

    def ota_varastosta(self, maara: float) -> float:
        if maara < 0:
            return 0.0
        otettava = min(maara, self.saldo)
        self.saldo -= otettava
        return otettava

    def __str__(self) -> str:
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
