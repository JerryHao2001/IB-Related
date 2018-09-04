from random import *

global deck, score, player, dealer
deck = []
score = {'Ace':11,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':10,'Queen':10,'King':10}
player = 0
dealer = 0

def makeDeck():
    global deck
    for i in "2 3 4 5 6 7 8 9 10 Jack Queen King Ace".split(' '):
        for j in "Club Diamond Heart Spade".split(' '):
            deck.append(i + ' of '+ j)

def drawCard():
    global deck
    card = choice(deck)
    deck.remove(card)
    return card

def dealCard():
    global deck, score, dealer
    dealercard = ''
    start3 = drawCard()
    start4 = drawCard()
    dealercard += start3 + start4
    dealer = score[start3.split(' ')[0]] + score[start4.split(' ')[0]]
    if dealer == 21:
        dealer == 'BLACK JACK!'
    else:
        while True:
            if dealer < 16:
                card = drawCard()
                dealercard += card
                dealer += score[card.split(" ")[0]]
            elif 16 <= dealer <= 21:
                print("dealer's score is {}".format(dealer))
                break
            elif dealer > 21:
                if 'Ace' in dealercard:
                    dealer = dealer - 10
                    dealercard.replace('Ace','')
                else:
                    print("dealer's score is {}".format(dealer),'\nCongratulation')
                    return "quit"

def playerCard():
    global player
    print("These are your start cards:")
    playercard = ''
    start1 = drawCard()
    start2 = drawCard()
    playercard += start1 + start2
    player = score[start1.split(' ')[0]] + score[start2.split(' ')[0]]
    print(start1,'|',start2,'\nyour score is {}'.format(player))
    if player == 21:
        player = 'BLACK JACK!'
        print("BLACK JACK!")
    else:
        while True:
            if player == 21:
                print("Terrific")
                break
            elif player > 21:
                if 'Ace' in playercard:
                    player = player - 10
                    playercard.replace('Ace','')
                else:
                    print("Sorry, try again")
                    return "quit"
            else:
                temp = input("hit or stay").lower()
                if temp == "stay":
                    break
                elif temp == "hit":
                    moreCard = drawCard()
                    playercard += moreCard
                    player += score[moreCard.split(' ')[0]]
                    if 'Ace' in playercard:
                        print("you get {} Ace in you hand".format(playercard.count('Ace')))
                    print(moreCard,"\nnow your score is {}".format(player))

def compare():
    if not(dealCard() == "quit"):
        print("your score is {}, dealer's score is {}".format(player,dealer))
        if (player == 'BLACK JACK!' and dealer !='BLACK JACK!') or (player > dealer):
            print("Congratulations")
        elif player == dealer:
            print('Draw')
        elif (player != 'BLACK JACK!' and dealer =='BLACK JACK!') or (player < dealer):
            print('Sorry, try again')

print("Welcome, let's start the Black Jack :).")
again = "yes"
while again == 'yes':
    makeDeck()
    shuffle(deck)
    if not (playerCard() == "quit"):
        compare()
    again = input("Would you want to play again?").lower()
