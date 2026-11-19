#Pokemon Tamagotchi Klasse
import random
class Pokemon:
    def __init__(self, name, hp, max_hp, level=5, xp=0, freundschaft=70):
        self.name = name
        self.level = level
        self.hp = hp
        self.max_hp = max_hp
        self.xp = xp
        self.freundschaft = freundschaft

    def xp_fuer_nächstes_level(self):
        return 50 + 10 * 1.1 * self.level
#XP Schleife brauchen wir um Levelkurve direkt anzugleichen d.h. Pokemon Levelt direkt mit allen vorhandenen XP
    def xp_erhalten(self, menge):
        self.xp +=menge
        while self.xp >= self.xp_fuer_naechstes_level():
            self.xp -= self.xp_fuer_naechsten_level()
            self.level += 1
            self.max_hp += 3
            print(f"{self.name} erreicht level {self.level}!")

    def schaden_erhalten(self, menge):
        self.hp = max(0, self.hp -menge)
        if self.hp == 0:
            print(f"{self.name} wurde besiegt!")

    def heilen(self, menge):
        self.hp = min(self.max_hp, self.hp + menge)
    #Kampfamfrage wird an Broker versendet
    def kampfanfrage(self):
        pass



karnimani = Pokemon("Karnimani", 50, max_hp=50)
katapuldra = Pokemon(name="Katapuldra", hp=50, max_hp=50)
absol = Pokemon(name="Absol", hp=50, max_hp=50)
rattfratz = Pokemon(name="Rattfratz", hp=50, max_hp=50)






