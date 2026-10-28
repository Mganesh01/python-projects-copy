class Player:
    # Player details / properties
    name = ""
    health = 100
    weapons = []

    # Player actions / methods
    def shoot(self):
        print("Player is shooting!")

    def heal(self):
        print("Player is healing!")



# Class tho multiple Players ni create chestham
player1 = Player()
player2 = Player()
player3 = Player()

# Veetini Objects antaru
print(player1)
print(player2)
print(player3)


class Player:
    # Player details
    name = ""
    health = 100
    weapon = ""

    # Player actions
    def shoot(self):
        print("Player is shooting")

    def heal(self):
        print("Player is healing")


# Class tho actual Players ni create chestham
player1 = Player()
player2 = Player()

# Ivi Class nundi create ayina Objects
print(player1)
print(player2)




# 👨‍💻 Manam oka MunnaBhai class create chesam
class MunnaBhai:
    # 🤝 Munna Bhai help chesthadu
    def help(self):
        print("Munna Bhai is helping! 🤝")

    # 🗣️ Munna Bhai matladathadu
    def talk(self):
        print("Munna Bhai is talking! 🗣️")

    # 💪 Munna Bhai fight chesthadu
    def fight(self):
        print("Munna Bhai is fighting! 😂🔥")



# 👤 Munna Bhai object create chesam
munna = MunnaBhai()

# Munna Bhai actions call chesthunnam
munna.help()
munna.talk()
munna.fight()


class MunnaBhai:
    # self = current object
    def talk(self):
        print("Munna Bhai is talking 🗣️")

# 👤 Object create chesam
munna = MunnaBhai()
# munna object talk() call chesthundi
munna.talk()
# Inside talk():
# self → munna object ni refer chestundi



class MunnaBhai:
    def fight(self):
        # 👈 self = current object
        print("Fight started by:", self)

# 👤 Munna Bhai object create chesam
munna = MunnaBhai()
# Munna object fight() call chesthundi
munna.fight()
# 🎯 Ikkada:
# munna → actual object
# self  → munna object ni refer chestundi



class MunnaBhai:
    def __init__(self, name):
        self.name = name

    # 👤 Instance Method
    # self → current object
    def talk(self):
        print(self.name, "is talking 🗣️")
# Object create chesam
munna = MunnaBhai("Munna Bhai")
# Object data ni use chestundi
munna.talk()


class MunnaBhai:
    # 🏫 Class data
    hospital = "Sanjay Gandhi Hospital"
    # 🏫 Class Method
    @classmethod
    def show_hospital(cls):
        # cls → current class
        print("Hospital:", cls.hospital)

# Class Method call
MunnaBhai.show_hospital()



class MunnaBhai:
    # ⚡ Static Method
    @staticmethod
    def say_hello():
        # No self
        # No cls
        print("Gandhigiri ki Jai! 😂🔥")

# Static Method call
MunnaBhai.say_hello()




