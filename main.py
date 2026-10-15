import json
import os
import unittest



class Vazifa:
    def __init__(self, matn, muhim=False):
        if matn.strip()=="":
            raise ValueError("Matn bo'sh bo'lmasin")
        self.matn = matn.strip()
        self.muhim = muhim
        self.bajarildi = False
    def bajar(self):
        self.bajarildi=True
    def __str__(self):
        if self.bajarildi:
            belgi = "[x]"
        else:
            belgi = "[ ]"
        natija = belgi + " " +self.matn
        if self.muhim:
            natija = natija + "excellent"
        return natija



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

def tanlovni_tekshir(matn, max_raqam):
    matn = matn.strip()
    if not matn.isdigit():
        return None
    n = int(matn)
    if 0 <= n <= max_raqam:
        return n
    return None
def ha_yoq(matn):
    return matn.strip().lower() in ("h", "ha")
def menyu():
    print("""
=== VAZIFALAR ===
1. Ro'yxat
2. Qo'shish
3. Bajarildi deb belgilash
4. O'chirish
5. Bajarilmaganlar
0. Chiqish
""")
def main():
    r = Royxat.yukla()
    while True:
        menyu()
        tanlov = tanlovni_tekshir(input("Tanlang: "), 5)
        try:
            if tanlov is None:
                print("0 dan 5 gacha szon kiriting")
            elif tanlov == 1:
                if not r.vazifalar:
                    print(" (ro'yxat bo'sh)")
                else:
                    index = 0
                    for v in r.vazifalar:
                        print(f"#{index} {v}")
                        index = index + 1
            elif tanlov == 2:
                matn = input("Vazifa: ")
                muhim = ha_yoq(input("Muhimmi? (h/y): "))
                index = r.qosh(matn, muhim)
                print(f"#{index} qo'shildi: {r.vazifalar[index]}")
            elif tanlov == 3:
                index = int(input("Vazifa raqami: "))
                if r.bajar(index):
                    print(f"#{index} bajarildi")
                else:
                    print("Allaqachon bajarilgan")
            elif tanlov == 4:
                index = int(input("Vazifa raqami: "))
                r.ochir(index)
                print(f"#{index} o'chirildi")
            elif tanlov == 5:
                qolgan = r.bajarilmaganlar()
                print(f"Bajarilmagan: {len(qolgan)} ta")
                for v in qolgan:
                    print(v)
            elif tanlov == 0:
                r.saqla()
                print("Saqlandi. Xayr!")
                break
        except ValueError as e:
            print(
                "Son kiriting!"
                if "invalid literal" in str(e)
                else f"Xato: {e}"
            )
        except IndexError:
            print("Bunday vazifa yo'q")


class VazifaTest(unittest.TestCase):
    def test_yangi_vazifa(self):
        v = Vazifa("Dars qilish")
        self.assertFalse(v.bajarildi)

    def test_bajar(self):
        v = Vazifa("Dars qilish")
        v.bajar()
        self.assertTrue(v.bajarildi)

    def test_bosh_matn(self):
        with self.assertRaises(ValueError):
            Vazifa("   ")


class YordamchiTest(unittest.TestCase):
    def test_tanlov(self):
        self.assertEqual(tanlovni_tekshir("3", 5), 3)
        self.assertIsNone(tanlovni_tekshir("9", 5))
        self.assertIsNone(tanlovni_tekshir("abc", 5))
    def test_ha_yoq(self):
        self.assertTrue(ha_yoq("h"))
        self.assertTrue(ha_yoq(" Ha "))
        self.assertFalse(ha_yoq("y"))


class RoyxatTest(unittest.TestCase):
    def setUp(self):
        self.r = Royxat()
        self.r.qosh("Dars qilish")

    def test_qosh(self):
        self.r.qosh("Kitob o'qish")
        self.assertEqual(len(self.r), 2)

    def test_bajar(self):
        self.assertTrue(self.r.bajar(0))
        self.assertFalse(self.r.bajar(0))

    def test_saqla_yukla(self):
            self.r.saqla("test_tmp.json")
            r2 = Royxat.yukla("test_tmp.json")
            self.assertEqual(len(r2), 1)

    def tearDown(self):
        if os.path.exists("test_tmp.json"):
            os.remove("test_tmp.json")


if __name__ == "__main__":
    main()
