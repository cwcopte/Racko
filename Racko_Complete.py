# authors -- Zi Chen  and  Wei Chen

import random

def main():
    global deck
    global discard
    deck=range(1,61)
    discard=[]

    shuffle()
    print "shuffle complete."
    
    (human_hand,computer_hand)=deal_initial_hands()
    print "dealing cards complete."

    userStarts = does_user_begin()
    
    print "The following are your hand:"
    print_top_to_bottom(human_hand)

    discard.append(deal_card()) # reveal one card to begin the discard pile

    print userStarts,"starts first.\n"

    while not (check_racko(human_hand) or check_racko(computer_hand)):
        if userStarts == 'computer':
            computer_hand = computer_play(computer_hand)
            print "Computer done.\n\n"


        if len(deck) == 0:  # check and make sure deck is not empty, or reshuffle and restart
            shuffle()
            deck , discard = discard , deck
            discard.append(deal_card())


        print "The top card of discard pile is: ", discard[-1]
        choice=raw_input('Do you want this card? y/n:  ')

        while (choice!='y') and (choice!='n'):   # ensure user to input right syntax choice
            choice=raw_input('Do you want this card? y/n:  ')
            

        print "The following are your hand:"
        print_top_to_bottom(human_hand)

        if choice == 'y':
            card=discard.pop()            

            card_to_be_replaced=input('Plese enter the card(number) to be replaced: ')
            find_and_replace(card,card_to_be_replaced,human_hand)

        elif choice == 'n':
            card=deal_card()
            print "The card you get from the deck is " + str(card)

            secondChoice=raw_input('Do you want to keep it? y/n:  ')

            while (secondChoice!='y') and (secondChoice!='n'):   # ensure user to input right syntax choice
                secondChoice=raw_input('Do you want to keep it? y/n:  ')

            if secondChoice == 'y':
                card_to_be_replaced=input('Plese enter the card(number) to be replaced: ')
                find_and_replace(card,card_to_be_replaced,human_hand)
            elif secondChoice == 'n':
                discard.append(card)

        print "The following are your hand:"
        print_top_to_bottom(human_hand)


        if len(deck) == 0:  # check and make sure deck is not empty, or reshuffle and restart
            shuffle()
            deck , discard = discard , deck
            discard.append(deal_card())

            
        if userStarts == 'human':
            computer_hand = computer_play(computer_hand)
            print "Computer done.\n\n"

    if check_racko(human_hand):
        print "\nCongratulation! You win !\n"
        print "Your hand as follow:"
        print_top_to_bottom(human_hand)
    else:
        print "\nComputer beats you !\n"
        print "Computer's hand as follow:"
        print_top_to_bottom(computer_hand)

    

def shuffle():
    '''shuffles the deck or the discard pile'''
    if len(deck) > 0:
        random.shuffle(deck)
    elif len(deck) == 0:
        random.shuffle(discard)

def check_racko(rack):
    '''determine if the given rack achieves Racko'''
    slot_rack=rack[-1::-1]
    temp=slot_rack[:]
    temp.sort()
    if temp == slot_rack:
        return True
    else:
        return False

def deal_card():
    '''get the top card from the deck and return it'''
    return deck.pop()
    
def deal_initial_hands():
    '''start the game off by dealing two hands of 10 cards each'''
    human_hand=[]
    computer_hand=[]
    for deal in range(1,11):
        computer_hand.append(deck.pop())
        human_hand.append(deck.pop())
    return (human_hand,computer_hand)

def does_user_begin():
    '''use a coin toss to decide who starts first'''
    coin=random.random()
    if coin < 0.5:
        return 'human'
    else:
        return 'computer'

def print_top_to_bottom(rack):
    '''print a rack out from top to bottom'''
    for index in range(0,10):
        print rack[index]

def find_and_replace(newCard,cardToBeReplaced,hand):
    '''find the card to be replaced and replace it with new card, modify hand and discard pile'''
    while cardToBeReplaced not in hand:
        print "the card you ask to be replaced is not in your hand. Please try again."
        cardToBeReplaced=input('Plese enter the card to be replaced: ')
    for index in range(0,10):
        if cardToBeReplaced == hand[index]:
            hand[index]=newCard
            add_card_to_discard(cardToBeReplaced)
            break

def add_card_to_discard(card):
    '''add the card(represented as integer) to the top of discard pile'''
    discard.append(card)

def computer_play(hand):
    '''computer's strategy'''
    computer_hand=[]
    lst=[range(55,61),range(49,55),range(43,49),range(37,43),range(31,37),
         range(25,31),range(19,25),range(13,19),range(7,13),range(1,7)]
    
    for i in range(0,10):
        if discard[-1] in lst[i]:
            break
    if hand[i] not in lst[i]:  # use top card of discard pile
        card=discard.pop()
        discard.append(hand[i])
        hand[i]=card        

    else:
        card=deck.pop()
        for j in range(0,10):
            if card in lst[j]:
                break
        if hand[j] not in lst[j]:
            discard.append(hand[j])
            hand[j]=card

        else:
            discard.append(card)

    computer_hand = hand
    return computer_hand

if __name__ == '__main__':
    main()
    
