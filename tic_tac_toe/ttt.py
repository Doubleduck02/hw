from random import randint
class Game:

    def __init__(self, players=1):
        if players<1:
            self._players=1
        elif players>2:
            self._players=2
        self._board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    def sign(self, x, y):
        return self._board[y][x]

    def playersign(self, player):
        if player==1:
            return 'o'
        return 'x'

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

    def columncheck(self)
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
        if self.sign(x,y)!=' ':
            return False
        self._board[y][x]=self.playersign(player)
        return True

    def botmove(self):
        for y in range(3):
            for x in range(3):
                if self.sign(x,y)==' ':

gm=Game()
print(gm.draw())
