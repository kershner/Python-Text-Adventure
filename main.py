import random
import rooms

# Creating class for all the 'actors' in the game
class Creature(object):
    def __init__(self, name, player_class, max_hp, hp, strength, ac, sta,
                 max_mana, mana, equipment, items, xp, back, used_item, weapon,
                 armor, combat):
        self.name = name
        self.player_class = player_class
        self.max_hp = max_hp
        self.hp = hp
        self.strength = strength
        self.ac = ac
        self.sta = sta
        self.max_mana = max_mana
        self.mana = mana
        self.equipment = equipment
        self.items = items
        self.xp = xp
        self.back = back
        self.used_item = used_item
        self.weapon = weapon
        self.armor = armor
        self.combat = combat
    level = 1
    # Method to handle a single melee attack
    def melee_attack(self, enemy):
        attack = 2 + self.strength + int(self.sta * random.random())
        damage = int(random.random() * (self.sta / 2)) + self.strength
        if attack >= enemy.ac:
            print "\n%s strikes %s with their %s for %d damage!" % \
                  (self.name, enemy.name, self.weapon, damage)
            enemy.hp -= damage
        else:
            print "\n%s missed!" % self.name
    def spells(self, enemy):
        player.back = False
        while True:
            print "\n[Heal | 4 MP] | [Fireball | 7 MP] | [Back] > "
            print " MP: %d" % player.mana
            choice = raw_input("\nSelect Spell >").lower()
            if choice == "back":
                player.back = True
                break
            elif choice == "heal":
                if player.mana < 4:
                    print "You do not have enough mana to cast Heal!"
                else:
                    self.hp += 5
                    self.mana -= 4
                    if self.hp > self.max_hp:
                        self.hp = self.max_hp
                    print "%s casts Heal and regains 5 HP!" % player.name
                    break
            elif choice == "fireball":
                if player.mana < 7:
                    print "You do not have enough mana to cast Fireball!"
                else:
                    self.mana -= 7
                    spell_damage = random.randint(10, 12)
                    enemy.hp -= spell_damage
                    print "\n%s casts Fireball! %s takes %d damage!" % \
                          (player.name, enemy.name, spell_damage)
                    break
    def inv(self):
        player.back = False
        while True:
            if len(self.equipment) < 1 and len(self.items) < 1:
                print "\nYou are not currently carrying anything."
            else:
                print "\nYou are currently carrying:"
                print "Equipment:"
                for i in self.equipment:
                    print self.equipment.index(i), i.name
                print "\nItems:"
                if len(player.items) < 1:
                    print "None"
                else:
                    for i in self.items:
                        print self.items.index(i), i.name
            choice = raw_input("\n[Equip] | [Use] | [Back] >").lower()
            if choice == "equip":
                self.change_equipment()
                if player.back:
                    continue
                else:
                    break
            elif choice == "use":
                if player.combat == True:
                    player.used_item = True
                    break
                elif player.combat == False:
                    self.use_item(spider)
                elif choice == "back":
                    continue
                else:
                    player.used_item = False
                    break
            elif choice =="back":
                player.back = True
                break
    def change_equipment(self):
        player.back = False
        while True:
            choice = raw_input("\nSelect item with its number or [Back] >").lower()
            if choice == "back":
                player.back = True
                break
            intchoice = int(choice)
            if player.weapon == self.equipment[intchoice].name or \
                            player.armor == self.equipment[intchoice].name:
                confirm = raw_input("Would you like to unequip the %s? >" %
                                    self.equipment[intchoice].name).lower()
                if "yes" in confirm:
                    self.equipment[intchoice].unequip()
                    break
            else:
                confirm = raw_input("Would you like to equip the %s? >" %
                                    self.equipment[intchoice].name).lower()
                if "yes" in confirm:
                    self.equipment[intchoice].equip()
                    break
    def use_item(self, enemy):
        player.used_item = False
        player.back = False
        while player.used_item == False:
            try:
                choice = raw_input("Select item by its number or [Back] > ").lower()
                if choice == "back":
                    player.back = True
                    break
                intchoice = int(choice)
                itemchoice = self.items[intchoice]
                confirm = raw_input("Would you like to use the %s? >" %
                                    self.items[intchoice].name).lower()
                if "yes" in confirm:
                    # These if statements are figuring out if the item chosen
                    # will add HP/Mana to the player or deal damage to the enemy
                    if itemchoice.plus_mana == 0 and itemchoice.damage == 0:
                        self.hp += itemchoice.plus_hp
                        if self.hp > self.max_hp:
                            self.hp = self.max_hp
                        raw_input("\n%s uses the %s and regains %d HP!" %
                                (self.name, itemchoice.name, itemchoice.plus_hp))
                        del self.items[intchoice]
                        player.used_item = True
                    elif itemchoice.plus_hp == 0 and itemchoice.damage == 0:
                        self.mana += itemchoice.plus_mana
                        if self.mana > self.max_mana:
                            self.mana = self.max_mana
                        raw_input("\n%s uses the %s and regains %d MP!" %
                                (self.name, itemchoice.name, itemchoice.plus_mana))
                        del self.items[intchoice]
                        player.used_item = True
                    elif itemchoice.plus_hp == 0 and itemchoice.plus_mana == 0:
                        if not player.combat:
                            raw_input("\nNothing to use %s on!" % itemchoice.name)
                        else:
                            raw_input("\n%s uses the %s on %s and deals %d damage!" %
                                (self.name, itemchoice.name, enemy.name, itemchoice.damage))
                            enemy.hp -= itemchoice.damage
                            del self.items[intchoice]
                            player.used_item = True
            except IndexError:
                print '\nYou are not currently carrying that item!'
                continue
    def status(self):
        player.back = False
        while True:
            print("\n%s\'s status:" % player.name)
            print "HP: %d, MP: %d" % (player.hp, player.mana)
            print "Strength: %d, Stamina: %d" % (player.strength, player.sta)
            print "AC: %d" % player.ac
            print "\nInventory:"
            if player.weapon == "":
                print "Weapon: None"
            else:
                print "Weapon: %s" % player.weapon
            if player.armor == "":
                print "Armor: None"
            else:
                print "Armor: %s" % player.armor
            print "\nItems:"
            if len(player.items) < 1:
                print "None"
            else:
                for i in player.items:
                    print i.name
            print "\nXP to next level: %d" % (10 - player.xp)
            print "Level %d %s" % (player.level, player.player_class)
            back = raw_input("\n[Back] >")
            if back in "back":
                player.back = True
                break
    def flee(self):
        while True:
            flee_chance = random.randint(1, 10)
            if flee_chance > 4:
                raw_input("\nYou scramble through the door behind you and flee! > ")
                raw_input("\nYou find yourself in an unfamiliar room with one untried door. > ")
                room_selector()
            else:
                raw_input("\nAs you turn to leave the monster blocks your exit!")
                break
    def levelup(self):
        self.max_hp += 5
        self.strength += 2
        self.ac += 1
        self.sta += 2
        self.max_mana += 5
        self.level += 1
        self.xp = 0
        raw_input("\n%s has gained a level!" % player.name)
    def rest(self):
        hours = random.randint(2,6)
        mp_regained = hours * .5
        raw_input("""
You spread the threadbare bedroll from your backpack on the ground before you.
Moments after you lay down, you begin to doze off. > """)
        if monster_chance():
            monster_during_rest()
        else:
            print "\nYou awaken after %d hours feeling refreshed" % hours
            if player.player_class == "mage":
                if player.hp == player.max_hp and player.mana != player.max_mana:
                    player.mana += mp_regained
                    if self.mana > self.max_mana:
                        self.mana = self.max_mana
                    print "\n%s regains %d MP!" % (player.name, mp_regained)
                elif player.hp != player.max_hp and player.mana == player.max_mana:
                    player.hp += hours
                    if self.hp > self.max_hp:
                        self.hp = self.max_hp
                    print "\n%s regains %d HP!" % (player.name, hours)
                else:
                    player.hp += hours
                    player.mana += mp_regained
                    if self.hp > self.max_hp:
                        self.hp = self.max_hp
                    if self.mana > self.max_mana:
                        self.mana = self.max_mana
                    print "\n%s regains %d HP and %d MP!" % (player.name, hours,
                                                           mp_regained)
            else:
                if player.hp != player.max_hp:
                    player.hp += hours
                    if self.hp > self.max_hp:
                        self.hp = self.max_hp
                    print "\n%s regains %d HP!" % (player.name, hours)

class Boss(object):
    def __init__(self, name, hp, ac, spells):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.spells = spells
    def attack(self, player):
        damage = random.randint(5,7)
        if random.randint(1,10) > 4:
            player.hp -= damage
            raw_input("\n%s casts %s on %s for %d damage!" % (self.name,
                        random.choice(self.spells), player.name, damage))
        else:
            raw_input("\n%s's spell fizzles!" % self.name)
    def special_attack(self, player):
        damage = random.randint(8, 15)
        if random.randint(1,10) > 4:
            player.hp -= damage
            raw_input('''
%s's eyes glaze over as an unnatural maelstrom materializes within the
chamber.  Bits of debris and intense winds tear at your body for %d damage. '''
                  % (self.name, damage))
    def transform(self):
        raw_input('''
The figure suddenly springs into the air and hovers a short ways off the
ground. Spears of light begin to radiate from its body, eroding the
surrounding skin and clothing.  You shield your eyes from an eruption of
intense light and behold the transformed figure.  A hulking demon nearly
thirty feet tall stands before you, covered in thick black fur and sporting
huge talons each the size of a long spear. > ''' % self.name)
        self.name = 'a hulking demon'
        self.hp = 25
        self.ac = 10
    def transform_attack(self, player):
        damage = random.randint(8,12)
        if random.randint(1, 10) > 4:
            player.hp -= damage
            raw_input("""
%s slashes %s with their monstrous claws for %d damage!"""
                      % (self.name, player.name, damage))
        else:
            raw_input("\n%s misses with their monstrous claws!" % self.name)
    def boss_battle(self, player):
        turn = 1
        player.combat = True
        # Victory/Death conditions
        while True:
            print "\n%s\'s HP: %d" % (player.name, player.hp)
            print "%s\'s MP: %d" % (player.name, player.mana)
            while True:
                print "\n%s\'s HP: %d" % (self.name, self.hp)
                choice = raw_input("\n[Attack] | [Spells] | [Inventory] | [Status] > ").lower()
                if choice == "attack":
                    player.melee_attack(self)
                    raw_input()
                    break
                elif choice == "spells":
                    player.spells(self)
                    if player.back:
                        continue
                    else:
                        break
                elif choice == "inventory":
                    player.inv()
                    if player.used_item == True:
                        player.use_item(self)
                        if player.used_item == False:
                            continue
                        elif player.used_item == True:
                            break
                    elif player.back:
                        continue
                    else:
                       break
                elif choice == "status":
                    player.status()
                    if player.back:
                        continue
                    else:
                        break
            if self.name == 'a mysterious figure' and self.hp <= 0:
                self.transform()
            elif self.hp < 1:
                raw_input('''
The %s is slain and the evil corruption plaguing the land has been destroyed.
\n\n\n\nGame Over''' % self.name)
            if turn % 3 == 0:
                self.special_attack(player)
            elif turn % 3 != 0 and self.name == 'a hulking demon':
                raw_input('\n%s readies their attack...' % self.name)
                self.transform_attack(player)
            elif turn == 5:
                self.transform()
            else:
                raw_input('\n%s begins to chant softly...' % self.name)
                self.attack(player)
            turn += 1
            if player.hp < 1:
                raw_input('''
%s has been slain by %s!\n\n\n\n\nGame Over. > ''' % (player.name, self.name))
                quit()

class Weapon(object):
    def __init__(self, name, attack, ac_penalty):
        self.name = name
        self.attack = attack
        self.ac_penalty = ac_penalty
    def equip(self):
        player.strength += self.attack
        player.sta += (self.attack / 2)
        player.ac -= self.ac_penalty
        player.weapon = self.name
        print "\nYou have equipped the %s." % self.name
    def unequip(self):
        player.strength -= self.attack
        player.sta -= (self.attack / 2)
        player.ac += self.ac_penalty
        player.weapon = ""
        print "\nYou have unequipped the %s." % self.name

class MagicWeapon(object):
    def __init__(self, name, attack, ac_penalty):
        self.name = name
        self.attack = attack
        self.ac_penalty = ac_penalty
    def equip(self):
        player.strength += self.attack
        player.sta += (self.attack / 2)
        player.ac -= self.ac_penalty
        player.weapon = self.name
        print "\nYou have equipped the %s." % self.name
    def unequip(self):
        player.strength -= self.attack
        player.sta -= (self.attack / 2)
        player.ac += self.ac_penalty
        player.weapon = ""
        print "\nYou have unequipped the %s." % self.name

class Armor(object):
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense
    def equip(self):
        player.ac += self.defense
        player.armor = self.name
        print "\nYou have equipped the %s." % self.name
    def unequip(self):
        player.ac -= self.defense
        player.weapon = ""
        print "\nYou have unequipped the %s." % self.name

class Item(object):
    def __init__(self, name, plus_hp, plus_mana, damage):
        self.name = name
        self.plus_hp = plus_hp
        self.plus_mana = plus_mana
        self.damage = damage

# Function to handle combat
def combat(player, enemy):
    enemy.hp = enemy.max_hp
    player.combat = True
    while True:
        print "\n%s\'s HP: %d" % (player.name, player.hp)
        print "%s\'s MP: %d" % (player.name, player.mana)
        while True:
            print "\n%s\'s HP: %d" % (enemy.name, enemy.hp)
            choice = raw_input("\n[Attack] | [Spells] | [Inventory] | [Status] | [Flee] > ").lower()
            if choice == "attack":
                player.melee_attack(enemy)
                break
            elif choice == "spells":
                player.spells(enemy)
                if player.back:
                    continue
                else:
                    break
            elif choice == "inventory":
                player.inv()
                if player.used_item == True:
                    player.use_item(enemy)
                    if player.used_item == False:
                        continue
                    elif player.used_item == True:
                        break
                elif player.back:
                    continue
                else:
                   break
            elif choice == "status":
                player.status()
                if player.back:
                    continue
                else:
                    break
            elif choice == "flee":
                player.flee()
                break
        # Victory conditions!
        if enemy.hp < 1:
            player.combat = False
            xp_gained = enemy.xp
            hp_regained = random.randint(1, 4)
            mp_regained = random.randint(1, 3)
            print "\n%s has vanquished %s!" % (player.name, enemy.name)
            if player.hp == player.max_hp and player.mp == player.max_mana:
                player.xp += xp_gained
                print "%s gains %d experience!" % (player.name, xp_gained)
                raw_input("")
            elif player.hp == player.max_hp and player.mp != player.max_mana:
                player.mana += mp_regained
                if player.mana > player.max_mana:
                    player.mana = player.max_mana
                player.xp += xp_gained
                print "%s gains %d MP and gains %d experience!" \
                  % (player.name, player.mp_regained, xp_gained)
                raw_input("")
            elif player.player_class == "mage" and player.hp == player.max_hp:
                player.mana += mp_regained
                if player.mana > player.max_mana:
                    player.mana = player.max_mana
                player.xp += xp_gained
                print "%s regains %d MP and gains %d experience!" % \
                      (player.name, mp_regained, xp_gained)
                raw_input("")
            elif player.hp != player.max_hp:
                player.hp += hp_regained
                if player.hp > player.max_hp:
                    player.hp = player.max_hp
                player.xp += xp_gained
                print "%s regains %d HP and gains %d experience!" % \
                      (player.name, hp_regained, xp_gained)
                raw_input("")
            if player.xp > 10:
                player.levelup()
            break
        raw_input("\n%s readies their attack... >" % enemy.name)
        enemy.melee_attack(player)
        # Player death
        if player.hp < 1:
            print "\n%s has vanquished %s!" % (enemy.name, player.name)
            print "\nGame Over."
            quit()

# Randomly selects the next room from the list
def room_selector():
    # When down to the final element of the list, go to final room
    if len(random_room) == 0:
        rooms.final_room()
    else:
        i = random.choice(random_room)
        random_room.remove(i)
        i()

# Randomly determine if a monster is present in a room or not
def monster_chance():
    if random.randint(1,10) > 5:
        return True
    else:
        return False

# Randomly selects a monster from the list, starts combat
def random_monster():
    i = random.choice(random_monsters)
    if len(random_monsters) == 0:
        pass
    elif player.player_class == "thief":
        print "\nYou open the door quietly and can see %s patrolling the next room." % i.name
        choice = raw_input("Do you attempt to sneak past the creature? > ").lower()
        if choice == "yes":
            stealth_chance = random.randint(1,100)
            if stealth_chance > 40:
                raw_input("\nYou slip by %s unnoticed. > " % i.name)
            else:
                random_monsters.remove(i)
                raw_input("\nYou've alerted %s!  The creature rushes toward you!" % i.name)
                combat(player, i)
        else:
            random_monsters.remove(i)
            print "\nYou rush toward %s!" % i.name
            combat(player, i)
    else:
        random_monsters.remove(i)
        raw_input("\nAs you open the door %s rushes toward you!" % i.name)
        combat(player, i)

def monster_during_rest():
    i = random.choice(random_monsters)
    print """
You abrubtly wake from your slumber to the sound of %s rushing toward you!
""" % i.name
    combat(player, i)

def loot_chance():
    chance = random.randint(1,100)
    if chance > 55:
        return True
    else:
        return False
def loot():
    loot_type = random.randint(1, 100)
    if 16 < loot_type < 95:
        i = random.choice(items)
        player.items.append(i)
        raw_input("\nYou find a %s!" % i.name)
    elif 0 < loot_type < 15:
        i = random.choice(weapons)
        player.equipment.append(i)
        raw_input("\nYou find a %s!" % i.name)
    else:
        i = random.choice(magic_weapons)
        player.equipment.append(i)
        raw_input("\nYou find a %s!" % i.name)

# Weapons - attributes are name, attack, and AC penalty
bastard_sword = Weapon("bastard sword", 4, 1)
staff = Weapon("gnarled staff", 2, 0)
dagger = Weapon("dagger", 1, 0)
spear = Weapon("spear", 3, 1)
mace = Weapon("mace", 3, 0)
two_hander = Weapon("two handed sword", 5, 2)
poleaxe = Weapon("poleaxe", 6, 3)

# Magic Weapons
magic_axe = MagicWeapon("Glowing Two-Handed Axe", 6, 2)
magic_dagger = MagicWeapon("Poisoned Dagger", 3, 0)

# Armor - attributes are name and defense
leather = Armor("leather jerkin", 2)
plate = Armor("plated mail", 4)
robes = Armor("cloth robe", 1)

# Items - attributes are name, plus_hp, plus_mana, and damage
healing_potion = Item("healing potion", 10, 0, 0)
mana_potion = Item("mana potion", 0, 10, 0)
frost_potion = Item("frost potion", 0, 0, 10)

# Monsters - attributes are: Name, class, Max HP, HP, STR, AC, STA, Max Mana, MANA
# equipment, items, xp, back, used_item, weapon, armor, combat
orc = Creature("an orc", "", 15, 15, 2, 3, 7, 0, 0, [], [], 4, False, False, "dagger", "", "")
goblin = Creature("a goblin", "", 15, 15, 2, 8, 8, 0, 0, [], [], 2, False, False, "bastard sword", "", "")
kobold = Creature("a kobold", "", 15, 15, 3, 7, 8, 0, 0, [], [], 3, False, False, "mace", "", "")
spider = Creature("a giant tarantula", "", 21, 21, 4, 6, 7, 0, 0, [], [], 3, False, False, "fangs", "", "")
player = Creature("Tyler", "", 21, 21, 2, 6, 5, 0, 0, [], [], 0, False, False, "", "", False)
sorceror = Boss('a mysterious figure', 20, 8, ['lightning strike', 'fireball', 'meteor', 'ice strike'])

# Lists of functions, objects for randomization
random_monsters = [orc, goblin, kobold, spider]
random_room = [rooms.room1, rooms.room2, rooms.room3, rooms.room4]
items = [healing_potion, mana_potion, frost_potion]
weapons = [bastard_sword, staff, dagger, spear, mace, two_hander, poleaxe]
armor = [leather, plate, robes]
magic_weapons = [magic_axe, magic_dagger]

rooms.start()