class Job:
    #Variables
    name = "None"
    health = 0
    magic = 0
    strength = 0;
    dexterity = 0;
    intellect = 0;
    movement_speed = 0;
    attack_speed = 0;

#Magic
class Alchemist(Job):
    def __init__(self):
        super().__init__(health=0, magic=3, strength=0, dexterity=1, intellect=2, movement_speed=0, attack_speed=0)

class Mage(Job):
    def __init__(self):
        super().__init__(health=0, magic=5, strength=0, dexterity=0, intellect=3, movement_speed=0, attack_speed=0)

class Cleric(Job):
    def __init__(self):
        super().__init__(health=0, magic=4, strength=0, dexterity=0, intellect=4, movement_speed=0, attack_speed=0)

#Meelee
class Brawler(Job):
    def __init__(self):
        super().__init__(health=10, magic=0, strength=3, dexterity=0, intellect=0, movement_speed=0, attack_speed=0)

class Martial_Artist(Job):
    def __init__(self):
        super().__init__(health=0, magic=0, strength=2, dexterity=2, intellect=0, movement_speed=0, attack_speed=0)

class Tank(Job):
    def __init__(self):
        super().__init__(health=30, magic=0, strength=4, dexterity=-2, intellect=0, movement_speed=0, attack_speed=0)

class Dualist(Job):
    def __init__(self):
        super().__init__(health=0, magic=0, strength=2, dexterity=2, intellect=0, movement_speed=0, attack_speed=0)

#Stealth
class Illusionist(Job):
    def __init__(self):
        super().__init__(health=0, magic=1, strength=0, dexterity=1, intellect=2, movement_speed=0, attack_speed=0)

class Bard(Job):
    def __init__(self):
        super().__init__(health=0, magic=2, strength=0, dexterity=1, intellect=2, movement_speed=0, attack_speed=0)

class Thief(Job):
    def __init__(self):
        super().__init__(health=0, magic=0, strength=0, dexterity=4, intellect=0, movement_speed=0, attack_speed=0)

#Ranged
class Bowman(Job):
    def __init__(self):
        super().__init__(health=0, magic=0, strength=1, dexterity=3, intellect=0, movement_speed=0, attack_speed=0)

class Crossman(Job):
    def __init__(self):
        super().__init__(health=0, magic=0, strength=3, dexterity=2, intellect=0, movement_speed=0, attack_speed=0)

class Slingman(Job):
    def __init__(self):
        super().__init__(health=0, magic=0, strength=1, dexterity=4, intellect=0, movement_speed=0, attack_speed=0)

class Character:
    #Variables
    name = "None"
    job = "None"
    health = 0
    magic = 0
    strength = 0;
    dexterity = 0;
    intellect = 0;
    movement_speed = 0;
    attack_speed = 0;

    #Constructors
    def __init__(self, health, magic, strength, dexterity, intellect, movement_speed, attack_speed):
        self.health = health
        self.magic = magic
        self.strength = strength
        self.dexterity = dexterity
        self.intellect = intellect
        self.movement_speed = movement_speed
        self.attack_speed = attack_speed

    # Getters
    def get_health(self): return self.health
    def get_magic(self): return self.magic
    def get_strength(self): return self.strength
    def get_dexterity(self): return self.dexterity
    def get_intellect(self): return self.intellect
    def get_movement_speed(self): return self.movement_speed

    # Setters
    def set_health(self, health): self.health = health
    def set_magic(self, magic): self.magic = magic
    def set_strength(self, strength): self.strength = strength
    def set_dexterity(self, dexterity): self.dexterity = dexterity
    def set_intellect(self, intellect): self.intellect = intellect
    def set_movement_speed(self, movement_speed): self.movement_speed = movement_speed
    def set_job(self, Job):
        if self.job == "None":
            self.health += Job.health
            self.magic += Job.magic
            self.strength += Job.strength
            self.dexterity += Job.dexterity
            self.intellect += Job.intellect
            self.movement_speed += Job.movement_speed
            self.attack_speed += Job.attack_speed
        else:
            print("Job is already set?")
        pass

    #Print
    def print_stats(self):
        print("Name: ", self.name)
        print("Job: ", self.job)
        print("Health: ", self.health) 
        print("Magic: ", self.magic) 
        print("Strength: ", self.strength )
        print("Dexterity: ", self.dexterity )
        print("Intellect: ", self.intellect )
        print("Movement_speed: ", self.movement_speed )
        print("Attack_speed: ", self.attack_speed )

class Human(Character):
    def __init__(self):
        super().__init__(health=100, magic=2, strength=3, dexterity=3, intellect=3, movement_speed=3, attack_speed=1)

class Elf(Character):
    def __init__(self):
        super().__init__(health=80, magic=4, strength=1, dexterity=2, intellect=5, movement_speed=5, attack_speed=1)

class Ogre(Character):
    def __init__(self):
        super().__init__(health=140, magic=1, strength=6, dexterity=2, intellect=1, movement_speed=1, attack_speed=1)

class Cursed(Character):
    def __init__(self):
        super().__init__(health=70, magic=3, strength=2, dexterity=4, intellect=4, movement_speed=3, attack_speed=1)

class Dwarf(Character):
    def __init__(self):
        super().__init__(health=110, magic=2, strength=4, dexterity=2, intellect=2, movement_speed=2, attack_speed=1)

#If not imported directly as module
if __name__ == "__main__":
    foo = Ogre()
    bar = Cursed()
    print(foo)
    print(bar)
    print("Foo health: ", foo.print_stats(), "\n")
    foo.set_job(Brawler())
    print("Foo health: ", foo.print_stats(), "\n")
