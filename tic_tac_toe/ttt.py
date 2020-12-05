from random import randint
from os import system
from msvcrt import getch

def check123(x):
    if x=='1' or x=='2' or x=='3':
        return True
    return False
class Game:
    '''
    Game (players = 1, p1sign = 'o', p2sign = 'x')

        init:
            players - ammount of players playing the game. If set above 2, it will change to 2, if set less than 1 it will change to 1
            p1sign, p2sign - the sign which players will use to play. If set to something shorter or longer than 1 it will change to the default value

        Game.boardset() - sets the board to empty

        Game.playersign(player) - returns the sign of given player

        Game.sign(x,y) - returns the sign on the board

        Game.draw() - returns the drawn board with the coordinates

        Game.columncheck() - checks columns for a win situation
        
        Game.rowncheck() - checks rows for a win situation

        Game.diagcheck() - checks diagonals for a win situation

        Game.wincheck() - checks the whole board for a win situation using the last 3 functions

        Game.move(player, x, y) - checks the board for empty space and moves if there is (also used to remove the sign if the player is set to 0)
            returns if move was made
        
        Game.botmove() - checks the bot's move to win, if not then to block the player, then randomly moves if neither

        Game.playermove(player) - prompts the player to choose the move

        Game.match(p1score=0, p2score=0, bot=True) - makes a match of tic-tac-toe
            returns which player wins (0 if draw)

        Game.game(winpoint = 5) - keeps repeating matches until one of the players reaches winpoint
            returns message about who wins the game
    '''
    def __init__(self, players=1, p1sign='o', p2sign='x'):
        if players<1:
            self.players=1
        elif players>2:
            self.players=2
        self._board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        if len(p1sign)!=1:
            p1sign='o'
        if len(p2sign)!=1:
            p2sign='x'
        self._p1sign=p1sign
        self._p2sign=p2sign

    def boardreset(self):
        self._board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
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
        s='   1   2   3 \n'
        for y in range(3):
            s=s+f'{y+1} '
            for x in range(3):
                if x==2:
                    s=s+' '+self.sign(x,y)+'\n'
                else:
                    s=s+' '+self.sign(x,y)+' \u2502'
            if y<2:
                s=s+'  '+('\u2500'*3+'\u253c')*2+'\u2500'*3+'\n'
        return s

    def columncheck(self):
        if (self.sign(0,0)==self.sign(0,1) and self.sign(0,0)==self.sign(0,2) and self.sign(0,0)!=' ') or (self.sign(1,0)==self.sign(1,1) and self.sign(1,0)==self.sign(1,2) and self.sign(1,0)!=' ') or (self.sign(2,0)==self.sign(2,1) and self.sign(2,0)==self.sign(2,2) and self.sign(2,0)!=' '):
            return True
        return False

    def rowcheck(self):
        if (self.sign(0,0)==self.sign(1,0) and self.sign(0,0)==self.sign(2,0) and self.sign(0,0)!=' ') or (self.sign(0,1)==self.sign(1,1) and self.sign(0,1)==self.sign(2,1) and self.sign(0,1)!=' ') or (self.sign(0,2)==self.sign(1,2) and self.sign(0,2)==self.sign(2,2) and self.sign(0,2)!=' '):
            return True
        return False

    def diagcheck(self):
        if (self.sign(0,0)==self.sign(1,1) and self.sign(0,0)==self.sign(2,2) and self.sign(0,0)!=' ') or (self.sign(2,0)==self.sign(1,1) and self.sign(2,0)==self.sign(0,2) and self.sign(2,0)!=' '):
            return True
        return False

    def wincheck(self):
        if self.columncheck() or self.rowcheck() or self.diagcheck():
            return True
        return False
    
    def move(self, player, x, y):
        if self.sign(x,y)!=' ' and player!=0:
            return False
        self._board[y][x]=self.playersign(player)
        return True

    def botmove(self):
        for y in range(3):
            for x in range(3):
                if self.sign(x,y)==' ':
                    self.move(2,x,y)
                    if self.wincheck():
                        return True
                    self.move(0,x,y)
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
            xinput=input('Column: ')
            yinput=input('Row: ')
            if check123(xinput) and check123(yinput):
                x=int(xinput)
                y=int(yinput)
                if x in range(1,4) and y in range(1,4):
                    if self.move(player,x-1,y-1):
                        return True
            print('Please choose again')
            
    def match(self, p1score=0, p2score=0, bot=True):
        self.boardreset()
        player=randint(1,2)
        print('Player %s turn'%(self.playersign(player)))
        print(f'{self.playersign(1)}    {p1score:2}:{p2score:2}    {self.playersign(2)}')
        print(self.draw())
        for i in range(9):
            if player==1:
                self.playermove(1)
                if self.wincheck():
                    return 1
                player=2
            elif player==2:
                if bot:
                    self.botmove()
                else:
                    self.playermove(2)
                if self.wincheck():
                    return 2
                player=1
            system('cls')
            print('Player %s turn'%(self.playersign(player)))
            print(f'{self.playersign(1)}    {p1score:2}:{p2score:2}    {self.playersign(2)}')
            print(self.draw())
        return 0

    def game(self, winpoint=5):
        p1score=0
        p2score=0
        while True:
            match=self.match(p1score, p2score)
            system('cls')
            if match==1:
                p1score+=1
                print('Player %s wins the match'%(self._p1sign))
            elif match==2:
                p2score+=1
                print(f'Player {self._p2sign} wins the match')
            else:
                print('Tie')
            print(f'{self.playersign(1)}    {p1score:2}:{p2score:2}    {self.playersign(2)}')
            print(self.draw())
            if p1score==winpoint:
                return f'Player {self._p1sign} wins the game'
            elif p2score==winpoint:
                return f'Player {self._p2sign} wins the game'
            print('Press any key to continue')
            getch()
            system('cls')


gm=Game()
print(gm.game())