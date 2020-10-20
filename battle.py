#This is the players health and defense
ph = 20
df = 4
#This is the bosses health
bh = 30

#main loop of game
# This is the meeting point of the ogre and the player
print('Your on a road and you see a giant ogre and you enter into battle.')
attack = input('You can Castspells:melee:defend')

#This is how the programs determines what input you gave
if attack == 'Castspells':
    spell = input('Fireball:healing:magicsheild')
    if spell == 'Fireball':
        print(bh - 5)
    if spell == 'Healing':
        print('You are all ready at full health you can not heal anymore')
    if spell == 'magicsheild':
        print('Your defense went up by 2')
        print(df + 2)
if attack == 'melee':
    print('You attack with a sword')
    print(bh - 4)
boss_attack = print('He takes a swing at he with his club you have 2 second to try and doge his attack')
answer = None

def check():
    time.sleep(2)
    if answer != None:
        return
    print("Too Slow the ogre hits you with his club")
    print(df - 4)

Thread(target = check).start()

answer = input('dodge')
if answer ==  'dodge':
    print('You dodge the ogres club')
#This is how the program determines what input you gave the computer
attack = input('You can Castspells:melee:defend')
if attack == 'Castspells':
    spell = input('Fireball:healing:magicsheild')
    if spell == 'Fireball':
        print(bh - 10)
    if spell == 'Healing':
        print(+4)
    if spell == 'magicsheild':
        print('Your defense went up by 2')
        print(df + 4)
if attack == 'melee':
    print('You attack with a sword')
    print(bh - 8)
boss_attack = print('He takes a swing at he with his fist you have 2 second to try and doge his attack')
answer = None

def check():
    time.sleep(2)
    if answer != None:
        return
    print("Too Slow the ogre hits you with his club")
    print(df - 4)

Thread(target = check).start()

answer = input('dodge')
if answer ==  'dodge':
    print('You dodge the ogres fist')
print('The ogre is getting bored')
#This is how the program determines what input you gave the computer
attack = input('You can Castspells:melee:defend')
if attack == 'Castspells':
    spell = input('Fireball:healing:magicsheild')
    if spell == 'Fireball':
        print(bh - 20)
    if spell == 'Healing':
        print(ph + 8)
    if spell == 'magicsheild':
        print('Your defense went up by 2')
        print(df + 8)
if attack == 'melee':
    print('You attack with a sword')
    print(bh - 16)
boss_attack = print('He takes a swing at he with his fist you have 2 second to try and doge his attack')
answer = None

def check():
    time.sleep(2)
    if answer != None:
        return
    print("Too Slow the ogre hits you with his club")
    print(df - 8)

Thread(target = check).start()

answer = input('dodge')
if answer ==  'dodge':
    print('You dodge the ogres fist')
print('The ogre has gotten bored of fighting you so he walks away')
