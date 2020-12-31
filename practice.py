from random import shuffle


class Card:
    suits = {1: "Ninja", 2: "Knight", 3: "Berserk", 4: "Witch"}
    values = [None, 1, 2, 3, 4, 5]

    def __init__(self, v, s):
        self.value = v
        self.suit = s


    def __repr__(self):
        v = str(self.values[self.value]) +\
            " of " + \
            str(self.suits[self.suit])
        return v


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(1, 5):
            for j in range(1, 4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("プレーヤー1の名前")
        name2 = input("プレーヤー2の名前")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        self.p1w = 0
        self.p2w = 0

    def wins(self, winner):
        w = "このラウンドは{}が勝ちました"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{}は{}、　{}は{}をドロー"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("開戦")

        while len(cards) >= 2:
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c.value > p2c.value:
                self.p1w += 1
                self.wins(self.p1.name)
            elif p1c.value == p2c.value:
                if p1c.suit > p2c.suit:
                    self.p1w += 1
                    self.wins(self.p1.name)
                else:
                    self.p2w += 1
                    self.wins(self.p2.name)

            else:
                self.p2w += 1
                self.wins(self.p2.name)

        else:
            win = self.winner(self.p1, self.p2)
            print("{}の勝利".format(win))

    def winner(self, p1, p2):
        if self.p1w > self.p2w:
            return p1.name
        if self.p1w < self.p2w:
            return p2.name
        return "引き分け"


game = Game()
game.play_game()
