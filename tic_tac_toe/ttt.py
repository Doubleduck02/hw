from random import randint
class Game:

    def __init__(self, players=1, p1sign='o', p2sign='x'):
        if players<1:
            self._players=1
        elif players>2:
            self._players=2
        self._board=[[0,0,0],[0,0,0],[0,0,0]]
        if len(p1sign)!=1:
            p1sign='o'
        if len(p2sign)!=1:
            p2sign='x'
        self._p1sign=p1sign
        self._p2sign=p2sign

    def playersign(self, player):
        if player==1:
            return self._p1sign
        elif player==2:
            return self._p2sign
        return ' '

    def sign(self, x, y):
        return self.playersign(self._board[y][x])

    def draw(self):
        s=''
        for y in range(3):
            for x in range(3):
                if x==2:
                    s=s+' '+self.sign(x,y)+'\n'
                else:
                    s=s+' '+self.sign(x,y)+' \u2502'
            if y<2:
                s=s+('\u2500'*3+'\u253c')*2+'\u2500'*3+'\n'
        return s

    def columncheck(self):
        if (self.sign(0,0)==self.sign(0,1) and self.sign(0,0)==self.sign(0,2)) or (self.sign(1,0)==self.sign(1,1) and self.sign(1,0)==self.sign(1,2)) or (self.sign(2,0)==self.sign(2,1) and self.sign(2,0)==self.sign(2,2)):
            return True
        return False

    def rowcheck(self):
        if (self.sign(0,0)==self.sign(1,0) and self.sign(0,0)==self.sign(2,0)) or (self.sign(0,1)==self.sign(1,1) and self.sign(0,1)==self.sign(2,1)) or (self.sign(0,2)==self.sign(1,2) and self.sign(0,2)==self.sign(2,2)):
            return True
        return False

    def diagcheck(self):
        if (self.sign(0,0)==self.sign(1,1) and self.sign(0,0)==self.sign(2,2)) or (self.sign(2,0)==self.sign(1,1) and self.sign(2,0)==self.sign(0,2)):
            return True
        return False

    def wincheck(self):
        if self.columncheck() or self.rowcheck() or self.diagcheck():
            return True
        return False
    
    def move(self, player, x, y):
        if self.sign(x,y)!=' ' and player!=0:
            return False
        self._board[y][x]=player
        return True

    def botmove(self):
        for y in range(3):
            for x in range(3):
                if self.sign(x,y)==' ':
                    self.move(1,x,y)
                    if self.wincheck():
                        self.move(0,x,y)
                        self.move(2,x,y)
                        return True
                    self.move(0,x,y)
        while not self.move(2,randint(0,2),randint(0,2)):
            pass
        return True

    def playermove(self, player):
        while True:
            x=int(input('Column: '))
            y=int(input('Row: '))
            if self.move(player,x,y):
                return True
            print('Please choose again')
            
    def match(self, p1score=0, p2score=0, bot=True):
        player=randint(1,2)
        for i in range(9):
            print('Player %s turn'%(self.playersign(player)))
            print(f'{self.playersign(1)}   {p1score:02}:{p2score:02}   {self.playersign(2)}')
            print(self.draw())
            if player==1:
                self.playermove(1)
                if self.wincheck():
                    return 1
            else:
                if bot:
                    self.botmove()
                else:
                    self.playermove(2)
                if self.wincheck():
                    return 2
            print('yes')
        return 0

    def game(self):
        p1score=0
        p2score=0
        match=self.match(p1score, p2score, self._players==1)
        if match==1:
            p1score+=1
            print('Player %s wins the match'%(self._p1sign))
        elif match==2:
            p2score+=1
            print(f'Player {self._p2sign} wins the match')
        else:
            print('Tie')
        print(f'{self.playersign(1)}   {p1score:02}:{p2score:02}   {self.playersign(2)}')
        print(self.draw())



gm=Game()
gm.match()
