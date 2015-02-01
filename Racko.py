# -*- coding: utf-8 -*-
import random

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
        return True
    else:
        print "replace a card not in the hand, please try again with another one\n"
        return False
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
    #deck=range(1,25)
    discard=[]
##    global human_hand
##    global computer_hand
    human_hand=[]
    computer_hand=[]
    #keep track of the round
    game_round=1
    shuffle()
    print deck
    #deal a card to the computer and a card to the user
    #repeat until both have 10 cards
    userStarts = does_user_begin()
    #print userStarts
    if userStarts=='heads':
        print "user first"
        human_hand,computer_hand= deal_initial_hands()
        print human_hand
        print computer_hand
    elif userStarts=='tails':
        print "computer first"
        computer_hand,human_hand= deal_initial_hands()
        print human_hand
        print computer_hand
    #while neither the computer nor the user has racko:
    while not (check_racko(human_hand)or check_racko(computer_hand)):
        if game_round==1:
            new_card=deck.pop()
            print 'The new card in deck is',new_card
            #reveal one card to begin the discard pile
        elif game_round==0:
            #run out of deck, update game round now
            print 'We run out of deck. Now the last discard is unvailable.\n'
            new_card=deck.pop()
            print 'The new card in deck is',new_card
        else:
            new_card=discard.pop()
            #new_card=discard[-1]
            print 'The card in the discard is',new_card
        print "Here is your rack now:\n"
        print_top_to_bottom(human_hand)
        first_choice=raw_input('Do you want to use this card?Y/N\n')
        first_input_validate=True
        second_input_validate=True
        while first_input_validate:
            if first_choice=='y' or first_choice=='Y':
                cardToBeReplaced=input('Enter the number on card you want to replace:\n')
                replaced=find_and_replace(new_card, cardToBeReplaced, human_hand)
                #ask the user for the number of the card they want to kick out
                #modify the user’s hand and the discard pile
                while replaced:
                    print "This is what your rack looks like after this round\n"
                    print_top_to_bottom(human_hand)
                    #update discard
                    add_card_to_discard(cardToBeReplaced)
                    first_input_validate=False
                    replaced=False
                #print the user’s hand
            elif first_choice=='n' or first_choice=='N':
                #update discard
                add_card_to_discard(new_card)
                if game_round==1 or game_round==0:
                    print "You skip this round\n"
                else:
                    new_card = deck.pop()
                    print 'The card you get from the deck is ' + str(new_card)
                    #ask the user if they want this
                    second_choice = raw_input('Do you want to keep it?Y/N\n')
                    while second_input_validate:
                        if second_choice=='y' or second_choice=='Y':
                            #modify user’s hand, the discard pile and then print user’s hand
                            not_replaced=True
                            while not_replaced:
                                cardToBeReplaced=input('Enter the number on card you want to replace:\n')
                                replaced=find_and_replace(new_card, cardToBeReplaced, human_hand)
                                #ask the user for the number of the card they want to kick out
                                #modify the user’s hand and the discard pile
                                if replaced:
                                    print "This is what your rack looks like after this round\n"
                                    print_top_to_bottom(human_hand)
                                    #update discard
                                    add_card_to_discard(cardToBeReplaced)
                                    #first_input_validate=False???
                                    not_replaced=False
                            second_input_validate=False
                        elif second_choice=='n' or second_choice=='N':
                            add_card_to_discard(new_card)
                            #print the user’s hand
                            print "This is what your rack looks like after this round\n"
                            print_top_to_bottom(human_hand)
                            second_input_validate=False
                        else:
                            #stay in the loop when the input is incorrect
                            while second_choice!='y' and second_choice!='Y' and second_choice!='n' and second_choice!='N':
                                second_choice=raw_input('Please enter n or y to continue.\nDo you want to keep it?Y/N\n')
                                break
                first_input_validate=False
            else:
                #stay in the loop when the input is incorrect
                while first_choice!='y' and first_choice!='Y' and first_choice!='n' and first_choice!='N':
                    first_choice=raw_input('Please enter n or y to continue.\nDo you want to use this card?Y/N\n')
                    break
        ##comment for testing, since there is no computer strategy
        #computer_hand = computer_play(computer_hand)
        if game_round==0:
            game_round=2
        if len(deck)==0:
            #print 'discard before',discard,'\n'
            shuffle()
            #print 'discard after',discard,'\n'
            discard_value=discard[:]
            #print discard_value,'\n'
            deck=discard_value
            #reset discard
            discard=[]
##            print 'deck',deck,'\n'
##            print 'discard now',discard
            game_round=-1
        #check and make sure there are still some cards in the deck
        #else reshuffle the discard and restart
        game_round=game_round+1
        #update game round number
        print 'game_round',game_round
        print 'deck',len(deck)
        print 'deck is',deck
        print 'discard is',discard
    #print conclusion
    if check_racko(human_hand):
        print 'Great! You win this game.'
    elif check_racko(computer_hand):
        print 'Sorry, you lose this game.'
        
if __name__ == '__main__':
    main()



    
