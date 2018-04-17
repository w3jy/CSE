class Character(object):
    def __init__(self, name, health, dialogue, status, inventory, description):
        self.name = name
        self.health = health
        self.dialogue = dialogue
        self.status = status
        self.inventory = []
        self.description = description

    def attack(self, target):
        target.health -= 10


player = Character("You", 100, None, None, [], "It's You")
enemy = Character("Mr.Wiebe", 50, None, None, [], "EVIL")
player.attack(enemy)
print(enemy.health)
enemy.attack(player)
print(player.health)


def interact(self, item):

    self.interact += []