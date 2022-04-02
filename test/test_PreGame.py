from testing_base import *

#code from Pre_Game file because importing messed with the cardgames file
def main():

    #######  this  code gives PlayerList values so Pre_game can run, we can delete when we merge code 
    joe = Player("Joe", 50)
    listofplayers = [joe]
    Pre_Game(listofplayers, "1")
    ########

def Pre_Game(PlayerList, user_in):

    while True:
        """user_in = input("Enter 1 to start game or 2 to quit: ")"""
        if user_in == "1":
            dealer = Dealer()
            deck = Deck()
            deck.shuffle()
            dealer.dealCards(2, PlayerList, deck)
            #River(Deck)  need Jacobs code for river
            return False
        if user_in == "2":
            break

main()

def test_PreGame():

    joe = Player("Joe", 50)
    listofplayers = [joe]
    Pre_Game(listofplayers,"1")
    print(len(listofplayers))
    assert len(listofplayers)==1
test_PreGame()