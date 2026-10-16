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
    from x import Royxat
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


if __name__ == "__main__":
    main()