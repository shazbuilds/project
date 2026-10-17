class Vazifa:
    def __init__(self, matn, muhim=False):
        if matn.strip() == "":
            raise ValueError("Matn bo'sh bo'lmasin")
        self.matn = matn.strip()
        self.muhim = muhim
        self.bajarildi = False

    def bajar(self):
        self.bajarildi = True

    def __str__(self):
        if self.bajarildi:
            belgi = "[x]"
        else:
            belgi = "[ ]"
        natija = belgi + " " + self.matn
        if self.muhim:
            natija = natija + " "
        return natija
