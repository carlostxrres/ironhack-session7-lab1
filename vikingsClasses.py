import random

# Los tests fallan porque están escritos en inglés, y las instrucciones estaban en español

# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} ha recibido {damage} puntos de daño"
        else:
            return f"{self.name} ha muerto en acto de combate"

    def battleCry(self):
        return "¡Odin os posee a todos!"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"Un 'Saxon' ha recibido {damage} puntos de daño"
        else:
            return f"Un 'Saxon' ha muerto en combate"

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        result = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return result
    
    def saxonAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        result = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "¡Los Vikingos han ganado la guerra del siglo!"
        elif len(self.vikingArmy) == 0:
            return "Los Sajones han luchado por sus vidas y sobreviven otro día..."
        else:
            return "Los Vikingos y los Sajones todavía están en plena batalla."
    pass