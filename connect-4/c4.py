from random import randint

def check1to7(x):
    if x in range(1,8):
        return True
    return False

class Game:
    def __init__(self, players=1, p1sign='o', p2sign='x'):
        if players<1:
            self.players=1
        elif players>2:
            self.players=2
        self._board=[]
        self.boardset()
        if len(p1sign)!=1:
            p1sign='o'
        if len(p2sign)!=1:
            p2sign='x'
        self._p1sign=p1sign
        self._p2sign=p2sign

    def boardset(self, x_size=7,y_size=6):
        x=[]
        for i in range(x_size):
            x.append(' ')
        for i in range(y_size):
            self._board.append(x)
        return True

    def playersign(self, player):
        if player==1:
            return self._p1sign
        elif player==2:
            return self._p2sign
        return ' '

    def sign(self, x, y):
        return self._board[y][x]

    def draw(self):
        s='  1   2   3   4   5   6   7\n'
        for y in range(6):
            for x in range(7):
                if x==6:
                    s=s+'\u2502 '+self.sign(x,y)+' \u2502\n'
                else:
                    s=s+'\u2502 '+self.sign(x,y)+' '
            if y<5:
                s=s+('\u2502'+' '*3)*7+'\u2502\n'
            else:
                s=s+'\u2514'+('\u2500'*3+'\u2534')*6+'\u2500'*3+'\u2518'
        return s

    def wincheck(self):
        for y in range(6):
            for x in range(7):
                if self.sign(x,y)==' ':
                    continue
                if x-4>=0:
                    for i in range(4):
                        if self.sign(x,y)!=self.sign(x-i,y):
                            break
                        if i==3:
                            return True
                    if y-4>=0:
                        for i in range(4):
                            if self.sign(x,y)!=self.sign(x-i,y-i):
                                break
                            if i==3:
                                return True
                    if y+4<6:
                        for i in range(4):
                            if self.sign(x,y)!=self.sign(x-i,y+i):
                                break
                            if i==3:
                                return True
                if x+4<7:
                    for i in range(4):
                        if self.sign(x,y)!=self.sign(x+i,y):
                            break
                        if i==3:
                            return True
                    if y-4>=0:
                        for i in range(4):
                            if self.sign(x,y)!=self.sign(x+i,y-i):
                                break
                            if i==3:
                                return True
                    if y+4<6:
                        for i in range(4):
                            if self.sign(x,y)!=self.sign(x+i,y+i):
                                break
                            if i==3:
                                return True
                if y-4>=0:
                    for i in range(4):
                        if self.sign(x,y)!=self.sign(x,y-i):
                            break
                        if i==3:
                            return True
                if y+4<6:
                    for i in range(4):
                        if self.sign(x,y)!=self.sign(x,y+i):
                            break
                        if i==3:
                            return True
    
    def move(self, player, x):
        for i in range(6):
            if self.sign(x,i)!=' ':
                if player==0:
                    self._board[i][x]=' '
                    return True
                elif i!=0:
                    self._board[i-1][x]=self.playersign(player)
                    return True
                return False
    
    def botmove(self):
        for x in range(7):
            if self.move(1,x):
                if self.wincheck():
                    self.move(0,x)
                    self.move(2,x)
                    return True
                self.move(0,x)
        self.move(2,randint(0,6))
        return True

    def playermove(self, player=1):
        while True:
            xinput=input('Column: ')
            if check1to7(xinput):
                x=int(xinput)
                if x in range(1,4) and y in range(1,4):
                    if self.move(player,x-1):
                        return True
            print('Please choose again')


game=Game()
print(game.wincheck())