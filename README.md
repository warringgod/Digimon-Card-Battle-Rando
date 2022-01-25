# Digimon-Card-Battle-Rando

I'M TERRIBLE AT MAKING UI AND I'M ALSO A TERRIBLE CODER SO SORRY IN ADVANCE.
I also haven't quite finished this and made it "fully" customisable for the average non coder.

#How to Use
## You'll need to edit randomize.py because i cant make a UI.
## Only change the bits which say CHANGE ME (currently between line 29 and 37)
## Unless you know how to code as likely to break something

# All the following "change values" will generate a random value between 80% and 120%
# Of the cards ORIGINAL value.

Change_HP = True
Change_Circle = True
Change_Triangle = True
Change_Cross = True

# Cross effect change, there have been balances,so that counter always makes 0 X power
# Going from 0 to "none" has a normal amount of X power and such, to make nothing too broken or bad.
Change_Cross_Effect = True

# there will be a 8/10 chance of having the normal dp, but 1/10 of having +- 10dp
Change_Plus_DP = True

# the number of cards to change element for, does not affect partners.
# I recommend not doing more than 50 unless you want some real crazy, 
# if you put more than 172 (all avail) then it will error.
Change_Element = 25 # Number of Cards to Change element for, max 172, set to 0 if dont want, 10 recommended
# Will randomise the decks of opponents, changing options but keeping the same
# type and number of rookies, champs and ultimates. if change element is only
# then a "formerly" dark card could replace a fire card in a fire deck.
Randomise_Enemy_Decks = True

# buffs rare cards stats by 10% across the board.
Buff_Rare = True

# to create a randomised rom, run the .exe file.
# Made using the simple randomiser maker, which is super awesome



