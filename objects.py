import numpy as np


types = [
    "NORMAL", "FIRE", "WATER",
    "ELECTRIC", "GRASS", "ICE",
    "FIGHTING", "POISON", "GROUND",
    "FLYING", "PSYCHIC", "BUB",
    "ROCK", "GHOST", "DRAGON",
    "DARK", "STEEL", "FAIRY"
]
effects = [
    [1,1,1,1,1,1,1,1,1,1,1,1,0.5,0,1,1,.5,1],
    [1,.5,.5,1,2,2,1,1,1,1,1,2,.5,1,.5,1,2,1],
    [1,2,.5,1,.5,1,1,1,2,1,1,1,2,1,.5,1,1,1],
    [1,1,2,.5,.5,1,1,1,0,2,1,1,1,1,.5,1,1,1],
    [1,.5,2,1,.5,1,1,.5,2,.5,1,.5,2,1,.5,1,.5,1],
    [1,.5,.5,1,2,.5,1,1,2,2,1,1,1,1,2,1,.5,1],
    [2,1,1,1,1,2,1,.5,1,.5,.5,.5,2,0,1,2,2,.5],
    [1,1,1,1,2,1,1,.5,.5,1,1,1,.5,.5,1,1,0,2],
    [1,2,1,2,.5,1,1,2,1,0,1,.5,2,1,1,1,2,1],
    [1,1,1,.5,2,1,2,1,1,1,1,2,.5,1,1,1,.5,1],
    [1,1,1,1,1,1,2,2,1,1,.5,1,1,1,1,0,.5,1],
    [1,.5,1,1,2,1,.5,.5,1,.5,2,1,1,.5,1,2,.5,.5],
    [1,2,1,1,1,2,.5,1,.5,2,1,2,1,1,1,1,.5,1],
    [0,1,1,1,1,1,1,1,1,1,2,1,1,2,1,.5,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,.5,0],
    [1,1,1,1,1,1,.5,1,1,1,2,1,1,2,1,.5,1,.5],
    [1,.5,.5,.5,1,2,1,1,1,1,1,1,2,1,1,1,.5,2],
    [1,.5,1,1,1,1,2,.5,1,1,1,1,1,1,2,2,.5,1]
]

class Nature:
    def __init__(self, name, attack, defense, sp_attack, sp_defense, speed) -> None:
        self.name = name
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed

hardy = Nature("Hardy", 1, 1, 1, 1, 1)
bold = Nature("Bold", 0.9, 1.1, 1, 1, 1)
modest = Nature("Modest", 0.9, 1, 1.1, 1, 1)
calm = Nature("Calm", 0.9, 1, 1, 1.1, 1)
timid = Nature("Timid", 0.9, 1, 1, 1, 1.1)

lonely = Nature("Lonely", 1.1, 0.9, 1, 1, 1)
docile = Nature("Docile", 1, 1, 1, 1, 1)
mild = Nature("Mild", 1, 0.9, 1.1, 1, 1)
gentile = Nature("Gentile", 1, 0.9, 1, 1.1, 1)
hasty = Nature("Hasty", 1, 0.9, 1, 1, 1.1)

adamant = Nature("Adamant", 1.1, 1, 0.9, 1, 1)
impish = Nature("Impish", 1, 1.1, 0.9, 1, 1)
bashfull = Nature("Bashfull", 1, 1, 1, 1, 1)
careful = Nature("Careful", 1, 1, 0.9, 1.1 ,1)
jolly = Nature("Jolly", 1, 1, 0.9, 1, 1.1)

naughty = Nature("Naughty", 1.1, 1, 1, 0.9, 1)
lax = Nature("Lax", 1, 1.1, 1, 0.9, 1)
rash = Nature("Rash", 1, 1, 1.1, 0.9, 1)
quirky = Nature("Quirky", 1, 1, 1, 1, 1)
naive = Nature("Naive", 1, 1, 1, 0.9, 1.1)

brave = Nature("Brave", 1.1 , 1, 1, 1, 0.9)
relaxed = Nature("Relaxed", 1, 1.1, 1, 1, 0.9)
quiet = Nature("Quiet", 1, 1, 1.1, 1, 0.9)
sassy = Nature("Sassy", 1, 1, 1, 1.1, 0.9)
serious = Nature("Serious", 1, 1, 1, 1, 1)

natures =  [hardy, bold, modest, calm, 
            timid, lonely, docile, mild, 
            gentile, hasty, adamant, impish,
            careful, jolly, naughty, lax,
            rash, quirky, naive, brave,
            relaxed, quiet, sassy, serious]


class Attack:
    def __init__(self, name, type, cat, power, acc, pp, stab) -> None:
        self.name = name
        self.index_type = type
        self.type = types[self.index_type]  # Tipo
        self.cat = cat  # Categoria / clase
        self.power = power  # Poder
        self.acc = acc  # Presicion
        self.pp = pp  # Usos / puntos de poder
        self.current_pp = self.pp
        self.stab = 1.5 if stab else 1  # Bonificacion por tipo de ataque y de pokemon

    """
    Funcion para restarle puntos de poder cuando el ataque es usado
    """
    def use(self):
        self.current_pp -= 1

    def __str__(self) -> str:
        return f"""
Movimiento:         {self.name}
Tipo:               {self.type}
Clase:              {self.category}
Poder:              {self.power}
Precision:          {self.accuracy}
Puntos de Poder:    {self.pp}
"""


class Pokemon:
    def __init__(self, name, type, stats, attacks) -> None:
        self.name = name
        self.index_type = type
        self.type = types[self.index_type]  # Tipo
        # Estadisticas base
        self.hp_base = stats[0]
        self.att_base = stats[1]
        self.def_base = stats[2]
        self.sp_att_base = stats[3]
        self.sp_def_base = stats[4]
        self.speed_base = stats[5]
        self.iv = np.random.randint(0, 32, size=6)  # ?
        self.nature = np.random.choice(natures)  # Naturaleza
        self.level = 5  # Nivel inicial
        # Formulas de estadisticas
        self.hp = int((
            (((self.hp_base * 2) + self.iv[0]) * self.level) / 100) + self.level + 10)
        self.attack = int((
            ((((2 * self.att_base) + self.iv[1]) * self.level) / 100) + 5) * self.nature.attack)
        self.defense = int((
            ((((2 * self.def_base) + self.iv[2]) * self.level) / 100) + 5) * self.nature.defense)
        self.sp_att = int((
            ((((2 * self.sp_att_base) + self.iv[3]) * self.level) / 100) + 5) * self.nature.sp_attack)
        self.sp_def = int((
            ((((2 * self.sp_def_base) + self.iv[4]) * self.level) / 100) + 5) * self.nature.sp_defense)
        self.speed = int((
            ((((2 * self.speed_base) + self.iv[5]) * self.level) / 100) + 5) * self.nature.speed)
        self.attacks = attacks  # Lista de ataques
        self.effect = 1  # Valor por defecto: 1 / Varia segun enfrentamiento y tipos
        self.current_hp = self.hp  # Vida inicial
        self.experience = 100  # Experiencia inicial para nivel 5

    """
    Funcion para determinar ataque fisico o ataque especial
    """
    def att_type(self, i, enemy):
        if self.attacks[i].cat == 0:  # 0: Movimiento fisico
            a = self.attack  # Ataque propio
            d = enemy.defense  # Defensa rival
        elif self.attacks[i].cat == 1:  # 1: Movimiento especial
            a = self.sp_att  # Ataque especial propio
            d = enemy.sp_def  # Defensa especial rival
        return a, d

    """
    Funcion para calcular daño de ataque
    """
    def att_damage(self, attack, a, d) -> int:
        v = np.random.randint(85, 101)  # Variacion
        damage = .01 * attack.stab * self.effect * v * (((.2*self.level+1)*a*attack.power)/(25*d)+2)
        return damage

    """
    Funcion para ataque
    """
    def attacking(self, enemy, move):
        i = self.attacks.index(move)
        self.attacks[i].use()
        a, d = self.att_type(i, enemy)
        self.effect = effects[self.attacks[i].index_type][enemy.index_type]  # Efectividad de tipo de ataque con tipo de rival
        damage = self.att_damage(enemy.attacks[i], a, d)
        enemy.current_hp -= int(damage)
        enemy.current_hp = 0 if enemy.current_hp < 0 else enemy.current_hp
        return enemy.current_hp, damage

    """
    Funcion para cuando ataca la cpu
    """
    def attack_cpu(self, enemy):
        move = np.random.choice(self.attacks, p=(.4, .6))  # Probs de elegir el at esp antes que el normal
        return self.attacking(enemy, move)

    """
    Funcion para acuando ataca el user
    """
    def attack_user(self, enemy, move):
        return self.attacking(enemy, move)

    """
    Funcion acumular experiencia
    """
    def win_xp(self, enemy):
        xp = (enemy.experience * enemy.level * 1.5)/7
        self.experience += xp
        return self.level_up()

    """
    Funcion para aumentar de nivel
    """
    def level_up(self):
        next_level = self.level + 1
        if self.experience >= .8*(next_level**3):
            self.level += 1

    def __str__(self) -> str:  # Muestra informacion del pokemon
        return f"""
       {self.name}         
Nivel:              {self.level} - ({round(self.experience, 1)}/{.8*((self.level+1)**3)})
Tipo:               {self.type}
Naturaleza:         {self.nature.name}
PS:                 {self.hp}
Ataque:             {self.attack}
Defense:            {self.defense}
Ataque Especial:    {self.sp_attack}
Defense Especial:   {self.sp_defense}
Velocidad:          {self.speed}
"""
