def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif p1 == 'scissors' and p2 == 'paper' or p1 == 'rock' and p2 == 'scissors' or p1 == 'paper' and p2 == 'rock':
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'

if __name__ == '__main__':
    print(rps('scissors','paper'))

'''
rps('scissors','paper') // Player 1 won!
rps('scissors','rock') // Player 2 won!
rps('paper','paper') // Draw!
'''
