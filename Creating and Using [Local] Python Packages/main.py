import random
b = 'R P S'
c = 0
d = 0

while True:
    def Player():
        v = list(input('\nPlayer \nPick between "R", "P" or "S": '))
        randN = random.choices(b.split(' '),k=1)
        player = Convert(v)
        cpu = Convert(randN)

        print('Player({})'.format(player), ' : CPU({})'.format(cpu))
        return v,randN
    def CPU():
        v = list(input('\nCPU \nPick between "R", "P" or "S": '))
        randN = random.choices(b.split(' '),k=1)
        player = Convert(v)
        cpu = Convert(randN)

        print('Player({})'.format(player), ' : CPU({})'.format(cpu))
        return v,randN

    def Convert(conv):
        result = ''
        if conv == ['R']:
            result = 'Rock'
        elif conv == ['P']:
            result = 'Paper'
        elif conv == ['S']:
            result = 'Scissors'
        return result
    v, randN = Player()
    if v == randN:
        c += 1
        if c >=1 and c < 3:
            print('Player Score: {}'.format(c))
        elif c == 3:
            print("Player WINS")
            break
    v, randN = CPU()
    if v == randN:
        d += 1
        if d >=1 and d < 3:
            print('CPU Score: {}'.format(d))
        elif d == 3:
            print("CPU WINS")
            break