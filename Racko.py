# -*- coding: utf-8 -*-
import random

#print deck

##print lst[-1]
##list.append
##list.pop
def shuffle():
    ''' shuffles the deck or the discard pile'''
    if len(deck)==0:
        #shuffle discard
        print 'shuffle discard'
        random.shuffle(discard)
    else:
        #shuffle deck
        print 'shuffle deck'
        random.shuffle(deck)
    # 60 cards, each numbered 1 to 60

def check_racko(rack):
    '''determine if Racko has been achieved, ascending order'''
    racklist=rack[:]
    #print racklist
    racklist.sort()
    #print racklist
    racklist.reverse()
    #print racklist
    if rack==racklist:
        is_racko=True
    else:
        is_racko=False
    return is_racko

def deal_card():
    '''get the top card from the deck'''
    deck.pop()
    #return top_card
def deal_initial_hands():
    ''' start the game off by dealing two hands of 10 cards each'''
##    User_hand=[]
##    Computer_hand=[]
##    for i in range(0,10):
##        User_hand.append(deck.pop())
##        Computer_hand.append(deck.pop())
##    return User_hand, Computer_hand
    First_hand=[]
    Second_hand=[]
    for i in range(0,10):
        First_hand.append(deck.pop())
        Second_hand.append(deck.pop())
    return First_hand, Second_hand

def does_user_begin():
    ''' simulate a coin toss by using the random library'''
    result=random.random()
    print result
    if result>0.5:
        coin='heads'
    else:
        coin='tails'
    print coin
    return coin
    #not decided by picking a card, right now, easier

def print_top_to_bottom(rack):
    ''' print it out from top to bottom in a manner more stack like than list like''' 
    for cards in rack:
        print str(cards)+"\n"

def find_and_replace(newCard, cardToBeReplaced, hand):
    '''ﬁnd the cardToBeReplaced in the hand and replace it with newCard'''
    if cardToBeReplaced in hand:
        index=hand.index(cardToBeReplaced)
        hand[index]=newCard
        #discard.append(cardToBeReplaced)
        return True
        #return (True, cardToBeReplaced)
    else:
        print "replace a card not in the hand, please try again with another one\n"
        return False
        #return (False, cardToBeReplaced)
        #print "replace a card not in the hand, please try again with another one\n"

def add_card_to_discard(card):
    '''add the card to the top of the discard pile'''
    discard.append(card)

def computer_play(hand):
    '''formulate the computer’s strategy'''
    #need strategy

def main():
    '''the Racko game function'''
    global deck
    global discard
    deck=range(1,61)
    discard=[]

##    global human_hand
##    global computer_hand
    human_hand=[]
    computer_hand=[]
    shuffle()
    print deck
    #deal a card to the computer and a card to the user
    #repeat until both have 10 cards
    userStarts = does_user_begin()
    #print userStarts
    userStarts=True
    #if userStarts=='heads':
    if userStarts==True:
        print "user first"
        human_hand,computer_hand= deal_initial_hands()
        print human_hand
        print computer_hand
        newCard=deck.pop()
        print 'The new card in deck is',newCard
        #reveal one card to begin the discard pile
        while (not check_racko(human_hand)) and (not check_racko(computer_hand)):
            print "Here is your rack now:\n"
            print_top_to_bottom(human_hand)
            use_Card=raw_input('Do you want to use this card?Y/N\n')
            do_input_validate=True
            #print use_Card
            while do_input_validate:
                if use_Card=='y' or use_Card=='Y':
                    cardToBeReplaced=input('Enter the number on card you want to replace?Y/N\n')
                    find_and_replace(newCard, cardToBeReplaced, human_hand)
                    #ask the user for the number of the card they want to kick out
                    #modify the user’s hand and the discard pile
                    print "This is what your rack looks like after this round\n"
                    print_top_to_bottom(human_hand)
                    do_input_validate=False
                    #break
                    #print the user’s han
                elif use_Card=='n' or use_Card=='N':
                    print 'n'
                    #break
                    do_input_validate=False
                else:
                    while use_Card!='y' and use_Card!='Y' and use_Card!='n' and use_Card!='N':
                        use_Card=raw_input('Please enter n or y to continue.\nDo you want to use this card?Y/N\n')
                        break
                    #do_input_validate=False
                #should think a better way to terminate
            break
        #while neither the computer nor the user has racko:
        computer_hand = computer_play(computer_hand) 
##    elif userStarts=='tails':
##        print "computer first"
##        computer_hand,human_hand= deal_initial_hands()
##        print human_hand
##        print computer_hand
##        #print_top_to_bottom(human_hand) 
    print 'deck',len(deck)
if __name__ == '__main__':
    main()

##def reverselist(x):
##    temp=x[:]
##    temp.reverse(). reverse
##    return temp

##lst.remove(i)
##lst.insert(i,x)



##for x,y in zip(one,two):
##    if x!=y:
##        is_racko=False
##        break

    
