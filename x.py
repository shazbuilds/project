import json
from m import Vazifa

class Royxat:
    def __init__(self):
        self.vazifalar = []

    def __len__(self):
        return len(self.vazifalar)

    def qosh(self, matn, muhim=False):
        vazifa = Vazifa(matn, muhim)
        self.vazifalar.append(vazifa)
        return len(self.vazifalar) - 1

    def bajar(self, index):
        vazifa = self.vazifalar[index]

        if vazifa.bajarildi:
            return False

        vazifa.bajar()
        return True

    def ochir(self, index):
        del self.vazifalar[index]

    def bajarilmaganlar(self):
        natija = []

        for vazifa in self.vazifalar:
            if not vazifa.bajarildi:
                natija.append(vazifa)

        return natija

    def saqla(self, fayl="vazifalar.json"):
        data = []

        for v in self.vazifalar:
            data.append({
                "matn": v.matn,
                "muhim": v.muhim,
                "bajarildi": v.bajarildi
            })

        with open(fayl, "w") as f:
            json.dump(data, f, indent=2)

    @classmethod
    def yukla(cls, fayl="vazifalar.json"):
        r = cls()

        try:
            with open(fayl, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            return r

        for d in data:
            index = r.qosh(d["matn"], d["muhim"])

            if d["bajarildi"]:
                r.bajar(index)

        return r