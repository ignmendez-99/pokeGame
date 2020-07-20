class Pokemon:
    HP = attack = defense = specialAttack = specialDefense = speed = 0

    def __init__(self, name, level,
                 baseHP, baseAttack, baseDefense, baseSpecialAttack, baseSpecialDefense, baseSpeed):
        self.name = name
        self.level = level
        # BASE STATS (we store them to make future calculations)
        self.baseHP = baseHP
        self.baseAttack = baseAttack
        self.baseDefense = baseDefense
        self.baseSpecialAttack = baseSpecialAttack
        self.baseSpecialDefense = baseSpecialDefense
        self.baseSpeed = baseSpeed
        # REAL STATS
        self.calculateStats()

    # called each time our Pokemon levels up
    def calculateStats(self):
        self.HP                 = 10 + (float(self.level) / 100.0 * float(self.baseHP * 2)) + self.level
        self.attack             = 5 + (float(self.level) / 100.0 * float(self.baseAttack * 2))
        self.defense            = 5 + (float(self.level) / 100.0 * float(self.baseDefense * 2))
        self.specialAttack      = 5 + (float(self.level) / 100.0 * float(self.baseSpecialAttack * 2))
        self.baseSpecialDefense = 5 + (float(self.level) / 100.0 * float(self.baseSpecialDefense * 2))
        self.speed              = 5 + (float(self.level) / 100.0 * float(self.baseSpeed * 2))
