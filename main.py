import random
import rooms


class Player(object):
    def __init__(self, name, player_class, max_hp, hp, strength, ac, sta,
                 max_mana, mana, equipment, items, gold, xp, back, used_item,
                 weapon, armor, combat, special, room):
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
        self.gold = gold
        self.xp = xp
        self.back = back
        self.used_item = used_item
        self.weapon = weapon
        self.armor = armor
        self.combat = combat
        self.special = special
        self.room = room
    level = 1

    def attack(self, enemy):
        """Attack method for fighter class."""
        player.back = False
        while True:
            print '\n[Weapon] | [Gut] punch | [Back]'
            choice = raw_input('Select Attack > ').lower()
            if choice == 'back':
                player.back = True
                break
            elif choice in 'weapon':
                self.melee_attack(enemy)
                break
            elif choice == 'gut':
                if player.special < 1:
                    raw_input('\nYou can\'t get a good shot at their stomach!')
                    continue
                else:
                    player.special -= 2
                    enemy.stunned = 2
                    damage = random.randint(1, 3)
                    enemy.hp -= damage
                    raw_input('\n%s punches %s in the stomach for %d damage!'
                              ' %s doubles over in pain.'
                              % (self.name, enemy.name, damage, enemy.name))
                break

    def melee_attack(self, enemy):
        """Basic melee attack for all classes."""
        attack = 2 + self.strength + int(self.sta * random.random())
        damage = int(random.random() * (self.sta / 2)) + self.strength
        if attack >= enemy.ac:
            raw_input('\n%s strikes %s with their %s for %d damage!' %
                     (self.name, enemy.name, self.weapon, damage))
            enemy.hp -= damage
        else:
            print '\n%s missed!' % self.name

    def thievery(self, enemy):
        """Handles additional options for thieves in combat."""
        player.back = False
        while True:
            choice = raw_input('\n[Steal] | [Backstab] | [Back] > ').lower()
            if choice == 'back':
                player.back = True
                break
            elif choice == 'steal':
                if random.randint(0, 10) > 2:
                    loot_type = random.randint(1, 100)
                    if loot_type > 65:
                        gold = random.randint(1, 15)
                        player.gold += gold
                        raw_input('\nYou successfully steal %d gold!' % gold)
                        break
                    elif 16 < loot_type < 65:
                        i = random.choice(items)
                        player.items.append(i)
                        raw_input('\nYou successfully steal a %s!' % i.name)
                        break
                    elif 0 < loot_type < 15:
                        i = random.choice(weapons)
                        player.equipment.append(i)
                        raw_input('\nYou successfully steal a %s!' % i.name)
                        break
                    else:
                        i = random.choice(magic_items)
                        player.equipment.append(i)
                        raw_input('\nYou successfully steal a %s!' % i.name)
                        break
                else:
                    raw_input('\nThe creature catches you rifling through its '
                              'things!')
                    break
            elif choice == 'backstab':
                if player.special < 1:
                    raw_input('\nYou are too exhausted to attempt another '
                              'backstab!')
                else:
                    raw_input('\nYou attempt to maneuver behind the creature...')
                    attack = 5 + self.strength + int(self.sta * random.random())
                    damage = int(random.random() * (self.sta / 2)) + self.strength + 10
                    if attack >= enemy.ac:
                        raw_input('\n%s backstabs %s with their %s for %d damage!' %
                                 (self.name, enemy.name, self.weapon, damage))
                        enemy.hp -= damage
                        player.special -= 1
                        break
                    else:
                        print '\n%s missed!' % self.name
                        player.special -= 1
                        break

    def spells(self, enemy):
        """Spells menu that only mages have access to."""
        player.back = False
        while True:
            print '\n[Heal | 4 MP] | [Fireball | 7 MP] | [Stun | 10 MP]' \
                  ' | [Back] > '
            print ' MP: %d' % player.mana
            choice = raw_input('\nSelect Spell > ').lower()
            if choice == 'back':
                player.back = True
                break
            elif choice == 'heal':
                if player.mana < 4:
                    print 'You do not have enough mana to cast Heal!'
                else:
                    self.hp += 8
                    self.mana -= 4
                    if self.hp > self.max_hp:
                        self.hp = self.max_hp
                    print '\n%s casts Heal and regains 8 HP!' % player.name
                    break
            elif choice == 'fireball':
                if not player.combat:
                    raw_input('\nNothing to cast Fireball on! > ')
                elif player.mana < 7:
                    print 'You do not have enough mana to cast Fireball!'
                else:
                    self.mana -= 7
                    spell_damage = random.randint(12, 15)
                    enemy.hp -= spell_damage
                    print '\n%s casts Fireball! %s takes %d damage!' % \
                          (player.name, enemy.name, spell_damage)
                    break
            elif choice == 'stun':
                if not player.combat:
                    raw_input('\nNothing to cast Stun on! > ')
                elif player.mana < 5:
                    print 'You do not have enough mana to cast Stun!'
                else:
                    self.mana -= 10
                    enemy.stunned = 2
                    raw_input('\n%s casts Stun! %s\'s eyes glaze over...' %
                             (self.name, enemy.name))
                    break

    def inv(self):
        """First layer of inventory function.  Displays list of items
           currently in inventory and actions that can be performed with
           them."""
        player.back = False
        while True:
            if len(self.equipment) < 1 and len(self.items) < 1 and self.gold < 1:
                print '\nYou are not currently carrying anything.'
            else:
                print '\n////////////////////////////'
                print 'You are currently carrying...'
                print '\nEquipment:'
                for i in self.equipment:
                    print i.name
                print '\nItems:'
                if len(player.items) < 1:
                    print 'None'
                else:
                    for i in self.items:
                        print i.name
                print '\nGold: %d' % player.gold
            choice = raw_input('\n[Equip] | [Use] | [Inspect] | [Back] > ').lower()
            if choice == 'equip':
                self.change_equipment()
                if player.back:
                    continue
                else:
                    break
            elif choice == 'use':
                if player.combat:
                    player.used_item = True
                    break
                elif not player.combat:
                    self.use_item(spider)
            elif choice == 'inspect':
                self.inspect()
                continue
            elif choice == 'back':
                player.back = True
                break
            else:
                continue

    def change_equipment(self):
        """Handles the [Equip] option from first inventory menu."""
        player.back = False
        while True:
            print '\nEquipment:'
            for i in self.equipment:
                print self.equipment.index(i), i.name
            try:
                choice = raw_input('\nSelect item with its number or '
                                   '[Back] > ').lower()
                if choice == 'back':
                    player.back = True
                    break
                intchoice = int(choice)
                if player.weapon == self.equipment[intchoice].name or \
                        player.armor == self.equipment[intchoice].name:
                    confirm = raw_input('Would you like to unequip the %s? > ' %
                                        self.equipment[intchoice].name).lower()
                    if 'yes' in confirm:
                        self.equipment[intchoice].unequip()
                        break
                else:
                    confirm = raw_input('Would you like to equip the %s? > ' %
                                        self.equipment[intchoice].name).lower()
                    if 'yes' in confirm:
                        self.equipment[intchoice].equip()
                        break
            except ValueError:
                continue

    def use_item(self, enemy):
        """Handles [Use] from first inventory menu."""
        player.used_item = False
        player.back = False
        while not player.used_item:
            print '\nItems:'
            for i in self.items:
                print self.items.index(i), i.name
            try:
                choice = raw_input('\nSelect item by its number or '
                                   '[Back] > ').lower()
                if choice == 'back':
                    player.back = True
                    break
                intchoice = int(choice)
                itemchoice = self.items[intchoice]
                confirm = raw_input('Would you like to use the %s? > ' %
                                    self.items[intchoice].name).lower()
                if 'yes' in confirm:
                    # These if statements are figuring out if the item chosen
                    # will add HP/Mana to the player or deal damage to the enemy
                    if itemchoice.plus_mana == 0 and itemchoice.damage == 0:
                        self.hp += itemchoice.plus_hp
                        if self.hp > self.max_hp:
                            self.hp = self.max_hp
                        raw_input('\n%s uses the %s and regains %d HP!' %
                                  (self.name, itemchoice.name,
                                   itemchoice.plus_hp))
                        del self.items[intchoice]
                        player.used_item = True
                    elif itemchoice.plus_hp == 0 and itemchoice.damage == 0:
                        self.mana += itemchoice.plus_mana
                        if self.mana > self.max_mana:
                            self.mana = self.max_mana
                        raw_input('\n%s uses the %s and regains %d MP!' %
                                  (self.name, itemchoice.name,
                                   itemchoice.plus_mana))
                        del self.items[intchoice]
                        player.used_item = True
                    elif itemchoice.plus_hp == 0 and itemchoice.plus_mana == 0:
                        if not player.combat:
                            raw_input('\nNothing to use %s on!' % itemchoice.name)
                        else:
                            raw_input('\n%s uses the %s on %s and deals %d damage!' %
                                      (self.name, itemchoice.name, enemy.name,
                                       itemchoice.damage))
                            enemy.hp -= itemchoice.damage
                            del self.items[intchoice]
                            player.used_item = True
            except ValueError:
                continue

    def inspect(self):
        """Handles [Inspect] option from inventory menu.  Displays an item's
           stats given its index in player.equipment."""
        player.back = False
        print('\nEquipment:')
        for i in self.equipment:
                    print self.equipment.index(i), i.name
        while True:
            try:
                choice = raw_input('\nInspect an item by its number or [BACK] > ').lower()
                if choice == 'back':
                    player.back = True
                    break
                intchoice = int(choice)
                if hasattr(self.equipment[intchoice], 'attack'):
                    print '\n', self.equipment[intchoice].name.title()
                    print 'Attack: %d' % self.equipment[intchoice].attack
                    print 'AC Penalty: %d' % self.equipment[intchoice].ac_penalty
                else:
                    print '\n', self.equipment[intchoice].name.title()
                    print 'Defense: %d' % self.equipment[intchoice].defense
            except ValueError:
                print '\nChoose an item by its number'

    def status(self):
        """Displays current player status."""
        player.back = False
        while True:
            print '\n////////////////////////////'
            print '%s\'s status:' % player.name
            print 'HP: %d, MP: %d' % (player.hp, player.mana)
            print 'Strength: %d, Stamina: %d' % (player.strength, player.sta)
            print 'AC: %d' % player.ac
            print '\nEquipped:'
            if player.weapon == '':
                print 'Weapon: None'
            else:
                print 'Weapon: %s' % player.weapon
            if player.armor == '':
                print 'Armor: None'
            else:
                print 'Armor: %s' % player.armor
            print '\nItems:'
            if len(player.items) < 1:
                print 'None'
            else:
                for i in player.items:
                    print i.name
            print '\nLevel %d %s' % (player.level, player.player_class)
            print 'XP to next level: %d' % (10 - player.xp)
            back = raw_input('\n[Back] > ')
            if back in 'back':
                player.back = True
                break

    def flee(self):
        """Handles the [Flee] option from the combat menu.  Randomly
           determines if the monster blocks your flight attempt."""
        while True:
            flee_chance = random.randint(1, 10)
            if flee_chance > 4:
                raw_input('\nYou scramble through the door behind you and '
                          'flee! > ')
                raw_input('\nYou find yourself in an unfamiliar room with one '
                          'untried door. > ')
                room_selector()
            else:
                raw_input('\nAs you turn to leave the monster blocks your '
                          'exit!')
                break

    def levelup(self):
        self.max_hp += 5
        self.strength += 2
        self.ac += 1
        self.sta += 2
        self.max_mana += 5
        self.level += 1
        self.xp = 0
        raw_input('\n%s has gained a level!' % player.name)

    def rest(self):
        """Handles [Rest] option from main menu."""
        confirm = raw_input('Are you sure you would like to rest? > ').lower()
        if confirm == 'no':
            player.back = True
        else:
            hours = random.randint(2, 6)
            mp_regained = hours
            raw_input('''
You spread the threadbare bedroll from your backpack on the ground before you.
Moments after you lay down, you begin to doze off. > ''')
            if random.randint(0, 10) > 6:
                monster_during_rest()
            else:
                raw_input('\nYou awaken after %d hours feeling refreshed.'
                          % hours)
                if player.player_class == 'mage':
                    if player.hp == player.max_hp and \
                       player.mana != player.max_mana:
                        player.mana += mp_regained
                        if self.mana > self.max_mana:
                            self.mana = self.max_mana
                        print '\n%s regains %d MP!' % (player.name, mp_regained)
                    elif player.hp != player.max_hp and player.mana == player.max_mana:
                        player.hp += hours
                        if self.hp > self.max_hp:
                            self.hp = self.max_hp
                        print '\n%s regains %d HP!' % (player.name, hours)
                    else:
                        player.hp += hours
                        player.mana += mp_regained
                        if self.hp > self.max_hp:
                            self.hp = self.max_hp
                        if self.mana > self.max_mana:
                            self.mana = self.max_mana
                        print '\n%s regains %d HP and %d MP!' % \
                              (player.name, hours, mp_regained)
                else:
                    if player.hp != player.max_hp:
                        player.hp += hours
                        if self.hp > self.max_hp:
                            self.hp = self.max_hp
                        print '\n%s regains %d HP!' % (player.name, hours)


class Monster(object):
    def __init__(self, name, max_hp, hp, strength, ac, sta, xp, weapon,
                 stunned):
        self.name = name
        self.max_hp = max_hp
        self.hp = hp
        self.strength = strength
        self.ac = ac
        self.sta = sta
        self.xp = xp
        self.weapon = weapon
        self.stunned = stunned

    def melee_attack(self, enemy):
        """Basic melee attack for monsters."""
        attack = 2 + self.strength + int(self.sta * random.random())
        damage = int(random.random() * (self.sta / 2)) + self.strength
        if attack >= enemy.ac:
            print '\n%s strikes %s with their %s for %d damage!' % \
                  (self.name, enemy.name, self.weapon, damage)
            enemy.hp -= damage
        else:
            print '\n%s missed!' % self.name


class Boss(object):
    def __init__(self, name, hp, ac, spells, stunned):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.spells = spells
        self.stunned = stunned

    def attack(self, player):
        """The boss's basic attack."""
        damage = random.randint(5, 7)
        if random.randint(1, 10) > 4:
            player.hp -= damage
            raw_input('\n%s casts %s on %s for %d damage!' % (self.name,
                      random.choice(self.spells), player.name, damage))
        else:
            raw_input('\n%s\'s spell fizzles!' % self.name)

    def special_attack(self, player):
        """Special attack that the boss uses every three turns."""
        damage = random.randint(8, 15)
        if random.randint(1, 10) > 4:
            player.hp -= damage
            raw_input('''
%s's eyes glaze over as an unnatural maelstrom materializes within the
chamber.  Bits of debris and intense winds tear at your body for %d damage. '''
                      % (self.name, damage))

    def transform(self):
        """Boss transforms once first form is reduced to 0 HP.  He gains
           HP/AC and a new attack."""
        raw_input('''
The figure suddenly springs into the air and hovers a short ways off the
ground. Spears of light begin to radiate from its body, eroding the
surrounding skin and clothing.  You shield your eyes from an eruption of
intense light and behold the transformed figure.  A hulking demon nearly
thirty feet tall stands before you, covered in thick black fur and sporting
huge talons each the size of a long spear. > ''')
        self.name = 'a hulking demon'
        self.hp = 25
        self.ac = 10

    def transform_attack(self, player):
        """New basic attack for the boss once he's transformed."""
        damage = random.randint(8, 12)
        if random.randint(1, 10) > 4:
            player.hp -= damage
            raw_input('''
%s slashes %s with their monstrous claws for %d damage!'''
                      % (self.name, player.name, damage))
        else:
            raw_input('\n%s misses with their monstrous claws!' % self.name)

    def boss_battle(self, player):
        """Separate method to handle combat with the boss since a few
           special cases are required."""
        turn = 1
        player.combat = True
        player.special = 2
        while True:
            combat_choice(player, self)
            if self.name == 'a mysterious figure' and self.hp <= 0:
                self.transform()
            elif self.hp < 1:
                raw_input('''
The demon is slain and the evil corruption plaguing the land has been
destroyed.
\n\n\n\nGame Over''')
                quit()
            if self.stunned > 0:
                raw_input('\n%s is stunned!' % self.name)
                self.stunned -= 1
            elif turn % 3 == 0:
                self.special_attack(player)
            elif turn % 3 != 0 and self.name == 'a hulking demon':
                raw_input('\n%s readies their attack...' % self.name)
                self.transform_attack(player)
            else:
                raw_input('\n%s begins to chant softly...' % self.name)
                self.attack(player)
            if player.hp < 1:
                raw_input('''
%s has been slain by %s!\n\n\n\n\nGame Over. > ''' % (player.name, self.name))
                quit()
            turn += 1


# Classes for all the items in the game follow.
class Weapon(object):
    def __init__(self, name, attack, ac_penalty, price):
        self.name = name
        self.attack = attack
        self.ac_penalty = ac_penalty
        self.price = price

    def equip(self):
        player.strength += self.attack
        player.sta += self.attack / 2
        player.ac -= self.ac_penalty
        player.weapon = self.name
        print '\nYou have equipped the %s.' % self.name

    def unequip(self):
        player.strength -= self.attack
        player.sta -= self.attack / 2
        player.ac += self.ac_penalty
        player.weapon = ''
        print '\nYou have unequipped the %s.' % self.name


class MagicWeapon(object):
    def __init__(self, name, attack, ac_penalty, price):
        self.name = name
        self.attack = attack
        self.ac_penalty = ac_penalty
        self.price = price

    def equip(self):
        player.strength += self.attack
        player.sta += self.attack / 2
        player.ac -= self.ac_penalty
        player.weapon = self.name
        print '\nYou have equipped the %s.' % self.name

    def unequip(self):
        player.strength -= self.attack
        player.sta -= self.attack / 2
        player.ac += self.ac_penalty
        player.weapon = ''
        print '\nYou have unequipped the %s.' % self.name


class Armor(object):
    def __init__(self, name, defense, price):
        self.name = name
        self.defense = defense
        self.price = price

    def equip(self):
        player.ac += self.defense
        player.armor = self.name
        print '\nYou have equipped the %s.' % self.name

    def unequip(self):
        player.ac -= self.defense
        player.armor = ''
        print '\nYou have unequipped the %s.' % self.name


class Item(object):
    def __init__(self, name, plus_hp, plus_mana, damage, price):
        self.name = name
        self.plus_hp = plus_hp
        self.plus_mana = plus_mana
        self.damage = damage
        self.price = price


def combat(player, enemy):
    """Handles the logic flow of combat."""
    enemy.hp = enemy.max_hp
    player.combat = True
    player.special = 2
    while True:
        combat_choice(player, enemy)
        if enemy.hp < 1:
            victory(player, enemy)
            break
        if enemy.stunned > 0:
            raw_input('\n%s is stunned!' % enemy.name)
            enemy.stunned -= 1
        else:
            raw_input('\n%s readies their attack... > ' % enemy.name)
            enemy.melee_attack(player)
        # Player death
        if player.hp < 1:
            print '\n%s has vanquished %s!' % (enemy.name, player.name)
            raw_input('\nGame Over.')
            quit()


def combat_choice(player, enemy):
    """This is the menu that is brought up for the player at the start of
       each combat round."""
    print '\n%s\'s HP: %d' % (player.name, player.hp)
    print '%s\'s MP: %d' % (player.name, player.mana)
    while True:
        print '\n%s\'s HP: %d' % (enemy.name, enemy.hp)
        if player.room == rooms.final_room:
            if player.player_class == 'mage':
                choice = raw_input('\n[Attack] | [Spells] | [Inventory] | '
                                   '[Status] > ').lower()
            elif player.player_class == 'thief':
                choice = raw_input('\n[Attack] | [Thievery] | [Inventory] | '
                                   '[Status] > ').lower()
            else:
                choice = raw_input('\n[Attack] | [Inventory] | [Status] > ').lower()
        elif player.player_class == 'mage':
            choice = raw_input('\n[Attack] | [Spells] | [Inventory] | '
                               '[Status] | [Flee] > ').lower()
        elif player.player_class == 'thief':
            choice = raw_input('\n[Attack] | [Thievery] | [Inventory] | '
                               '[Status] | [Flee] > ').lower()
        else:
            choice = raw_input('\n[Attack] | [Inventory] | [Status] | '
                               '[Flee] > ').lower()
        if choice == 'attack':
            if player.player_class == 'fighter':
                player.attack(enemy)
                if player.back:
                    continue
            else:
                player.melee_attack(enemy)
            break
        elif choice == 'spells':
            player.spells(enemy)
            if player.back:
                continue
            else:
                break
        elif choice == 'thievery':
            player.thievery(enemy)
            if player.back:
                continue
            else:
                break
        elif choice == 'inventory':
            player.inv()
            if player.used_item:
                player.use_item(enemy)
                if not player.used_item:
                    continue
                elif player.used_item:
                    break
            elif player.back:
                continue
            else:
                break
        elif choice == 'status':
            player.status()
            if player.back:
                continue
            else:
                break
        elif choice == 'flee':
            player.flee()
            break


def victory(player, enemy):
    """Victory conditions."""
    player.combat = False
    xp_gained = enemy.xp
    hp_regained = random.randint(1, 4)
    mp_regained = random.randint(1, 3)
    print '\n%s has vanquished %s!' % (player.name, enemy.name)
    gold_gained = random.randint(1, 10)
    player.gold += gold_gained
    if player.player_class == 'mage':
        player.xp += xp_gained
        player.hp += hp_regained
        player.mana += mp_regained
        if player.hp > player.max_hp:
            player.hp = player.max_hp
        if player.mana > player.max_mana:
            player.mana = player.max_mana
        raw_input('%s regains %d HP, %d MP, gains %d gold, and gains %d '
                  'experience! > ' % (player.name, hp_regained, mp_regained,
                                      gold_gained, xp_gained))
    else:
        player.xp += xp_gained
        player.hp += hp_regained
        if player.hp > player.max_hp:
            player.hp = player.max_hp
        raw_input('%s regains %d HP, gains %d gold, and gains %d experience! > '
                  ' ' % (player.name, hp_regained, gold_gained, xp_gained))
    if player.xp > 9:
        player.levelup()


def room_selector():
    """Randomly selects the next room from the random_room list.
       When down to the final element of the list, go to final room."""
    if len(random_room) == 0:
        rooms.final_room.enter()
    else:
        i = random.choice(random_room)
        random_room.remove(i)
        i()


def monster_chance():
    """Randomly determine if a monster is present in a room or not."""
    if random.randint(0, 10) > 3:
        return True
    else:
        return False


def random_monster():
    """Randomly selects a monster from the list, starts combat."""
    i = random.choice(random_monsters)
    if len(random_monsters) == 0:
        pass
    elif player.player_class == 'thief':
        print '\nYou open the door quietly and can see %s ' \
              'patrolling the next room.' % i.name
        choice = raw_input('Do you attempt to sneak past the creature? > ').lower()
        if choice == 'yes':
            stealth_chance = random.randint(1, 100)
            if stealth_chance > 40:
                raw_input('\nYou slip by %s unnoticed. > ' % i.name)
            else:
                random_monsters.remove(i)
                raw_input('\nYou\'ve alerted %s!  The creature rushes toward '
                          'you!' % i.name)
                combat(player, i)
        else:
            random_monsters.remove(i)
            print '\nYou rush toward %s!' % i.name
            combat(player, i)
    else:
        random_monsters.remove(i)
        raw_input('\nAs you open the door %s rushes toward you!' % i.name)
        combat(player, i)


def monster_during_rest():
    """Determines if a monster will attack while the player rests."""
    i = random.choice(random_monsters)
    raw_input('''
You abrubtly wake from your slumber to the sound of %s rushing
toward you! ''' % i.name)
    combat(player, i)


def loot_chance():
    """Chance that the player will find loot."""
    chance = random.randint(1, 100)
    if chance > 55:
        return True
    else:
        return False


def loot():
    """Determines type of loot, appends it to player.equipment
       or player.items."""
    loot_type = random.randint(1, 100)
    if 36 < loot_type < 75:
        i = random.choice(items)
        player.items.append(i)
        raw_input('\nYou find a %s!' % i.name)
    elif 0 < loot_type < 35:
        i = random.choice(weapons)
        player.equipment.append(i)
        raw_input('\nYou find a %s!' % i.name)
    else:
        i = random.choice(magic_items)
        player.equipment.append(i)
        raw_input('\nYou find a %s!' % i.name)

# Weapons - attributes are name, attack, AC penalty, price.
bastard_sword = Weapon('bastard sword', 4, 1, 20)
staff = Weapon('gnarled staff', 2, 0, 15)
dagger = Weapon('dagger', 2, 0, 8)
spear = Weapon('spear', 3, 1, 16)
mace = Weapon('mace', 3, 0, 12)
two_hander = Weapon('two handed sword', 5, 2, 25)
poleaxe = Weapon('poleaxe', 6, 3, 30)

# Magic Items - attributes are name, attack, AC penalty, price.
magic_axe = MagicWeapon('Glowing Two-Handed Axe', 6, 2, 35)
magic_dagger = MagicWeapon('Poisoned Dagger', 3, 0, 30)

# Armor - attributes are name, defense, price
leather = Armor('leather jerkin', 2, 10)
plate = Armor('plated mail', 4, 15)
robes = Armor('cloth robe', 1, 8)

# Items - attributes are name, plus_hp, plus_mana, damage, price
healing_potion = Item('healing potion', 10, 0, 0, 5)
mana_potion = Item('mana potion', 0, 10, 0, 5)
frost_potion = Item('frost potion', 0, 0, 10, 5)

# Monsters - attributes are: Name, max HP, HP, strength, AC, sta, XP,
# weapon, stunned.
orc = Monster('an orc', 21, 21, 2, 3, 7, 5, 'mace', 0)
goblin = Monster('a goblin', 20, 20, 2, 8, 8, 4, 'dagger', 0)
kobold = Monster('a kobold', 19, 19, 3, 7, 8, 5, 'flail', 0)
spider = Monster('a giant tarantula', 21, 21, 4, 6, 7, 6, 'fangs', 0)

# Player - attributes are: Name, class, Max HP, HP, STR, AC, STA, Max Mana,
# MANA equipment, items, gold, xp, back, used_item, weapon, armor, combat,
# special, room.
player = Player('', '', 21, 21, 2, 6, 5, 0, 0, [], [], 15, 0, False,
                False, '', '', False, 0, None)

#Boss - attributes are: Name, HP, AC, spells, stunned.
sorceror = Boss('a mysterious figure', 20, 8, ['lightning strike', 'fireball',
                                               'meteor', 'ice strike'], 0)

# Lists of functions, objects for randomization/use in selector functions.
random_monsters = [orc, goblin, kobold, spider]
random_room = [rooms.room1.enter, rooms.room2.enter, rooms.room3.enter,
               rooms.room4.enter]
items = [healing_potion, mana_potion, frost_potion]
weapons = [bastard_sword, staff, dagger, spear, mace, two_hander, poleaxe]
armor = [leather, plate, robes]
magic_items = [magic_axe, magic_dagger]

rooms.title()