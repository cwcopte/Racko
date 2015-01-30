# -*- coding: utf-8 -*-
import random
global deck
global discard
lst = [3, 17, 11, 30, 33, 38, 49, 46, 25, 53]
##print lst[-1]
##list.append
##list.pop
def shuffle():
    ''' shuffles the deck or the discard pile'''
    if len(deck)==0:
        #shuffle discard
        print 'shuffle discard'
    else:
        #shuffle deck
        print 'shuffle deck'
    return shuffled
    # 60 cards, each numbered 1 to 60
def check_racko(rack):
    '''determine if Racko has been achieved, ascending order'''
    return is_racko
def deal_card():
    '''get the top card from the deck'''
    return top_card
def deal_initial_hands():
    ''' start the game oﬀ by dealing two hands of 10 cards each'''
    #return User_hand, Computer_hand
def does_user_begin():
    ''' simulate a coin toss by using the random library'''
    result=random.random()
    if result>0.5:
        coin='heads'
    else:
        coin='tails'
    return coin
def print_top_to_bottom(rack):
    ''' print it out from top to bottom in a manner more stack like than list like''' 
    for cards in rack:
        print cards+"\n"
def find_and_replace(newCard, cardToBeReplaced, hand):
    '''ﬁnd the cardToBeReplaced in the hand and replace it with newCard'''
    print "replace a card not in the hand, please try again with another one\n"
def add_card_to_discard(card):
    '''add the card to the top of the discard pile'''
def computer_play(hand):
    '''formulate the computer’s strategy'''
def main():
    '''the Racko game function'''

if __name__ == '__main__':
    main()

def reverselist(x):
    temp=x[:]
    temp.reverse()
    return temp
##lst.remove(i)
##lst.insert(i,x)
##lst.reverse()
##list1=lst[:]
##list1==list2

##for x,y in zip(one,two):
##    if x!=y:
##        is_racko=False
##        break

    
