The Mini Ultimatum Game is a simple web-based experiment designed using oTree, a platform for creating and administering economic experiments. This game simulates a scenario with three players: Player 1, Player 2, and Player 3.

In this game, Player 1 is endowed with a certain amount of money (e.g., Ksh 200) and is asked to decide how much of that money to send to Player 2. Player 3, also known as the "Punisher," observes the amount Player 1 has decided to send to Player 2. Depending on their judgment of fairness, Player 3 can choose to either "Punish" or "Not Punish" Player 1. The decisions of Player 3 impact the payoffs of all players involved.

Game Flow
Player 1's Decision (Page 1):

Player 1 starts the game with an endowment of Ksh 200.
They are asked to send an amount between 0 and 200 to Player 2.
Player 1's decision is kept confidential from Player 3.
Player 3's Decision (Page 2):

Player 3 sees the amount Player 1 has chosen to send to Player 2.
Player 3 must decide whether to "Punish" or "Not Punish" Player 1.
If Player 3 punishes Player 1, neither Player 1 nor Player 2 receives any payout.
Results Page (Page 3):

Player 1 is informed about the following:
The amount they sent to Player 2.
The decision made by Player 3.
The final payout they receive.
Player 2 is informed about the following:
The amount received from Player 1.
The decision made by Player 3.
The final payout they receive.
Development
Prerequisites
Python (3.6 or higher)
oTree (install using pip install otree)
