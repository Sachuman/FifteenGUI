#Author = Sachin Jain
#Date - 26th May 2023
#file - fifteen.py
#description - fifteen puzzle


import numpy as np
from random import choice


class Fifteen:

    def __init__(self, size=4):
        self.tiles = np.array([i for i in range(1, size ** 2)] + [0])
        self.adj = [
            [1, 4], [0, 2, 5],
            [1, 3, 6],
            [2, 7],
            [0, 5, 8],
            [1, 4, 6, 9],
            [2, 5, 7, 10],
            [3, 6, 11],
            [4, 9, 12],
            [5, 8, 10, 13],
            [6, 9, 11, 14],
            [7, 10, 15],
            [8, 13],
            [9, 12, 14],
            [10, 13, 15],
            [11, 14]]



    def update(self, move):
        index = np.where(self.tiles == 0)[0][0]
        movie = np.where(self.tiles == move)[0][0]
        if movie in self.adj[index]:
            self.tiles[movie], self.tiles[index] = self.tiles[index], self.tiles[movie]


    def transpose(self, i, j):
        return self[i], self[j] == self[j], self[i]

    def shuffle(self, steps=100):
        index = np.where(self.tiles == 0)[0][0]
        for ily in range(steps):
            move_index = choice(self.adj[index])
            self.tiles[index], self.tiles[move_index] = self.tiles[move_index], self.tiles[index]
            index = move_index

    def is_valid_move(self, move):
        iodex = np.where(self.tiles == move)[0][0]  # Find the index of the empty tile (0)
        for i in self.adj[iodex]:
            if self.tiles[i]== 0:
                return True
        return False

    def is_solved(self):
        chuhiya = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])
        return np.array_equal(chuhiya, self.tiles)

    def draw(self):
        print('+---+---+---+---+')
        print('| {} | {} | {} | {} |'.format(' ' if self.tiles[0] == 0 else self.tiles[0],
                                             ' ' if self.tiles[1] == 0 else self.tiles[1],
                                             ' ' if self.tiles[2] == 0 else self.tiles[2],
                                             ' ' if self.tiles[3] == 0 else self.tiles[3]))
        print('+---+---+---+---+')
        print('| {} | {} | {} | {} |'.format(' ' if self.tiles[4] == 0 else self.tiles[4],
                                             ' ' if self.tiles[5] == 0 else self.tiles[5],
                                             ' ' if self.tiles[6] == 0 else self.tiles[6],
                                             ' ' if self.tiles[7] == 0 else self.tiles[7]))
        print('+---+---+---+---+')
        print('| {} | {} | {} | {} |'.format(' ' if self.tiles[8] == 0 else self.tiles[8],
                                             ' ' if self.tiles[9] == 0 else self.tiles[9],
                                             ' ' if self.tiles[10] == 0 else self.tiles[10],
                                             ' ' if self.tiles[11] == 0 else self.tiles[11]))
        print('+---+---+---+---+')
        print('| {} | {} |{} | {} |'.format(' ' if self.tiles[12] == 0 else self.tiles[12],
                                             ' ' if self.tiles[13] == 0 else self.tiles[13],
                                             ' ' if self.tiles[14] == 0 else self.tiles[14],
                                             ' ' if self.tiles[15] == 0 else self.tiles[15]))
        print('+---+---+---+---+')

    def __str__(self):
        ooty = ''
        for i in range(16):
            if self.tiles[i] == 0:
                ooty += '   '
            else:
                ooty += f'{self.tiles[i]:2d} '
            if (i + 1) % 4 == 0:
                ooty += '\n'
        return ooty


if __name__ == '__main__':
    
    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False

    

    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')
