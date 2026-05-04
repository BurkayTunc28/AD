class Hund:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def bellen(self):
        print(self.name + "bellt gerade")

hund1 = Hund("Bello ", 12)
hund2= Hund("Gustav ", 13)

hund1.bellen()
hund2.bellen()