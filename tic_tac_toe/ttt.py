class Game:

    def __init__(self, players=1):
        if players<1:
            players=1
        elif players>2:
            players=2
        self._players=players
        self._data=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    def sign(self, x, y):
        return self._data[y][x]

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

    def move(self, player, x, y):
        if self.sign(x,y)==' ':
            return False
        self._data[y][x]=self.playersign(player)
        return True

gm=Game()
print(gm.draw())
