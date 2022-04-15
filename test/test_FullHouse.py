from testing_base import *

def test_FullHouse():
    deckUsed = CardGames.Deck()
    deckUsed.shuffle()
    testPlayer = CardGames.Player("Test")
    riverPlayer = CardGames.Player("River")

    s5 = deckUsed.findCard(5, "Spades")
    c5 = deckUsed.findCard(5, "Clubs")
    s10 = deckUsed.findCard(10, "Spades")
    d5 = deckUsed.findCard(5, "Diamonds")
    h8 = deckUsed.findCard(8, "Hearts")
    h5 = deckUsed.findCard(5, "Hearts")
    s8 = deckUsed.findCard(8, "Spades")

    testPlayer.hand.append(s5)
    testPlayer.hand.append(c5)
    riverPlayer.hand.append(s10)
    riverPlayer.hand.append(d5)
    riverPlayer.hand.append(h8)
    riverPlayer.hand.append(h5)
    riverPlayer.hand.append(s8)

    print(findFullHouse(testPlayer, riverPlayer))
    assert(findFullHouse(testPlayer, riverPlayer) == (True, 5, 8))