# This is a randomizer file for the Simple Randomizer Maker.
# This file must be named randomizer.py in order to work.

from classes import *
import random

def value(name):
	for att in Attributes:
		if att.name == name:
			return att
	print("This attribute does not exist: "+name)
	return None

########################
# EDIT BELOW THIS LINE #
########################

Program_Name = "Digimon Card Battle Randomiser"
Rom_Name = "Digimon Card Battle .bin"
Rom_File_Format = "bin" # Rom file format (nes, gba, etc.)
About_Page_Text = "This Randomiser changes DP, +DP, HP, Circle, Triangle, Cross and Cross effect of cards, and elements In the future" \
				  " i'll also try to change the card support effects."
Timeout = 10
Slow_Mode = False

### CHANGE ME!!!!!!!!!!!!!!!!!!!!!!!!
# need to change the element shuffle so it swaps a champion with another champion of another element

Change_HP = True
Change_Circle = True
Change_Triangle = True
Change_Cross = True
Change_Cross_Effect = True
Change_Plus_DP = True
Change_Element = 25 # Number of Cards to Change element for, max 172, set to 0 if dont want, 10 recommended
Randomise_Enemy_Decks = True
Buff_Rare = True

### CHANGE ME!!!!!!!!!!!!!!!!!!!!!!!!

#constants
fire_special_modifier="fire"
nature_special_modifier="nature"
ice_special_modifier="ice"
darkness_special_modifier="darkness"
rare_special_modifier="rare"
rookie_modifier = 2
champion_modifier = 5
ultimate_modifier = 10

number_element_to_swap = int(Change_Element/5)
elements = [0,16,32,48,64]
normal_card_dict_of_elements = {}
card_list_of_elements = {}
fire_ultimates = []
fire_champions = []
fire_rookies = []
ice_ultimates = []
ice_champions = []
ice_rookies = []
nature_ultimates =[]
nature_champions = []
nature_rookies = []
darkness_ultimates = []
darkness_champions = []
darkness_rookies =[]
rare_ultimates = []
rare_champions = []
rare_rookies = []
current_deck_card_number = None
strong_option_card_numbers = [191, 192, 197, 198, 285, 286, 287, 288, 289, 290, 291, 292,
							  293]  # cards which would be OP early
normal_option_card_numbers = []
already_inserted_into_deck = []

# this makes sure that if you swap 15, at least 3 will come from each element
fire_card_list_to_change = random.sample(range(0, 34), min(number_element_to_swap,34))
ice_card_list_to_change = random.sample(range(34, 69), min(number_element_to_swap,35))
nature_card_list_to_change = random.sample(range(69, 103), min(number_element_to_swap,34))
darkness_card_list_to_change = random.sample(range(103, 139), min(number_element_to_swap,36))
rare_card_list_to_change = random.sample(range(140, 172), min(number_element_to_swap,32))

all_list_to_change = fire_card_list_to_change + ice_card_list_to_change + nature_card_list_to_change + darkness_card_list_to_change + rare_card_list_to_change

#Decks
Red_Deck = [16,16,20,20,26,26,126,126,130,130,27,27,29,29,30,33,33,133,133,134,134,135,135,175,264,264,266,267,267,299]
Green_Deck = [91,91,92,92,95,95,162,162,163,163,97,97,99,99,101,102,102,165,165,169,169,170,170,182,266,266,270,270,272,299]
Yellow_Deck = [55,55,56,56,157,157,159,159,161,161,62,62,66,66,67,67,166,166,168,170,170,171,171,190,262,263,263,266,266,299]
Meramon_Deck = [10,10,18,18,18,18,20,20,20,26,26,26,28,28,28,29,29,30,30,31,31,31,32,32,32,33,258,258,258,258]
Phoenixmon_Deck = [3, 3, 3, 3, 13, 13, 20, 20, 20, 23, 23, 23, 28, 28, 28, 28, 29, 29, 29, 29, 30, 30, 239, 258, 264, 265, 265, 268, 268, 269]
Veemon_Deck = [8,9,9,10,10,14,14,14,16,16,16,17,17,17,27,27,27,27,28,28,29,32,32,33,175,264,264,264,267,267]
Vegiemon_Deck = [78,78,79,79,80,80,84,84,89,89,94,94,95,95,95,95,97,97,97,97,98,98,98,98,99,99,99,99,102,102]
Ninjamon_Deck = [83,83,89,89,89,89,91,91,93,93,97,97,98,98,99,99,100,100,101,101,260,260,296,296,296,296,300,300,300,300]
Veedramon_Deck =  [72,72,80,81,81,81,81,87,87,87,97,97,97,98,98,98,99,99,99,102,102,215,247,248,251,265,264,264,266,266]
Wormmon_Deck = [90,90,91,119,119,126,126,100,100,102,102,102,132,132,132,136,136,136,137,137,187,254,254,261,261,263,263,264,264,269]
Frigimon_Deck = [38,45,52,52,52,52,55,60,60,61,61,62,62,64,64,64,67,67,67,191,242,242,243,243,244,244,244,259,259,266]
Whamon_Deck = [40,42,44,47,47,48,48,49,49,56,61,61,61,63,63,63,65,65,65,66,66,66,236,236,270,270,271,271,272,272]
Garurumon_Deck = [39,40,40,46,46,46,46,59,59,60,60,62,62,62,64,64,64,66,66,67,67,67,249,249,250,250,251,251,264,264]
Stingmon_Deck = [112,112,114,114,117,117,120,120,129,129,133,133,133,135,135,135,135,138,138,138,201,209,213,214,230,240,254,263,265,265]
Garurumon2_Deck = [39,40,40,46,46,46,46,59,59,60,60,62,62,62,64,64,64,66,66,67,67,67,249,249,250,250,251,251,264,264]
Hagurumon_Deck = [146,148,149,152,152,153,153,159,159,165,165,166,166,166,166,167,167,168,168,169,169,193,193,226,226,235,238,262,262,262]
ShellNumemon_Deck = [155,155,155,155,157,157,157,160,160,168,168,168,170,170,170,171,171,171,214,214,220,220,238,238,253,270,270,271,272,272]
KingSukamon_Deck = [154,154,156,158,158,158,158,165,168,168,168,169,169,169,169,170,170,170,201,201,201,225,225,252,252,252,252,262,262,262]
Shadramon_Deck = [10,109,114,114,26,26,26,117,117,117,117,130,130,31,31,31,31,135,135,136,136,137,137,187,219,219,295,295,299,299]
Wormmon2_Deck = [113,115,90,90,119,119,126,126,100,102,102,102,132,132,136,136,136,137,137,187,254,254,261,261,263,263,264,264,269,299]
Stingmon2_Deck = [112,112,114,114,117,117,117,117,120,129,129,133,133,135,135,135,135,138,138,138,187,201,209,213,214,230,240,254,263,265]
Shadramon2_Deck = [10,111,111,114,26,26,117,117,117,130,130,31,31,31,31,135,135,136,137,137,187,219,219,239,239,294,295,295,299,299]
Quetzalmon_Deck = [43,43,112,112,114,50,50,58,117,117,120,120,120,65,65,65,65,132,132,136,136,136,187,209,216,216,218,218,220,220]
Digimon_Emperor_Deck = [104,104,109,117,117,117,118,118,124,132,132,134,134,135,135,138,138,138,138,187,209,209,253,253,253,253,261,261,265,265]
Centarumon_Deck = [11,11,11,17,17,19,19,19,23,23,24,27,27,27,27,31,31,31,31,32,32,223,223,223,224,224,224,236,236,236]
Tyrannomon_Deck = [8,8,8,80,16,16,16,16,17,91,91,92,92,27,27,27,29,29,30,30,97,97,101,101,101,244,244,244,258,258]
Angemon_Deck = [75,77,77,82,82,82,82,88,88,96,96,97,97,97,98,98,98,99,99,99,99,237,237,237,246,246,246,260,260,260]
Davis_Deck = [4,4,9,12,12,12,14,14,18,26,27,27,27,29,29,29,31,31,32,32,175,198,258,258,258,264,264,264,267,267]
Keeley_Deck = [76,76,79,81,81,87,87,87,94,94,97,97,97,99,99,99,100,100,100,182,201,213,240,241,242,243,245,249,250,251]
Cody_Deck = [142,142,143,151,151,151,161,161,163,163,165,165,165,166,166,167,167,168,168,190,197,197,210,210,247,247,247,247,248,248]
TK_Deck = [75,75,77,82,82,82,87,87,88,88,97,97,97,97,98,99,99,99,99,183,221,221,239,265,265,294,297,297,298,299]
Wizardmon_Deck = [45,115,115,57,57,118,118,118,118,127,67,67,67,134,134,135,135,138,138,138,193,199,205,219,222,241,241,255,255,295]
AeroVeedramon_Deck = [72,72,72,72,81,81,81,81,85,85,85,97,97,97,98,98,98,99,100,100,100,193,193,231,231,232,232,235,235,254]
Gatomon_Deck = [83,83,83,83,85,85,85,91,91,99,99,99,100,100,100,101,101,101,101,227,227,230,230,251,251,251,264,264,264,264]
Kari_Deck = [73,77,77,78,20,83,83,83,84,84,84,29,98,98,98,98,99,99,99,99,184,193,193,211,211,260,260,260,295,295]
Goburimon_Deck = [33,33,33,68,68,68,101,101,101,138,138,138,166,166,166,198,202,202,202,202,231,231,231,231,264,264,264,264,296,296]
DemiDevimon_Deck = [106,111,111,113,113,114,132,132,132,132,133,133,133,133,135,135,135,135,136,136,136,136,137,137,137,137,297,297,297,297]
Megadramon_Deck = [112,112,112,112,119,119,119,119,129,129,129,129,133,133,134,134,134,134,135,135,135,135,230,230,261,261,269,269,299,299]
Gigadramon_Deck = [5,5,112,112,20,26,26,26,124,124,124,127,27,27,27,28,28,134,134,134,136,136,194,194,230,230,233,233,299,299]
Togemon_Deck = [78,78,84,84,84,84,89,89,89,92,98,98,98,98,100,100,100,102,102,102,204,204,227,227,245,245,260,260,269,269]
Kabuterimon_Deck = [79,79,86,86,86,86,90,90,90,94,97,97,97,97,101,101,101,102,102,102,234,234,234,234,247,247,248,248,254,254]
Ikkakumon_Deck = [40,40,47,47,47,47,52,52,52,58,61,61,61,61,64,64,64,65,65,65,67,249,249,249,259,259,259,266,266,266]
Birdramon_Deck = [7,7,13,13,20,20,20,20,21,21,29,29,29,29,31,31,31,33,33,33,196,196,204,204,249,249,250,250,251,251]
WereGarurumon_Deck = [39,39,39,39,46,46,46,46,59,59,60,62,62,62,64,64,64,66,67,67,67,191,191,221,221,221,246,246,246,266]
MetalGreymon_Deck = [6,6,6,6,14,20,46,47,82,84,86,27,27,27,27,29,61,62,97,98,99,258,258,258,295,295,295,295,296,296]
Tuskmon_Deck = [108,113,113,121,121,121,121,122,126,128,133,133,133,135,135,135,138,138,138,138,202,202,215,215,215,215,228,228,267,267]
Phantomon_Deck = [114,114,114,114,123,123,123,123,127,127,127,135,135,135,137,137,137,137,138,138,138,205,205,205,253,253,264,264,269,269]
MegaSeadramon_Deck = [42,42,42,42,47,48,48,52,52,55,55,64,64,64,65,65,65,67,67,68,68,68,201,201,201,201,252,252,252,252]
VenomMyotismon_Deck = [106,106,106,106,119,119,119,121,121,123,123,132,132,132,132,133,133,133,135,135,135,192,192,192,199,199,205,205,299,299]
Leomon_Deck = [85,85,85,85,91,91,126,126,126,99,99,99,100,100,101,133,133,133,138,196,196,196,260,260,260,261,261,261,295,295]
Devimon_Deck = [58,58,58,58,120,120,120,120,65,65,68,68,68,68,132,132,132,132,136,136,192,192,234,234,259,259,259,261,261,261]
MetalEtemon_Deck = [141,141,141,150,150,162,162,163,163,164,164,165,165,165,169,169,169,170,170,170,191,191,195,195,237,237,297,297,299,299]
Myotismon_Deck = [111,111,111,111,119,119,119,121,121,123,123,132,132,132,132,133,133,133,135,135,135,192,192,192,199,199,205,205,299,299]
Greymon_Deck = [6,6,6,6,14,14,14,14,20,20,27,27,27,27,29,29,29,29,33,33,258,258,264,264,266,266,299,299,299,299]
ExVeemon_Deck = [12,12,12,12,14,14,15,15,27,27,27,27,30,30,30,31,31,31,215,215,215,232,232,232,234,234,234,249,249,249]
Flamedramon_Deck = [11,11,12,12,18,25,25,25,25,27,28,28,28,28,31,31,31,32,32,175,196,196,243,243,246,246,246,266,266,266]
Raidramon_Deck = [12,12,12,26,118,118,118,125,29,29,29,30,30,134,134,134,136,136,175,204,204,204,248,248,248,261,265,265,294,298]
Hawkmon_Deck = [83,83,84,87,87,87,91,91,91,99,99,99,99,101,101,101,101,102,102,182,216,217,218,219,220,248,248,248,248,257]
Aquilamon_Deck = [7,7,72,72,13,13,20,20,87,87,94,94,28,29,29,29,29,97,97,97,100,182,206,206,260,260,269,269,296,296]
Halsemon_Deck = [76,76,76,81,81,87,87,87,94,94,97,97,97,99,99,99,100,100,100,182,241,241,241,242,242,242,243,243,243,294]
Penguinmon_Deck = [51,52,52,56,56,57,162,162,163,61,61,62,62,62,64,64,64,64,65,65,169,169,171,171,266,270,270,271,271,272]
Rosemon_Deck = [73,73,73,84,84,92,92,131,131,22,98,98,98,98,101,101,101,137,137,137,28,28,260,266,266,264,269,269,299,299]
Armadillomon_Deck = [159,159,159,159,165,165,166,166,166,170,170,169,169,169,190,212,212,213,213,225,225,225,247,247,255,255,255,255,262,262]
Ankylomon_Deck = [144,144,144,151,151,151,151,154,154,163,163,165,165,165,168,168,169,169,170,170,170,222,222,222,223,223,223,224,224,224]
Digmon_Deck = [142,142,159,159,159,159,165,165,166,166,166,170,170,169,169,190,203,203,210,213,213,221,221,221,225,225,255,255,255,255]
Thundermon_Deck = [146,146,146,153,153,153,153,164,164,166,166,166,166,167,167,167,167,169,169,197,197,201,201,226,226,227,227,262,299,299]
MetalMamemon_Deck = [146,146,148,148,149,149,89,89,89,152,152,153,153,156,156,97,97,101,101,101,166,166,166,168,168,168,295,295,299,299]
SuperStarmon_Deck = [140,140,140,140,147,152,152,152,152,161,161,161,161,165,165,165,165,166,166,166,169,169,169,169,237,237,264,264,299,299]
Bakemon_Deck = [123,123,123,123,127,127,127,127,133,133,133,135,135,135,137,137,137,137,197,221,221,221,246,246,246,246,266,266,266,266]
Devimon2_Deck = [113,113,119,119,120,120,120,120,122,122,132,132,132,132,135,135,135,138,138,138,192,192,192,192,235,235,237,237,261,261]
SkullGreymon_Deck = [113,113,113,113,120,120,120,122,122,125,125,132,132,132,132,135,135,135,138,138,138,218,218,218,225,225,225,255,255,255]
Myotismon2_Deck = [111,111,111,111,118,118,118,118,120,120,120,132,132,132,135,135,135,135,137,137,137,199,199,200,205,239,263,263,287,292]
Patamon_Deck = [97,97,98,98,99,99,100,100,101,101,102,102,183,208,208,208,208,221,231,231,231,231,260,260,260,260,266,266,266,266]
Baronmon_Deck = [11,11,75,75,26,26,26,82,82,82,28,28,28,32,32,99,99,101,101,101,183,258,258,258,260,260,260,295,295,296]
Pegasusmon_Deck = [70,70,75,75,82,82,82,87,87,88,88,97,97,97,97,98,99,99,99,99,183,221,221,265,265,294,297,297,298,299]
Gatomon2_Deck = [75,75,85,85,85,91,91,99,99,99,100,100,100,101,101,101,184,193,193,203,203,211,211,246,246,253,253,257,264,264]
Nefertimon_Deck = [71,71,77,77,87,87,87,88,88,88,98,98,99,99,99,99,100,100,100,184,193,193,193,196,196,221,211,211,257,298]
Tylomon_Deck = [38,38,71,71,50,50,56,82,82,96,63,63,63,66,66,99,99,99,102,184,236,236,241,241,259,259,295,295,294,298]
Tentomon_Deck = [80,80,86,86,90,90,92,92,92,92,97,97,97,97,99,99,102,102,102,102,191,191,249,249,250,250,251,251,253,253]
Kuwagamon_Deck = [84,90,90,90,90,91,91,97,97,97,97,100,100,100,101,101,101,192,198,202,202,215,215,227,227,228,240,240,245,245]
HerculesKabuterimon_Deck = [74,74,74,74,79,86,86,90,90,94,117,117,117,97,97,97,102,102,102,134,134,136,136,204,204,204,260,260,264,264]
Wargreymon_Deck = [2,2,2,2,6,14,14,14,14,15,15,16,27,27,27,27,28,28,28,28,29,29,196,196,224,224,258,258,299,299]
Rosemon2_Deck = [73,73,73,84,84,92,92,131,131,22,98,98,98,98,101,101,101,137,137,137,28,28,260,266,266,264,269,269,299,299]
Tai_Deck = [1,2,2,2,6,6,6,27,27,27,27,29,29,29,30,30,31,31,203,203,203,221,221,221,266,266,297,297,297,297]
Paildramon_Deck = [4,4,4,4,12,12,12,19,19,27,27,27,27,30,30,30,31,31,31,249,249,249,250,250,250,251,251,251,299,299]
Garudamon_Deck = [7,7,7,7,13,13,13,20,20,20,20,27,27,27,28,28,28,28,29,29,29,29,244,244,244,244,266,266,266,266]
Sora_Deck = [7,7,7,7,20,20,20,20,26,26,27,27,27,29,29,29,29,30,30,30,295,295,296,296,297,297,299,299,299,300]
Shurimon_Deck = [76,76,89,89,89,156,156,156,98,98,101,101,168,168,169,169,169,182,203,203,203,204,204,245,245,245,265,265,295,295]
Lillymon_Deck = [73,78,78,78,78,80,80,83,84,84,84,84,89,89,96,96,96,97,97,97,98,98,98,98,99,99,100,100,101,101]
Mimi_Deck = [78,78,78,78,53,53,84,84,84,122,157,158,66,66,66,98,98,98,98,137,137,165,165,165,203,203,203,260,260,262]
Submarimon_Deck = [34,142,47,47,56,56,151,151,151,61,61,61,63,63,63,165,165,165,190,221,221,221,238,238,238,257,259,294,295,295]
Metalgarurumon_Deck = [34,142,47,47,56,56,151,151,151,61,61,61,63,63,63,165,165,165,190,221,221,221,238,238,238,257,259,294,295,295]
Matt_Deck = [36,36,36,75,46,46,46,46,82,82,82,62,62,62,62,64,64,100,100,100,101,259,259,260,260,265,265,267,267,268]
Zudomon_Deck = [40,40,40,40,47,47,47,47,57,57,59,118,61,61,61,61,68,68,68,68,138,138,194,226,227,230,230,245,245,245]
# Joes last 3 cards are 0 , so not sure what thats about
Joe_Deck = [38,38,38,39,40,40,47,47,47,48,48,48,52,52,55,55,61,61,61,61,63,63,63,63,66,66,66,0,0,0]
MegaKabuterimon_Deck =  [79,79,79,79,46,46,46,86,86,86,90,90,90,161,161,161,97,97,97,97,101,101,101,102,102,102,251,251,251,251]
Izzy_Deck =  [79,79,86,86,86,86,90,90,90,97,97,97,97,101,101,101,102,102,102,247,247,248,248,254,254,256,256,257,265]
MagnaAngemon_Deck =  [70,75,75,75,82,82,82,82,88,88,96,97,97,98,98,98,99,99,99,99,183,237,237,237,246,246,246,260,260,260]
Angewomon_Deck =  [77,77,77,77,87,87,87,87,88,88,98,98,99,99,99,99,100,100,100,184,191,193,196,196,211,221,235,239,242,257]
GranKuwagamon_Deck =  [104,104,104,104,117,117,117,119,119,121,132,132,134,134,137,137,138,138,138,138,187,201,201,205,205,230,251,251,299,299]
Ken_Deck =  [104,104,104,117,117,117,118,118,124,132,132,134,135,135,138,138,138,138,187,209,209,253,253,253,253,265,265,294,299,299]
MetalSeadramon_Deck =  [36,36,36,42,43,50,50,50,51,51,54,54,63,63,63,65,65,65,65,66,66,66,222,222,222,223,223,224,224,224]
Puppetmon_Deck =  [139,139,139,139,147,159,159,159,159,163,163,163,165,165,166,166,167,167,167,167,168,168,168,225,225,226,226,235,262,262]
Machinedramon_Deck =  [108,108,108,108,116,124,124,124,124,159,159,159,134,134,134,134,165,165,165,166,166,166,202,202,254,261,261,299,299,299]
LadyDevimon_Deck =  [110,110,110,119,119,119,120,120,120,132,132,132,132,135,135,135,137,137,137,137,201,201,213,213,240,240,241,241,245,245]
Piedmon_Deck =  [36,107,108,139,50,50,124,124,125,125,159,159,65,65,65,166,166,166,166,167,167,167,199,199,259,261,262,295,295,295]
Magnamon_Deck =  [4,4,4,12,12,12,17,23,23,23,27,27,27,27,29,29,29,31,31,31,175,193,193,247,254,254,257,265,294,298]
Sylphymon_Deck =  [76,76,76,76,81,81,87,87,87,89,89,97,97,97,97,98,98,98,101,101,182,203,203,222,222,223,224,224,234,235]
Shakkoumon_Deck =  [142,142,142,143,151,151,151,159,159,163,163,165,165,165,165,169,169,169,170,170,170,205,205,220,220,225,225,238,238,239]
Seraphimon_Deck =  [70,70,70,75,82,82,82,82,88,88,96,97,97,98,98,98,99,99,99,99,183,208,208,208,260,260,260,297,297,297]
Magnadramon_Deck =  [71,71,71,71,87,87,87,87,88,88,98,98,99,99,99,99,100,100,100,184,221,221,221,246,246,246,253,253,266,266]
Infermon_Deck =  [109,109,109,109,123,123,127,127,127,127,154,154,154,154,134,134,134,134,137,137,137,137,138,138,138,138,247,247,247,247]
Diaboromon_Deck =  [105,105,105,105,124,124,124,125,125,125,133,133,134,134,134,134,137,137,137,137,203,203,205,205,253,253,253,299,299,299]




New_Red_Deck = []
New_Green_Deck = []
New_Yellow_Deck = []
New_Meramon_Deck = []
New_Phoenixmon_Deck = []
New_Veemon_Deck = []
New_Vegiemon_Deck = []
New_Ninjamon_Deck = []
New_Veedramon_Deck = []
New_Wormmon_Deck = []
New_Frigimon_Deck = []
New_Whamon_Deck = []
New_Garurumon_Deck = []
New_Stingmon_Deck = []
New_Garurumon2_Deck = []
New_Hagurumon_Deck = []
New_ShellNumemon_Deck = []
New_KingSukamon_Deck = []
New_Shadramon_Deck = []
New_Wormmon2_Deck = []
New_Stingmon2_Deck = []
New_Shadramon2_Deck = []
New_Quetzalmon_Deck = []
New_Digimon_Emperor_Deck = []
New_Centarumon_Deck = []
New_Tyrannomon_Deck = []
New_Angemon_Deck = []
New_Davis_Deck = []
New_Keeley_Deck = []
New_Cody_Deck = []
New_TK_Deck = []
New_Wizardmon_Deck = []
New_AeroVeedramon_Deck = []
New_Gatomon_Deck = []
New_Kari_Deck = []
New_Goburimon_Deck = []
New_DemiDevimon_Deck = []
New_Megadramon_Deck = []
New_Gigadramon_Deck = []
New_Togemon_Deck = []
New_Kabuterimon_Deck = []
New_Ikkakumon_Deck = []
New_Birdramon_Deck = []
New_WereGarurumon_Deck = []
New_MetalGreymon_Deck = []
New_Tuskmon_Deck = []
New_Phantomon_Deck = []
New_MegaSeadramon_Deck = []
New_VenomMyotismon_Deck = []
New_Leomon_Deck = []
New_Devimon_Deck = []
New_MetalEtemon_Deck = []
New_Myotismon_Deck = []
New_Greymon_Deck = []
New_ExVeemon_Deck = []
New_Flamedramon_Deck = []
New_Raidramon_Deck = []
New_Hawkmon_Deck = []
New_Aquilamon_Deck = []
New_Halsemon_Deck = []
New_Penguinmon_Deck = []
New_Rosemon_Deck = []
New_Armadillomon_Deck = []
New_Ankylomon_Deck = []
New_Digmon_Deck = []
New_Thundermon_Deck = []
New_MetalMamemon_Deck = []
New_SuperStarmon_Deck = []
New_Bakemon_Deck = []
New_Devimon2_Deck = []
New_SkullGreymon_Deck = []
New_Myotismon2_Deck = []
New_Patamon_Deck = []
New_Baronmon_Deck = []
New_Pegasusmon_Deck = []
New_Gatomon2_Deck = []
New_Nefertimon_Deck = []
New_Tylomon_Deck = []
New_Tentomon_Deck = []
New_Kuwagamon_Deck = []
New_HerculesKabuterimon_Deck = []
New_Wargreymon_Deck = []
New_Rosemon2_Deck = []
New_Tai_Deck = []
New_Paildramon_Deck = []
New_Garudamon_Deck = []
New_Sora_Deck = []
New_Shurimon_Deck = []
New_Lillymon_Deck = []
New_Mimi_Deck = []
New_Submarimon_Deck = []
New_Metalgarurumon_Deck = []
New_Matt_Deck = []
New_Zudomon_Deck = []
New_Joe_Deck = []
New_MegaKabuterimon_Deck = []
New_Izzy_Deck = []
New_MagnaAngemon_Deck = []
New_Angewomon_Deck = []
New_GranKuwagamon_Deck = []
New_Ken_Deck = []
New_MetalSeadramon_Deck = []
New_Puppetmon_Deck = []
New_Machinedramon_Deck = []
New_LadyDevimon_Deck = []
New_Piedmon_Deck = []
New_Magnamon_Deck = []
New_Sylphymon_Deck = []
New_Shakkoumon_Deck = []
New_Seraphimon_Deck = []
New_Magnadramon_Deck = []
New_Infermon_Deck = []
New_Diaboromon_Deck = []



def randomise_elements():
	card_list_of_elements.clear()
	normal_card_dict_of_elements.clear()
	for i in range(0, 172):
		if i <= 11 or (34 <= i <= 45) or (69 <= i <= 80) or (103 <= i <= 116) or (139 <= i <= 150):
			level_number = 3
		elif (12 <= i <= 26) or (46 <= i <= 60) or (81 <= i <= 96) or (117 <= i <= 131) or (151 <= i <= 164):
			level_number = 2
		else:
			level_number = 0

		if i <= 33:
			normal_element = 0
		elif 34 <= i <= 68:
			normal_element = 16
		elif 69 <= i <= 103:
			normal_element = 32
		elif 104 <= i <= 138:
			normal_element = 48
		elif 139 <= i <= 171:
			normal_element = 64

		normal_card_dict_of_elements.update({i: level_number + normal_element})

		if i in all_list_to_change:
			card_list_of_elements.update({i: level_number + random.choice(elements)})
		else:
			card_list_of_elements.update({i: level_number + normal_element})


def element_level_groups():

	fire_ultimates.clear()
	fire_champions.clear()
	fire_rookies.clear()
	ice_ultimates.clear()
	ice_champions.clear()
	ice_rookies.clear()
	nature_ultimates.clear()
	nature_champions.clear()
	nature_rookies.clear()
	darkness_ultimates.clear()
	darkness_champions.clear()
	darkness_rookies.clear()
	rare_ultimates.clear()
	rare_champions.clear()
	rare_rookies.clear()

	for i in range(0, 172):

		element_level_number = card_list_of_elements.get(i)

		if element_level_number == 3:
			fire_ultimates.append(i)
		elif element_level_number == 2:
			fire_champions.append(i)
		elif element_level_number == 0:
			fire_rookies.append(i)
		elif element_level_number == 19:
			ice_ultimates.append(i)
		elif element_level_number == 18:
			ice_champions.append(i)
		elif element_level_number == 16:
			ice_rookies.append(i)
		elif element_level_number == 35:
			nature_ultimates.append(i)
		elif element_level_number == 34:
			nature_champions.append(i)
		elif element_level_number == 32:
			nature_rookies.append(i)
		elif element_level_number == 51:
			darkness_ultimates.append(i)
		elif element_level_number == 50:
			darkness_champions.append(i)
		elif element_level_number == 48:
			darkness_rookies.append(i)
		elif element_level_number == 67:
			rare_ultimates.append(i)
		elif element_level_number == 66:
			rare_champions.append(i)
		elif element_level_number == 64:
			rare_rookies.append(i)


# make sure each element has at least 6 rookies, will cause problems in deck randomisation else
while (len(fire_rookies) < 6) or (len(ice_rookies) < 6) or (len(nature_rookies) < 6) or (len(darkness_rookies) < 6) or (len(rare_rookies) < 6) or (len(fire_champions) < 8) or (len(ice_champions) < 8) or (len(nature_champions) < 8) or (len(darkness_champions) < 8) or (len(rare_champions) < 8):
	randomise_elements()
	element_level_groups()

for i in range(191, 300):
	if i not in strong_option_card_numbers:
		normal_option_card_numbers.append(i)


def Pick_Card(card_number, unique_deck):
	# must be a better way of doing this
	global current_deck_card_number
	current_deck_card_number = card_number
	normal_ele = normal_card_dict_of_elements.get(card_number)

	x = 1

	while current_deck_card_number in unique_deck or (x == 1):
		x = 0
		if card_number in normal_option_card_numbers:
			current_deck_card_number = random.choice(normal_option_card_numbers)
		elif normal_ele == 3:
			current_deck_card_number = random.choice(fire_ultimates)
		elif normal_ele == 2:
			current_deck_card_number = random.choice(fire_champions)
		elif normal_ele == 0:
			current_deck_card_number = random.choice(fire_rookies)
		elif normal_ele == 19:
			current_deck_card_number = random.choice(ice_ultimates)
		elif normal_ele == 18:
			current_deck_card_number = random.choice(ice_champions)
		elif normal_ele == 16:
			current_deck_card_number = random.choice(ice_rookies)
		elif normal_ele == 35:
			current_deck_card_number = random.choice(nature_ultimates)
		elif normal_ele == 34:
			current_deck_card_number = random.choice(nature_champions)
		elif normal_ele == 32:
			current_deck_card_number = random.choice(nature_rookies)
		elif normal_ele == 51:
			current_deck_card_number = random.choice(darkness_ultimates)
		elif normal_ele == 50:
			current_deck_card_number = random.choice(darkness_champions)
		elif normal_ele == 48:
			current_deck_card_number = random.choice(darkness_rookies)
		elif normal_ele == 67:
			current_deck_card_number = random.choice(rare_ultimates)
		elif normal_ele == 66:
			current_deck_card_number = random.choice(rare_champions)
		elif normal_ele == 64:
			current_deck_card_number = random.choice(rare_rookies)

	# current_deck_card_number = [current_deck_card_number]
	return current_deck_card_number


def Generate_Deck(deck_list, new_deck_list):
	# gives unique cards
	for i in range(0, len(deck_list)):
		if deck_list[i] not in new_deck_list:
			new_deck_list.append(deck_list[i])

	# change card if card element has changed, but not to another card in deck
	# change option cards if rando on, and change if card element has changed or rando on, but pick_card makes sure not to another card in deck

	for i in range(0, len(new_deck_list)):
		l_card_number = new_deck_list[i]
		
# this fn doesnt work for strong option card numbers
		
		if l_card_number in normal_option_card_numbers and Randomise_Enemy_Decks:
			new_deck_list[i] = Pick_Card(l_card_number, new_deck_list)
		elif normal_card_dict_of_elements.get(l_card_number) != card_list_of_elements.get(
				l_card_number) or Randomise_Enemy_Decks:
			# need to do this so it can rando to itself
			new_deck_list[i] = None
			new_deck_list[i] = Pick_Card(l_card_number, new_deck_list)


# Level and element is intertwined, very annoying!
def Get_Element_Type(base_element, level_modifier, card_number):
	# 0 = fire_rookie
	# 1 = fire_armour
	# 2 = fire_champion
	# 3 = fire_ultimate
	# +16 = ice, +32 = nature, +48 = darkness, +64 = rare

	# 12 fire ults, 15 fire champs,7 fire rookies
	# 12 ice ults, 15 ice champs,8 ice rookies
	# 12 nature ults, 16 nature champs,6 nature rookies
	# 14 darkness ults, 15 darkness champs,7 darkness rookies
	# 12 rare ults, 14 rare champs,7 rare rookies
	# not changing partner cards

	# make sure the card is in the list, and that the element is different to the original
	# adds the element_level number to a list so 2nd time round it gets called retrives same number

	element_level_number = card_list_of_elements.get(card_number)

	return element_level_number


if Change_Plus_DP:
	Zero_DP_Change = [0, 0, 0, 0, 10]
	Ten_DP_Change = [0, 10, 10, 10, 10, 20]
	Twenty_DP_Change = [10, 20, 20, 20, 20, 30]
	Thirty_DP_Change = [20, 30, 30, 30, 30, 40]
else:
	Zero_DP_Change = [0]
	Ten_DP_Change = [10]
	Twenty_DP_Change = [20]
	Thirty_DP_Change = [30]


# this fn works with most cards given a HP memory address value, and most cards are 13C bytes away from eachother
def Get_Address(HP_Address, attribute):
    Card_HP_Address = int(HP_Address)

    if attribute == "DP":
        offset = -int(0x02)
    elif attribute == "HP":
        offset = int(0x00)
    elif attribute == "CIRCLE":
        offset = int(0x02)
    elif attribute == "TRIANGLE":
        offset = int(0x1e)
    elif attribute == "CROSS":
        offset = int(0x3a)
    elif attribute == "CROSSEFFECT":
        offset = int(0xc6)
    else:
        offset = 0

    SumInt = Card_HP_Address + offset
    SumHex = hex(SumInt)
    return SumHex

### Change_DP
def Change_Plus_DP_Values(base_plus_dp):

	if not Change_Plus_DP:
		return base_plus_dp

	if base_plus_dp ==0:
		return [0,0,0,0,10]
	elif base_plus_dp ==10:
		return [0,10,10,10,10,20]
	elif base_plus_dp ==20:
		return [10,20,20,20,20,30]
	elif base_plus_dp ==30:
		return [20,30,30,30,30,40]
	else:
		return [40]

#I think that having low hp threshold same as others would be bad as a lot of one shot potential so lowering variance
### Change_HP
def Min_HP_Multiplier(base_hp,card_element,card_level_modifier):

	if not Change_HP:
		return base_hp

	if (card_element == "rare") and (card_level_modifier != ultimate_modifier) and Buff_Rare:
		base_hp = base_hp * 1.1

	return round(base_hp * 0.90/10)*10

def Max_HP_Multiplier(base_hp,card_element,card_level_modifier):

	if not Change_HP:
		return base_hp

	if (card_element == "rare") and (card_level_modifier != ultimate_modifier) and Buff_Rare:
		base_hp = base_hp * 1.1

	return round(base_hp * 1.10 / 10) * 10
### Change_HP
### Change_Circle
def Min_Circle_Multiplier(base_circle,card_element,card_level_modifier):

	if not Change_Circle:
		return base_circle

	if (card_element == "rare") and (card_level_modifier != ultimate_modifier) and Buff_Rare:
		base_circle = base_circle * 1.1

	return round(base_circle * 0.80/ 10) * 10

def Max_Circle_Multiplier(base_circle,card_element,card_level_modifier):

	if not Change_Circle:
		return base_circle

	if (card_element == "rare") and (card_level_modifier != ultimate_modifier) and Buff_Rare:
		base_circle = base_circle * 1.1

	return round(base_circle * 1.20 / 10) * 10

### Change_Circle
### Change_Triangle
def Min_Triangle_Multiplier(base_triangle,card_element,card_level_modifier):

	if not Change_Triangle:
		return base_triangle

	if (card_element == "rare") and (card_level_modifier != ultimate_modifier) and Buff_Rare:
		base_triangle = base_triangle * 1.1

	return round(base_triangle * 0.80/10)*10

def Max_Triangle_Multiplier(base_triangle,card_element,card_level_modifier):

	if not Change_Triangle:
		return base_triangle

	if (card_element == "rare") and (card_level_modifier != ultimate_modifier) and Buff_Rare:
		base_triangle = base_triangle * 1.1

	return round(base_triangle * 1.20 / 10) * 10

def Min_Cross_Multiplier(base_cross,card_element,card_level_modifier,base_special_effect):

	global special_effect
	global cross_special_effect

	if not Change_Cross_Effect:
		special_effect = base_special_effect
	else:
		special_effect = random.randint(0, 15)

	cross_special_effect = [special_effect]

	if not Change_Cross:
		return base_cross

	if card_element == "rare":
		card_element_modifier = 30
	else:
		card_element_modifier = 20

# conditional buff to rares
	if (card_element == "rare") and (card_level_modifier != ultimate_modifier) and Buff_Rare:
		base_cross = base_cross * 1.1

# if counter or crash
	if 5 <= special_effect <=8:
		return 0
# if new effect is x3 or eat up hp, nerf slightly
	if (11 <= special_effect <= 15 or special_effect == 9) and (11 <= base_special_effect <= 15 or base_special_effect == 9):
		base_cross = base_cross * 0.90
# if it had none special effect before it would have a strong X
	if base_special_effect == 0:
		base_cross = base_cross * 0.8
# if it had a 0 cross before, use a formula to get a new cross power
	if base_cross == 0:
		base_cross = 70 + (card_element_modifier * card_level_modifier)
	return round(base_cross * 0.80/10)*10

def Max_Cross_Multiplier(base_cross,card_element,card_level_modifier,base_special_effect):

	global special_effect

	if not Change_Cross:
		return base_cross

	if card_element == "rare":
		card_element_modifier = 30
	else:
		card_element_modifier = 20

	if (card_element == "rare") and (card_level_modifier != ultimate_modifier) and Buff_Rare:
		base_cross = base_cross * 1.1

	# if counter or crash
	if 5 <= special_effect <= 8:
		return 0
	# if new effect is x3 or eat up hp, nerf slightlys
	if (11 <= special_effect <= 15 or special_effect == 9) and (11 <= base_special_effect <= 15 or base_special_effect == 9):
		base_cross = base_cross * 0.90
	# if it had none special effect before it would have a strong X
	if base_special_effect == 0:
		base_cross = base_cross * 0.8
	# if it had a 0 cross before, use a formula to get a new cross power
	if base_cross == 0:
		base_cross = 130 + (card_element_modifier * card_level_modifier)
	return round(base_cross * 1.20 / 10)*10

# Generate Decks
Generate_Deck(Red_Deck, New_Red_Deck)
Generate_Deck(Green_Deck, New_Green_Deck)
Generate_Deck(Yellow_Deck, New_Yellow_Deck)
Generate_Deck(Meramon_Deck, New_Meramon_Deck)
Generate_Deck(Phoenixmon_Deck, New_Phoenixmon_Deck)
Generate_Deck(Veemon_Deck, New_Veemon_Deck)
Generate_Deck(Vegiemon_Deck, New_Vegiemon_Deck)
Generate_Deck(Ninjamon_Deck, New_Ninjamon_Deck)
Generate_Deck(Veedramon_Deck, New_Veedramon_Deck)
Generate_Deck(Wormmon_Deck, New_Wormmon_Deck)
Generate_Deck(Frigimon_Deck, New_Frigimon_Deck)
Generate_Deck(Whamon_Deck, New_Whamon_Deck)
Generate_Deck(Garurumon_Deck, New_Garurumon_Deck)
Generate_Deck(Stingmon_Deck, New_Stingmon_Deck)
Generate_Deck(Hagurumon_Deck, New_Hagurumon_Deck)
Generate_Deck(Garurumon2_Deck, New_Garurumon2_Deck)
Generate_Deck(ShellNumemon_Deck, New_ShellNumemon_Deck)
Generate_Deck(KingSukamon_Deck, New_KingSukamon_Deck)
Generate_Deck(Shadramon_Deck, New_Shadramon_Deck)
Generate_Deck(Wormmon2_Deck, New_Wormmon2_Deck)
Generate_Deck(Stingmon2_Deck, New_Stingmon2_Deck)
Generate_Deck(Shadramon2_Deck, New_Shadramon2_Deck)
Generate_Deck(Quetzalmon_Deck, New_Quetzalmon_Deck)
Generate_Deck(Digimon_Emperor_Deck, New_Digimon_Emperor_Deck)
Generate_Deck(Centarumon_Deck, New_Centarumon_Deck)
Generate_Deck(Tyrannomon_Deck, New_Tyrannomon_Deck)
Generate_Deck(Angemon_Deck, New_Angemon_Deck)
Generate_Deck(Davis_Deck, New_Davis_Deck)
Generate_Deck(Keeley_Deck, New_Keeley_Deck)
Generate_Deck(Cody_Deck, New_Cody_Deck)
Generate_Deck(TK_Deck, New_TK_Deck)
Generate_Deck(Wizardmon_Deck, New_Wizardmon_Deck)
Generate_Deck(AeroVeedramon_Deck, New_AeroVeedramon_Deck)
Generate_Deck(Gatomon_Deck, New_Gatomon_Deck)
Generate_Deck(Kari_Deck, New_Kari_Deck)
Generate_Deck(Goburimon_Deck, New_Goburimon_Deck)
Generate_Deck(DemiDevimon_Deck, New_DemiDevimon_Deck)
Generate_Deck(Megadramon_Deck, New_Megadramon_Deck)
Generate_Deck(Gigadramon_Deck, New_Gigadramon_Deck)
Generate_Deck(Togemon_Deck, New_Togemon_Deck)
Generate_Deck(Kabuterimon_Deck, New_Kabuterimon_Deck)
Generate_Deck(Ikkakumon_Deck, New_Ikkakumon_Deck)
Generate_Deck(Birdramon_Deck, New_Birdramon_Deck)
Generate_Deck(WereGarurumon_Deck, New_WereGarurumon_Deck)
Generate_Deck(MetalGreymon_Deck, New_MetalGreymon_Deck)
Generate_Deck(Tuskmon_Deck, New_Tuskmon_Deck)
Generate_Deck(Phantomon_Deck, New_Phantomon_Deck)
Generate_Deck(MegaSeadramon_Deck, New_MegaSeadramon_Deck)
Generate_Deck(VenomMyotismon_Deck, New_VenomMyotismon_Deck)
Generate_Deck(Leomon_Deck, New_Leomon_Deck)
Generate_Deck(Devimon_Deck, New_Devimon_Deck)
Generate_Deck(MetalEtemon_Deck, New_MetalEtemon_Deck)
Generate_Deck(Myotismon_Deck, New_Myotismon_Deck)
Generate_Deck(Greymon_Deck, New_Greymon_Deck)
Generate_Deck(ExVeemon_Deck, New_ExVeemon_Deck)
Generate_Deck(Flamedramon_Deck, New_Flamedramon_Deck)
Generate_Deck(Raidramon_Deck, New_Raidramon_Deck)
Generate_Deck(Hawkmon_Deck, New_Hawkmon_Deck)
Generate_Deck(Aquilamon_Deck, New_Aquilamon_Deck)
Generate_Deck(Halsemon_Deck, New_Halsemon_Deck)
Generate_Deck(Penguinmon_Deck, New_Penguinmon_Deck)
Generate_Deck(Rosemon_Deck, New_Rosemon_Deck)
Generate_Deck(Armadillomon_Deck, New_Armadillomon_Deck)
Generate_Deck(Ankylomon_Deck, New_Ankylomon_Deck)
Generate_Deck(Digmon_Deck, New_Digmon_Deck)
Generate_Deck(Thundermon_Deck, New_Thundermon_Deck)
Generate_Deck(MetalMamemon_Deck, New_MetalMamemon_Deck)
Generate_Deck(SuperStarmon_Deck, New_SuperStarmon_Deck)
Generate_Deck(Bakemon_Deck, New_Bakemon_Deck)
Generate_Deck(Devimon2_Deck, New_Devimon2_Deck)
Generate_Deck(SkullGreymon_Deck, New_SkullGreymon_Deck)
Generate_Deck(Myotismon2_Deck, New_Myotismon2_Deck)
Generate_Deck(Patamon_Deck, New_Patamon_Deck)
Generate_Deck(Baronmon_Deck, New_Baronmon_Deck)
Generate_Deck(Pegasusmon_Deck, New_Pegasusmon_Deck)
Generate_Deck(Gatomon2_Deck, New_Gatomon2_Deck)
Generate_Deck(Nefertimon_Deck, New_Nefertimon_Deck)
Generate_Deck(Tylomon_Deck, New_Tylomon_Deck)
Generate_Deck(Tentomon_Deck, New_Tentomon_Deck)
Generate_Deck(Kuwagamon_Deck, New_Kuwagamon_Deck)
Generate_Deck(HerculesKabuterimon_Deck, New_HerculesKabuterimon_Deck)
Generate_Deck(Wargreymon_Deck, New_Wargreymon_Deck)
Generate_Deck(Rosemon2_Deck, New_Rosemon2_Deck)
Generate_Deck(Tai_Deck, New_Tai_Deck)
Generate_Deck(Paildramon_Deck, New_Paildramon_Deck)
Generate_Deck(Garudamon_Deck, New_Garudamon_Deck)
Generate_Deck(Sora_Deck, New_Sora_Deck)
Generate_Deck(Shurimon_Deck, New_Shurimon_Deck)
Generate_Deck(Lillymon_Deck, New_Lillymon_Deck)
Generate_Deck(Mimi_Deck, New_Mimi_Deck)
Generate_Deck(Submarimon_Deck, New_Submarimon_Deck)
Generate_Deck(Metalgarurumon_Deck, New_Metalgarurumon_Deck)
Generate_Deck(Matt_Deck, New_Matt_Deck)
Generate_Deck(Zudomon_Deck, New_Zudomon_Deck)
Generate_Deck(Joe_Deck, New_Joe_Deck)
Generate_Deck(MegaKabuterimon_Deck, New_MegaKabuterimon_Deck)
Generate_Deck(Izzy_Deck, New_Izzy_Deck)
Generate_Deck(MagnaAngemon_Deck, New_MagnaAngemon_Deck)
Generate_Deck(Angewomon_Deck, New_Angewomon_Deck)
Generate_Deck(GranKuwagamon_Deck, New_GranKuwagamon_Deck)
Generate_Deck(Ken_Deck, New_Ken_Deck)
Generate_Deck(MetalSeadramon_Deck, New_MetalSeadramon_Deck)
Generate_Deck(Puppetmon_Deck, New_Puppetmon_Deck)
Generate_Deck(Machinedramon_Deck, New_Machinedramon_Deck)
Generate_Deck(LadyDevimon_Deck, New_LadyDevimon_Deck)
Generate_Deck(Piedmon_Deck, New_Piedmon_Deck)
Generate_Deck(Magnamon_Deck, New_Magnamon_Deck)
Generate_Deck(Sylphymon_Deck, New_Sylphymon_Deck)
Generate_Deck(Shakkoumon_Deck, New_Shakkoumon_Deck)
Generate_Deck(Seraphimon_Deck, New_Seraphimon_Deck)
Generate_Deck(Magnadramon_Deck, New_Magnadramon_Deck)
Generate_Deck(Infermon_Deck, New_Infermon_Deck)
Generate_Deck(Diaboromon_Deck, New_Diaboromon_Deck)


Attributes = [
#Imperialdramon 000
	Attribute(
		name="Imperialdramon Element",
		addresses=[0x0266331a],
		number_of_bytes=1,
		min_value=Get_Element_Type(0,3,0),
		max_value=Get_Element_Type(0,3,0),
		is_little_endian=True,),
	Attribute(
		name="Imperialdramon +DP",
		addresses=[0x0266331c],
		number_of_bytes=2,
		possible_values= Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Imperialdramon HP",
		addresses=[0x0266331E],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1900,fire_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1900,fire_special_modifier,ultimate_modifier),
		min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Imperialdramon Circle",
		addresses=[0x02663320],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(980,fire_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(980,fire_special_modifier,ultimate_modifier),
		min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Imperialdramon Triangle",
		addresses=[0x0266333c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(670,fire_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(670,fire_special_modifier,ultimate_modifier),
		min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Imperialdramon Cross",
		addresses=[0x02663358],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,fire_special_modifier,ultimate_modifier,5),
		max_value=Max_Cross_Multiplier(0,fire_special_modifier,ultimate_modifier,5),
		min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Imperialdramon Cross Effect",
		addresses=[0x026633e4],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Omnimon I 001
	Attribute(
		name="Omnimon I Element",
		addresses=[0x02663456],
		number_of_bytes=1,
		min_value=Get_Element_Type(0,3,1),
		max_value=Get_Element_Type(0,3,1),
		is_little_endian=True,),
	Attribute(
		name="Omnimon I +DP",
		addresses=[0x02663458],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Omnimon I HP",
		addresses=[0x0266345A],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1800,fire_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1800,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
        is_little_endian=True,),
	Attribute(
		name="Omnimon I Circle",
		addresses=[0x0266345C],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(960,fire_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(960,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
        is_little_endian=True,),
	Attribute(
		name="Omnimon I Triangle",
		addresses=[0x02663478],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(560,fire_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(560,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
        is_little_endian=True,),
	Attribute(
		name="Omnimon I Cross",
		addresses=[0x02663494],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,fire_special_modifier,ultimate_modifier,7),
		max_value=Max_Cross_Multiplier(0,fire_special_modifier,ultimate_modifier,7),
        min_max_interval=10,
        is_little_endian=True,),
	Attribute(
		name="Omnimon I Cross Effect",
		addresses=[0x02663520],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Wargreymon 002
	Attribute(
		name="Wargreymon Element",
		addresses=[0x02663592],
		number_of_bytes=1,
		min_value=Get_Element_Type(0,3,2),
		max_value=Get_Element_Type(0,3,2),
		is_little_endian=True,),
	Attribute(
		name="Wargreymon +DP",
		addresses=[0x02663594],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Wargreymon HP",
		addresses=[0x02663596],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1650,fire_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1650,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Wargreymon Circle",
		addresses=[0x02663598],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(900,fire_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(900,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Wargreymon Triangle",
		addresses=[0x026635b4],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(670,fire_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(670,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Wargreymon Cross",
		addresses=[0x026635d0],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(380,fire_special_modifier,ultimate_modifier,12),
		max_value=Max_Cross_Multiplier(380,fire_special_modifier,ultimate_modifier,12),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Wargreymon Cross Effect",
		addresses=[0x0266365c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Phoenixmon 003
	Attribute(
		name="Phoenixmon Element",
		addresses=[0x026636ce],
		number_of_bytes=1,
		min_value=Get_Element_Type(0,3,3),
		max_value=Get_Element_Type(0,3,3),
		is_little_endian=True,),
	Attribute(
		name="Phoenixmon +DP",
		addresses=[0x026636d0],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Phoenixmon HP",
		addresses=[0x026636D2],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1320,fire_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1320,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Phoenixmon Circle",
		addresses=[0x026636D4],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(750,fire_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(750,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Phoenixmon Triangle",
		addresses=[0x026636f0],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(560,fire_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(560,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Phoenixmon Cross",
		addresses=[0x0266370c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(200,fire_special_modifier,ultimate_modifier,9),
		max_value=Max_Cross_Multiplier(200,fire_special_modifier,ultimate_modifier,9),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Phoenixmon Cross Effect",
		addresses=[0x02663798],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Paildramon 004
	Attribute(
		name="Paildramon Element",
		addresses=[0x0266380a],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 3, 4),
		max_value=Get_Element_Type(0, 3, 4),
		is_little_endian=True, ),
	Attribute(
		name="Paildramon +DP",
		addresses=[0x0266380c],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Paildramon HP",
		addresses=[0x0266380E],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1230,fire_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1230,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Paildramon Circle",
		addresses=[0x02663810],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(800,fire_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(800,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Paildramon Triangle",
		addresses=[0x0266382c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(620,fire_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(620,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Paildramon Cross",
		addresses=[0x02663848],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,fire_special_modifier,ultimate_modifier,4),
		max_value=Max_Cross_Multiplier(0,fire_special_modifier,ultimate_modifier,4),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Paildramon Cross Effect",
		addresses=[0x026638d4],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Gigadramon 005
	Attribute(
		name="Gigadramon Element",
		addresses=[0x02663946],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 3, 5),
		max_value=Get_Element_Type(0, 3, 5),
		is_little_endian=True, ),
	Attribute(
		name="Gigadramon +DP",
		addresses=[0x02663948],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Gigadramon HP",
		addresses=[0x0266394A],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1480,fire_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1480,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gigadramon Circle",
		addresses=[0x0266394C],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(900,fire_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(900,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gigadramon Triangle",
		addresses=[0x02663968],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(710,fire_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(710,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gigadramon Cross",
		addresses=[0x02663984],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(550,fire_special_modifier,ultimate_modifier,0),
		max_value=Max_Cross_Multiplier(550,fire_special_modifier,ultimate_modifier,0),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gigadramon Cross Effect",
		addresses=[0x02663a10],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#RealMetalGreymon 006
	Attribute(
		name="Phoenixmon Element",
		addresses=[0x02663a82],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 3, 6),
		max_value=Get_Element_Type(0, 3, 6),
		is_little_endian=True, ),
	Attribute(
		name="RealMetalGreymon +DP",
		addresses=[0x02663a84],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="RealMetalGreymon HP",
		addresses=[0x02663A86],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1540,fire_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1540,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="RealMetalGreymon Circle",
		addresses=[0x02663A88],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(850,fire_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(850,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="RealMetalGreymon Triangle",
		addresses=[0x02663aa4],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(600,fire_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(600,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="RealMetalGreymon Cross",
		addresses=[0x02663ac0],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,fire_special_modifier,ultimate_modifier,5),
		max_value=Max_Cross_Multiplier(0,fire_special_modifier,ultimate_modifier,5),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="RealMetalGreymon Cross Effect",
		addresses=[0x2663C7C],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Garudamon 007
	Attribute(
		name="Phoenixmon Element",
		addresses=[0x02663cee],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 3, 7),
		max_value=Get_Element_Type(0, 3, 7),
		is_little_endian=True, ),
	Attribute(
		name="Garudamon +DP",
		addresses=[0x02663cf0],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Garudamon HP",
		addresses=[0x02663CF2],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1320,fire_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1320,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Garudamon Circle",
		addresses=[0x02663CF4],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(730,fire_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(730,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Garudamon Triangle",
		addresses=[0x02663d10],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(550,fire_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(550,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Garudamon Cross",
		addresses=[0x02663d2c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(320,fire_special_modifier,ultimate_modifier,1),
		max_value=Max_Cross_Multiplier(320,fire_special_modifier,ultimate_modifier,1),
        min_max_interval=10,
		is_little_endian=True,),
#MasterTyrannomon 008
	Attribute(
		name="MasterTyrannomon Element",
		addresses=[0x2663e2a],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 3, 8),
		max_value=Get_Element_Type(0, 3, 8),
		is_little_endian=True, ),
	Attribute(
		name="MasterTyrannomon +DP",
		addresses=[0x2663e2c],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="MasterTyrannomon HP",
		addresses=[0x2663e2e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1280,fire_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1280,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MasterTyrannomon Circle",
		addresses=[0x2663e30],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(850,fire_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(850,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MasterTyrannomon Triangle",
		addresses=[0x2663e4c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(520,fire_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(520,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MasterTyrannomon Cross",
		addresses=[0x2663e68],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(370,fire_special_modifier,ultimate_modifier,1),
		max_value=Max_Cross_Multiplier(370,fire_special_modifier,ultimate_modifier,1),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MasterTyrannomon Cross Effect",
		addresses=[0x2663ef4],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
	Attribute(
		name="Garudamon Cross Effect",
		addresses=[0x02663db8],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#MetalGreymon 009
	Attribute(
		name="MetalGreymon Element",
		addresses=[0x02663f66],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 3, 9),
		max_value=Get_Element_Type(0, 3, 9),
		is_little_endian=True, ),
	Attribute(
		name="MetalGreymon +DP",
		addresses=[0x02663f68],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="MetalGreymon HP",
		addresses=[0x02663F6A],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1540,fire_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1540,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MetalGreymon Circle",
		addresses=[0x02663F6C],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(720,fire_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(720,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MetalGreymon Triangle",
		addresses=[0x02663f88],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(540,fire_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(540,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MetalGreymon Cross",
		addresses=[0x02663fa4],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,fire_special_modifier,ultimate_modifier,12),
		max_value=Max_Cross_Multiplier(0,fire_special_modifier,ultimate_modifier,12),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MetalGreymon Cross Effect",
		addresses=[0x02664030],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Vermilimon 010
	Attribute(
		name="Vermilimon Element",
		addresses=[0x026640a2],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 3, 10),
		max_value=Get_Element_Type(0, 3, 10),
		is_little_endian=True, ),
	Attribute(
		name="Vermilimon +DP",
		addresses=[0x026640a4],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Vermilimon HP",
		addresses=[0x026640A6],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1430,fire_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1430,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Vermilimon Circle",
		addresses=[0x026640A8],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(700,fire_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(700,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Vermilimon Triangle",
		addresses=[0x026640c4],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(510,fire_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(510,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Vermilimon Cross",
		addresses=[0x026640e0],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,fire_special_modifier,ultimate_modifier,6),
		max_value=Max_Cross_Multiplier(0,fire_special_modifier,ultimate_modifier,6),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Vermilimon Cross Effect",
		addresses=[0x0266416c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Meteormon 011
	Attribute(
		name="Meteormon Element",
		addresses=[0x026641de],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 3, 11),
		max_value=Get_Element_Type(0, 3, 11),
		is_little_endian=True, ),
	Attribute(
		name="Meteormon +DP",
		addresses=[0x026641e0],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Meteormon HP",
		addresses=[0x026641E2],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1150,fire_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1150,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Meteormon Circle",
		addresses=[0x026641E4],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(750,fire_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(750,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Meteormon Triangle",
		addresses=[0x02664200],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(400,fire_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(400,fire_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Meteormon Cross",
		addresses=[0x0266421c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(200,fire_special_modifier,ultimate_modifier,2),
		max_value=Max_Cross_Multiplier(200,fire_special_modifier,ultimate_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Meteormon Cross Effect",
		addresses=[0x026642a8],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#ExVeemon 012
	Attribute(
		name="ExVeemon Element",
		addresses=[0x0266431a],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 2, 12),
		max_value=Get_Element_Type(0, 2, 12),
		is_little_endian=True, ),
	Attribute(
		name="ExVeemon +DP",
		addresses=[0x0266431c],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="ExVeemon HP",
		addresses=[0x0266431E],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(810,fire_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(810,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ExVeemon Circle",
		addresses=[0x02664320],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(580,fire_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(580,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ExVeemon Triangle",
		addresses=[0x0266433c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(480,fire_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(480,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ExVeemon Cross",
		addresses=[0x02664358],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,fire_special_modifier,champion_modifier,5),
		max_value=Max_Cross_Multiplier(0,fire_special_modifier,champion_modifier,5),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ExVeemon Cross Effect",
		addresses=[0x026643e4],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Aquilamon 013
	Attribute(
		name="Aquilamon Element",
		addresses=[0x02664586],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 2, 13),
		max_value=Get_Element_Type(0, 2, 13),
		is_little_endian=True, ),
	Attribute(
		name="Aquilamon +DP",
		addresses=[0x02664588],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Aquilamon HP",
		addresses=[0x266458A],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(670,fire_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(670,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Aquilamon Circle",
		addresses=[0x266458C],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(570,fire_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(570,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Aquilamon Triangle",
		addresses=[0x026645a8],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(450,fire_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(450,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Aquilamon Cross",
		addresses=[0x026645c4],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(200,fire_special_modifier,champion_modifier,1),
		max_value=Max_Cross_Multiplier(200,fire_special_modifier,champion_modifier,1),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Aquilamon Cross Effect",
		addresses=[0x02664650],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Greymon 014
	Attribute(
		name="Greymon Element",
		addresses=[0x026646c2],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 2, 14),
		max_value=Get_Element_Type(0, 2, 14),
		is_little_endian=True, ),
	Attribute(
		name="Greymon +DP",
		addresses=[0x026646c4],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Greymon HP",
		addresses=[0x026646C6],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(850,fire_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(850,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Greymon Circle",
		addresses=[0x026646C8],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(600,fire_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(600,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Greymon Triangle",
		addresses=[0x026646e4],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(420,fire_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(420,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Greymon Cross",
		addresses=[0x02664700],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,fire_special_modifier,champion_modifier,5),
		max_value=Max_Cross_Multiplier(0,fire_special_modifier,champion_modifier,5),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Greymon Cross Effect",
		addresses=[0x0266478c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Apemon 015
	Attribute(
		name="Apemon Element",
		addresses=[0x26647FE],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 2, 15),
		max_value=Get_Element_Type(0, 2, 15),
		is_little_endian=True, ),
	Attribute(
		name="Apemon +DP",
		addresses=[0x02664800],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Apemon HP",
		addresses=[0x02664802],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(830,fire_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(830,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Apemon Circle",
		addresses=[0x02664804],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(550,fire_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(550,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Apemon Triangle",
		addresses=[0x02664820],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(420,fire_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(420,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Apemon Cross",
		addresses=[0x0266483c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,fire_special_modifier,champion_modifier,5),
		max_value=Max_Cross_Multiplier(0,fire_special_modifier,champion_modifier,5),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Apemon Cross Effect",
		addresses=[0x026648c8],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Tyrannomon 016
	Attribute(
		name="Tyrannomon Element",
		addresses=[0x0266493a],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 2, 16),
		max_value=Get_Element_Type(0, 2, 16),
		is_little_endian=True, ),
	Attribute(
		name="Tyrannomon +DP",
		addresses=[0x0266493c],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Tyrannomon HP",
		addresses=[0x0266493E],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(810,fire_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(810,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tyrannomon Circle",
		addresses=[0x02664940],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(520,fire_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(520,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tyrannomon Triangle",
		addresses=[0x0266495c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(380,fire_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(380,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tyrannomon Cross",
		addresses=[0x02664978],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(150,fire_special_modifier,champion_modifier,13),
		max_value=Max_Cross_Multiplier(150,fire_special_modifier,champion_modifier,13),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tyrannomon Cross Effect",
		addresses=[0x02664a04],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Monochromon 017
	Attribute(
		name="Monochromon Element",
		addresses=[0x02664a76],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 2, 17),
		max_value=Get_Element_Type(0, 2, 17),
		is_little_endian=True, ),
	Attribute(
		name="Monochromon +DP",
		addresses=[0x02664a78],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Monochromon HP",
		addresses=[0x02664A7A],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(950,fire_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(950,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Monochromon Circle",
		addresses=[0x02664A7C],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(540,fire_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(540,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Monochromon Triangle",
		addresses=[0x02664a98],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(260,fire_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(260,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Monochromon Cross",
		addresses=[0x02664ab4],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(200,fire_special_modifier,champion_modifier,2),
		max_value=Max_Cross_Multiplier(200,fire_special_modifier,champion_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Monochromon Cross Effect",
		addresses=[0x02664b40],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Meramon 018
	Attribute(
		name="Meramon Element",
		addresses=[0x02664bb2],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 2, 18),
		max_value=Get_Element_Type(0, 2, 18),
		is_little_endian=True, ),
	Attribute(
		name="Meramon +DP",
		addresses=[0x02664bb4],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Meramon HP",
		addresses=[0x02664BB6],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(740,fire_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(740,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Meramon Circle",
		addresses=[0x02664BB8],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(550,fire_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(550,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Meramon Triangle",
		addresses=[0x02664bd4],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(300,fire_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(300,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Meramon Cross",
		addresses=[0x02664bf0],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(220,fire_special_modifier,champion_modifier,12),
		max_value=Max_Cross_Multiplier(220,fire_special_modifier,champion_modifier,12),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Meramon Cross Effect",
		addresses=[0x02664c7c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Centarumon 019
	Attribute(
		name="Centarumon Element",
		addresses=[0x02664cee],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 2, 19),
		max_value=Get_Element_Type(0, 2, 19),
		is_little_endian=True, ),
	Attribute(
		name="Centarumon +DP",
		addresses=[0x02664cf0],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Centarumon HP",
		addresses=[0x02664CF2],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(800,fire_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(800,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Centarumon Circle",
		addresses=[0x02664CF4],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(450,fire_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(450,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Centarumon Triangle",
		addresses=[0x02664d10],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(360,fire_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(360,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Centarumon Cross",
		addresses=[0x02664d2c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(220,fire_special_modifier,champion_modifier,12),
		max_value=Max_Cross_Multiplier(220,fire_special_modifier,champion_modifier,12),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Centarumon Cross Effect",
		addresses=[0x2664EE8],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Birdramon 020
	Attribute(
		name="ExVeemon Element",
		addresses=[0x02664f5a],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 2, 20),
		max_value=Get_Element_Type(0, 2, 20),
		is_little_endian=True, ),
	Attribute(
		name="Birdramon +DP",
		addresses=[0x02664f5c],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Birdramon HP",
		addresses=[0x02664F5E],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(710,fire_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(710,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Birdramon Circle",
		addresses=[0x02664f60],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(500,fire_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(500,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Birdramon Triangle",
		addresses=[0x02664f7c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(310,fire_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(310,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Birdramon Cross",
		addresses=[0x02664f98],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(130,fire_special_modifier,champion_modifier,1),
		max_value=Max_Cross_Multiplier(130,fire_special_modifier,champion_modifier,1),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Birdramon Cross Effect",
		addresses=[0x02665024],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Tankmon 021
	Attribute(
		name="ExVeemon Element",
		addresses=[0x02665096],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 2, 21),
		max_value=Get_Element_Type(0, 2, 21),
		is_little_endian=True, ),
	Attribute(
		name="Tankmon +DP",
		addresses=[0x02665098],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Tankmon HP",
		addresses=[0x0266509A],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1000,fire_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(1000,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tankmon Circle",
		addresses=[0x0266509C],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(400,fire_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(400,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tankmon Triangle",
		addresses=[0x026650b8],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(290,fire_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(290,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tankmon Cross",
		addresses=[0x026650d4],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(120,fire_special_modifier,champion_modifier,1),
		max_value=Max_Cross_Multiplier(120,fire_special_modifier,champion_modifier,1),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tankmon Cross Effect",
		addresses=[0x02665160],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#RedVegiemon 022
	Attribute(
		name="RedVegiemon Element",
		addresses=[0x026651d2],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 2, 22),
		max_value=Get_Element_Type(0, 2, 22),
		is_little_endian=True, ),
	Attribute(
		name="RedVegiemon +DP",
		addresses=[0x026651d4],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="RedVegiemon HP",
		addresses=[0x026651D6],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(850,fire_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(850,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="RedVegiemon Circle",
		addresses=[0x026651D8],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(400,fire_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(400,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="RedVegiemon Triangle",
		addresses=[0x026651f4],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(310,fire_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(310,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="RedVegiemon Cross",
		addresses=[0x02665210],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,fire_special_modifier,champion_modifier,0),
		max_value=Max_Cross_Multiplier(0,fire_special_modifier,champion_modifier,0),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="RedVegiemon Cross Effect",
		addresses=[0x0266529c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Piddomon 023
	Attribute(
		name="Piddomon Element",
		addresses=[0x266530E],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 2, 23),
		max_value=Get_Element_Type(0, 2, 23),
		is_little_endian=True, ),
	Attribute(
		name="Piddomon +DP",
		addresses=[0x02665310],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Piddomon HP",
		addresses=[0x02665312],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(750,fire_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(750,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Piddomon Circle",
		addresses=[0x02665314],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(450,fire_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(450,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Piddomon Triangle",
		addresses=[0x02665330],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(360,fire_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(360,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Piddomon Cross",
		addresses=[0x0266534c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(220,fire_special_modifier,champion_modifier,2),
		max_value=Max_Cross_Multiplier(220,fire_special_modifier,champion_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Piddomon Cross Effect",
		addresses=[0x026653d8],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Akatorimon 024
	Attribute(
		name="Akatorimon Element",
		addresses=[0x0266544a],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 2, 24),
		max_value=Get_Element_Type(0, 2, 24),
		is_little_endian=True, ),
	Attribute(
		name="Akatorimon +DP",
		addresses=[0x0266544c],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Akatorimon HP",
		addresses=[0x0266544E],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(600,fire_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(600,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Akatorimon Circle",
		addresses=[0x02665450],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(400,fire_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(400,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Akatorimon Triangle",
		addresses=[0x0266546c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(460,fire_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(460,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Akatorimon Cross",
		addresses=[0x02665488],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(100,fire_special_modifier,champion_modifier,2),
		max_value=Max_Cross_Multiplier(100,fire_special_modifier,champion_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Akatorimon Cross Effect",
		addresses=[0x02665514],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#BomberNanimon 025
	Attribute(
		name="BomberNanimon Element",
		addresses=[0x02665586],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 2, 25),
		max_value=Get_Element_Type(0, 2, 25),
		is_little_endian=True, ),
	Attribute(
		name="BomberNanimon +DP",
		addresses=[0x02665588],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="BomberNanimon HP",
		addresses=[0x0266558A],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(650,fire_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(650,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="BomberNanimon Circle",
		addresses=[0x0266558C],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(520,fire_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(520,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="BomberNanimon Triangle",
		addresses=[0x026655a8],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(390,fire_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(390,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="BomberNanimon Cross",
		addresses=[0x026655c4],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,fire_special_modifier,champion_modifier,8),
		max_value=Max_Cross_Multiplier(0,fire_special_modifier,champion_modifier,8),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="BomberNanimon Cross Effect",
		addresses=[0x02665650],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Flarerizamon 026
	Attribute(
		name="Flarerizamon Element",
		addresses=[0x026657f2],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 2, 26),
		max_value=Get_Element_Type(0, 2, 26),
		is_little_endian=True, ),
	Attribute(
		name="Flarerizamon +DP",
		addresses=[0x026657f4],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Flarerizamon HP",
		addresses=[0x026657F6],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(730,fire_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(730,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Flarerizamon Circle",
		addresses=[0x026657F8],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(550,fire_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(550,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Flarerizamon Triangle",
		addresses=[0x02665814],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(320,fire_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(320,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Flarerizamon Cross",
		addresses=[0x02665830],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(240,fire_special_modifier,champion_modifier,0),
		max_value=Max_Cross_Multiplier(240,fire_special_modifier,champion_modifier,0),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Flarerizamon Cross Effect",
		addresses=[0x26658BC],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Agumon 027
	Attribute(
		name="Agumon Element",
		addresses=[0x0266592e],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 0, 27),
		max_value=Get_Element_Type(0, 0, 27),
		is_little_endian=True, ),
	Attribute(
		name="Agumon +DP",
		addresses=[0x02665930],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Agumon HP",
		addresses=[0x02665932],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(570,fire_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(570,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Agumon Circle",
		addresses=[0x02665934],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(380,fire_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(380,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Agumon Triangle",
		addresses=[0x02665950],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(200,fire_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(200,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Agumon Cross",
		addresses=[0x0266596c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(120,fire_special_modifier,rookie_modifier,2),
		max_value=Max_Cross_Multiplier(120,fire_special_modifier,rookie_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Agumon Cross Effect",
		addresses=[0x026659f8],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Solarmon 028
	Attribute(
		name="Solarmon Element",
		addresses=[0x02665A6a],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 0, 28),
		max_value=Get_Element_Type(0, 0, 28),
		is_little_endian=True, ),
	Attribute(
		name="Solarmon +DP",
		addresses=[0x02665A6C],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Solarmon HP",
		addresses=[0x02665A6E],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(500,fire_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(500,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Solarmon Circle",
		addresses=[0x02665a70],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(350,fire_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(350,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Solarmon Triangle",
		addresses=[0x02665a8c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(210,fire_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(210,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Solarmon Cross",
		addresses=[0x02665aa8],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,fire_special_modifier,rookie_modifier,8),
		max_value=Max_Cross_Multiplier(0,fire_special_modifier,rookie_modifier,8),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Solarmon Cross Effect",
		addresses=[0x02665b34],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Biyomon 029
	Attribute(
		name="Biyomon Element",
		addresses=[0x02665ba6],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 0, 29),
		max_value=Get_Element_Type(0, 0, 29),
		is_little_endian=True, ),
	Attribute(
		name="Biyomon +DP",
		addresses=[0x02665ba8],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Biyomon HP",
		addresses=[0x02665BAA],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(510,fire_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(510,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Biyomon Circle",
		addresses=[0x02665BAC],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(350,fire_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(350,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Biyomon Triangle",
		addresses=[0x02665bc8],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(170,fire_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(170,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Biyomon Cross",
		addresses=[0x02665be4],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(130,fire_special_modifier,rookie_modifier,1),
		max_value=Max_Cross_Multiplier(130,fire_special_modifier,rookie_modifier,1),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Biyomon Cross Effect",
		addresses=[0x02665c70],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Muchomon 030
	Attribute(
		name="Muchomon Element",
		addresses=[0x02665CE2],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 0, 30),
		max_value=Get_Element_Type(0, 0, 30),
		is_little_endian=True, ),
	Attribute(
		name="Muchomon +DP",
		addresses=[0x02665CE4],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Muchomon HP",
		addresses=[0x02665CE6],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(600,fire_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(600,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Muchomon Circle",
		addresses=[0x02665CE8],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(320,fire_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(320,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Muchomon Triangle",
		addresses=[0x02665d04],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(220,fire_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(220,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Muchomon Cross",
		addresses=[0x02665d20],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,fire_special_modifier,rookie_modifier,7),
		max_value=Max_Cross_Multiplier(0,fire_special_modifier,rookie_modifier,7),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Muchomon Cross Effect",
		addresses=[0x02665dac],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Candlemon 031
	Attribute(
		name="Candlemon Element",
		addresses=[0x02665E1e],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 0, 31),
		max_value=Get_Element_Type(0, 0, 31),
		is_little_endian=True, ),
	Attribute(
		name="Candlemon +DP",
		addresses=[0x02665E20],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Candlemon HP",
		addresses=[0x02665E22],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(480,fire_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(480,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Candlemon Circle",
		addresses=[0x02665E24],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(380,fire_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(380,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Candlemon Triangle",
		addresses=[0x02665e40],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(270,fire_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(270,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Candlemon Cross",
		addresses=[0x02665e5c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,fire_special_modifier,rookie_modifier,5),
		max_value=Max_Cross_Multiplier(0,fire_special_modifier,rookie_modifier,5),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Candlemon Cross Effect",
		addresses=[0x02665ee8],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#D-Otamamon 032
	Attribute(
		name="D-Otamamon Element",
		addresses=[0x02665F5A],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 0, 32),
		max_value=Get_Element_Type(0, 0, 32),
		is_little_endian=True, ),
	Attribute(
		name="D-Otamamon +DP",
		addresses=[0x02665F5C],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="D-Otamamon HP",
		addresses=[0x02665F5E],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(550,fire_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(550,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="D-Otamamon Circle",
		addresses=[0x02665f60],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(300,fire_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(300,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="D-Otamamon Triangle",
		addresses=[0x02665f7c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(200,fire_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(200,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="D-Otamamon Cross",
		addresses=[0x02665f98],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(150,fire_special_modifier,rookie_modifier,12),
		max_value=Max_Cross_Multiplier(150,fire_special_modifier,rookie_modifier,12),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="D-Otamamon Cross Effect",
		addresses=[0x2666154],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Goburimon 033
	Attribute(
		name="Goburimon Element",
		addresses=[0x026661c6],
		number_of_bytes=1,
		min_value=Get_Element_Type(0, 0, 33),
		max_value=Get_Element_Type(0, 0, 33),
		is_little_endian=True, ),
	Attribute(
		name="Goburimon +DP",
		addresses=[0x026661c8],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Goburimon HP",
		addresses=[0x026661CA],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(500,fire_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(500,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Goburimon Circle",
		addresses=[0x026661CC],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(300,fire_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(300,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Goburimon Triangle",
		addresses=[0x026661e8],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(300,fire_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(300,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Goburimon Cross",
		addresses=[0x02666204],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(300,fire_special_modifier,rookie_modifier,0),
		max_value=Max_Cross_Multiplier(300,fire_special_modifier,rookie_modifier,0),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Goburimon Cross Effect",
		addresses=[0x02666290],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Vikemon 034
	Attribute(
		name="Vikemon Element",
		addresses=[0x2666302],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 3, 34),
		max_value=Get_Element_Type(16, 3, 34),
		is_little_endian=True, ),
	Attribute(
		name="Vikemon +DP",
		addresses=[0x2666304],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Vikemon HP",
		addresses=[0x2666306],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2420,ice_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(2420,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Vikemon Circle",
		addresses=[0x2666308],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(760,ice_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(760,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Vikemon Triangle",
		addresses=[0x2666324],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(570,ice_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(570,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Vikemon Cross",
		addresses=[0x2666340],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(390,ice_special_modifier,ultimate_modifier,2),
		max_value=Max_Cross_Multiplier(390,ice_special_modifier,ultimate_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Vikemon Cross Effect",
		addresses=[0x26663cc],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Omnimon II 035
	Attribute(
		name="Omnimon II Element",
		addresses=[0x266643e],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 3, 35),
		max_value=Get_Element_Type(16, 3, 35),
		is_little_endian=True, ),
	Attribute(
		name="Omnimon II +DP",
		addresses=[0x2666440],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Omnimon II HP",
		addresses=[0x2666442],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2420,ice_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(2420,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Omnimon II Circle",
		addresses=[0x2666444],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(550,ice_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(550,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Omnimon II Triangle",
		addresses=[0x2666460],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(800,ice_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(800,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Omnimon II Cross",
		addresses=[0x266647c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,ice_special_modifier,ultimate_modifier,7),
		max_value=Max_Cross_Multiplier(0,ice_special_modifier,ultimate_modifier,7),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Omnimon II Cross Effect",
		addresses=[0x2666508],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#MetalSeadramon 036
	Attribute(
		name="MetalSeadramon Element",
		addresses=[0x266657a],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 3, 36),
		max_value=Get_Element_Type(16, 3, 36),
		is_little_endian=True, ),
	Attribute(
		name="MetalSeadramon +DP",
		addresses=[0x266657c],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="MetalSeadramon HP",
		addresses=[0x266657e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2030,ice_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(2030,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MetalSeadramon Circle",
		addresses=[0x2666580],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(700,ice_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(700,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MetalSeadramon Triangle",
		addresses=[0x266659c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(450,ice_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(450,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MetalSeadramon Cross",
		addresses=[0x26665b8],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(400,ice_special_modifier,ultimate_modifier,11),
		max_value=Max_Cross_Multiplier(400,ice_special_modifier,ultimate_modifier,11),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MetalSeadramon Cross Effect",
		addresses=[0x2666644],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#MetalGarurumon 037
	Attribute(
		name="MetalGarurumon Element",
		addresses=[0x26666b6],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 3, 37),
		max_value=Get_Element_Type(16, 3, 37),
		is_little_endian=True, ),
	Attribute(
		name="MetalGarurumon +DP",
		addresses=[0x26666b8],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="MetalGarurumon HP",
		addresses=[0x26666ba],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2250,ice_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(2250,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MetalGarurumon Circle",
		addresses=[0x26666bc],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(700,ice_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(700,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MetalGarurumon Triangle",
		addresses=[0x26666d8],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(450,ice_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(450,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MetalGarurumon Cross",
		addresses=[0x26666f4],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(400,ice_special_modifier,ultimate_modifier,11),
		max_value=Max_Cross_Multiplier(400,ice_special_modifier,ultimate_modifier,11),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MetalGarurumon Cross Effect",
		addresses=[0x2666780],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#MarineAngemon 038
	Attribute(
		name="MarineAngemon Element",
		addresses=[0x26667f2],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 3, 38),
		max_value=Get_Element_Type(16, 3, 38),
		is_little_endian=True, ),
	Attribute(
		name="MarineAngemon +DP",
		addresses=[0x26667f4],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="MarineAngemon HP",
		addresses=[0x26667f6],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1540,ice_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1540,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MarineAngemon Circle",
		addresses=[0x26667f8],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(630,ice_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(630,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MarineAngemon Triangle",
		addresses=[0x2666814],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(480,ice_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(480,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MarineAngemon Cross",
		addresses=[0x2666830],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(220,ice_special_modifier,ultimate_modifier,2),
		max_value=Max_Cross_Multiplier(220,ice_special_modifier,ultimate_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MarineAngemon Cross Effect",
		addresses=[0x26668bc],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#WereGarurumon 039
	Attribute(
		name="WereGarurumon Element",
		addresses=[0x2666a5e],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 3, 39),
		max_value=Get_Element_Type(16, 3, 39),
		is_little_endian=True, ),
	Attribute(
		name="WereGarurumon +DP",
		addresses=[0x2666a60],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="WereGarurumon HP",
		addresses=[0x2666a62],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1820,ice_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1820,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="WereGarurumon Circle",
		addresses=[0x2666a64],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(670,ice_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(670,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="WereGarurumon Triangle",
		addresses=[0x2666a80],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(500,ice_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(500,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="WereGarurumon Cross",
		addresses=[0x2666a9c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,ice_special_modifier,ultimate_modifier,6),
		max_value=Max_Cross_Multiplier(0,ice_special_modifier,ultimate_modifier,6),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="WereGarurumon Cross Effect",
		addresses=[0x2666b28],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Zudomon 040
	Attribute(
		name="Zudomon Element",
		addresses=[0x2666b9a],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 3, 40),
		max_value=Get_Element_Type(16, 3, 40),
		is_little_endian=True, ),
	Attribute(
		name="Zudomon +DP",
		addresses=[0x2666b9c],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Zudomon HP",
		addresses=[0x2666b9e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2090,ice_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(2090,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Zudomon Circle",
		addresses=[0x2666ba0],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(700,ice_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(700,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Zudomon Triangle",
		addresses=[0x2666bbc],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(300,ice_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(300,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Zudomon Cross",
		addresses=[0x2666bd8],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(250,ice_special_modifier,ultimate_modifier,2),
		max_value=Max_Cross_Multiplier(250,ice_special_modifier,ultimate_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Zudomon Cross Effect",
		addresses=[0x2666c64],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Panjyamon 041
	Attribute(
		name="Panjyamon Element",
		addresses=[0x2666cd6],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 3, 41),
		max_value=Get_Element_Type(16, 3, 41),
		is_little_endian=True, ),
	Attribute(
		name="Panjyamon +DP",
		addresses=[0x2666cd8],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Panjyamon HP",
		addresses=[0x2666cda],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1800,ice_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1800,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Panjyamon Circle",
		addresses=[0x2666cdc],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(620,ice_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(620,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Panjyamon Triangle",
		addresses=[0x2666cf8],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(390,ice_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(390,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Panjyamon Cross",
		addresses=[0x2666d14],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,ice_special_modifier,ultimate_modifier,6),
		max_value=Max_Cross_Multiplier(0,ice_special_modifier,ultimate_modifier,6),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Panjyamon Cross Effect",
		addresses=[0x2666da0],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#MegaSeadramon 042
	Attribute(
		name="MegaSeadramon Element",
		addresses=[0x2666e12],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 3, 42),
		max_value=Get_Element_Type(16, 3, 42),
		is_little_endian=True, ),
	Attribute(
		name="MegaSeadramon +DP",
		addresses=[0x2666e14],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="MegaSeadramon HP",
		addresses=[0x2666e16],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1870,ice_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1870,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MegaSeadramon Circle",
		addresses=[0x2666e18],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(650,ice_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(650,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MegaSeadramon Triangle",
		addresses=[0x2666e34],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(360,ice_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(360,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MegaSeadramon Cross",
		addresses=[0x2666e50],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,ice_special_modifier,ultimate_modifier,5),
		max_value=Max_Cross_Multiplier(0,ice_special_modifier,ultimate_modifier,5),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MegaSeadramon Cross Effect",
		addresses=[0x2666edc],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#WaruSeadramon 043
	Attribute(
		name="WaruSeadramon Element",
		addresses=[0x2666f4e],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 3, 43),
		max_value=Get_Element_Type(16, 3, 43),
		is_little_endian=True, ),
	Attribute(
		name="WaruSeadramon +DP",
		addresses=[0x2666f50],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="WaruSeadramon HP",
		addresses=[0x2666f52],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1760,ice_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1760,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="WaruSeadramon Circle",
		addresses=[0x2666f54],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(650,ice_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(650,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="WaruSeadramon Triangle",
		addresses=[0x2666f70],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(360,ice_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(360,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="WaruSeadramon Cross",
		addresses=[0x2666f8c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(200,ice_special_modifier,ultimate_modifier,10),
		max_value=Max_Cross_Multiplier(200,ice_special_modifier,ultimate_modifier,10),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="WaruSeadramon Cross Effect",
		addresses=[0x2667018],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Brachiomon 044
	Attribute(
		name="Brachiomon Element",
		addresses=[0x266708a],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 3, 44),
		max_value=Get_Element_Type(16, 3, 44),
		is_little_endian=True, ),
	Attribute(
		name="Brachiomon +DP",
		addresses=[0x266708c],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Brachiomon HP",
		addresses=[0x266708e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2300,ice_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(2300,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Brachiomon Circle",
		addresses=[0x2667090],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(600,ice_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(600,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Brachiomon Triangle",
		addresses=[0x26670ac],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(380,ice_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(380,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Brachiomon Cross",
		addresses=[0x26670c8],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(150,ice_special_modifier,ultimate_modifier,2),
		max_value=Max_Cross_Multiplier(150,ice_special_modifier,ultimate_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Brachiomon Cross Effect",
		addresses=[0x2667154],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#BlueMeramon 045
	Attribute(
		name="BlueMeramon Element",
		addresses=[0x26671c6],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 3, 45),
		max_value=Get_Element_Type(16, 3, 45),
		is_little_endian=True, ),
	Attribute(
		name="BlueMeramon +DP",
		addresses=[0x26671c8],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="BlueMeramon HP",
		addresses=[0x26671ca],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1430,ice_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1430,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="BlueMeramon Circle",
		addresses=[0x26671cc],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(700,ice_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(700,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="BlueMeramon Triangle",
		addresses=[0x26671e8],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(480,ice_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(480,ice_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="BlueMeramon Cross",
		addresses=[0x2667204],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(360,ice_special_modifier,ultimate_modifier,4),
		max_value=Max_Cross_Multiplier(360,ice_special_modifier,ultimate_modifier,4),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="BlueMeramon Cross Effect",
		addresses=[0x2667290],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Garurumon 046
	Attribute(
		name="Garurumon Element",
		addresses=[0x2667432],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 2, 46),
		max_value=Get_Element_Type(16, 2, 46),
		is_little_endian=True, ),
	Attribute(
		name="Garurumon +DP",
		addresses=[0x2667434],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Garurumon HP",
		addresses=[0x2667436],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1100,ice_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(1100,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Garurumon Circle",
		addresses=[0x2667438],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(350,ice_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(350,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Garurumon Triangle",
		addresses=[0x2667454],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(230,ice_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(230,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Garurumon Cross",
		addresses=[0x2667470],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,ice_special_modifier,champion_modifier,5),
		max_value=Max_Cross_Multiplier(0,ice_special_modifier,champion_modifier,5),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Garurumon Cross Effect",
		addresses=[0x26674fc],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Ikkakumon 047
	Attribute(
		name="Garurumon Element",
		addresses=[0x266756e],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 2, 47),
		max_value=Get_Element_Type(16, 2, 47),
		is_little_endian=True, ),
	Attribute(
		name="Ikkakumon +DP",
		addresses=[0x2667570],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Ikkakumon HP",
		addresses=[0x2667572],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1200,ice_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(1200,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Ikkakumon Circle",
		addresses=[0x2667574],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(340,ice_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(340,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Ikkakumon Triangle",
		addresses=[0x2667590],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(250,ice_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(250,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Ikkakumon Cross",
		addresses=[0x26675ac],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(200,ice_special_modifier,champion_modifier,11),
		max_value=Max_Cross_Multiplier(200,ice_special_modifier,champion_modifier,11),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Ikkakumon Cross Effect",
		addresses=[0x2667638],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Dolphmon 048
	Attribute(
		name="Garurumon Element",
		addresses=[0x26676aa],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 2, 48),
		max_value=Get_Element_Type(16, 2, 48),
		is_little_endian=True, ),
	Attribute(
		name="Dolphmon +DP",
		addresses=[0x26676ac],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Dolphmon HP",
		addresses=[0x26676ae],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1000,ice_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(1000,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Dolphmon Circle",
		addresses=[0x26676b0],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(330,ice_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(330,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Dolphmon Triangle",
		addresses=[0x26676cc],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(290,ice_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(290,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Dolphmon Cross",
		addresses=[0x26676e8],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(200,ice_special_modifier,champion_modifier,4),
		max_value=Max_Cross_Multiplier(200,ice_special_modifier,champion_modifier,4),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Dolphmon Cross Effect",
		addresses=[0x2667774],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Whamon 049
	Attribute(
		name="Garurumon Element",
		addresses=[0x26677e6],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 2, 49),
		max_value=Get_Element_Type(16, 2, 49),
		is_little_endian=True, ),
	Attribute(
		name="Whamon +DP",
		addresses=[0x26677e8],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Whamon HP",
		addresses=[0x26677ea],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1300,ice_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(1300,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Whamon Circle",
		addresses=[0x26677ec],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(340,ice_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(340,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Whamon Triangle",
		addresses=[0x2667808],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(220,ice_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(220,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Whamon Cross",
		addresses=[0x2667824],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(150,ice_special_modifier,champion_modifier,3),
		max_value=Max_Cross_Multiplier(150,ice_special_modifier,champion_modifier,3),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Whamon Cross Effect",
		addresses=[0x26678b0],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Seadramon 050
	Attribute(
		name="Seadramon Element",
		addresses=[0x2667922],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 2, 50),
		max_value=Get_Element_Type(16, 2, 50),
		is_little_endian=True, ),
	Attribute(
		name="Seadramon +DP",
		addresses=[0x2667924],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Seadramon HP",
		addresses=[0x2667926],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1150,ice_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(1150,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Seadramon Circle",
		addresses=[0x2667928],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(360,ice_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(360,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Seadramon Triangle",
		addresses=[0x2667944],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(250,ice_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(250,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Seadramon Cross",
		addresses=[0x2667960],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(100,ice_special_modifier,champion_modifier,2),
		max_value=Max_Cross_Multiplier(100,ice_special_modifier,champion_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Seadramon Cross Effect",
		addresses=[0x26679ec],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Gesomon 051
	Attribute(
		name="Gesomon Element",
		addresses=[0x2667a5e],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 2, 51),
		max_value=Get_Element_Type(16, 2, 51),
		is_little_endian=True, ),
	Attribute(
		name="Gesomon +DP",
		addresses=[0x2667a60],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Gesomon HP",
		addresses=[0x2667a62],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1030,ice_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(1030,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gesomon Circle",
		addresses=[0x2667a64],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(400,ice_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(400,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gesomon Triangle",
		addresses=[0x2667a80],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(250,ice_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(250,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gesomon Cross",
		addresses=[0x2667a9c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(160,ice_special_modifier,champion_modifier,2),
		max_value=Max_Cross_Multiplier(160,ice_special_modifier,champion_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gesomon Cross Effect",
		addresses=[0x2667b28],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Frigimon 052
	Attribute(
		name="Frigimon Element",
		addresses=[0x2667cca],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 2, 52),
		max_value=Get_Element_Type(16, 2, 52),
		is_little_endian=True, ),
	Attribute(
		name="Frigimon +DP",
		addresses=[0x2667ccc],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Frigimon HP",
		addresses=[0x2667cce],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(990,ice_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(990,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Frigimon Circle",
		addresses=[0x2667cd0],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(350,ice_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(350,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Frigimon Triangle",
		addresses=[0x2667cec],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(200,ice_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(200,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Frigimon Cross",
		addresses=[0x2667d08],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(170,ice_special_modifier,champion_modifier,11),
		max_value=Max_Cross_Multiplier(170,ice_special_modifier,champion_modifier,11),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gesomon Cross Effect",
		addresses=[0x2667d94],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Gekomon 053
	Attribute(
		name="Gekomon Element",
		addresses=[0x2667e06],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 2, 53),
		max_value=Get_Element_Type(16, 2, 53),
		is_little_endian=True, ),
	Attribute(
		name="Gekomon +DP",
		addresses=[0x2667e08],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Gekomon HP",
		addresses=[0x2667e0a],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(960,ice_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(960,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gekomon Circle",
		addresses=[0x2667e0c],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(340,ice_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(340,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gekomon Triangle",
		addresses=[0x2667e28],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(220,ice_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(220,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gekomon Cross",
		addresses=[0x2667e44],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(100,ice_special_modifier,champion_modifier,2),
		max_value=Max_Cross_Multiplier(100,ice_special_modifier,champion_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gekomon Cross Effect",
		addresses=[0x2667ed0],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Coelamon 054
	Attribute(
		name="Coelamon Element",
		addresses=[0x2667f42],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 2, 54),
		max_value=Get_Element_Type(16, 2, 54),
		is_little_endian=True, ),
	Attribute(
		name="Coelamon +DP",
		addresses=[0x2667f44],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Coelamon HP",
		addresses=[0x2667f46],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1270,ice_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(1270,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Coelamon Circle",
		addresses=[0x2667f48],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(400,ice_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(400,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Coelamon Triangle",
		addresses=[0x2667f64],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(290,ice_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(290,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Coelamon Cross",
		addresses=[0x2667f80],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(210,ice_special_modifier,champion_modifier,2),
		max_value=Max_Cross_Multiplier(210,ice_special_modifier,champion_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Coelamon Cross Effect",
		addresses=[0x266800c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Mojyamon 055
	Attribute(
		name="Mojyamon Element",
		addresses=[0x266807e],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 2, 55),
		max_value=Get_Element_Type(16, 2, 55),
		is_little_endian=True, ),
	Attribute(
		name="Mojyamon +DP",
		addresses=[0x2668080],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Mojyamon HP",
		addresses=[0x2668082],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(980,ice_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(980,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Mojyamon Circle",
		addresses=[0x2668084],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(370,ice_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(370,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Mojyamon Triangle",
		addresses=[0x26680a0],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(290,ice_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(290,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Mojyamon Cross",
		addresses=[0x26680bc],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(210,ice_special_modifier,champion_modifier,0),
		max_value=Max_Cross_Multiplier(210,ice_special_modifier,champion_modifier,0),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Mojyamon Cross Effect",
		addresses=[0x2668148],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Shellmon 056
	Attribute(
		name="Shellmon Element",
		addresses=[0x26681ba],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 2, 56),
		max_value=Get_Element_Type(16, 2, 56),
		is_little_endian=True, ),
	Attribute(
		name="Shellmon +DP",
		addresses=[0x26681bc],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Shellmon HP",
		addresses=[0x26681be],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1250,ice_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(1250,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Shellmon Circle",
		addresses=[0x26681c0],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(340,ice_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(340,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Shellmon Triangle",
		addresses=[0x26681dc],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(200,ice_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(200,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Shellmon Cross",
		addresses=[0x26681f8],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(150,ice_special_modifier,champion_modifier,2),
		max_value=Max_Cross_Multiplier(150,ice_special_modifier,champion_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Shellmon Cross Effect",
		addresses=[0x2668284],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Sorcerimon 057
	Attribute(
		name="Sorcerimon Element",
		addresses=[0x26682f6],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 2, 57),
		max_value=Get_Element_Type(16, 2, 57),
		is_little_endian=True, ),
	Attribute(
		name="Sorcerimon +DP",
		addresses=[0x26682f8],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Sorcerimon HP",
		addresses=[0x26682fa],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(900,ice_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(900,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Sorcerimon Circle",
		addresses=[0x26682fc],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(440,ice_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(440,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Sorcerimon Triangle",
		addresses=[0x2668318],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(370,ice_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(370,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Sorcerimon Cross",
		addresses=[0x2668334],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(170,ice_special_modifier,champion_modifier,10),
		max_value=Max_Cross_Multiplier(170,ice_special_modifier,champion_modifier,10),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Sorcerimon Cross Effect",
		addresses=[0x26683c0],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#IceDevimon 058
	Attribute(
		name="IceDevimon Element",
		addresses=[0x2668432],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 2, 58),
		max_value=Get_Element_Type(16, 2, 58),
		is_little_endian=True, ),
	Attribute(
		name="IceDevimon +DP",
		addresses=[0x2668434],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="IceDevimon HP",
		addresses=[0x2668436],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(990,ice_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(990,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="IceDevimon Circle",
		addresses=[0x2668438],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(390,ice_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(390,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="IceDevimon Triangle",
		addresses=[0x2668454],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(290,ice_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(290,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="IceDevimon Cross",
		addresses=[0x2668470],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(180,ice_special_modifier,champion_modifier,11),
		max_value=Max_Cross_Multiplier(180,ice_special_modifier,champion_modifier,11),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="IceDevimon Cross Effect",
		addresses=[0x266862C],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Hyogamon 059
	Attribute(
		name="Hyogamon Element",
		addresses=[0x266869E],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 2, 59),
		max_value=Get_Element_Type(16, 2, 59),
		is_little_endian=True, ),
	Attribute(
		name="Hyogamon +DP",
		addresses=[0x26686a0],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Hyogamon HP",
		addresses=[0x26686a2],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1200,ice_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(1200,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Hyogamon Circle",
		addresses=[0x26686a4],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(460,ice_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(460,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Hyogamon Triangle",
		addresses=[0x26686c0],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(250,ice_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(250,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Hyogamon Cross",
		addresses=[0x26686dc],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,ice_special_modifier,champion_modifier,5),
		max_value=Max_Cross_Multiplier(0,ice_special_modifier,champion_modifier,5),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Hyogamon Cross Effect",
		addresses=[0x2668768],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Icemon 060
	Attribute(
		name="Icemon Element",
		addresses=[0x26687da],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 2, 60),
		max_value=Get_Element_Type(16, 2, 60),
		is_little_endian=True, ),
	Attribute(
		name="Icemon +DP",
		addresses=[0x26687dc],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Icemon HP",
		addresses=[0x26687de],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1140,ice_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(1140,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Icemon Circle",
		addresses=[0x26687e0],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(370,ice_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(370,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Icemon Triangle",
		addresses=[0x26687fc],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(240,ice_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(240,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Icemon Cross",
		addresses=[0x2668818],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,ice_special_modifier,champion_modifier,7),
		max_value=Max_Cross_Multiplier(0,ice_special_modifier,champion_modifier,7),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Icemon Cross Effect",
		addresses=[0x26688a4],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Gomamon 061
	Attribute(
		name="Gomamon Element",
		addresses=[0x2668916],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 0, 61),
		max_value=Get_Element_Type(16, 0, 61),
		is_little_endian=True, ),
	Attribute(
		name="Gomamon +DP",
		addresses=[0x2668918],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Gomamon HP",
		addresses=[0x266891a],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(700,ice_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(700,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gomamon Circle",
		addresses=[0x266891c],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(300,ice_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(300,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gomamon Triangle",
		addresses=[0x2668938],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(240,ice_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(240,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gomamon Cross",
		addresses=[0x2668954],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(200,ice_special_modifier,rookie_modifier,3),
		max_value=Max_Cross_Multiplier(200,ice_special_modifier,rookie_modifier,3),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gomamon Cross Effect",
		addresses=[0x26689e0],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Gabumon 062
	Attribute(
		name="Gabumon Element",
		addresses=[0x2668a52],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 0, 62),
		max_value=Get_Element_Type(16, 0, 62),
		is_little_endian=True, ),
	Attribute(
		name="Gabumon +DP",
		addresses=[0x2668a54],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Gabumon HP",
		addresses=[0x2668a56],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(680,ice_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(680,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gabumon Circle",
		addresses=[0x2668a58],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(350,ice_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(350,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gabumon Triangle",
		addresses=[0x2668a74],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(220,ice_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(220,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gabumon Cross",
		addresses=[0x2668a90],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(140,ice_special_modifier,rookie_modifier,2),
		max_value=Max_Cross_Multiplier(140,ice_special_modifier,rookie_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gabumon Cross Effect",
		addresses=[0x2668b1c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Betamon 063
	Attribute(
		name="Betamon Element",
		addresses=[0x2668b8e],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 0, 63),
		max_value=Get_Element_Type(16, 0, 63),
		is_little_endian=True, ),
	Attribute(
		name="Betamon +DP",
		addresses=[0x2668b90],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Betamon HP",
		addresses=[0x2668b92],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(730,ice_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(730,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Betamon Circle",
		addresses=[0x2668b94],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(300,ice_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(300,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Betamon Triangle",
		addresses=[0x2668bb0],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(190,ice_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(190,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Betamon Cross",
		addresses=[0x2668bcc],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(170,ice_special_modifier,rookie_modifier,2),
		max_value=Max_Cross_Multiplier(170,ice_special_modifier,rookie_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Betamon Cross Effect",
		addresses=[0x2668c58],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Penguinmon 064
	Attribute(
		name="Penguinmon Element",
		addresses=[0x2668cca],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 0, 64),
		max_value=Get_Element_Type(16, 0, 64),
		is_little_endian=True, ),
	Attribute(
		name="Penguinmon +DP",
		addresses=[0x2668ccc],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Penguinmon HP",
		addresses=[0x2668cce],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(670,ice_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(670,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Penguinmon Circle",
		addresses=[0x2668cd0],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(320,ice_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(320,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Penguinmon Triangle",
		addresses=[0x2668cec],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(180,ice_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(180,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Penguinmon Cross",
		addresses=[0x2668d08],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(170,ice_special_modifier,rookie_modifier,2),
		max_value=Max_Cross_Multiplier(170,ice_special_modifier,rookie_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Penguinmon Cross Effect",
		addresses=[0x2668d94],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Gizamon 065
	Attribute(
		name="Gizamon Element",
		addresses=[0x2668f36],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 0, 65),
		max_value=Get_Element_Type(16, 0, 65),
		is_little_endian=True, ),
	Attribute(
		name="Gizamon +DP",
		addresses=[0x2668f38],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Gizamon HP",
		addresses=[0x2668f3a],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(650,ice_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(650,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gizamon Circle",
		addresses=[0x2668f3c],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(260,ice_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(260,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gizamon Triangle",
		addresses=[0x2668f58],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(200,ice_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(200,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gizamon Cross",
		addresses=[0x2668f74],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(150,ice_special_modifier,rookie_modifier,11),
		max_value=Max_Cross_Multiplier(150,ice_special_modifier,rookie_modifier,11),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gizamon Cross Effect",
		addresses=[0x2669000],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Otamamon 066
	Attribute(
		name="Otamamon Element",
		addresses=[0x2669072],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 0, 66),
		max_value=Get_Element_Type(16, 0, 66),
		is_little_endian=True, ),
	Attribute(
		name="Otamamon +DP",
		addresses=[0x2669074],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Otamamon HP",
		addresses=[0x2669076],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(710,ice_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(710,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Otamamon Circle",
		addresses=[0x2669078],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(330,ice_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(330,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Otamamon Triangle",
		addresses=[0x2669094],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(130,ice_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(130,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Otamamon Cross",
		addresses=[0x26690b0],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(100,ice_special_modifier,rookie_modifier,2),
		max_value=Max_Cross_Multiplier(100,ice_special_modifier,rookie_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Otamamon Cross Effect",
		addresses=[0x266913c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#SnowAgumon 067
	Attribute(
		name="SnowAgumon Element",
		addresses=[0x26691ae],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 0, 67),
		max_value=Get_Element_Type(16, 0, 67),
		is_little_endian=True, ),
	Attribute(
		name="SnowAgumon +DP",
		addresses=[0x26691b0],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="SnowAgumon HP",
		addresses=[0x26691b2],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(720,ice_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(720,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="SnowAgumon Circle",
		addresses=[0x26691b4],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(160,ice_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(160,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="SnowAgumon Triangle",
		addresses=[0x26691d0],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(200,ice_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(200,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="SnowAgumon Cross",
		addresses=[0x26691ec],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(220,ice_special_modifier,rookie_modifier,4),
		max_value=Max_Cross_Multiplier(220,ice_special_modifier,rookie_modifier,4),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="SnowAgumon Cross Effect",
		addresses=[0x2669278],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#SnowGoburimon 068
	Attribute(
		name="SnowGoburimon Element",
		addresses=[0x26692ea],
		number_of_bytes=1,
		min_value=Get_Element_Type(16, 0, 68),
		max_value=Get_Element_Type(16, 0, 68),
		is_little_endian=True, ),
	Attribute(
		name="SnowGoburimon +DP",
		addresses=[0x26692ec],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="SnowGoburimon HP",
		addresses=[0x26692ee],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(770,ice_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(770,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="SnowGoburimon Circle",
		addresses=[0x26692f0],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(230,ice_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(230,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="SnowGoburimon Triangle",
		addresses=[0x266930c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(230,ice_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(230,ice_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="SnowGoburimon Cross",
		addresses=[0x2669328],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(230,ice_special_modifier,rookie_modifier,0),
		max_value=Max_Cross_Multiplier(230,ice_special_modifier,rookie_modifier,0),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="SnowGoburimon Cross Effect",
		addresses=[0x26693b4],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Valkyrimon 069
	Attribute(
		name="Valkyrimon Element",
		addresses=[0x2669426],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 3, 69),
		max_value=Get_Element_Type(32, 3, 69),
		is_little_endian=True, ),
	Attribute(
		name="Valkyrimon +DP",
		addresses=[0x2669428],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Valkyrimon HP",
		addresses=[0x266942a],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1590,nature_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1590,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Valkyrimon Circle",
		addresses=[0x266942c],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(840,nature_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(840,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Valkyrimon Triangle",
		addresses=[0x2669448],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(550,nature_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(550,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Valkyrimon Cross",
		addresses=[0x2669464],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(350,nature_special_modifier,ultimate_modifier,2),
		max_value=Max_Cross_Multiplier(350,nature_special_modifier,ultimate_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Valkyrimon Cross Effect",
		addresses=[0x26694f0],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Seraphimon 070
	Attribute(
		name="Seraphimon Element",
		addresses=[0x2669562],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 3, 70),
		max_value=Get_Element_Type(32, 3, 70),
		is_little_endian=True, ),
	Attribute(
		name="Seraphimon +DP",
		addresses=[0x2669564],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Seraphimon HP",
		addresses=[0x2669566],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1650,nature_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1650,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Seraphimon Circle",
		addresses=[0x2669568],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(900,nature_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(900,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Seraphimon Triangle",
		addresses=[0x2669584],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(510,nature_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(510,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Seraphimon Cross",
		addresses=[0x26695a0],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(420,nature_special_modifier,ultimate_modifier,14),
		max_value=Max_Cross_Multiplier(420,nature_special_modifier,ultimate_modifier,14),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Seraphimon Cross Effect",
		addresses=[0x266962c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Magnadramon 071
	Attribute(
		name="Magnadramon Element",
		addresses=[0x266969e],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 3, 71),
		max_value=Get_Element_Type(32, 3, 71),
		is_little_endian=True, ),
	Attribute(
		name="Magnadramon +DP",
		addresses=[0x26696a0],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Magnadramon HP",
		addresses=[0x26696a2],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1870,nature_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1870,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Magnadramon Circle",
		addresses=[0x26696a4],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(800,nature_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(800,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Magnadramon Triangle",
		addresses=[0x26696c0],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(610,nature_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(610,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
#Magndramons cross isn't in a predictable place for some reason, lots fo random text in between
	Attribute(
		name="Magnadramon Cross",
		addresses=[0x266980C],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(370,nature_special_modifier,ultimate_modifier,4),
		max_value=Max_Cross_Multiplier(370,nature_special_modifier,ultimate_modifier,4),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Magnadramon Cross Effect",
		addresses=[0x2669898],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#AeroVeedramon 072
	Attribute(
		name="AeroVeedramon Element",
		addresses=[0x266990a],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 3, 72),
		max_value=Get_Element_Type(32, 3, 72),
		is_little_endian=True, ),
	Attribute(
		name="AeroVeedramon +DP",
		addresses=[0x266990c],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="AeroVeedramon HP",
		addresses=[0x266990e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1430,nature_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1430,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="AeroVeedramon Circle",
		addresses=[0x2669910],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(750,nature_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(750,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="AeroVeedramon Triangle",
		addresses=[0x266992c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(550,nature_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(550,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="AeroVeedramon Cross",
		addresses=[0x2669948],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(360,nature_special_modifier,ultimate_modifier,1),
		max_value=Max_Cross_Multiplier(360,nature_special_modifier,ultimate_modifier,1),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="AeroVeedramon Cross Effect",
		addresses=[0x26699d4],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Rosemon 073
	Attribute(
		name="Rosemon Element",
		addresses=[0x2669a46],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 3, 73),
		max_value=Get_Element_Type(32, 3, 73),
		is_little_endian=True, ),
	Attribute(
		name="Rosemon +DP",
		addresses=[0x2669a48],
		number_of_bytes=2,
		possible_values=Thirty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Rosemon HP",
		addresses=[0x2669a4a],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1210,nature_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1210,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Rosemon Circle",
		addresses=[0x2669a4c],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(720,nature_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(720,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Rosemon Triangle",
		addresses=[0x2669a68],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(480,nature_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(480,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Rosemon Cross",
		addresses=[0x2669a84],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(320,nature_special_modifier,ultimate_modifier,9),
		max_value=Max_Cross_Multiplier(320,nature_special_modifier,ultimate_modifier,9),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Rosemon Cross Effect",
		addresses=[0x2669b10],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#HerculesKabuterimon 074
	Attribute(
		name="HerculesKabuterimon Element",
		addresses=[0x2669b82],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 3, 74),
		max_value=Get_Element_Type(32, 3, 74),
		is_little_endian=True, ),
	Attribute(
		name="HerculesKabuterimon +DP",
		addresses=[0x2669b84],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="HerculesKabuterimon HP",
		addresses=[0x2669b86],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1700,nature_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1700,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="HerculesKabuterimon Circle",
		addresses=[0x2669b88],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(790,nature_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(790,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="HerculesKabuterimon Triangle",
		addresses=[0x2669ba4],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(490,nature_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(490,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="HerculesKabuterimon Cross",
		addresses=[0x2669bc0],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(250,nature_special_modifier,ultimate_modifier,1),
		max_value=Max_Cross_Multiplier(250,nature_special_modifier,ultimate_modifier,1),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="HerculesKabuterimon Cross Effect",
		addresses=[0x2669c4c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#MagnaAngemon 075
	Attribute(
		name="MagnaAngemon Element",
		addresses=[0x2669cbe],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 3, 75),
		max_value=Get_Element_Type(32, 3, 75),
		is_little_endian=True, ),
	Attribute(
		name="MagnaAngemon +DP",
		addresses=[0x2669cc0],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="MagnaAngemon HP",
		addresses=[0x2669cc2],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1320,nature_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1320,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MagnaAngemon Circle",
		addresses=[0x2669cc4],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(770,nature_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(770,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MagnaAngemon Triangle",
		addresses=[0x2669ce0],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(570,nature_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(570,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MagnaAngemon Cross",
		addresses=[0x2669CFC],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(370,nature_special_modifier,ultimate_modifier,14),
		max_value=Max_Cross_Multiplier(370,nature_special_modifier,ultimate_modifier,14),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MagnaAngemon Cross Effect",
		addresses=[0x2669d88],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Silphymon 076
	Attribute(
		name="Silphymon Element",
		addresses=[0x2669dfa],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 3, 76),
		max_value=Get_Element_Type(32, 3, 76),
		is_little_endian=True, ),
	Attribute(
		name="Silphymon +DP",
		addresses=[0x2669dfc],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Silphymon HP",
		addresses=[0x2669dfe],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1540,nature_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1540,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Silphymon Circle",
		addresses=[0x2669e00],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(680,nature_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(680,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Silphymon Triangle",
		addresses=[0x2669e1c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(500,nature_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(500,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Silphymon Cross",
		addresses=[0x2669e38],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(400,nature_special_modifier,ultimate_modifier,3),
		max_value=Max_Cross_Multiplier(400,nature_special_modifier,ultimate_modifier,3),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Silphymon Cross Effect",
		addresses=[0x2669ec4],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Angewomon 077
	Attribute(
		name="Angewomon Element",
		addresses=[0x2669f36],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 3, 77),
		max_value=Get_Element_Type(32, 3, 77),
		is_little_endian=True, ),
	Attribute(
		name="Angewomon +DP",
		addresses=[0x2669f38],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Angewomon HP",
		addresses=[0x2669f3a],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1370,nature_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1370,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Angewomon Circle",
		addresses=[0x2669f3c],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(720,nature_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(720,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Angewomon Triangle",
		addresses=[0x2669f58],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(520,nature_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(520,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Angewomon Cross",
		addresses=[0x2669f74],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(330,nature_special_modifier,ultimate_modifier,14),
		max_value=Max_Cross_Multiplier(330,nature_special_modifier,ultimate_modifier,14),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Angewomon Cross Effect",
		addresses=[0x266a000],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Lillymon 078
	Attribute(
		name="Lillymon Element",
		addresses=[0x266a1a2],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 3, 78),
		max_value=Get_Element_Type(32, 3, 78),
		is_little_endian=True, ),
	Attribute(
		name="Lillymon +DP",
		addresses=[0x266a1a4],
		number_of_bytes=2,
		possible_values=Thirty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Lillymon HP",
		addresses=[0x266a1a6],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1100,nature_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1100,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Lillymon Circle",
		addresses=[0x266a1a8],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(650,nature_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(650,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Lillymon Triangle",
		addresses=[0x266a1c4],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(340,nature_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(340,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Lillymon Cross",
		addresses=[0x266a1e0],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(200,nature_special_modifier,ultimate_modifier,9),
		max_value=Max_Cross_Multiplier(200,nature_special_modifier,ultimate_modifier,9),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Lillymon Cross Effect",
		addresses=[0x266a26c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#MegaKabuterimon 079
	Attribute(
		name="MegaKabuterimon Element",
		addresses=[0x266a2de],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 3, 79),
		max_value=Get_Element_Type(32, 3, 79),
		is_little_endian=True, ),
	Attribute(
		name="MegaKabuterimon +DP",
		addresses=[0x266a2e0],
		number_of_bytes=2,
		possible_values=Thirty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="MegaKabuterimon HP",
		addresses=[0x266a2e2],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1480,nature_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1480,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MegaKabuterimon Circle",
		addresses=[0x266a2e4],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(700,nature_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(700,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MegaKabuterimon Triangle",
		addresses=[0x266a300],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(400,nature_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(400,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MegaKabuterimon Cross",
		addresses=[0x266a31c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,nature_special_modifier,ultimate_modifier,5),
		max_value=Max_Cross_Multiplier(0,nature_special_modifier,ultimate_modifier,5),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MegaKabuterimon Cross Effect",
		addresses=[0x266a3a8],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Piximon 080
	Attribute(
		name="Piximon Element",
		addresses=[0x266a41a],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 3, 80),
		max_value=Get_Element_Type(32, 3, 80),
		is_little_endian=True, ),
	Attribute(
		name="Piximon +DP",
		addresses=[0x266a41c],
		number_of_bytes=2,
		possible_values=Thirty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Piximon HP",
		addresses=[0x266a41e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1370,nature_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1370,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Piximon Circle",
		addresses=[0x266a420],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(670,nature_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(670,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Piximon Triangle",
		addresses=[0x266a43c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(430,nature_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(430,nature_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Piximon Cross",
		addresses=[0x266a458],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(320,nature_special_modifier,ultimate_modifier,0),
		max_value=Max_Cross_Multiplier(320,nature_special_modifier,ultimate_modifier,0),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Piximon Cross Effect",
		addresses=[0x266a4e4],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Veedramon 081
	Attribute(
		name="Veedramon Element",
		addresses=[0x266a556],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 2, 81),
		max_value=Get_Element_Type(32, 2, 81),
		is_little_endian=True, ),
	Attribute(
		name="Veedramon +DP",
		addresses=[0x266a558],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Veedramon HP",
		addresses=[0x266a55a],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(880,nature_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(880,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Veedramon Circle",
		addresses=[0x266a55c],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(500,nature_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(500,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Veedramon Triangle",
		addresses=[0x266a578],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(360,nature_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(360,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Veedramon Cross",
		addresses=[0x266a594],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(200,nature_special_modifier,champion_modifier,1),
		max_value=Max_Cross_Multiplier(200,nature_special_modifier,champion_modifier,1),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Veedramon Cross Effect",
		addresses=[0x266a620],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Angemon 082
	Attribute(
		name="Angemon Element",
		addresses=[0x266a692],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 2, 82),
		max_value=Get_Element_Type(32, 2, 82),
		is_little_endian=True, ),
	Attribute(
		name="Angemon +DP",
		addresses=[0x266a694],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Angemon HP",
		addresses=[0x266a696],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(940,nature_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(940,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Angemon Circle",
		addresses=[0x266a698],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(400,nature_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(400,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Angemon Triangle",
		addresses=[0x266a6b4],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(200,nature_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(200,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Angemon Cross",
		addresses=[0x266a6d0],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(260,nature_special_modifier,champion_modifier,14),
		max_value=Max_Cross_Multiplier(260,nature_special_modifier,champion_modifier,14),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Angemon Cross Effect",
		addresses=[0x266a75c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#R-Gatomon 083
	Attribute(
		name="R-Gatomon Element",
		addresses=[0x266a7ce],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 2, 83),
		max_value=Get_Element_Type(32, 2, 83),
		is_little_endian=True, ),
	Attribute(
		name="R-Gatomon +DP",
		addresses=[0x266a7d0],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="R-Gatomon HP",
		addresses=[0x266a7d2],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(750,nature_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(750,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="R-Gatomon Circle",
		addresses=[0x266a7d4],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(410,nature_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(410,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="R-Gatomon Triangle",
		addresses=[0x266a7f0],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(300,nature_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(300,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="R-Gatomon Cross",
		addresses=[0x266a80c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(210,nature_special_modifier,champion_modifier,4),
		max_value=Max_Cross_Multiplier(210,nature_special_modifier,champion_modifier,4),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="R-Gatomon Cross Effect",
		addresses=[0x266a898],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Togemon 084
	Attribute(
		name="Togemon Element",
		addresses=[0x266a90a],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 2, 84),
		max_value=Get_Element_Type(32, 2, 84),
		is_little_endian=True, ),
	Attribute(
		name="Togemon +DP",
		addresses=[0x266a90c],
		number_of_bytes=2,
		possible_values=Thirty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Togemon HP",
		addresses=[0x266a90e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(800,nature_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(800,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Togemon Circle",
		addresses=[0x266a910],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(380,nature_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(380,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Togemon Triangle",
		addresses=[0x266a92c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(250,nature_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(250,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Togemon Cross",
		addresses=[0x266AA78],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(170,nature_special_modifier,champion_modifier,3),
		max_value=Max_Cross_Multiplier(170,nature_special_modifier,champion_modifier,3),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Togemon Cross Effect",
		addresses=[0x266AB04],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Leomon 085
	Attribute(
		name="Leomon Element",
		addresses=[0x266ab76],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 2, 85),
		max_value=Get_Element_Type(32, 2, 85),
		is_little_endian=True, ),
	Attribute(
		name="Leomon +DP",
		addresses=[0x266ab78],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Leomon HP",
		addresses=[0x266ab7a],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(890,nature_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(890,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Leomon Circle",
		addresses=[0x266ab7c],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(430,nature_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(430,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Leomon Triangle",
		addresses=[0x266ab98],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(280,nature_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(280,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Leomon Cross",
		addresses=[0x266abb4],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(200,nature_special_modifier,champion_modifier,0),
		max_value=Max_Cross_Multiplier(200,nature_special_modifier,champion_modifier,0),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Leomon Cross Effect",
		addresses=[0x266ac40],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Kabuterimon 086
	Attribute(
		name="Kabuterimon Element",
		addresses=[0x266acb2],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 2, 86),
		max_value=Get_Element_Type(32, 2, 86),
		is_little_endian=True, ),
	Attribute(
		name="Kabuterimon +DP",
		addresses=[0x266acb4],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Kabuterimon HP",
		addresses=[0x266acb6],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(950,nature_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(950,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Kabuterimon Circle",
		addresses=[0x266acb8],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(550,nature_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(550,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Kabuterimon Triangle",
		addresses=[0x266acd4],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(360,nature_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(360,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Kabuterimon Cross",
		addresses=[0x266acf0],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,nature_special_modifier,champion_modifier,5),
		max_value=Max_Cross_Multiplier(0,nature_special_modifier,champion_modifier,5),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Kabuterimon Cross Effect",
		addresses=[0x266ad7c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Airdramon 087
	Attribute(
		name="Airdramon Element",
		addresses=[0x266adee],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 2, 87),
		max_value=Get_Element_Type(32, 2, 87),
		is_little_endian=True, ),
	Attribute(
		name="Airdramon +DP",
		addresses=[0x266adf0],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Airdramon HP",
		addresses=[0x266adf2],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(950,nature_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(950,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Airdramon Circle",
		addresses=[0x266adf4],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(430,nature_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(430,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Airdramon Triangle",
		addresses=[0x266ae10],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(200,nature_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(200,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Airdramon Cross",
		addresses=[0x266ae2c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(50,nature_special_modifier,champion_modifier,2),
		max_value=Max_Cross_Multiplier(50,nature_special_modifier,champion_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Airdramon Cross Effect",
		addresses=[0x266aeb8],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Unimon 088
	Attribute(
		name="Unimon Element",
		addresses=[0x266af2a],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 2, 88),
		max_value=Get_Element_Type(32, 2, 88),
		is_little_endian=True, ),
	Attribute(
		name="Unimon +DP",
		addresses=[0x266af2c],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Unimon HP",
		addresses=[0x266af2e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(950,nature_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(950,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Unimon Circle",
		addresses=[0x266af30],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(390,nature_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(390,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Unimon Triangle",
		addresses=[0x266af4c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(210,nature_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(210,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Unimon Cross",
		addresses=[0x266af68],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(150,nature_special_modifier,champion_modifier,2),
		max_value=Max_Cross_Multiplier(150,nature_special_modifier,champion_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Unimon Cross Effect",
		addresses=[0x266aff4],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Ninjamon 089
	Attribute(
		name="Ninjamon Element",
		addresses=[0x266b066],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 2, 89),
		max_value=Get_Element_Type(32, 2, 89),
		is_little_endian=True, ),
	Attribute(
		name="Ninjamon +DP",
		addresses=[0x266b068],
		number_of_bytes=2,
		possible_values=Thirty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Ninjamon HP",
		addresses=[0x266b06a],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(650,nature_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(650,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Ninjamon Circle",
		addresses=[0x266b06c],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(440,nature_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(440,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Ninjamon Triangle",
		addresses=[0x266b088],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(350,nature_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(350,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Ninjamon Cross",
		addresses=[0x266b0a4],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(250,nature_special_modifier,champion_modifier,1),
		max_value=Max_Cross_Multiplier(250,nature_special_modifier,champion_modifier,1),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Ninjamon Cross Effect",
		addresses=[0x266b130],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Kuwagamon 090
	Attribute(
		name="Kuwagamon Element",
		addresses=[0x266b1a2],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 2, 90),
		max_value=Get_Element_Type(32, 2, 90),
		is_little_endian=True, ),
	Attribute(
		name="Kuwagamon +DP",
		addresses=[0x266b1a4],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Kuwagamon HP",
		addresses=[0x266b1a6],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(900,nature_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(900,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Kuwagamon Circle",
		addresses=[0x266b1a8],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(530,nature_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(530,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Kuwagamon Triangle",
		addresses=[0x266b1c4],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(400,nature_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(400,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Kuwagamon Cross",
		addresses=[0x266b1e0],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,nature_special_modifier,champion_modifier,6),
		max_value=Max_Cross_Multiplier(0,nature_special_modifier,champion_modifier,6),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Kuwagamon Cross Effect",
		addresses=[0x266B39C],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Drimogemon 091
	Attribute(
		name="Drimogemon Element",
		addresses=[0x266B40E],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 2, 91),
		max_value=Get_Element_Type(32, 2, 91),
		is_little_endian=True, ),
	Attribute(
		name="Drimogemon +DP",
		addresses=[0x266b410],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Drimogemon HP",
		addresses=[0x266b412],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(850,nature_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(850,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Drimogemon Circle",
		addresses=[0x266b414],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(450,nature_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(450,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Drimogemon Triangle",
		addresses=[0x266b430],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(310,nature_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(310,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Drimogemon Cross",
		addresses=[0x266b44c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(280,nature_special_modifier,champion_modifier,0),
		max_value=Max_Cross_Multiplier(280,nature_special_modifier,champion_modifier,0),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Drimogemon Cross Effect",
		addresses=[0x266b4d8],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Vegiemon 092
	Attribute(
		name="Vegiemon Element",
		addresses=[0x266b54a],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 2, 92),
		max_value=Get_Element_Type(32, 2, 92),
		is_little_endian=True, ),
	Attribute(
		name="Vegiemon +DP",
		addresses=[0x266b54c],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Vegiemon HP",
		addresses=[0x266b54e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(810,nature_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(810,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Vegiemon Circle",
		addresses=[0x266b550],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(390,nature_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(390,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Vegiemon Triangle",
		addresses=[0x266b56c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(270,nature_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(270,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Vegiemon Cross",
		addresses=[0x266b588],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(100,nature_special_modifier,champion_modifier,10),
		max_value=Max_Cross_Multiplier(100,nature_special_modifier,champion_modifier,10),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Vegiemon Cross Effect",
		addresses=[0x266b614],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Kokatorimon 093
	Attribute(
		name="Kokatorimon Element",
		addresses=[0x266b686],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 2, 93),
		max_value=Get_Element_Type(32, 2, 93),
		is_little_endian=True, ),
	Attribute(
		name="Kokatorimon +DP",
		addresses=[0x266b688],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Kokatorimon HP",
		addresses=[0x266b68a],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(910,nature_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(910,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Kokatorimon Circle",
		addresses=[0x266b68c],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(350,nature_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(350,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Kokatorimon Triangle",
		addresses=[0x266b6a8],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(260,nature_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(260,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Kokatorimon Cross",
		addresses=[0x266b6c4],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(150,nature_special_modifier,champion_modifier,2),
		max_value=Max_Cross_Multiplier(150,nature_special_modifier,champion_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Kokatorimon Cross Effect",
		addresses=[0x266b750],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Yanmamon 094
	Attribute(
		name="Yanmamon Element",
		addresses=[0x266b7c2],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 2, 94),
		max_value=Get_Element_Type(32, 2, 94),
		is_little_endian=True, ),
	Attribute(
		name="Yanmamon +DP",
		addresses=[0x266b7c4],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Yanmamon HP",
		addresses=[0x266b7c6],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(740,nature_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(740,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Yanmamon Circle",
		addresses=[0x266b7c8],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(400,nature_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(400,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Yanmamon Triangle",
		addresses=[0x266b7e4],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(250,nature_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(250,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Yanmamon Cross",
		addresses=[0x266b800],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(170,nature_special_modifier,champion_modifier,1),
		max_value=Max_Cross_Multiplier(170,nature_special_modifier,champion_modifier,1),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Yanmamon Cross Effect",
		addresses=[0x266b88c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#J-Mojyamon 095
	Attribute(
		name="J-Mojyamon Element",
		addresses=[0x266B8FE],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 2, 95),
		max_value=Get_Element_Type(32, 2, 95),
		is_little_endian=True, ),
	Attribute(
		name="J-Mojyamon +DP",
		addresses=[0x266b900],
		number_of_bytes=2,
		possible_values=Thirty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="J-Mojyamon HP",
		addresses=[0x266b902],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(750,nature_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(750,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="J-Mojyamon Circle",
		addresses=[0x266b904],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(280,nature_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(280,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="J-Mojyamon Triangle",
		addresses=[0x266b920],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(250,nature_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(250,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="J-Mojyamon Cross",
		addresses=[0x266b93c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(180,nature_special_modifier,champion_modifier,0),
		max_value=Max_Cross_Multiplier(180,nature_special_modifier,champion_modifier,0),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="J-Mojyamon Cross Effect",
		addresses=[0x266b9c8],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#MoriShellmon 096
	Attribute(
		name="MoriShellmon Element",
		addresses=[0x266ba3a],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 2, 96),
		max_value=Get_Element_Type(32, 2, 96),
		is_little_endian=True, ),
	Attribute(
		name="MoriShellmon +DP",
		addresses=[0x266ba3c],
		number_of_bytes=2,
		possible_values=Thirty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="MoriShellmon HP",
		addresses=[0x266ba3e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(910,nature_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(910,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MoriShellmon Circle",
		addresses=[0x266ba40],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(390,nature_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(390,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MoriShellmon Triangle",
		addresses=[0x266ba5c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(240,nature_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(240,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MoriShellmon Cross",
		addresses=[0x266ba78],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(190,nature_special_modifier,champion_modifier,2),
		max_value=Max_Cross_Multiplier(190,nature_special_modifier,champion_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MoriShellmon Cross Effect",
		addresses=[0x266bb04],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Tentomon 097
	Attribute(
		name="Tentomon Element",
		addresses=[0x266BB76],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 0, 97),
		max_value=Get_Element_Type(32, 0, 97),
		is_little_endian=True, ),
	Attribute(
		name="Tentomon +DP",
		addresses=[0x266BB78],
		number_of_bytes=2,
		possible_values=Thirty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Tentomon HP",
		addresses=[0x266BB7A],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(670,nature_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(670,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tentomon Circle",
		addresses=[0x266BB7C],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(380,nature_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(380,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tentomon Triangle",
		addresses=[0x266BCC8],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(220,nature_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(220,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tentomon Cross",
		addresses=[0x266BCE4],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(160,nature_special_modifier,rookie_modifier,2),
		max_value=Max_Cross_Multiplier(160,nature_special_modifier,rookie_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tentomon Cross Effect",
		addresses=[0x266BD70],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Palmon 098
	Attribute(
		name="Palmon Element",
		addresses=[0x266bde2],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 0, 98),
		max_value=Get_Element_Type(32, 0, 98),
		is_little_endian=True, ),
	Attribute(
		name="Palmon +DP",
		addresses=[0x266bde4],
		number_of_bytes=2,
		possible_values=Thirty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Palmon HP",
		addresses=[0x266bde6],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(500,nature_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(500,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Palmon Circle",
		addresses=[0x266bde8],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(370,nature_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(370,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Palmon Triangle",
		addresses=[0x266be04],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(240,nature_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(240,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Palmon Cross",
		addresses=[0x266be20],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(160,nature_special_modifier,rookie_modifier,9),
		max_value=Max_Cross_Multiplier(160,nature_special_modifier,rookie_modifier,9),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Palmon Cross Effect",
		addresses=[0x266beac],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Salamon 099
	Attribute(
		name="Salamon Element",
		addresses=[0x266bf1e],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 0, 99),
		max_value=Get_Element_Type(32, 0, 99),
		is_little_endian=True, ),
	Attribute(
		name="Salamon +DP",
		addresses=[0x266bf20],
		number_of_bytes=2,
		possible_values=Thirty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Salamon HP",
		addresses=[0x266bf22],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(600,nature_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(600,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Salamon Circle",
		addresses=[0x266bf24],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(300,nature_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(300,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Salamon Triangle",
		addresses=[0x266bf40],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(230,nature_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(230,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Salamon Cross",
		addresses=[0x266bf5c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,nature_special_modifier,rookie_modifier,6),
		max_value=Max_Cross_Multiplier(0,nature_special_modifier,rookie_modifier,6),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Salamon Cross Effect",
		addresses=[0x266bfe8],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Elecmon 100
	Attribute(
		name="Elecmon Element",
		addresses=[0x266c05a],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 0, 100),
		max_value=Get_Element_Type(32, 0, 100),
		is_little_endian=True, ),
	Attribute(
		name="Elecmon +DP",
		addresses=[0x266c05c],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Elecmon HP",
		addresses=[0x266c05e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(650,nature_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(650,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Elecmon Circle",
		addresses=[0x266c060],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(310,nature_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(310,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Elecmon Triangle",
		addresses=[0x266c07c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(240,nature_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(240,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Elecmon Cross",
		addresses=[0x266c098],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(130,nature_special_modifier,rookie_modifier,12),
		max_value=Max_Cross_Multiplier(130,nature_special_modifier,rookie_modifier,12),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Elecmon Cross Effect",
		addresses=[0x266c124],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Gotsumon 101
	Attribute(
		name="Gotsumon Element",
		addresses=[0x266c196],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 0, 101),
		max_value=Get_Element_Type(32, 0, 101),
		is_little_endian=True, ),
	Attribute(
		name="Gotsumon +DP",
		addresses=[0x266c198],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Gotsumon HP",
		addresses=[0x266c19a],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(700,nature_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(700,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gotsumon Circle",
		addresses=[0x266c19c],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(290,nature_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(290,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gotsumon Triangle",
		addresses=[0x266c1b8],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(180,nature_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(180,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gotsumon Cross",
		addresses=[0x266c1d4],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(130,nature_special_modifier,rookie_modifier,4),
		max_value=Max_Cross_Multiplier(130,nature_special_modifier,rookie_modifier,4),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gotsumon Cross Effect",
		addresses=[0x266c260],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Kunemon 102
	Attribute(
		name="Kunemon Element",
		addresses=[0x266c2d2],
		number_of_bytes=1,
		min_value=Get_Element_Type(32, 0, 102),
		max_value=Get_Element_Type(32, 0, 102),
		is_little_endian=True, ),
	Attribute(
		name="Kunemon +DP",
		addresses=[0x266c2d4],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Kunemon HP",
		addresses=[0x266c2d6],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(680,nature_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(680,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Kunemon Circle",
		addresses=[0x266c2d8],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(350,nature_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(350,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Kunemon Triangle",
		addresses=[0x266c2f4],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(220,nature_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(220,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Kunemon Cross",
		addresses=[0x266c310],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(190,nature_special_modifier,rookie_modifier,10),
		max_value=Max_Cross_Multiplier(190,nature_special_modifier,rookie_modifier,10),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Kunemon Cross Effect",
		addresses=[0x266c39c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Apokarimon 103
	Attribute(
		name="Apokarimon Element",
		addresses=[0x266C40e],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 3, 103),
		max_value=Get_Element_Type(48, 3, 103),
		is_little_endian=True, ),
	Attribute(
		name="Apokarimon +DP",
		addresses=[0x266C410],
		number_of_bytes=2,
		possible_values=Zero_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Apokarimon HP",
		addresses=[0x266C412],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2750,darkness_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(2750,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Apokarimon Circle",
		addresses=[0x266C414],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(990,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(990,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Apokarimon Triangle",
		addresses=[0x266C430],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(680,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(680,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Apokarimon Cross",
		addresses=[0x266C44c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,darkness_special_modifier,ultimate_modifier,8),
		max_value=Max_Cross_Multiplier(0,darkness_special_modifier,ultimate_modifier,8),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Apokarimon Cross Effect",
		addresses=[0x266C608],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#GranKuwagamon 104
	Attribute(
		name="GranKuwagamon Element",
		addresses=[0x266c67a],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 3, 104),
		max_value=Get_Element_Type(48, 3, 104),
		is_little_endian=True, ),
	Attribute(
		name="GranKuwagamon +DP",
		addresses=[0x266c67c],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="GranKuwagamon HP",
		addresses=[0x266c67e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1760,darkness_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1760,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="GranKuwagamon Circle",
		addresses=[0x266c680],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(800,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(800,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="GranKuwagamon Triangle",
		addresses=[0x266c69c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(700,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(700,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="GranKuwagamon Cross",
		addresses=[0x266c6b8],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(600,darkness_special_modifier,ultimate_modifier,0),
		max_value=Max_Cross_Multiplier(600,darkness_special_modifier,ultimate_modifier,0),
		min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="GranKuwagamon Cross Effect",
		addresses=[0x266c744],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Diaboromon 105
	Attribute(
		name="Diaboromon Element",
		addresses=[0x266C7B6],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 3, 105),
		max_value=Get_Element_Type(48, 3, 105),
		is_little_endian=True, ),
	Attribute(
		name="Diaboromon +DP",
		addresses=[0x266C7B8],
		number_of_bytes=2,
		possible_values=Zero_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Diaboromon HP",
		addresses=[0x266C7BA],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2580,darkness_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(2580,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Diaboromon Circle",
		addresses=[0x266C7BC],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(970,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(970,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Diaboromon Triangle",
		addresses=[0x266C7D8],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(720,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(720,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Diaboromon Cross",
		addresses=[0x266c7f4],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,darkness_special_modifier,ultimate_modifier,8),
		max_value=Max_Cross_Multiplier(0,darkness_special_modifier,ultimate_modifier,8),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Diaboromon Cross Effect",
		addresses=[0x266C880],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#VenomMyotismon 106
	Attribute(
		name="VenomMyotismon Element",
		addresses=[0x266c8f2],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 3, 106),
		max_value=Get_Element_Type(48, 3, 106),
		is_little_endian=True, ),
	Attribute(
		name="VenomMyotismon +DP",
		addresses=[0x266c8f4],
		number_of_bytes=2,
		possible_values=Zero_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="VenomMyotismon HP",
		addresses=[0x266c8f6],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2310,darkness_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(2310,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="VenomMyotismon Circle",
		addresses=[0x266c8f8],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(920,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(920,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="VenomMyotismon Triangle",
		addresses=[0x266c914],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(530,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(530,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="VenomMyotismon Cross",
		addresses=[0x266c930],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(400,darkness_special_modifier,ultimate_modifier,13),
		max_value=Max_Cross_Multiplier(400,darkness_special_modifier,ultimate_modifier,13),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="VenomMyotismon Cross Effect",
		addresses=[0x266c9bc],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Piedmon 107
	Attribute(
		name="Piedmon Element",
		addresses=[0x266ca2e],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 3, 107),
		max_value=Get_Element_Type(48, 3, 107),
		is_little_endian=True, ),
	Attribute(
		name="Piedmon +DP",
		addresses=[0x266ca30],
		number_of_bytes=2,
		possible_values=Zero_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Piedmon HP",
		addresses=[0x266ca32],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1650,darkness_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1650,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Piedmon Circle",
		addresses=[0x266ca34],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(800,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(800,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Piedmon Triangle",
		addresses=[0x266ca50],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(500,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(500,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Piedmon Cross",
		addresses=[0x266ca6c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(400,darkness_special_modifier,ultimate_modifier,10),
		max_value=Max_Cross_Multiplier(400,darkness_special_modifier,ultimate_modifier,10),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Piedmon Cross Effect",
		addresses=[0x266caf8],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Machinedramon 108
	Attribute(
		name="Machinedramon Element",
		addresses=[0x266cb6a],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 3, 108),
		max_value=Get_Element_Type(48, 3, 108),
		is_little_endian=True, ),
	Attribute(
		name="Machinedramon +DP",
		addresses=[0x266cb6c],
		number_of_bytes=2,
		possible_values=Zero_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Machinedramon HP",
		addresses=[0x266cb6e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2400,darkness_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(2400,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Machinedramon Circle",
		addresses=[0x266cb70],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(980,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(980,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Machinedramon Triangle",
		addresses=[0x266cb8c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(520,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(520,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Machinedramon Cross",
		addresses=[0x266cba8],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,darkness_special_modifier,ultimate_modifier,8),
		max_value=Max_Cross_Multiplier(0,darkness_special_modifier,ultimate_modifier,8),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Machinedramon Cross Effect",
		addresses=[0x266cc34],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Infermon 109
	Attribute(
		name="Infermon Element",
		addresses=[0x266cca6],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 3, 109),
		max_value=Get_Element_Type(48, 3, 109),
		is_little_endian=True, ),
	Attribute(
		name="Infermon +DP",
		addresses=[0x266cca8],
		number_of_bytes=2,
		possible_values=Zero_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Infermon HP",
		addresses=[0x266ccaa],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1100,darkness_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1100,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Infermon Circle",
		addresses=[0x266ccac],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(610,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(610,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Infermon Triangle",
		addresses=[0x266ccc8],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(370,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(370,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Infermon Cross",
		addresses=[0x266cce4],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(180,darkness_special_modifier,ultimate_modifier,10),
		max_value=Max_Cross_Multiplier(180,darkness_special_modifier,ultimate_modifier,10),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Infermon Cross Effect",
		addresses=[0x266cd70],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#LadyDevimon 110
	Attribute(
		name="LadyDevimon Element",
		addresses=[0x266cde2],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 3, 110),
		max_value=Get_Element_Type(48, 3, 110),
		is_little_endian=True, ),
	Attribute(
		name="LadyDevimon +DP",
		addresses=[0x266cde4],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="LadyDevimon HP",
		addresses=[0x266cde6],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1150,darkness_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1150,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="LadyDevimon Circle",
		addresses=[0x266cde8],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(620,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(620,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="LadyDevimon Triangle",
		addresses=[0x266CF34],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(360,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(360,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="LadyDevimon Cross",
		addresses=[0x266CF50],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(250,darkness_special_modifier,ultimate_modifier,9),
		max_value=Max_Cross_Multiplier(250,darkness_special_modifier,ultimate_modifier,9),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="LadyDevimon Cross Effect",
		addresses=[0x266CFDC],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Myotismon 111
	Attribute(
		name="Myotismon Element",
		addresses=[0x266d04e],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 3, 111),
		max_value=Get_Element_Type(48, 3, 111),
		is_little_endian=True, ),
	Attribute(
		name="Myotismon +DP",
		addresses=[0x266d050],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Myotismon HP",
		addresses=[0x266d052],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1100,darkness_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1100,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Myotismon Circle",
		addresses=[0x266d054],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(650,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(650,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Myotismon Triangle",
		addresses=[0x266d070],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(400,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(400,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Myotismon Cross",
		addresses=[0x266d08c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(300,darkness_special_modifier,ultimate_modifier,9),
		max_value=Max_Cross_Multiplier(300,darkness_special_modifier,ultimate_modifier,9),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Myotismon Cross Effect",
		addresses=[0x266d118],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Megadramon 112
	Attribute(
		name="Megadramon Element",
		addresses=[0x266d18a],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 3, 112),
		max_value=Get_Element_Type(48, 3, 112),
		is_little_endian=True, ),
	Attribute(
		name="Megadramon +DP",
		addresses=[0x266d18c],
		number_of_bytes=2,
		possible_values=Zero_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Megadramon HP",
		addresses=[0x266d18e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1810,darkness_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1810,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Megadramon Circle",
		addresses=[0x266d190],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(920,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(920,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Megadramon Triangle",
		addresses=[0x266d1ac],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(290,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(290,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Megadramon Cross",
		addresses=[0x266D1C8],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(300,darkness_special_modifier,ultimate_modifier,1),
		max_value=Max_Cross_Multiplier(300,darkness_special_modifier,ultimate_modifier,1),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Megadramon Cross Effect",
		addresses=[0x266d254],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#SkullGreymon 113
	Attribute(
		name="SkullGreymon Element",
		addresses=[0x266d2c6],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 3, 113),
		max_value=Get_Element_Type(48, 3, 113),
		is_little_endian=True, ),
	Attribute(
		name="SkullGreymon +DP",
		addresses=[0x266d2c8],
		number_of_bytes=2,
		possible_values=Zero_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="SkullGreymon HP",
		addresses=[0x266d2ca],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1700,darkness_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1700,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="SkullGreymon Circle",
		addresses=[0x266d2cc],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(960,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(960,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="SkullGreymon Triangle",
		addresses=[0x266d2e8],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(350,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(350,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="SkullGreymon Cross",
		addresses=[0x266d304],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(450,darkness_special_modifier,ultimate_modifier,13),
		max_value=Max_Cross_Multiplier(450,darkness_special_modifier,ultimate_modifier,13),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="SkullGreymon Cross Effect",
		addresses=[0x266d390],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Phantomon 114
	Attribute(
		name="Phantomon Element",
		addresses=[0x266d402],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 3, 114),
		max_value=Get_Element_Type(48, 3, 114),
		is_little_endian=True, ),
	Attribute(
		name="Phantomon +DP",
		addresses=[0x266d404],
		number_of_bytes=2,
		possible_values=Zero_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Phantomon HP",
		addresses=[0x266d406],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1100,darkness_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1100,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Phantomon Circle",
		addresses=[0x266d408],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(600,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(600,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Phantomon Triangle",
		addresses=[0x266d424],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(400,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(400,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Phantomon Cross",
		addresses=[0x266d440],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(300,darkness_special_modifier,ultimate_modifier,9),
		max_value=Max_Cross_Multiplier(300,darkness_special_modifier,ultimate_modifier,9),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Phantomon Cross Effect",
		addresses=[0x266d4cc],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#WaruMonzaemon 115
	Attribute(
		name="WaruMonzaemon Element",
		addresses=[0x266d53e],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 3, 115),
		max_value=Get_Element_Type(48, 3, 115),
		is_little_endian=True, ),
	Attribute(
		name="WaruMonzaemon +DP",
		addresses=[0x266d540],
		number_of_bytes=2,
		possible_values=Zero_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="WaruMonzaemon HP",
		addresses=[0x266d542],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1590,darkness_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1590,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="WaruMonzaemon Circle",
		addresses=[0x266d544],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(700,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(700,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="WaruMonzaemon Triangle",
		addresses=[0x266d560],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(440,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(440,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="WaruMonzaemon Cross",
		addresses=[0x266d57c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(200,darkness_special_modifier,ultimate_modifier,10),
		max_value=Max_Cross_Multiplier(200,darkness_special_modifier,ultimate_modifier,10),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="WaruMonzaemon Cross Effect",
		addresses=[0x266d608],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Andromon 116
	Attribute(
		name="Andromon Element",
		addresses=[0x266d67a],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 3, 116),
		max_value=Get_Element_Type(48, 3, 116),
		is_little_endian=True, ),
	Attribute(
		name="Andromon +DP",
		addresses=[0x266d67c],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Andromon HP",
		addresses=[0x266d67e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1700,darkness_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1700,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Andromon Circle",
		addresses=[0x266d680],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(690,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(690,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Andromon Triangle",
		addresses=[0x266d69c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(590,darkness_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(590,darkness_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Andromon Cross",
		addresses=[0x266d6b8],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(150,darkness_special_modifier,ultimate_modifier,0),
		max_value=Max_Cross_Multiplier(150,darkness_special_modifier,ultimate_modifier,0),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Andromon Cross Effect",
		addresses=[0x266d744],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Stingmon 117
	Attribute(
		name="Stingmon Element",
		addresses=[0x266d8e6],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 2, 117),
		max_value=Get_Element_Type(48, 2, 117),
		is_little_endian=True, ),
	Attribute(
		name="Stingmon +DP",
		addresses=[0x266d8e8],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Stingmon HP",
		addresses=[0x266d8ea],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(880,darkness_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(880,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Stingmon Circle",
		addresses=[0x266d8ec],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(530,darkness_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(530,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Stingmon Triangle",
		addresses=[0x266d908],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(370,darkness_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(370,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Stingmon Cross",
		addresses=[0x266d924],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(270,darkness_special_modifier,champion_modifier,9),
		max_value=Max_Cross_Multiplier(270,darkness_special_modifier,champion_modifier,9),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Stingmon Cross Effect",
		addresses=[0x266d9b0],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Wizardmon 118
	Attribute(
		name="Wizardmon Element",
		addresses=[0x266da22],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 2, 118),
		max_value=Get_Element_Type(48, 2, 118),
		is_little_endian=True, ),
	Attribute(
		name="Wizardmon +DP",
		addresses=[0x266da24],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Wizardmon HP",
		addresses=[0x266da26],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(850,darkness_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(850,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Wizardmon Circle",
		addresses=[0x266da28],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(540,darkness_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(540,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Wizardmon Triangle",
		addresses=[0x266da44],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(370,darkness_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(370,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Wizardmon Cross",
		addresses=[0x266da60],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(220,darkness_special_modifier,champion_modifier,10),
		max_value=Max_Cross_Multiplier(220,darkness_special_modifier,champion_modifier,10),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Wizardmon Cross Effect",
		addresses=[0x266daec],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Devidramon 119
	Attribute(
		name="Devidramon Element",
		addresses=[0x266db5e],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 2, 119),
		max_value=Get_Element_Type(48, 2, 119),
		is_little_endian=True, ),
	Attribute(
		name="Devidramon +DP",
		addresses=[0x266db60],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Devidramon HP",
		addresses=[0x266db62],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1100,darkness_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(1100,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Devidramon Circle",
		addresses=[0x266db64],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(520,darkness_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(520,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Devidramon Triangle",
		addresses=[0x266db80],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(440,darkness_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(440,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Devidramon Cross",
		addresses=[0x266db9c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(370,darkness_special_modifier,champion_modifier,0),
		max_value=Max_Cross_Multiplier(370,darkness_special_modifier,champion_modifier,0),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Devidramon Cross Effect",
		addresses=[0x266dc28],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Devimon 120
	Attribute(
		name="Devimon Element",
		addresses=[0x266dc9a],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 2, 120),
		max_value=Get_Element_Type(48, 2, 120),
		is_little_endian=True, ),
	Attribute(
		name="Devimon +DP",
		addresses=[0x266dc9c],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Devimon HP",
		addresses=[0x266dc9e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(960,darkness_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(960,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Devimon Circle",
		addresses=[0x266dca0],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(490,darkness_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(490,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Devimon Triangle",
		addresses=[0x266dcbc],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(350,darkness_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(350,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Devimon Cross",
		addresses=[0x266dcd8],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(250,darkness_special_modifier,champion_modifier,13),
		max_value=Max_Cross_Multiplier(250,darkness_special_modifier,champion_modifier,13),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Devimon Cross Effect",
		addresses=[0x266dd64],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Tuskmon 121
	Attribute(
		name="Tuskmon Element",
		addresses=[0x266ddd6],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 2, 121),
		max_value=Get_Element_Type(48, 2, 121),
		is_little_endian=True, ),
	Attribute(
		name="Tuskmon +DP",
		addresses=[0x266ddd8],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Tuskmon HP",
		addresses=[0x266ddda],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1150,darkness_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(1150,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tuskmon Circle",
		addresses=[0x266dddc],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(410,darkness_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(410,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tuskmon Triangle",
		addresses=[0x266ddf8],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(360,darkness_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(360,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tuskmon Cross",
		addresses=[0x266de14],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(300,darkness_special_modifier,champion_modifier,0),
		max_value=Max_Cross_Multiplier(300,darkness_special_modifier,champion_modifier,0),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tuskmon Cross Effect",
		addresses=[0x266dea0],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Ogremon 122
	Attribute(
		name="Ogremon Element",
		addresses=[0x266df12],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 2, 122),
		max_value=Get_Element_Type(48, 2, 122),
		is_little_endian=True, ),
	Attribute(
		name="Ogremon +DP",
		addresses=[0x266df14],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Ogremon HP",
		addresses=[0x266df16],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1050,darkness_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(1050,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Ogremon Circle",
		addresses=[0x266df18],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(530,darkness_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(530,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Ogremon Triangle",
		addresses=[0x266df34],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(320,darkness_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(320,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Ogremon Cross",
		addresses=[0x266df50],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,darkness_special_modifier,champion_modifier,6),
		max_value=Max_Cross_Multiplier(0,darkness_special_modifier,champion_modifier,6),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Ogremon Cross Effect",
		addresses=[0x266dfdc],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Bakemon 123
	Attribute(
		name="Bakemon Element",
		addresses=[0x266E04e],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 2, 123),
		max_value=Get_Element_Type(48, 2, 123),
		is_little_endian=True, ),
	Attribute(
		name="Bakemon +DP",
		addresses=[0x266E050],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Bakemon HP",
		addresses=[0x266E052],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(860,darkness_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(860,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Bakemon Circle",
		addresses=[0x266E054],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(450,darkness_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(450,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Bakemon Triangle",
		addresses=[0x266E1A0],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(270,darkness_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(270,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Bakemon Cross",
		addresses=[0x266E1BC],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(170,darkness_special_modifier,champion_modifier,9),
		max_value=Max_Cross_Multiplier(170,darkness_special_modifier,champion_modifier,9),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Bakemon Cross Effect",
		addresses=[0x266E248],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Guardromon 124
	Attribute(
		name="Guardromon Element",
		addresses=[0x266e2ba],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 2, 124),
		max_value=Get_Element_Type(48, 2, 124),
		is_little_endian=True, ),
	Attribute(
		name="Guardromon +DP",
		addresses=[0x266e2bc],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Guardromon HP",
		addresses=[0x266e2be],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(750,darkness_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(750,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Guardromon Circle",
		addresses=[0x266e2c0],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(430,darkness_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(430,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Guardromon Triangle",
		addresses=[0x266e2dc],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(200,darkness_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(200,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Guardromon Cross",
		addresses=[0x266e2f8],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,darkness_special_modifier,champion_modifier,8),
		max_value=Max_Cross_Multiplier(0,darkness_special_modifier,champion_modifier,8),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Guardromon Cross Effect",
		addresses=[0x266e384],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Tekkamon 125
	Attribute(
		name="Tekkamon Element",
		addresses=[0x266e3f6],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 2, 125),
		max_value=Get_Element_Type(48, 2, 125),
		is_little_endian=True, ),
	Attribute(
		name="Tekkamon +DP",
		addresses=[0x266e3f8],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Tekkamon HP",
		addresses=[0x266e3fa],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1100,darkness_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(1100,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tekkamon Circle",
		addresses=[0x266e3fc],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(350,darkness_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(350,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tekkamon Triangle",
		addresses=[0x266e418],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(200,darkness_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(200,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tekkamon Cross",
		addresses=[0x266e434],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,darkness_special_modifier,champion_modifier,8),
		max_value=Max_Cross_Multiplier(0,darkness_special_modifier,champion_modifier,8),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tekkamon Cross Effect",
		addresses=[0x266e4c0],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Gururumon 126
	Attribute(
		name="Gururumon Element",
		addresses=[0x266e532],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 2, 126),
		max_value=Get_Element_Type(48, 2, 126),
		is_little_endian=True, ),
	Attribute(
		name="Gururumon +DP",
		addresses=[0x266e534],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Gururumon HP",
		addresses=[0x266e536],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1040,darkness_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(1040,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gururumon Circle",
		addresses=[0x266e538],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(470,darkness_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(470,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gururumon Triangle",
		addresses=[0x266e554],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(340,darkness_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(340,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gururumon Cross",
		addresses=[0x266e570],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(100,darkness_special_modifier,champion_modifier,2),
		max_value=Max_Cross_Multiplier(100,darkness_special_modifier,champion_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gururumon Cross Effect",
		addresses=[0x266e5fc],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Soulmon 127
	Attribute(
		name="Soulmon Element",
		addresses=[0x266e66e],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 2, 127),
		max_value=Get_Element_Type(48, 2, 127),
		is_little_endian=True, ),
	Attribute(
		name="Soulmon +DP",
		addresses=[0x266e670],
		number_of_bytes=2,
		possible_values=Zero_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Soulmon HP",
		addresses=[0x266e672],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(500,darkness_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(500,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Soulmon Circle",
		addresses=[0x266e674],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(330,darkness_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(330,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Soulmon Triangle",
		addresses=[0x266e690],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(310,darkness_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(310,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Soulmon Cross",
		addresses=[0x266e6ac],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(290,darkness_special_modifier,champion_modifier,9),
		max_value=Max_Cross_Multiplier(290,darkness_special_modifier,champion_modifier,9),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Soulmon Cross Effect",
		addresses=[0x266e738],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Fugamon 128
	Attribute(
		name="Fugamon Element",
		addresses=[0x266e7aa],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 2, 128),
		max_value=Get_Element_Type(48, 2, 128),
		is_little_endian=True, ),
	Attribute(
		name="Fugamon +DP",
		addresses=[0x266e7ac],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Fugamon HP",
		addresses=[0x266e7ae],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(940,darkness_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(940,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Fugamon Circle",
		addresses=[0x266e7b0],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(460,darkness_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(460,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Fugamon Triangle",
		addresses=[0x266e7cc],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(430,darkness_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(430,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Fugamon Cross",
		addresses=[0x266e7e8],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(400,darkness_special_modifier,champion_modifier,0),
		max_value=Max_Cross_Multiplier(400,darkness_special_modifier,champion_modifier,0),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Fugamon Cross Effect",
		addresses=[0x266e874],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Saberdramon 129
	Attribute(
		name="Saberdramon Element",
		addresses=[0x266E8E6],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 2, 129),
		max_value=Get_Element_Type(48, 2, 129),
		is_little_endian=True, ),
	Attribute(
		name="Saberdramon +DP",
		addresses=[0x266E8E8],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Saberdramon HP",
		addresses=[0x266E8EA],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(670,darkness_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(670,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Saberdramon Circle",
		addresses=[0x266E8EC],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(400,darkness_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(400,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Saberdramon Triangle",
		addresses=[0x266E908],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(150,darkness_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(150,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Saberdramon Cross",
		addresses=[0x266E924],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(240,darkness_special_modifier,champion_modifier,1),
		max_value=Max_Cross_Multiplier(240,darkness_special_modifier,champion_modifier,1),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Saberdramon Cross Effect",
		addresses=[0x266EAE0],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Darkrizamon 130
	Attribute(
		name="Darkrizamon Element",
		addresses=[0x266eb52],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 2, 130),
		max_value=Get_Element_Type(48, 2, 130),
		is_little_endian=True, ),
	Attribute(
		name="Darkrizamon +DP",
		addresses=[0x266eb54],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Darkrizamon HP",
		addresses=[0x266eb56],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(890,darkness_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(890,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Darkrizamon Circle",
		addresses=[0x266eb58],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(330,darkness_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(330,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Darkrizamon Triangle",
		addresses=[0x266eb74],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(440,darkness_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(440,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Darkrizamon Cross",
		addresses=[0x266eb90],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(30,darkness_special_modifier,champion_modifier,2),
		max_value=Max_Cross_Multiplier(30,darkness_special_modifier,champion_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Darkrizamon Cross Effect",
		addresses=[0x266ec1c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Zassomon 131
	Attribute(
		name="Zassomon Element",
		addresses=[0x266ec8e],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 2, 131),
		max_value=Get_Element_Type(48, 2, 131),
		is_little_endian=True, ),
	Attribute(
		name="Zassomon +DP",
		addresses=[0x266ec90],
		number_of_bytes=2,
		possible_values=Zero_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Zassomon HP",
		addresses=[0x266ec92],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(600,darkness_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(600,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Zassomon Circle",
		addresses=[0x266ec94],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(480,darkness_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(480,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Zassomon Triangle",
		addresses=[0x266ecb0],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(410,darkness_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(410,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Zassomon Cross",
		addresses=[0x266eccc],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(350,darkness_special_modifier,champion_modifier,0),
		max_value=Max_Cross_Multiplier(350,darkness_special_modifier,champion_modifier,0),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Zassomon Cross Effect",
		addresses=[0x266ED58],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#DemiDevimon 132
	Attribute(
		name="DemiDevimon Element",
		addresses=[0x266edca],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 0, 132),
		max_value=Get_Element_Type(48, 0, 132),
		is_little_endian=True, ),
	Attribute(
		name="DemiDevimon +DP",
		addresses=[0x266edcc],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="DemiDevimon HP",
		addresses=[0x266edce],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(490,darkness_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(490,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="DemiDevimon Circle",
		addresses=[0x266edd0],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(360,darkness_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(360,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="DemiDevimon Triangle",
		addresses=[0x266edec],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(200,darkness_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(200,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="DemiDevimon Cross",
		addresses=[0x266ee08],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(190,darkness_special_modifier,rookie_modifier,13),
		max_value=Max_Cross_Multiplier(190,darkness_special_modifier,rookie_modifier,13),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="DemiDevimon Cross Effect",
		addresses=[0x266ee94],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#BKGatomon 133
	Attribute(
		name="BKGatomon Element",
		addresses=[0x266ef06],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 0, 133),
		max_value=Get_Element_Type(48, 0, 133),
		is_little_endian=True, ),
	Attribute(
		name="BKGatomon +DP",
		addresses=[0x266ef08],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="BKGatomon HP",
		addresses=[0x266ef0a],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(520,darkness_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(520,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="BKGatomon Circle",
		addresses=[0x266ef0c],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(360,darkness_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(360,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="BKGatomon Triangle",
		addresses=[0x266ef28],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(300,darkness_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(300,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="BKGatomon Cross",
		addresses=[0x266ef44],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(240,darkness_special_modifier,rookie_modifier,4),
		max_value=Max_Cross_Multiplier(240,darkness_special_modifier,rookie_modifier,4),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="BKGatomon Cross Effect",
		addresses=[0x266efd0],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Kokuwamon 134
	Attribute(
		name="Kokuwamon Element",
		addresses=[0x266f042],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 0, 134),
		max_value=Get_Element_Type(48, 0, 134),
		is_little_endian=True, ),
	Attribute(
		name="Kokuwamon +DP",
		addresses=[0x266f044],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Kokuwamon HP",
		addresses=[0x266f046],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(670,darkness_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(670,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Kokuwamon Circle",
		addresses=[0x266f048],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(270,darkness_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(270,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Kokuwamon Triangle",
		addresses=[0x266f064],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(240,darkness_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(240,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Kokuwamon Cross",
		addresses=[0x266F07A],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(200,darkness_special_modifier,rookie_modifier,3),
		max_value=Max_Cross_Multiplier(200,darkness_special_modifier,rookie_modifier,3),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Kokuwamon Cross Effect",
		addresses=[0x266f10c],
		number_of_bytes=1,
		possible_values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
		is_little_endian=True, ),
#Tsukaimon 135
	Attribute(
		name="Tsukaimon Element",
		addresses=[0x266f17e],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 0, 135),
		max_value=Get_Element_Type(48, 0, 135),
		is_little_endian=True, ),
	Attribute(
		name="Tsukaimon +DP",
		addresses=[0x266f180],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Tsukaimon HP",
		addresses=[0x266f182],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(630,darkness_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(630,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tsukaimon Circle",
		addresses=[0x266f184],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(240,darkness_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(240,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tsukaimon Triangle",
		addresses=[0x266f1a0],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(200,darkness_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(200,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tsukaimon Cross",
		addresses=[0x266f1bc],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(160,darkness_special_modifier,rookie_modifier,2),
		max_value=Max_Cross_Multiplier(160,darkness_special_modifier,rookie_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tsukaimon Cross Effect",
		addresses=[0x266f248],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Dokunemon 136
	Attribute(
		name="Dokunemon Element",
		addresses=[0x266f3ea],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 0, 136),
		max_value=Get_Element_Type(48, 0, 136),
		is_little_endian=True, ),
	Attribute(
		name="Dokunemon +DP",
		addresses=[0x266f3ec],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Dokunemon HP",
		addresses=[0x266f3ee],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(650,darkness_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(650,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Dokunemon Circle",
		addresses=[0x266f3f0],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(280,darkness_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(280,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Dokunemon Triangle",
		addresses=[0x266f40c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(220,darkness_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(220,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Dokunemon Cross",
		addresses=[0x266f428],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(190,darkness_special_modifier,rookie_modifier,15),
		max_value=Max_Cross_Multiplier(190,darkness_special_modifier,rookie_modifier,15),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Dokunemon Cross Effect",
		addresses=[0x266f4b4],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Aruraumon 137
	Attribute(
		name="Aruraumon Element",
		addresses=[0x266f526],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 0, 137),
		max_value=Get_Element_Type(48, 0, 137),
		is_little_endian=True, ),
	Attribute(
		name="Aruraumon +DP",
		addresses=[0x266f528],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Aruraumon HP",
		addresses=[0x266f52a],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(420,darkness_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(420,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Aruraumon Circle",
		addresses=[0x266f52c],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(340,darkness_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(340,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Aruraumon Triangle",
		addresses=[0x266f548],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(240,darkness_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(240,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Aruraumon Cross",
		addresses=[0x266f564],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(190,darkness_special_modifier,rookie_modifier,9),
		max_value=Max_Cross_Multiplier(190,darkness_special_modifier,rookie_modifier,9),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Aruraumon Cross Effect",
		addresses=[0x266f5f0],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Sharmamon 138
	Attribute(
		name="Sharmamon Element",
		addresses=[0x266f662],
		number_of_bytes=1,
		min_value=Get_Element_Type(48, 0, 138),
		max_value=Get_Element_Type(48, 0, 138),
		is_little_endian=True, ),
	Attribute(
		name="Sharmamon +DP",
		addresses=[0x266f664],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Sharmamon HP",
		addresses=[0x266f666],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(570,darkness_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(570,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Sharmamon Circle",
		addresses=[0x266f668],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(350,darkness_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(350,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Sharmamon Triangle",
		addresses=[0x266f684],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(220,darkness_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(220,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Sharmamon Cross",
		addresses=[0x266f6a0],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(100,darkness_special_modifier,rookie_modifier,10),
		max_value=Max_Cross_Multiplier(100,darkness_special_modifier,rookie_modifier,10),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Sharmamon Cross Effect",
		addresses=[0x266f72c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Puppetmon 139
	Attribute(
		name="Puppetmon Element",
		addresses=[0x266f79e],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 3, 139),
		max_value=Get_Element_Type(64, 3, 139),
		is_little_endian=True, ),
	Attribute(
		name="Puppetmon +DP",
		addresses=[0x266f7a0],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Puppetmon HP",
		addresses=[0x266f7a2],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1540,rare_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1540,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Puppetmon Circle",
		addresses=[0x266f7a4],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(790,rare_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(790,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Puppetmon Triangle",
		addresses=[0x266f7c0],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(570,rare_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(570,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Puppetmon Cross",
		addresses=[0x266f7dc],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(380,rare_special_modifier,ultimate_modifier,10),
		max_value=Max_Cross_Multiplier(380,rare_special_modifier,ultimate_modifier,10),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Puppetmon Cross Effect",
		addresses=[0x266f868],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#SuperStarmon 140
	Attribute(
		name="SuperStarmon Element",
		addresses=[0x266f8da],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 3, 140),
		max_value=Get_Element_Type(64, 3, 140),
		is_little_endian=True, ),
	Attribute(
		name="SuperStarmon +DP",
		addresses=[0x266f8dc],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="SuperStarmon HP",
		addresses=[0x266f8de],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1650,rare_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1650,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="SuperStarmon Circle",
		addresses=[0x266f8e0],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(730,rare_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(730,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="SuperStarmon Triangle",
		addresses=[0x266f8fc],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(600,rare_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(600,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="SuperStarmon Cross",
		addresses=[0x266f918],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(380,rare_special_modifier,ultimate_modifier,15),
		max_value=Max_Cross_Multiplier(380,rare_special_modifier,ultimate_modifier,15),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="SuperStarmon Cross Effect",
		addresses=[0x266f9a4],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#MetalEtemon 141
	Attribute(
		name="MetalEtemon Element",
		addresses=[0x266fa16],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 3, 141),
		max_value=Get_Element_Type(64, 3, 141),
		is_little_endian=True, ),
	Attribute(
		name="MetalEtemon +DP",
		addresses=[0x266fa18],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="MetalEtemon HP",
		addresses=[0x266fa1a],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1650,rare_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1650,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MetalEtemon Circle",
		addresses=[0x266fa1c],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(300,rare_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(300,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MetalEtemon Triangle",
		addresses=[0x266fa38],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(750,rare_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(750,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MetalEtemon Cross",
		addresses=[0x266fa54],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,rare_special_modifier,ultimate_modifier,5),
		max_value=Max_Cross_Multiplier(0,rare_special_modifier,ultimate_modifier,5),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MetalEtemon Cross Effect",
		addresses=[0x266fae0],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Shakkoumon 142
	Attribute(
		name="Shakkoumon Element",
		addresses=[0x266fb52],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 3, 142),
		max_value=Get_Element_Type(64, 3, 142),
		is_little_endian=True, ),
	Attribute(
		name="Shakkoumon +DP",
		addresses=[0x266fb54],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Shakkoumon HP",
		addresses=[0x266fb56],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1760,rare_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1760,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Shakkoumon Circle",
		addresses=[0x266fb58],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(680,rare_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(680,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Shakkoumon Triangle",
		addresses=[0x266fb74],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(520,rare_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(520,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Shakkoumon Cross",
		addresses=[0x266fb90],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(300,rare_special_modifier,ultimate_modifier,10),
		max_value=Max_Cross_Multiplier(300,rare_special_modifier,ultimate_modifier,10),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Shakkoumon Cross Effect",
		addresses=[0x266FD4C],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Jijimon 143
	Attribute(
		name="Jijimon Element",
		addresses=[0x266fdbe],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 3, 143),
		max_value=Get_Element_Type(64, 3, 143),
		is_little_endian=True, ),
	Attribute(
		name="Jijimon +DP",
		addresses=[0x266fdc0],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Jijimon HP",
		addresses=[0x266fdc2],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1260,rare_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1260,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Jijimon Circle",
		addresses=[0x266fdc4],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(650,rare_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(650,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Jijimon Triangle",
		addresses=[0x266fde0],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(560,rare_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(560,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Jijimon Cross",
		addresses=[0x266fdfc],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(250,rare_special_modifier,ultimate_modifier,3),
		max_value=Max_Cross_Multiplier(250,rare_special_modifier,ultimate_modifier,3),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Jijimon Cross Effect",
		addresses=[0x266fe88],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Digitamamon 144
	Attribute(
		name="Digitamamon Element",
		addresses=[0x266fefa],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 3, 144),
		max_value=Get_Element_Type(64, 3, 144),
		is_little_endian=True, ),
	Attribute(
		name="Digitamamon +DP",
		addresses=[0x266fefc],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Digitamamon HP",
		addresses=[0x266fefe],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1810,rare_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1810,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Digitamamon Circle",
		addresses=[0x266ff00],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(800,rare_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(800,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Digitamamon Triangle",
		addresses=[0x266ff1c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(540,rare_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(540,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Digitamamon Cross",
		addresses=[0x266ff38],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(300,rare_special_modifier,ultimate_modifier,2),
		max_value=Max_Cross_Multiplier(300,rare_special_modifier,ultimate_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Digitamamon Cross Effect",
		addresses=[0x266ffc4],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Vademon 145
	Attribute(
		name="Vademon Element",
		addresses=[0x2670036],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 3, 145),
		max_value=Get_Element_Type(64, 3, 145),
		is_little_endian=True, ),
	Attribute(
		name="Vademon +DP",
		addresses=[0x2670038],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Vademon HP",
		addresses=[0x267003a],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1370,rare_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1370,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Vademon Circle",
		addresses=[0x267003c],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(850,rare_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(850,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Vademon Triangle",
		addresses=[0x2670058],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(600,rare_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(600,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Vademon Cross",
		addresses=[0x2670074],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(200,rare_special_modifier,ultimate_modifier,10),
		max_value=Max_Cross_Multiplier(200,rare_special_modifier,ultimate_modifier,10),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Vademon Cross Effect",
		addresses=[0x2670100],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Giromon 146
	Attribute(
		name="Giromon Element",
		addresses=[0x2670172],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 3, 146),
		max_value=Get_Element_Type(64, 3, 146),
		is_little_endian=True, ),
	Attribute(
		name="Giromon +DP",
		addresses=[0x2670174],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Giromon HP",
		addresses=[0x2670176],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1900,rare_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1900,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Giromon Circle",
		addresses=[0x2670178],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(720,rare_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(720,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Giromon Triangle",
		addresses=[0x2670194],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(520,rare_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(520,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Giromon Cross",
		addresses=[0x26701b0],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,rare_special_modifier,ultimate_modifier,8),
		max_value=Max_Cross_Multiplier(0,rare_special_modifier,ultimate_modifier,8),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Giromon Cross Effect",
		addresses=[0x267023c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Monzaemon 147
	Attribute(
		name="Monzaemon Element",
		addresses=[0x26702ae],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 3, 147),
		max_value=Get_Element_Type(64, 3, 147),
		is_little_endian=True, ),
	Attribute(
		name="Monzaemon +DP",
		addresses=[0x26702b0],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Monzaemon HP",
		addresses=[0x26702b2],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(2030,rare_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(2030,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Monzaemon Circle",
		addresses=[0x26702b4],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(850,rare_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(850,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Monzaemon Triangle",
		addresses=[0x26702d0],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(500,rare_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(500,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Monzaemon Cross",
		addresses=[0x26702ec],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(430,rare_special_modifier,ultimate_modifier,14),
		max_value=Max_Cross_Multiplier(430,rare_special_modifier,ultimate_modifier,14),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Monzaemon Cross Effect",
		addresses=[0x2670378],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#MetalMamemon 148
	Attribute(
		name="MetalMamemon Element",
		addresses=[0x26703ea],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 3, 148),
		max_value=Get_Element_Type(64, 3, 148),
		is_little_endian=True, ),
	Attribute(
		name="MetalMamemon +DP",
		addresses=[0x26703ec],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="MetalMamemon HP",
		addresses=[0x26703ee],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1920,rare_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1920,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MetalMamemon Circle",
		addresses=[0x26703f0],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(770,rare_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(770,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MetalMamemon Triangle",
		addresses=[0x267040c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(570,rare_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(570,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MetalMamemon Cross",
		addresses=[0x2670428],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(280,rare_special_modifier,ultimate_modifier,1),
		max_value=Max_Cross_Multiplier(280,rare_special_modifier,ultimate_modifier,1),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MetalMamemon Cross Effect",
		addresses=[0x26704b4],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Mamemon 149
	Attribute(
		name="Mamemon Element",
		addresses=[0x2670656],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 3, 149),
		max_value=Get_Element_Type(64, 3, 149),
		is_little_endian=True, ),
	Attribute(
		name="Mamemon +DP",
		addresses=[0x2670658],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Mamemon HP",
		addresses=[0x267065a],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1700,rare_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1700,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Mamemon Circle",
		addresses=[0x267065c],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(820,rare_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(820,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Mamemon Triangle",
		addresses=[0x2670678],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(650,rare_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(650,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Mamemon Cross",
		addresses=[0x2670694],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,rare_special_modifier,ultimate_modifier,5),
		max_value=Max_Cross_Multiplier(0,rare_special_modifier,ultimate_modifier,5),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Mamemon Cross Effect",
		addresses=[0x2670720],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Etemon 150
	Attribute(
		name="Etemon Element",
		addresses=[0x2670792],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 3, 150),
		max_value=Get_Element_Type(64, 3, 150),
		is_little_endian=True, ),
	Attribute(
		name="Etemon +DP",
		addresses=[0x2670794],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Etemon HP",
		addresses=[0x2670796],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1480,rare_special_modifier,ultimate_modifier),
		max_value=Max_HP_Multiplier(1480,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Etemon Circle",
		addresses=[0x2670798],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(700,rare_special_modifier,ultimate_modifier),
		max_value=Max_Circle_Multiplier(700,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Etemon Triangle",
		addresses=[0x26707b4],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(530,rare_special_modifier,ultimate_modifier),
		max_value=Max_Triangle_Multiplier(530,rare_special_modifier,ultimate_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Etemon Cross",
		addresses=[0x26707d0],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(150,rare_special_modifier,ultimate_modifier,10),
		max_value=Max_Cross_Multiplier(150,rare_special_modifier,ultimate_modifier,10),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Etemon Cross Effect",
		addresses=[0x267085c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Ankylomon 151
	Attribute(
		name="Ankylomon Element",
		addresses=[0x26708ce],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 2, 151),
		max_value=Get_Element_Type(64, 2, 151),
		is_little_endian=True, ),
	Attribute(
		name="Ankylomon +DP",
		addresses=[0x26708d0],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Ankylomon HP",
		addresses=[0x26708d2],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(1000,rare_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(1000,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Ankylomon Circle",
		addresses=[0x26708d4],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(420,rare_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(420,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Ankylomon Triangle",
		addresses=[0x26708f0],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(240,rare_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(240,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Ankylomon Cross",
		addresses=[0x267090c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(120,rare_special_modifier,champion_modifier,2),
		max_value=Max_Cross_Multiplier(120,rare_special_modifier,champion_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Ankylomon Cross Effect",
		addresses=[0x2670998],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Starmon 152
	Attribute(
		name="Starmon Element",
		addresses=[0x2670a0a],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 2, 152),
		max_value=Get_Element_Type(64, 2, 152),
		is_little_endian=True, ),
	Attribute(
		name="Starmon +DP",
		addresses=[0x2670a0c],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Starmon HP",
		addresses=[0x2670a0e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(900,rare_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(900,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Starmon Circle",
		addresses=[0x2670a10],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(470,rare_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(470,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Starmon Triangle",
		addresses=[0x2670a2c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(370,rare_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(370,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Starmon Cross",
		addresses=[0x2670a48],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(230,rare_special_modifier,champion_modifier,14),
		max_value=Max_Cross_Multiplier(230,rare_special_modifier,champion_modifier,14),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Starmon Cross Effect",
		addresses=[0x2670ad4],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Thundermon 153
	Attribute(
		name="Thundermon Element",
		addresses=[0x2670b46],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 2, 153),
		max_value=Get_Element_Type(64, 2, 153),
		is_little_endian=True, ),
	Attribute(
		name="Thundermon +DP",
		addresses=[0x2670b48],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Thundermon HP",
		addresses=[0x2670b4a],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(710,rare_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(710,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Thundermon Circle",
		addresses=[0x2670b4c],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(350,rare_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(350,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Thundermon Triangle",
		addresses=[0x2670b68],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(300,rare_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(300,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Thundermon Cross",
		addresses=[0x2670b84],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,rare_special_modifier,champion_modifier,7),
		max_value=Max_Cross_Multiplier(0,rare_special_modifier,champion_modifier,7),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Thundermon Cross Effect",
		addresses=[0x2670c10],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#PlatinumSukamon 154
	Attribute(
		name="PlatinumSukamon Element",
		addresses=[0x2670c82],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 2, 154),
		max_value=Get_Element_Type(64, 2, 154),
		is_little_endian=True, ),
	Attribute(
		name="PlatinumSukamon +DP",
		addresses=[0x2670c84],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="PlatinumSukamon HP",
		addresses=[0x2670c86],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(850,rare_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(850,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="PlatinumSukamon Circle",
		addresses=[0x2670c88],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(240,rare_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(240,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="PlatinumSukamon Triangle",
		addresses=[0x2670ca4],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(200,rare_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(200,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="PlatinumSukamon Cross",
		addresses=[0x2670cc0],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(100,rare_special_modifier,champion_modifier,2),
		max_value=Max_Cross_Multiplier(100,rare_special_modifier,champion_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="PlatinumSukamon Cross Effect",
		addresses=[0x2670d4c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#ShellNumemon 155
	Attribute(
		name="ShellNumemon Element",
		addresses=[0x2670dbe],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 2, 155),
		max_value=Get_Element_Type(64, 2, 155),
		is_little_endian=True, ),
	Attribute(
		name="ShellNumemon +DP",
		addresses=[0x2670dc0],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="ShellNumemon HP",
		addresses=[0x2670dc2],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(900,rare_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(900,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ShellNumemon Circle",
		addresses=[0x2670dc4],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(250,rare_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(250,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ShellNumemon Triangle",
		addresses=[0x2670de0],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(150,rare_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(150,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ShellNumemon Cross",
		addresses=[0x2670DFC],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(150,rare_special_modifier,champion_modifier,2),
		max_value=Max_Cross_Multiplier(150,rare_special_modifier,champion_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ShellNumemon Cross Effect",
		addresses=[0x2670FBA],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Nanimon 156
	Attribute(
		name="Nanimon Element",
		addresses=[0x267102a],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 2, 156),
		max_value=Get_Element_Type(64, 2, 156),
		is_little_endian=True, ),
	Attribute(
		name="Nanimon +DP",
		addresses=[0x267102c],
		number_of_bytes=2,
		possible_values=Zero_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Nanimon HP",
		addresses=[0x267102e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(700,rare_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(700,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Nanimon Circle",
		addresses=[0x2671030],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(390,rare_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(390,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Nanimon Triangle",
		addresses=[0x267104c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(270,rare_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(270,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Nanimon Cross",
		addresses=[0x2671068],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,rare_special_modifier,champion_modifier,7),
		max_value=Max_Cross_Multiplier(0,rare_special_modifier,champion_modifier,7),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Nanimon Cross Effect",
		addresses=[0x26710f4],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Numemon 157
	Attribute(
		name="Numemon Element",
		addresses=[0x2671166],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 2, 157),
		max_value=Get_Element_Type(64, 2, 157),
		is_little_endian=True, ),
	Attribute(
		name="Numemon +DP",
		addresses=[0x2671168],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Numemon HP",
		addresses=[0x267116a],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(700,rare_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(700,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Numemon Circle",
		addresses=[0x267116c],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(250,rare_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(250,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Numemon Triangle",
		addresses=[0x2671188],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(250,rare_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(250,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Numemon Cross",
		addresses=[0x26711a4],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(100,rare_special_modifier,champion_modifier,4),
		max_value=Max_Cross_Multiplier(100,rare_special_modifier,champion_modifier,4),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Numemon Cross Effect",
		addresses=[0x2671230],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Sukamon 158
	Attribute(
		name="Sukamon Element",
		addresses=[0x26712a2],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 2, 158),
		max_value=Get_Element_Type(64, 2, 158),
		is_little_endian=True, ),
	Attribute(
		name="Sukamon +DP",
		addresses=[0x26712a4],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Sukamon HP",
		addresses=[0x26712a6],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(600,rare_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(600,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Sukamon Circle",
		addresses=[0x26712a8],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(300,rare_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(300,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Sukamon Triangle",
		addresses=[0x26712c4],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(150,rare_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(150,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Sukamon Cross",
		addresses=[0x26712e0],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(200,rare_special_modifier,champion_modifier,10),
		max_value=Max_Cross_Multiplier(200,rare_special_modifier,champion_modifier,10),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Sukamon Cross Effect",
		addresses=[0x267136c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Rockmon 159
	Attribute(
		name="Rockmon Element",
		addresses=[0x26713de],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 2, 159),
		max_value=Get_Element_Type(64, 2, 159),
		is_little_endian=True, ),
	Attribute(
		name="Rockmon +DP",
		addresses=[0x26713e0],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Rockmon HP",
		addresses=[0x26713e2],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(700,rare_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(700,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Rockmon Circle",
		addresses=[0x26713e4],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(350,rare_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(350,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Rockmon Triangle",
		addresses=[0x2671400],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(160,rare_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(160,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Rockmon Cross",
		addresses=[0x267141c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(250,rare_special_modifier,champion_modifier,15),
		max_value=Max_Cross_Multiplier(250,rare_special_modifier,champion_modifier,15),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Rockmon Cross Effect",
		addresses=[0x26714a8],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Geremon 160
	Attribute(
		name="Geremon Element",
		addresses=[0x267151a],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 2, 160),
		max_value=Get_Element_Type(64, 2, 160),
		is_little_endian=True, ),
	Attribute(
		name="Geremon +DP",
		addresses=[0x267151c],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Geremon HP",
		addresses=[0x267151e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(690,rare_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(690,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Geremon Circle",
		addresses=[0x2671520],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(280,rare_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(280,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Geremon Triangle",
		addresses=[0x267153c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(330,rare_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(330,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Geremon Cross",
		addresses=[0x2671558],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(120,rare_special_modifier,champion_modifier,0),
		max_value=Max_Cross_Multiplier(120,rare_special_modifier,champion_modifier,0),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Geremon Cross Effect",
		addresses=[0x26715e4],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#NiseDrimogemon 161
	Attribute(
		name="NiseDrimogemon Element",
		addresses=[0x2671656],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 2, 161),
		max_value=Get_Element_Type(64, 2, 161),
		is_little_endian=True, ),
	Attribute(
		name="NiseDrimogemon +DP",
		addresses=[0x2671658],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="NiseDrimogemon HP",
		addresses=[0x267165a],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(750,rare_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(750,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="NiseDrimogemon Circle",
		addresses=[0x267165c],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(400,rare_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(400,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="NiseDrimogemon Triangle",
		addresses=[0x2671678],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(300,rare_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(300,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="NiseDrimogemon Cross",
		addresses=[0x2671694],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(220,rare_special_modifier,champion_modifier,15),
		max_value=Max_Cross_Multiplier(220,rare_special_modifier,champion_modifier,15),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="NiseDrimogemon Cross Effect",
		addresses=[0x2671720],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#ShimaUnimon 162
	Attribute(
		name="ShimaUnimon Element",
		addresses=[0x26718c2],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 2, 162),
		max_value=Get_Element_Type(64, 2, 162),
		is_little_endian=True, ),
	Attribute(
		name="ShimaUnimon +DP",
		addresses=[0x26718c4],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="ShimaUnimon HP",
		addresses=[0x26718c6],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(800,rare_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(800,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ShimaUnimon Circle",
		addresses=[0x26718c8],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(430,rare_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(430,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ShimaUnimon Triangle",
		addresses=[0x26718e4],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(250,rare_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(250,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ShimaUnimon Cross",
		addresses=[0x2671900],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,rare_special_modifier,champion_modifier,5),
		max_value=Max_Cross_Multiplier(0,rare_special_modifier,champion_modifier,5),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ShimaUnimon Cross Effect",
		addresses=[0x267198c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#MudFrigimon 163
	Attribute(
		name="MudFrigimon Element",
		addresses=[0x26719FE],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 2, 163),
		max_value=Get_Element_Type(64, 2, 163),
		is_little_endian=True, ),
	Attribute(
		name="MudFrigimon +DP",
		addresses=[0x2671a00],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="MudFrigimon HP",
		addresses=[0x2671a02],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(930,rare_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(930,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MudFrigimon Circle",
		addresses=[0x2671a04],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(480,rare_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(480,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MudFrigimon Triangle",
		addresses=[0x2671a20],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(360,rare_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(360,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MudFrigimon Cross",
		addresses=[0x2671a3c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(320,rare_special_modifier,champion_modifier,0),
		max_value=Max_Cross_Multiplier(320,rare_special_modifier,champion_modifier,0),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="MudFrigimon Cross Effect",
		addresses=[0x2671ac8],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#SandYanmamon 164
	Attribute(
		name="SandYanmamon Element",
		addresses=[0x2671b3a],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 2, 164),
		max_value=Get_Element_Type(64, 2, 164),
		is_little_endian=True, ),
	Attribute(
		name="SandYanmamon +DP",
		addresses=[0x2671b3c],
		number_of_bytes=2,
		possible_values=Ten_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="SandYanmamon HP",
		addresses=[0x2671b3e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(600,rare_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(600,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="SandYanmamon Circle",
		addresses=[0x2671b40],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(250,rare_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(250,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="SandYanmamon Triangle",
		addresses=[0x2671b5c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(340,rare_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(340,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="SandYanmamon Cross",
		addresses=[0x2671b78],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(210,rare_special_modifier,champion_modifier,1),
		max_value=Max_Cross_Multiplier(210,rare_special_modifier,champion_modifier,1),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="SandYanmamon Cross Effect",
		addresses=[0x2671c04],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#L-ToyAgumon 165
	Attribute(
		name="L-ToyAgumon Element",
		addresses=[0x2671c76],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 0, 165),
		max_value=Get_Element_Type(64, 0, 165),
		is_little_endian=True, ),
	Attribute(
		name="L-ToyAgumon +DP",
		addresses=[0x2671c78],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="L-ToyAgumon HP",
		addresses=[0x2671c7a],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(590,rare_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(590,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="L-ToyAgumon Circle",
		addresses=[0x2671c7c],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(270,rare_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(270,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="L-ToyAgumon Triangle",
		addresses=[0x2671c98],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(210,rare_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(210,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="L-ToyAgumon Cross",
		addresses=[0x2671cb4],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(180,rare_special_modifier,rookie_modifier,0),
		max_value=Max_Cross_Multiplier(180,rare_special_modifier,rookie_modifier,0),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="L-ToyAgumon Cross Effect",
		addresses=[0x2671d40],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Hagurumon 166
	Attribute(
		name="L-ToyAgumon Element",
		addresses=[0x2671db2],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 0, 166),
		max_value=Get_Element_Type(64, 0, 166),
		is_little_endian=True, ),
	Attribute(
		name="Hagurumon +DP",
		addresses=[0x2671db4],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Hagurumon HP",
		addresses=[0x2671db6],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(500,rare_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(500,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Hagurumon Circle",
		addresses=[0x2671db8],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(240,rare_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(240,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Hagurumon Triangle",
		addresses=[0x2671dd4],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(200,rare_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(200,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Hagurumon Cross",
		addresses=[0x2671df0],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,rare_special_modifier,rookie_modifier,8),
		max_value=Max_Cross_Multiplier(0,rare_special_modifier,rookie_modifier,8),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Hagurumon Cross Effect",
		addresses=[0x2671e7c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#ToyAgumon 167
	Attribute(
		name="ToyAgumon Element",
		addresses=[0x2671eee],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 0, 167),
		max_value=Get_Element_Type(64, 0, 167),
		is_little_endian=True, ),
	Attribute(
		name="ToyAgumon +DP",
		addresses=[0x2671ef0],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="ToyAgumon HP",
		addresses=[0x2671ef2],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(530,rare_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(530,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ToyAgumon Circle",
		addresses=[0x2671ef4],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(280,rare_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(280,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ToyAgumon Triangle",
		addresses=[0x2671f10],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(130,rare_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(130,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ToyAgumon Cross",
		addresses=[0x2671f2c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,rare_special_modifier,rookie_modifier,6),
		max_value=Max_Cross_Multiplier(0,rare_special_modifier,rookie_modifier,6),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ToyAgumon Cross Effect",
		addresses=[0x2671fb8],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#ClearAgumon 168
	Attribute(
		name="ClearAgumon Element",
		addresses=[0x267202a],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 0, 168),
		max_value=Get_Element_Type(64, 0, 168),
		is_little_endian=True, ),
	Attribute(
		name="ClearAgumon +DP",
		addresses=[0x267202c],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="ClearAgumon HP",
		addresses=[0x267202e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(580,rare_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(580,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ClearAgumon Circle",
		addresses=[0x2672030],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(270,rare_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(270,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ClearAgumon Triangle",
		addresses=[0x267204c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(220,rare_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(220,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ClearAgumon Cross",
		addresses=[0x2672068],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(50,rare_special_modifier,rookie_modifier,10),
		max_value=Max_Cross_Multiplier(50,rare_special_modifier,rookie_modifier,10),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ClearAgumon Cross Effect",
		addresses=[0x2672224],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Vi-Elecmon 169
	Attribute(
		name="Vi-Elecmon Element",
		addresses=[0x2672296],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 0, 169),
		max_value=Get_Element_Type(64, 0, 169),
		is_little_endian=True, ),
	Attribute(
		name="Vi-Elecmon +DP",
		addresses=[0x2672298],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Vi-Elecmon HP",
		addresses=[0x267229a],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(620,rare_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(620,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Vi-Elecmon Circle",
		addresses=[0x267229c],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(260,rare_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(260,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Vi-Elecmon Triangle",
		addresses=[0x26722b8],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(220,rare_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(220,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Vi-Elecmon Cross",
		addresses=[0x26722d4],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(190,rare_special_modifier,rookie_modifier,15),
		max_value=Max_Cross_Multiplier(190,rare_special_modifier,rookie_modifier,15),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Vi-Elecmon Cross Effect",
		addresses=[0x2672360],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Psychemon 170
	Attribute(
		name="Psychemon Element",
		addresses=[0x26723d2],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 0, 170),
		max_value=Get_Element_Type(64, 0, 170),
		is_little_endian=True, ),
	Attribute(
		name="Psychemon +DP",
		addresses=[0x26723d4],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Psychemon HP",
		addresses=[0x26723d6],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(470,rare_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(470,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Psychemon Circle",
		addresses=[0x26723d8],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(250,rare_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(250,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Psychemon Triangle",
		addresses=[0x26723f4],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(120,rare_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(120,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Psychemon Cross",
		addresses=[0x2672410],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(90,rare_special_modifier,rookie_modifier,2),
		max_value=Max_Cross_Multiplier(90,rare_special_modifier,rookie_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Psychemon Cross Effect",
		addresses=[0x267249c],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#ModokiBetamon 171
	Attribute(
		name="ModokiBetamon Element",
		addresses=[0x267250e],
		number_of_bytes=1,
		min_value=Get_Element_Type(64, 0, 171),
		max_value=Get_Element_Type(64, 0, 171),
		is_little_endian=True, ),
	Attribute(
		name="ModokiBetamon +DP",
		addresses=[0x2672510],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="ModokiBetamon HP",
		addresses=[0x2672512],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(550,rare_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(550,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ModokiBetamon Circle",
		addresses=[0x2672514],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(120,rare_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(120,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ModokiBetamon Triangle",
		addresses=[0x2672530],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(280,rare_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(280,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ModokiBetamon Cross",
		addresses=[0x267254c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(190,rare_special_modifier,rookie_modifier,2),
		max_value=Max_Cross_Multiplier(190,rare_special_modifier,rookie_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="ModokiBetamon Cross Effect",
		addresses=[0x26725d8],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Flamedramon 172
	Attribute(
		name="Flamedramon +DP",
		addresses=[0x267264c],
		number_of_bytes=2,
		possible_values=[0],
		is_little_endian=True,),
	Attribute(
		name="Flamedramon HP",
		addresses=[0x267264e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(600,fire_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(600,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Flamedramon Circle",
		addresses=[0x2672650],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(500,fire_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(500,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Flamedramon Triangle",
		addresses=[0x267266c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(350,fire_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(350,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Flamedramon Cross",
		addresses=[0x2672688],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,fire_special_modifier,champion_modifier,5),
		max_value=Max_Cross_Multiplier(0,fire_special_modifier,champion_modifier,5),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Flamedramon Cross Effect",
		addresses=[0x2672714],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Magnamon 173
	Attribute(
		name="Magnamon +DP",
		addresses=[0x2672788],
		number_of_bytes=2,
		possible_values=[0],
		is_little_endian=True,),
	Attribute(
		name="Magnamon HP",
		addresses=[0x267278a],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(650,fire_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(650,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Magnamon Circle",
		addresses=[0x267278c],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(550,fire_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(550,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Magnamon Triangle",
		addresses=[0x26727a8],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(300,fire_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(300,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Magnamon Cross",
		addresses=[0x26727c4],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(200,fire_special_modifier,champion_modifier,2),
		max_value=Max_Cross_Multiplier(200,fire_special_modifier,champion_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Magnamon Cross Effect",
		addresses=[0x2672850],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Baronmon 174
	Attribute(
		name="Baronmon +DP",
		addresses=[0x26728C4],
		number_of_bytes=2,
		possible_values=[0],
		is_little_endian=True,),
	Attribute(
		name="Baronmon HP",
		addresses=[0x26728C6],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(600,fire_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(600,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Baronmon Circle",
		addresses=[0x26728C8],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(550,fire_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(550,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Baronmon Triangle",
		addresses=[0x26728E4],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(450,fire_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(450,fire_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Baronmon Cross",
		addresses=[0x2672900],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(150,fire_special_modifier,champion_modifier,2),
		max_value=Max_Cross_Multiplier(150,fire_special_modifier,champion_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Baronmon Cross Effect",
		addresses=[0x267298C],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Veemon 175
	Attribute(
		name="Veemon +DP",
		addresses=[0x2672b30],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Veemon HP",
		addresses=[0x2672b32],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(550,fire_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(550,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Veemon Circle",
		addresses=[0x2672b34],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(350,fire_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(350,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Veemon Triangle",
		addresses=[0x2672b50],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(280,fire_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(280,fire_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Veemon Cross",
		addresses=[0x2672b6c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(200,fire_special_modifier,rookie_modifier,0),
		max_value=Max_Cross_Multiplier(200,fire_special_modifier,rookie_modifier,0),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Veemon Cross Effect",
		addresses=[0x2672bf8],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Submarimon 176
	Attribute(
		name="Submarimon +DP",
		addresses=[0x2672c6c],
		number_of_bytes=2,
		possible_values=[0],
		is_little_endian=True,),
	Attribute(
		name="Submarimon HP",
		addresses=[0x2672c6e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(850,ice_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(850,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Submarimon Circle",
		addresses=[0x2672c70],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(400,ice_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(400,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Submarimon Triangle",
		addresses=[0x2672c8c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(300,ice_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(300,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Submarimon Cross",
		addresses=[0x2672ca8],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(200,ice_special_modifier,champion_modifier,2),
		max_value=Max_Cross_Multiplier(200,ice_special_modifier,champion_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Submarimon Cross Effect",
		addresses=[0x2672d34],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Quetzalmon 171
	Attribute(
		name="Quetzalmon +DP",
		addresses=[0x2672da8],
		number_of_bytes=2,
		possible_values=[0],
		is_little_endian=True,),
	Attribute(
		name="Quetzalmon HP",
		addresses=[0x2672daa],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(800,ice_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(800,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Quetzalmon Circle",
		addresses=[0x2672dac],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(400,ice_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(400,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Quetzalmon Triangle",
		addresses=[0x2672dc8],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(350,ice_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(350,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Quetzalmon Cross",
		addresses=[0x2672de4],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,ice_special_modifier,champion_modifier,7),
		max_value=Max_Cross_Multiplier(0,ice_special_modifier,champion_modifier,7),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Quetzalmon Cross Effect",
		addresses=[0x2672e70],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Tylomon 178
	Attribute(
		name="Tylomon +DP",
		addresses=[0x2672ee4],
		number_of_bytes=2,
		possible_values=[0],
		is_little_endian=True,),
	Attribute(
		name="Tylomon HP",
		addresses=[0x2672ee8],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(900,ice_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(900,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tylomon Circle",
		addresses=[0x2672ee8],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(350,ice_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(350,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tylomon Triangle",
		addresses=[0x2672f04],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(300,ice_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(300,ice_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tylomon Cross",
		addresses=[0x2672f20],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(250,ice_special_modifier,champion_modifier,11),
		max_value=Max_Cross_Multiplier(250,ice_special_modifier,champion_modifier,11),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Tylomon Cross Effect",
		addresses=[0x2672fac],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Halsemon 171
	Attribute(
		name="Halsemon +DP",
		addresses=[0x2673020],
		number_of_bytes=2,
		possible_values=[0],
		is_little_endian=True,),
	Attribute(
		name="Halsemon HP",
		addresses=[0x2673022],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(700,nature_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(700,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Halsemon Circle",
		addresses=[0x2673024],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(400,nature_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(400,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Halsemon Triangle",
		addresses=[0x2673040],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(300,nature_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(300,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Halsemon Cross",
		addresses=[0x267305c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(250,nature_special_modifier,champion_modifier,2),
		max_value=Max_Cross_Multiplier(250,nature_special_modifier,champion_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Halsemon Cross Effect",
		addresses=[0x26730e8],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Pegasusmon 180
	Attribute(
		name="Pegasusmon +DP",
		addresses=[0x267315c],
		number_of_bytes=2,
		possible_values=[0],
		is_little_endian=True,),
	Attribute(
		name="Pegasusmon HP",
		addresses=[0x267315e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(750,nature_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(750,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Pegasusmon Circle",
		addresses=[0x2673160],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(400,nature_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(400,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Pegasusmon Triangle",
		addresses=[0x267317c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(300,nature_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(300,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Pegasusmon Cross",
		addresses=[0x2673198],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(200,nature_special_modifier,champion_modifier,1),
		max_value=Max_Cross_Multiplier(200,nature_special_modifier,champion_modifier,1),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Pegasusmon Cross Effect",
		addresses=[0x2673224],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Nefertimon 181
	Attribute(
		name="Nefertimon +DP",
		addresses=[0x2673298],
		number_of_bytes=2,
		possible_values=[0],
		is_little_endian=True,),
	Attribute(
		name="Nefertimon HP",
		addresses=[0x267329A],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(650,nature_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(650,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Nefertimon Circle",
		addresses=[0x267329C],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(500,nature_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(500,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Nefertimon Triangle",
		addresses=[0x26732B8],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(300,nature_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(300,nature_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Nefertimon Cross",
		addresses=[0x26732D4],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(200,nature_special_modifier,champion_modifier,2),
		max_value=Max_Cross_Multiplier(200,nature_special_modifier,champion_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Nefertimon Cross Effect",
		addresses=[0x2673490],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Hawkmon 182
	Attribute(
		name="Hawkmon +DP",
		addresses=[0x2673504],
		number_of_bytes=2,
		possible_values=Thirty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Hawkmon HP",
		addresses=[0x2673506],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(600,nature_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(600,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Hawkmon Circle",
		addresses=[0x2673508],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(300,nature_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(300,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Hawkmon Triangle",
		addresses=[0x2673524],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(220,nature_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(220,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Hawkmon Cross",
		addresses=[0x2673540],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,nature_special_modifier,rookie_modifier,5),
		max_value=Max_Cross_Multiplier(0,nature_special_modifier,rookie_modifier,5),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Hawkmon Cross Effect",
		addresses=[0x26735cc],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Patamon 183
	Attribute(
		name="Patamon +DP",
		addresses=[0x2673640],
		number_of_bytes=2,
		possible_values=Thirty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Patamon HP",
		addresses=[0x2673642],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(630,nature_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(630,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Patamon Circle",
		addresses=[0x2673644],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(370,nature_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(370,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Patamon Triangle",
		addresses=[0x2673660],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(170,nature_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(170,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Patamon Cross",
		addresses=[0x267367c],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,nature_special_modifier,rookie_modifier,5),
		max_value=Max_Cross_Multiplier(0,nature_special_modifier,rookie_modifier,5),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Patamon Cross Effect",
		addresses=[0x2673708],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Gatomon 184
	Attribute(
		name="Gatomon +DP",
		addresses=[0x267377c],
		number_of_bytes=2,
		possible_values=Thirty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Gatomon HP",
		addresses=[0x267377e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(600,nature_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(600,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gatomon Circle",
		addresses=[0x2673780],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(290,nature_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(290,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gatomon Triangle",
		addresses=[0x267379c],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(200,nature_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(200,nature_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gatomon Cross",
		addresses=[0x26737b8],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(0,nature_special_modifier,rookie_modifier,6),
		max_value=Max_Cross_Multiplier(0,nature_special_modifier,rookie_modifier,6),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Gatomon Cross Effect",
		addresses=[0x2673844],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Raidramon 185
	Attribute(
		name="Raidramon +DP",
		addresses=[0x26738b8],
		number_of_bytes=2,
		possible_values=[0],
		is_little_endian=True,),
	Attribute(
		name="Raidramon HP",
		addresses=[0x26738ba],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(650,darkness_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(650,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Raidramon Circle",
		addresses=[0x26738bc],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(300,darkness_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(300,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Raidramon Triangle",
		addresses=[0x26738d8],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(300,darkness_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(300,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Raidramon Cross",
		addresses=[0x26738f4],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(400,darkness_special_modifier,champion_modifier,3),
		max_value=Max_Cross_Multiplier(400,darkness_special_modifier,champion_modifier,3),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Raidramon Cross Effect",
		addresses=[0x2673980],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Shadramon 186
	Attribute(
		name="Shadramon +DP",
		addresses=[0x26739f4],
		number_of_bytes=2,
		possible_values=[0],
		is_little_endian=True,),
	Attribute(
		name="Shadramon HP",
		addresses=[0x26739f6],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(650,darkness_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(650,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Shadramon Circle",
		addresses=[0x26739f8],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(500,darkness_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(500,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Shadramon Triangle",
		addresses=[0x2673a14],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(350,darkness_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(350,darkness_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Shadramon Cross",
		addresses=[0x2673a30],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(150,darkness_special_modifier,champion_modifier,10),
		max_value=Max_Cross_Multiplier(150,darkness_special_modifier,champion_modifier,10),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Shadramon Cross Effect",
		addresses=[0x2673abc],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Wormmon 187
	Attribute(
		name="Wormmon +DP",
		addresses=[0x2673b30],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Wormmon HP",
		addresses=[0x2673b32],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(550,darkness_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(550,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Wormmon Circle",
		addresses=[0x2673b34],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(300,darkness_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(300,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Wormmon Triangle",
		addresses=[0x2673b50],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(250,darkness_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(250,darkness_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Wormmon Cross",
		addresses=[0x2673B6C],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(170,darkness_special_modifier,rookie_modifier,2),
		max_value=Max_Cross_Multiplier(170,darkness_special_modifier,rookie_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Wormmon Cross Effect",
		addresses=[0x2673BF8],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Shurimon 188
	Attribute(
		name="Shurimon +DP",
		addresses=[0x2673d9c],
		number_of_bytes=2,
		possible_values=[0],
		is_little_endian=True,),
	Attribute(
		name="Shurimon HP",
		addresses=[0x2673d9e],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(600,rare_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(600,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Shurimon Circle",
		addresses=[0x2673da0],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(450,rare_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(450,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Shurimon Triangle",
		addresses=[0x2673dbc],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(350,rare_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(350,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Shurimon Cross",
		addresses=[0x2673dd8],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(250,rare_special_modifier,champion_modifier,4),
		max_value=Max_Cross_Multiplier(250,rare_special_modifier,champion_modifier,4),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Shurimon Cross Effect",
		addresses=[0x2673e64],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Digmon 189
	Attribute(
		name="Digmon +DP",
		addresses=[0x2673ed8],
		number_of_bytes=2,
		possible_values=[0],
		is_little_endian=True,),
	Attribute(
		name="Digmon HP",
		addresses=[0x2673eda],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(800,rare_special_modifier,champion_modifier),
		max_value=Max_HP_Multiplier(800,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Digmon Circle",
		addresses=[0x2673edc],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(400,rare_special_modifier,champion_modifier),
		max_value=Max_Circle_Multiplier(400,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Digmon Triangle",
		addresses=[0x2673ef8],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(400,rare_special_modifier,champion_modifier),
		max_value=Max_Triangle_Multiplier(400,rare_special_modifier,champion_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Digmon Cross",
		addresses=[0x2673f14],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(400,rare_special_modifier,champion_modifier,0),
		max_value=Max_Cross_Multiplier(400,rare_special_modifier,champion_modifier,0),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Digmon Cross Effect",
		addresses=[0x2673fa0],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Armadillomon 190
	Attribute(
		name="Armadillomon +DP",
		addresses=[0x2674014],
		number_of_bytes=2,
		possible_values=Twenty_DP_Change,
		is_little_endian=True,),
	Attribute(
		name="Armadillomon HP",
		addresses=[0x2674016],
		number_of_bytes=2,
		min_value=Min_HP_Multiplier(650,rare_special_modifier,rookie_modifier),
		max_value=Max_HP_Multiplier(650,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Armadillomon Circle",
		addresses=[0x2674018],
		number_of_bytes=2,
		min_value=Min_Circle_Multiplier(280,rare_special_modifier,rookie_modifier),
		max_value=Max_Circle_Multiplier(280,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Armadillomon Triangle",
		addresses=[0x2674034],
		number_of_bytes=2,
		min_value=Min_Triangle_Multiplier(240,rare_special_modifier,rookie_modifier),
		max_value=Max_Triangle_Multiplier(240,rare_special_modifier,rookie_modifier),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Armadillomon Cross",
		addresses=[0x2674050],
		number_of_bytes=2,
		min_value=Min_Cross_Multiplier(190,rare_special_modifier,rookie_modifier,2),
		max_value=Max_Cross_Multiplier(190,rare_special_modifier,rookie_modifier,2),
        min_max_interval=10,
		is_little_endian=True,),
	Attribute(
		name="Armadillomon Cross Effect",
		addresses=[0x26740dc],
		number_of_bytes=1,
		possible_values = cross_special_effect,
		is_little_endian=True,),
#Red Deck 16,16,20,20,26,26,126,126,130,130,27,27,29,29,30,33,33,133,133,134,134,135,135,175,264,264,266,267,267,299,
	Attribute(
		name="Red Deck 1",
		addresses=[0x26a98e4,0x26a98e6],
		number_of_bytes=2,
		possible_values=[New_Red_Deck[0]],
		is_little_endian=True, ),
    Attribute(
        name="Red Deck 2",
        addresses=[0x26a98e8,0x26a98ea],
        number_of_bytes=2,
        possible_values=[New_Red_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Red Deck 3",
        addresses=[0x26a98ec,0x26a98ee],
        number_of_bytes=2,
        possible_values=[New_Red_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Red Deck 4",
        addresses=[0x26a98f0,0x26a98f2],
        number_of_bytes=2,
        possible_values=[New_Red_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Red Deck 5",
        addresses=[0x26a98f4,0x26a98f6],
        number_of_bytes=2,
        possible_values=[New_Red_Deck[4]],
        is_little_endian=True, ),
    Attribute(
        name="Red Deck 6",
        addresses=[0x26a98f8,0x26a98fa],
        number_of_bytes=2,
        possible_values=[New_Red_Deck[5]],
        is_little_endian=True, ),
    Attribute(
        name="Red Deck 7",
        addresses=[0x26a98fc,0x26a98fe],
        number_of_bytes=2,
        possible_values=[New_Red_Deck[6]],
        is_little_endian=True, ),
    Attribute(
        name="Red Deck 8",
        addresses=[0x26a9900],
        number_of_bytes=2,
        possible_values=[New_Red_Deck[7]],
        is_little_endian=True, ),
    Attribute(
        name="Red Deck 9",
        addresses=[0x26a9902,0x26a9904],
        number_of_bytes=2,
        possible_values=[New_Red_Deck[8]],
        is_little_endian=True, ),
    Attribute(
        name="Red Deck 10",
        addresses=[0x26a9906,0x26a9908],
        number_of_bytes=2,
        possible_values=[New_Red_Deck[9]],
        is_little_endian=True, ),
    Attribute(
        name="Red Deck 11",
        addresses=[0x26a990a,0x26a990c],
        number_of_bytes=2,
        possible_values=[New_Red_Deck[10]],
        is_little_endian=True, ),
    Attribute(
        name="Red Deck 12",
        addresses=[0x26a990e,0x26a9910],
        number_of_bytes=2,
        possible_values=[New_Red_Deck[11]],
        is_little_endian=True, ),
    Attribute(
        name="Red Deck 13",
        addresses=[0x26a9912],
        number_of_bytes=2,
        possible_values=[175],
        is_little_endian=True, ),
    Attribute(
        name="Red Deck 14",
        addresses=[0x26a9914,0x26a9916],
        number_of_bytes=2,
        possible_values=[New_Red_Deck[13]],
        is_little_endian=True, ),
    Attribute(
        name="Red Deck 15",
        addresses=[0x26a9918],
        number_of_bytes=2,
        possible_values=[New_Red_Deck[14]],
        is_little_endian=True, ),
    Attribute(
        name="Red Deck 16",
        addresses=[0x26a991a,0x26a991c],
        number_of_bytes=2,
        possible_values=[New_Red_Deck[15]],
        is_little_endian=True, ),
    Attribute(
        name="Red Deck 17",
        addresses=[0x26a991e],
        number_of_bytes=2,
        possible_values=[New_Red_Deck[16]],
        is_little_endian=True, ),
#Green_Deck = [91,91,92,92,95,95,162,162,163,163,97,97,99,99,101,102,102,165,165,169,169,170,170,182,266,266,270,270,272,299]
    Attribute(
        name="Green Deck 1",
        addresses=[0x26a9952,0x26a9954],
        number_of_bytes=2,
        possible_values=[New_Green_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Green Deck 2",
        addresses=[0x26a9956,0x26a9958],
        number_of_bytes=2,
        possible_values=[New_Green_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Green Deck 3",
        addresses=[0x26a995a,0x26a995c],
        number_of_bytes=2,
        possible_values=[New_Green_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Green Deck 4",
        addresses=[0x26a995e,0x26a9960],
        number_of_bytes=2,
        possible_values=[New_Green_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Green Deck 5",
        addresses=[0x26a9962,0x26a9964],
        number_of_bytes=2,
        possible_values=[New_Green_Deck[4]],
        is_little_endian=True, ),
    Attribute(
        name="Green Deck 6",
        addresses=[0x26a9966,0x26a9968],
        number_of_bytes=2,
        possible_values=[New_Green_Deck[5]],
        is_little_endian=True, ),
    Attribute(
        name="Green Deck 7",
        addresses=[0x26a996a,0x26a996c],
        number_of_bytes=2,
        possible_values=[New_Green_Deck[6]],
        is_little_endian=True, ),
    Attribute(
        name="Green Deck 8",
        addresses=[0x26a996e],
        number_of_bytes=2,
        possible_values=[New_Green_Deck[7]],
        is_little_endian=True, ),
    Attribute(
        name="Green Deck 9",
        addresses=[0x26a9970,0x26a9972],
        number_of_bytes=2,
        possible_values=[New_Green_Deck[8]],
        is_little_endian=True, ),
    Attribute(
        name="Green Deck 10",
        addresses=[0x26a9974,0x26a9976],
        number_of_bytes=2,
        possible_values=[New_Green_Deck[9]],
        is_little_endian=True, ),
    Attribute(
        name="Green Deck 11",
        addresses=[0x26a9978,0x26a997a],
        number_of_bytes=2,
        possible_values=[New_Green_Deck[10]],
        is_little_endian=True, ),
    Attribute(
        name="Green Deck 12",
        addresses=[0x26a997c,0x26a997e],
        number_of_bytes=2,
        possible_values=[New_Green_Deck[11]],
        is_little_endian=True, ),
    Attribute(
        name="Green Deck 13",
        addresses=[0x26a9980],
        number_of_bytes=2,
        possible_values=[182],
        is_little_endian=True, ),
    Attribute(
        name="Green Deck 14",
        addresses=[0x26a9982,0x26a9984],
        number_of_bytes=2,
        possible_values=[New_Green_Deck[13]],
        is_little_endian=True, ),
    Attribute(
        name="Green Deck 15",
        addresses=[0x26a9986,0x26a9988],
        number_of_bytes=2,
        possible_values=[New_Green_Deck[14]],
        is_little_endian=True, ),
    Attribute(
        name="Green Deck 16",
        addresses=[0x26a998a],
        number_of_bytes=2,
        possible_values=[New_Green_Deck[15]],
        is_little_endian=True, ),
    Attribute(
        name="Green Deck 17",
        addresses=[0x26a998c],
        number_of_bytes=2,
        possible_values=[New_Green_Deck[16]],
        is_little_endian=True, ),
# Yellow_Deck = [55,55,56,56,157,157,159,159,161,161,62,62,66,66,67,67,166,166,168,170,170,171,171,190,262,263,263,266,266,299]
Attribute(
        name="Yellow Deck 1",
        addresses=[0x26a99c0,0x26a99c2],
        number_of_bytes=2,
        possible_values=[New_Yellow_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Yellow Deck 2",
        addresses=[0x26a99c4,0x26a99c6],
        number_of_bytes=2,
        possible_values=[New_Yellow_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Yellow Deck 3",
        addresses=[0x26a99c8,0x26a99ca],
        number_of_bytes=2,
        possible_values=[New_Yellow_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Yellow Deck 4",
        addresses=[0x26a99cc,0x26a99ce],
        number_of_bytes=2,
        possible_values=[New_Yellow_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Yellow Deck 5",
        addresses=[0x26a99d0,0x26a99d2],
        number_of_bytes=2,
        possible_values=[New_Yellow_Deck[4]],
        is_little_endian=True, ),
    Attribute(
        name="Yellow Deck 6",
        addresses=[0x26a99d4,0x26a99d6],
        number_of_bytes=2,
        possible_values=[New_Yellow_Deck[5]],
        is_little_endian=True, ),
    Attribute(
        name="Yellow Deck 7",
        addresses=[0x26a99d8,0x26a99da],
        number_of_bytes=2,
        possible_values=[New_Yellow_Deck[6]],
        is_little_endian=True, ),
    Attribute(
        name="Yellow Deck 8",
        addresses=[0x26a99dc,0x26a99de],
        number_of_bytes=2,
        possible_values=[New_Yellow_Deck[7]],
        is_little_endian=True, ),
    Attribute(
        name="Yellow Deck 9",
        addresses=[0x26a99e0,0x26a99e2],
        number_of_bytes=2,
        possible_values=[New_Yellow_Deck[8]],
        is_little_endian=True, ),
    Attribute(
        name="Yellow Deck 10",
        addresses=[0x26a99e4],
        number_of_bytes=2,
        possible_values=[New_Yellow_Deck[9]],
        is_little_endian=True, ),
    Attribute(
        name="Yellow Deck 11",
        addresses=[0x26a99e6,0x26a99e8],
        number_of_bytes=2,
        possible_values=[New_Yellow_Deck[10]],
        is_little_endian=True, ),
    Attribute(
        name="Yellow Deck 12",
        addresses=[0x26a99ea,0x26a99ec],
        number_of_bytes=2,
        possible_values=[New_Yellow_Deck[11]],
        is_little_endian=True, ),
    Attribute(
        name="Yellow Deck 13",
        addresses=[0x26a99ee],
        number_of_bytes=2,
        possible_values=[190],
        is_little_endian=True, ),
    Attribute(
        name="Yellow Deck 14",
        addresses=[0x26a99f0],
        number_of_bytes=2,
        possible_values=[New_Yellow_Deck[13]],
        is_little_endian=True, ),
    Attribute(
        name="Yellow Deck 15",
        addresses=[0x26a99f2,0x26a99f4],
        number_of_bytes=2,
        possible_values=[New_Yellow_Deck[14]],
        is_little_endian=True, ),
    Attribute(
        name="Yellow Deck 16",
        addresses=[0x26a99f6,0x26a99f8],
        number_of_bytes=2,
        possible_values=[New_Yellow_Deck[15]],
        is_little_endian=True, ),
    Attribute(
        name="Yellow Deck 17",
        addresses=[0x26a99fa],
        number_of_bytes=2,
        possible_values=[New_Yellow_Deck[16]],
        is_little_endian=True, ),

#PHOENIXMON
	Attribute(
		name="Phoenixmon Deck Ults1",
		addresses=[0x26a55b6,0x26a55b8,0x26a55ba,0x26a55bc],
		number_of_bytes=2,
		possible_values=[New_Phoenixmon_Deck[0]],
		is_little_endian=True, ),
    Attribute(
		name="Phoenixmon Deck Champs1",
		addresses=[0x26a55be, 0x26a55c0],
		number_of_bytes=2,
		possible_values=[New_Phoenixmon_Deck[1]],
		is_little_endian=True, ),
	Attribute(
		name="Phoenixmon Deck Champs2",
		addresses=[0x26a55c2, 0x26a55c4, 0x26a55c6],
		number_of_bytes=2,
		possible_values=[New_Phoenixmon_Deck[2]],
		is_little_endian=True, ),
	Attribute(
		name="Phoenixmon Deck Champs3",
		addresses=[0x26a55c8, 0x26a55ca, 0x26a55cc],
		number_of_bytes=2,
		possible_values=[New_Phoenixmon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Phoenixmon Deck Rookies1",
		addresses=[0x26a55ce, 0x26a55d0, 0x26a55d2, 0x26a55d4],
		number_of_bytes=2,
		possible_values=[New_Phoenixmon_Deck[4]],
		is_little_endian=True, ),
	Attribute(
		name="Phoenixmon Deck Rookies2",
		addresses=[0x26a55d6, 0x26a55d8, 0x26a55da, 0x26a55dc],
		number_of_bytes=2,
		possible_values=[New_Phoenixmon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Phoenixmon Deck Rookies3",
		addresses=[0x26a55de, 0x26a55e0],
		number_of_bytes=2,
		possible_values=[New_Phoenixmon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Phoenixmon Deck Option1",
		addresses=[0x26a55e2],
		number_of_bytes=2,
		possible_values=[New_Phoenixmon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Phoenixmon Deck Option2",
		addresses=[0x26a55e4],
		number_of_bytes=2,
		possible_values=[New_Phoenixmon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Phoenixmon Deck Option3",
		addresses=[0x26a55e6],
		number_of_bytes=2,
		possible_values=[New_Phoenixmon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Phoenixmon Deck Option5",
		addresses=[0x26a55e8,0x26a55ea],
		number_of_bytes=2,
		possible_values=[New_Phoenixmon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Phoenixmon Deck Option5",
		addresses=[0x26a55ec,0x26a55ee],
		number_of_bytes=2,
		possible_values=[New_Phoenixmon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Phoenixmon Deck Option6",
		addresses=[0x26a55f0],
		number_of_bytes=2,
		possible_values=[New_Phoenixmon_Deck[12]],
		is_little_endian=True, ),
#MERAMON
	Attribute(
		name="MERAMON Deck Ults1",
		addresses=[0x26a5548,0x26a554a],
		number_of_bytes=2,
		possible_values=[New_Meramon_Deck[0]],
		is_little_endian=True, ),
	Attribute(
		name="MERAMON Deck Champs1",
		addresses=[0x26a554c,0x26a554e,0x26a5550,0x26a5552],
		number_of_bytes=2,
		possible_values=[New_Meramon_Deck[1]],
		is_little_endian=True, ),
	Attribute(
		name="MERAMON Deck Champs2",
		addresses=[0x26a5554,0x26a5556,0x26a5558],
		number_of_bytes=2,
		possible_values=[New_Meramon_Deck[2]],
		is_little_endian=True, ),
	Attribute(
		name="MERAMON Deck Champs3",
		addresses=[0x26a555a,0x26a555c,0x26a555e],
		number_of_bytes=2,
		possible_values=[New_Meramon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="MERAMON Deck Rookies1",
		addresses=[0x26a5560,0x26a5562,0x26a5564],
		number_of_bytes=2,
		possible_values=[New_Meramon_Deck[4]],
		is_little_endian=True, ),
	Attribute(
		name="MERAMON Deck Rookies2",
		addresses=[0x26a5566,0x26a5568],
		number_of_bytes=2,
		possible_values=[New_Meramon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="MERAMON Deck Rookies3",
		addresses=[0x26a556a,0x26a556c],
		number_of_bytes=2,
		possible_values=[New_Meramon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="MERAMON Deck Rookies4",
		addresses=[0x26a556e,0x26a5570,0x26a5572],
		number_of_bytes=2,
		possible_values=[New_Meramon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="MERAMON Deck Rookies5",
		addresses=[0x26a5574,0x26a5576,0x26a5578],
		number_of_bytes=2,
		possible_values=[New_Meramon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="MERAMON Deck Rookies6",
		addresses=[0x26a557a],
		number_of_bytes=2,
		possible_values=[New_Meramon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="MERAMON Deck Option1",
		addresses=[0x26a557c,0x26a557e,0x26a5580,0x26a5582],
		number_of_bytes=2,
		possible_values=[New_Meramon_Deck[10]],
		is_little_endian=True, ),
#Veemon
	Attribute(
		name="Veemon Deck Ults1",
		addresses=[0x26a5624],
		number_of_bytes=2,
		possible_values=[New_Veemon_Deck[0]],
		is_little_endian=True, ),
	Attribute(
		name="Veemon Deck Ults2",
		addresses=[0x26a5626,0x26a5628],
		number_of_bytes=2,
		possible_values=[New_Veemon_Deck[1]],
		is_little_endian=True, ),
	Attribute(
		name="Veemon Deck Ults3",
		addresses=[0x26a562a,0x26a562c],
		number_of_bytes=2,
		possible_values=[New_Veemon_Deck[2]],
		is_little_endian=True, ),
	Attribute(
		name="Veemon Deck Champs1",
		addresses=[0x26a562e,0x26a5630,0x26a5632],
		number_of_bytes=2,
		possible_values=[New_Veemon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Veemon Deck Champs2",
		addresses=[0x26a5634,0x26a5636,0x26a5638],
		number_of_bytes=2,
		possible_values=[New_Veemon_Deck[4]],
		is_little_endian=True, ),
	Attribute(
		name="Veemon Deck Champs3",
		addresses=[0x26a563a,0x26a563c,0x26a563e],
		number_of_bytes=2,
		possible_values=[New_Veemon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Veemon Deck Rookies1",
		addresses=[0x26a5640,0x26a5642,0x26a5644,0x26a5646],
		number_of_bytes=2,
		possible_values=[New_Veemon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Veemon Deck Rookies2",
		addresses=[0x26a5648,0x26a564a],
		number_of_bytes=2,
		possible_values=[New_Veemon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Veemon Deck Rookies3",
		addresses=[0x26a564c],
		number_of_bytes=2,
		possible_values=[New_Veemon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Veemon Deck Rookies4",
		addresses=[0x26a564e,0x26a5650],
		number_of_bytes=2,
		possible_values=[New_Veemon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Veemon Deck Rookies5",
		addresses=[0x26a5652],
		number_of_bytes=2,
		possible_values=[New_Veemon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Veemon Deck Rookies6 Partner Card",
		addresses=[0x26a5654],
		number_of_bytes=2,
		possible_values=[175],
		is_little_endian=True, ),
	Attribute(
		name="Veemon Deck Options1",
		addresses=[0x26a5656,0x26a5658,0x26a565a],
		number_of_bytes=2,
		possible_values=[New_Veemon_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Veemon Deck Options2",
		addresses=[0x26a565c,0x26a565e],
		number_of_bytes=2,
		possible_values=[New_Veemon_Deck[13]],
		is_little_endian=True, ),
#Vegiemon
	Attribute(
		name="Vegiemon Deck Ults1",
		addresses=[0x26a5692,0x26a5694],
		number_of_bytes=2,
		possible_values=[New_Vegiemon_Deck[0]],
		is_little_endian=True, ),
	Attribute(
		name="Vegiemon Deck Ults2",
		addresses=[0x26a5696,0x26a5698],
		number_of_bytes=2,
		possible_values=[New_Vegiemon_Deck[1]],
		is_little_endian=True, ),
	Attribute(
		name="Vegiemon Deck Ults3",
		addresses=[0x26a569a,0x26a569c],
		number_of_bytes=2,
		possible_values=[New_Vegiemon_Deck[2]],
		is_little_endian=True, ),
	Attribute(
		name="Vegiemon Deck Champs1",
		addresses=[0x26a569e,0x26a56a0],
		number_of_bytes=2,
		possible_values=[New_Vegiemon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Vegiemon Deck Champs2",
		addresses=[0x26a56a2,0x26a56a4],
		number_of_bytes=2,
		possible_values=[New_Vegiemon_Deck[4]],
		is_little_endian=True, ),
	Attribute(
		name="Vegiemon Deck Champs3",
		addresses=[0x26a56a6,0x26a56a8],
		number_of_bytes=2,
		possible_values=[New_Vegiemon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Vegiemon Deck Champs4",
		addresses=[0x26a56aa,0x26a56ac,0x26a56ae,0x26a56b0],
		number_of_bytes=2,
		possible_values=[New_Vegiemon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Vegiemon Deck Rookies1",
		addresses=[0x26a56b2,0x26a56b4,0x26a56b6,0x26a56b8],
		number_of_bytes=2,
		possible_values=[New_Vegiemon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Vegiemon Deck Rookies2",
		addresses=[0x26a56ba,0x26a56bc,0x26a56be,0x26a56c0],
		number_of_bytes=2,
		possible_values=[New_Vegiemon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Vegiemon Deck Rookies3",
		addresses=[0x26a56c2,0x26a56c4,0x26a56c6,0x26a56c8],
		number_of_bytes=2,
		possible_values=[New_Vegiemon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Vegiemon Deck Rookies4",
		addresses=[0x26a56ca,0x26a56cc],
		number_of_bytes=2,
		possible_values=[New_Vegiemon_Deck[10]],
		is_little_endian=True, ),
# Ninjamon_Deck = Ninjamon_Deck = [83,83,89,89,89,89,91,91,93,93,97,97,98,98,99,99,100,100,101,101,260,260,296,296,296,296,300,300,300,300]
	Attribute(
		name="Ninjamon Deck Champs1",
		addresses=[0x26a5700,0x26a5702],
		number_of_bytes=2,
		possible_values=[New_Ninjamon_Deck[0]],
		is_little_endian=True, ),
	Attribute(
		name="Ninjamon Deck Champs2",
		addresses=[0x26a5704,0x26a5706,0x26a5708,0x26a570a],
		number_of_bytes=2,
		possible_values=[New_Ninjamon_Deck[1]],
		is_little_endian=True, ),
	Attribute(
		name="Ninjamon Deck Champs3",
		addresses=[0x26a570c,0x26a570e],
		number_of_bytes=2,
		possible_values=[New_Ninjamon_Deck[2]],
		is_little_endian=True, ),
	Attribute(
		name="Ninjamon Deck Champs4",
		addresses=[0x26a5710,0x26a5712],
		number_of_bytes=2,
		possible_values=[New_Ninjamon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Ninjamon Deck Rookies1",
		addresses=[0x26a5714,0x26a5716],
		number_of_bytes=2,
		possible_values=[New_Ninjamon_Deck[4]],
		is_little_endian=True, ),
	Attribute(
		name="Ninjamon Deck Rookies2",
		addresses=[0x26a5718,0x26a571a],
		number_of_bytes=2,
		possible_values=[New_Ninjamon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Ninjamon Deck Rookies3",
		addresses=[0x26a571c,0x26a571e],
		number_of_bytes=2,
		possible_values=[New_Ninjamon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Ninjamon Deck Rookies4",
		addresses=[0x26a5720,0x26a5722],
		number_of_bytes=2,
		possible_values=[New_Ninjamon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Ninjamon Deck Rookies5",
		addresses=[0x26a5724,0x26a5726],
		number_of_bytes=2,
		possible_values=[New_Ninjamon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Ninjamon Deck Option1",
		addresses=[0x26a5728,0x26a572a],
		number_of_bytes=2,
		possible_values=[New_Ninjamon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Ninjamon Deck Option2",
		addresses=[0x26a572c,0x26a572e,0x26a5730,0x26a5732],
		number_of_bytes=2,
		possible_values=[New_Ninjamon_Deck[10]],
		is_little_endian=True, ),
    Attribute(
		name="Ninjamon Deck Option3",
		addresses=[0x26a5734,0x26a5736,0x26a5738,0x26a573a],
		number_of_bytes = 2,
		possible_values = [New_Ninjamon_Deck[11]],
		is_little_endian = True, ),
# veedramon = 215,247,248,251,265,264,264,266,266,
    Attribute(
        name="Veedramon Deck Ult1",
        addresses=[0x26a576e,0x26a5770],
        number_of_bytes=2,
        possible_values=[New_Veedramon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Veedramon Deck Ult2",
        addresses=[0x26a5772],
        number_of_bytes=2,
        possible_values=[New_Veedramon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Veedramon Deck Champ1",
        addresses=[0x26a5774,0x26a5776,0x26a5778,0x26a577a],
        number_of_bytes=2,
        possible_values=[New_Veedramon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Veedramon Deck Champ2",
        addresses=[0x26a577c,0x26a577e,0x26a5780],
        number_of_bytes=2,
        possible_values=[New_Veedramon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Veedramon Deck Rookie1",
        addresses=[0x26a5782,0x26a5784,0x26a5786],
        number_of_bytes=2,
        possible_values=[New_Veedramon_Deck[4]],
        is_little_endian=True, ),
    Attribute(
        name="Veedramon Deck Rookie2",
        addresses=[0x26a5788,0x26a578a,0x26a578c],
        number_of_bytes=2,
        possible_values=[New_Veedramon_Deck[5]],
        is_little_endian=True, ),
    Attribute(
        name="Veedramon Deck Rookie3",
        addresses=[0x26a578e,0x26a5790,0x26a5792],
        number_of_bytes=2,
        possible_values=[New_Veedramon_Deck[6]],
        is_little_endian=True, ),
    Attribute(
        name="Veedramon Deck Rookie4",
        addresses=[0x26a5794,0x26a5796],
        number_of_bytes=2,
        possible_values=[New_Veedramon_Deck[7]],
        is_little_endian=True, ),
    Attribute(
        name="Veedramon Deck Option1",
        addresses=[0x26a5798],
        number_of_bytes=2,
        possible_values=[New_Veedramon_Deck[8]],
        is_little_endian=True, ),
    Attribute(
        name="Veedramon Deck Option2",
        addresses=[0x26a579a],
        number_of_bytes=2,
        possible_values=[New_Veedramon_Deck[9]],
        is_little_endian=True, ),
    Attribute(
        name="Veedramon Deck Option3",
        addresses=[0x26a579c],
        number_of_bytes=2,
        possible_values=[New_Veedramon_Deck[10]],
        is_little_endian=True, ),
    Attribute(
        name="Veedramon Deck Option4",
        addresses=[0x26a579e],
        number_of_bytes=2,
        possible_values=[New_Veedramon_Deck[11]],
        is_little_endian=True, ),
    Attribute(
        name="Veedramon Deck Option5",
        addresses=[0x26a57a0],
        number_of_bytes=2,
        possible_values=[New_Veedramon_Deck[12]],
        is_little_endian=True, ),
    Attribute(
        name="Veedramon Deck Option6",
        addresses=[0x26a57a2,0x26a57a4],
        number_of_bytes=2,
        possible_values=[New_Veedramon_Deck[13]],
        is_little_endian=True, ),
    Attribute(
        name="Veedramon Deck Option7",
        addresses=[0x26a57a6,0x26a57a8],
        number_of_bytes=2,
        possible_values=[New_Veedramon_Deck[14]],
        is_little_endian=True, ),

#Wormmon_Deck = [261,261,263,263,264,264,269]
    Attribute(
        name="Wormmon Deck 1",
        addresses=[0x26a57dc,0x26a57de],
        number_of_bytes=2,
        possible_values=[New_Wormmon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Wormmon Deck 2",
        addresses=[0x26a57e0],
        number_of_bytes=2,
        possible_values=[New_Wormmon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Wormmon Deck 3",
        addresses=[0x26a57e2,0x26a57e4],
        number_of_bytes=2,
        possible_values=[New_Wormmon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Wormmon Deck 4",
        addresses=[0x26a57e6,0x26a57e8],
        number_of_bytes=2,
        possible_values=[New_Wormmon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Wormmon Deck 5",
        addresses=[0x26a57ea,0x26a57ec],
        number_of_bytes=2,
        possible_values=[New_Wormmon_Deck[4]],
        is_little_endian=True, ),
    Attribute(
        name="Wormmon Deck 6",
        addresses=[0x26a57ee,0x26a57f0,0x26a57f2],
        number_of_bytes=2,
        possible_values=[New_Wormmon_Deck[5]],
        is_little_endian=True, ),
    Attribute(
        name="Wormmon Deck 7",
        addresses=[0x26a57f4,0x26a57f6,0x26a57f8],
        number_of_bytes=2,
        possible_values=[New_Wormmon_Deck[6]],
        is_little_endian=True, ),
    Attribute(
        name="Wormmon Deck 8",
        addresses=[0x26a57fa,0x26a57fc,0x26a57fe],
        number_of_bytes=2,
        possible_values=[New_Wormmon_Deck[7]],
        is_little_endian=True, ),
    Attribute(
        name="Wormmon Deck 9",
        addresses=[0x26a5800,0x26a5802],
        number_of_bytes=2,
        possible_values=[New_Wormmon_Deck[8]],
        is_little_endian=True, ),
    Attribute(
        name="Wormmon Deck 10",
        addresses=[0x26a5804],
        number_of_bytes=2,
        possible_values=[187],
        is_little_endian=True, ),
    Attribute(
        name="Wormmon Deck 11",
        addresses=[0x26a5806,0x26a5808],
        number_of_bytes=2,
        possible_values=[New_Wormmon_Deck[10]],
        is_little_endian=True, ),
    Attribute(
        name="Wormmon Deck 12",
        addresses=[0x26a580a,0x26a580c],
        number_of_bytes=2,
        possible_values=[New_Wormmon_Deck[11]],
        is_little_endian=True, ),
    Attribute(
        name="Wormmon Deck 13",
        addresses=[0x26a580e,0x26a5810],
        number_of_bytes=2,
        possible_values=[New_Wormmon_Deck[12]],
        is_little_endian=True, ),
    Attribute(
        name="Wormmon Deck 14",
        addresses=[0x26a5812,0x26a5814],
        number_of_bytes=2,
        possible_values=[New_Wormmon_Deck[13]],
        is_little_endian=True, ),
    Attribute(
        name="Wormmon Deck 15",
        addresses=[0x26a5816],
        number_of_bytes=2,
        possible_values=[New_Wormmon_Deck[14]],
        is_little_endian=True, ),
#Frigimon_Deck
    Attribute(
        name="Frigimon Deck 1",
        addresses=[0x26a584a],
        number_of_bytes=2,
        possible_values=[New_Frigimon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Frigimon Deck 2",
        addresses=[0x26a584c],
        number_of_bytes=2,
        possible_values=[New_Frigimon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Frigimon Deck 3",
        addresses=[0x26a584e,0x26a5850,0x26a5852,0x26a5854],
        number_of_bytes=2,
        possible_values=[New_Frigimon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Frigimon Deck 4",
        addresses=[0x26a5856],
        number_of_bytes=2,
        possible_values=[New_Frigimon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Frigimon Deck 5",
        addresses=[0x26a5858,0x26a585a],
        number_of_bytes=2,
        possible_values=[New_Frigimon_Deck[4]],
        is_little_endian=True, ),
    Attribute(
        name="Frigimon Deck 6",
        addresses=[0x26a585c,0x26a585e],
        number_of_bytes=2,
        possible_values=[New_Frigimon_Deck[5]],
        is_little_endian=True, ),
    Attribute(
        name="Frigimon Deck 7",
        addresses=[0x26a5860,0x26a5862],
        number_of_bytes=2,
        possible_values=[New_Frigimon_Deck[6]],
        is_little_endian=True, ),
    Attribute(
        name="Frigimon Deck 8",
        addresses=[0x26a5864,0x26a5866,0x26a5868],
        number_of_bytes=2,
        possible_values=[New_Frigimon_Deck[7]],
        is_little_endian=True, ),
    Attribute(
        name="Frigimon Deck 9",
        addresses=[0x26a586a,0x26a586c,0x26a586e],
        number_of_bytes=2,
        possible_values=[New_Frigimon_Deck[8]],
        is_little_endian=True, ),
    Attribute(
        name="Frigimon Deck 10",
        addresses=[0x26a5870],
        number_of_bytes=2,
        possible_values=[New_Frigimon_Deck[9]],
        is_little_endian=True, ),
    Attribute(
        name="Frigimon Deck 11",
        addresses=[0x26a5872,0x26a5874],
        number_of_bytes=2,
        possible_values=[New_Frigimon_Deck[10]],
        is_little_endian=True, ),
    Attribute(
        name="Frigimon Deck 12",
        addresses=[0x26a5876,0x26a5878],
        number_of_bytes=2,
        possible_values=[New_Frigimon_Deck[11]],
        is_little_endian=True, ),
    Attribute(
        name="Frigimon Deck 13",
        addresses=[0x26a587a,0x26a587c,0x26a587e],
        number_of_bytes=2,
        possible_values=[New_Frigimon_Deck[12]],
        is_little_endian=True, ),
    Attribute(
        name="Frigimon Deck 14",
        addresses=[0x26a5880,0x26a5882],
        number_of_bytes=2,
        possible_values=[New_Frigimon_Deck[13]],
        is_little_endian=True, ),
    Attribute(
        name="Frigimon Deck 15",
        addresses=[0x26a5884],
        number_of_bytes=2,
        possible_values=[New_Frigimon_Deck[14]],
        is_little_endian=True, ),
#Whamon_Deck
    Attribute(
        name="Whamon Deck 1",
        addresses=[0x26a58b8],
        number_of_bytes=2,
        possible_values=[New_Whamon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Whamon Deck 2",
        addresses=[0x26a58ba],
        number_of_bytes=2,
        possible_values=[New_Whamon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Whamon Deck 3",
        addresses=[0x26a58bc],
        number_of_bytes=2,
        possible_values=[New_Whamon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Whamon Deck 4",
        addresses=[0x26a58be,0x26a58c0],
        number_of_bytes=2,
        possible_values=[New_Whamon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Whamon Deck 5",
        addresses=[0x26a58c2,0x26a58c4],
        number_of_bytes=2,
        possible_values=[New_Whamon_Deck[4]],
        is_little_endian=True, ),
    Attribute(
        name="Whamon Deck 6",
        addresses=[0x26a58c6,0x26a58c8],
        number_of_bytes=2,
        possible_values=[New_Whamon_Deck[5]],
        is_little_endian=True, ),
    Attribute(
        name="Whamon Deck 7",
        addresses=[0x26a58ca],
        number_of_bytes=2,
        possible_values=[New_Whamon_Deck[6]],
        is_little_endian=True, ),
    Attribute(
        name="Whamon Deck 8",
        addresses=[0x26a58cc,0x26a58ce,0x26a58d0],
        number_of_bytes=2,
        possible_values=[New_Whamon_Deck[7]],
        is_little_endian=True, ),
    Attribute(
        name="Whamon Deck 9",
        addresses=[0x26a58d2,0x26a58d4,0x26a58d6],
        number_of_bytes=2,
        possible_values=[New_Whamon_Deck[8]],
        is_little_endian=True, ),
    Attribute(
        name="Whamon Deck 10",
        addresses=[0x26a58d8,0x26a58da,0x26a58dc],
        number_of_bytes=2,
        possible_values=[New_Whamon_Deck[9]],
        is_little_endian=True, ),
    Attribute(
        name="Whamon Deck 11",
        addresses=[0x26a58de,0x26a58e0,0x26a58e2],
        number_of_bytes=2,
        possible_values=[New_Whamon_Deck[10]],
        is_little_endian=True, ),
    Attribute(
        name="Whamon Deck 12",
        addresses=[0x26a58e4,0x26a58e6],
        number_of_bytes=2,
        possible_values=[New_Whamon_Deck[11]],
        is_little_endian=True, ),
    Attribute(
        name="Whamon Deck 13",
        addresses=[0x26a58e8,0x26a58ea],
        number_of_bytes=2,
        possible_values=[New_Whamon_Deck[12]],
        is_little_endian=True, ),
    Attribute(
        name="Whamon Deck 14",
        addresses=[0x26a58ec,0x26a58ee],
        number_of_bytes=2,
        possible_values=[New_Whamon_Deck[13]],
        is_little_endian=True, ),
    Attribute(
        name="Whamon Deck 15",
        addresses=[0x26a58f0,0x26a58f2],
        number_of_bytes=2,
        possible_values=[New_Whamon_Deck[14]],
        is_little_endian=True, ),
#Garurumon_Deck
    Attribute(
        name="Garurumon Deck 1",
        addresses=[0x26a5926],
        number_of_bytes=2,
        possible_values=[New_Garurumon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Garurumon Deck 2",
        addresses=[0x26a5928,0x26a592a],
        number_of_bytes=2,
        possible_values=[New_Garurumon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Garurumon Deck 3",
        addresses=[0x26a592c,0x26a592e,0x26a5930,0x26a5932],
        number_of_bytes=2,
        possible_values=[New_Garurumon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Garurumon Deck 4",
        addresses=[0x26a5934,0x26a5936],
        number_of_bytes=2,
        possible_values=[New_Garurumon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Garurumon Deck 5",
        addresses=[	0x26a5938,0x26a593a],
        number_of_bytes=2,
        possible_values=[New_Garurumon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Garurumon Deck 6",
		addresses=[	0x26a593c,0x26a593e,0x26a5940],
		number_of_bytes=2,
		possible_values=[New_Garurumon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Garurumon Deck 7",
		addresses=[	0x26a5942,0x26a5944,0x26a5946],
		number_of_bytes=2,
		possible_values=[New_Garurumon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Garurumon Deck 8",
		addresses=[	0x26a5948,0x26a594a],
		number_of_bytes=2,
		possible_values=[New_Garurumon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Garurumon Deck 9",
		addresses=[	0x26a594c,0x26a594e,0x26a5950],
		number_of_bytes=2,
		possible_values=[New_Garurumon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Garurumon Deck 10",
		addresses=[	0x26a5952,0x26a5954],
		number_of_bytes=2,
		possible_values=[New_Garurumon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Garurumon Deck 11",
		addresses=[	0x26a5956,0x26a5958],
		number_of_bytes=2,
		possible_values=[New_Garurumon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Garurumon Deck 12",
		addresses=[	0x26a595a,0x26a595c],
		number_of_bytes=2,
		possible_values=[New_Garurumon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Garurumon Deck 13",
		addresses=[	0x26a595e,0x26a5960],
		number_of_bytes=2,
		possible_values=[New_Garurumon_Deck[12]],
		is_little_endian=True, ),
#Stingmon_Deck
    Attribute(
        name="Stingmon Deck 1",
        addresses=[0x26a5994,0x26a5996],
        number_of_bytes=2,
        possible_values=[New_Stingmon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Stingmon Deck 2",
        addresses=[0x26a5998,0x26a599a],
        number_of_bytes=2,
        possible_values=[New_Stingmon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Stingmon Deck 3",
        addresses=[0x26a599c,0x26a599e],
        number_of_bytes=2,
        possible_values=[New_Stingmon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Stingmon Deck 4",
        addresses=[0x26a59a0,0x26a59a2],
        number_of_bytes=2,
        possible_values=[New_Stingmon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Stingmon Deck 5",
        addresses=[0x26a59a4,0x26a59a6],
        number_of_bytes=2,
        possible_values=[New_Stingmon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Stingmon Deck 6",
		addresses=[0x26a59a8,0x26a59aa,0x26a59ac],
		number_of_bytes=2,
		possible_values=[New_Stingmon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Stingmon Deck 7",
		addresses=[0x26a59ae,0x26a59b0,0x26a59b2,0x26a59b4],
		number_of_bytes=2,
		possible_values=[New_Stingmon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Stingmon Deck 8",
		addresses=[0x26a59b6,0x26a59b8,0x26a59ba],
		number_of_bytes=2,
		possible_values=[New_Stingmon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Stingmon Deck 9",
		addresses=[0x26a59bc],
		number_of_bytes=2,
		possible_values=[New_Stingmon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Stingmon Deck 10",
		addresses=[0x26a59be],
		number_of_bytes=2,
		possible_values=[New_Stingmon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Stingmon Deck 11",
		addresses=[0x26a59c0],
		number_of_bytes=2,
		possible_values=[New_Stingmon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Stingmon Deck 12",
		addresses=[0x26a59c2],
		number_of_bytes=2,
		possible_values=[New_Stingmon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Stingmon Deck 13",
		addresses=[0x26a59c4],
		number_of_bytes=2,
		possible_values=[New_Stingmon_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Stingmon Deck 14",
		addresses=[0x26a59c6],
		number_of_bytes=2,
		possible_values=[New_Stingmon_Deck[13]],
		is_little_endian=True, ),
	Attribute(
		name="Stingmon Deck 15",
		addresses=[0x26a59c8],
		number_of_bytes=2,
		possible_values=[New_Stingmon_Deck[14]],
		is_little_endian=True, ),
	Attribute(
		name="Stingmon Deck 16",
		addresses=[0x26a59ca],
		number_of_bytes=2,
		possible_values=[New_Stingmon_Deck[15]],
		is_little_endian=True, ),
	Attribute(
		name="Stingmon Deck 17",
		addresses=[0x26a59cc,0x26a59ce],
		number_of_bytes=2,
		possible_values=[New_Stingmon_Deck[16]],
		is_little_endian=True, ),
#Garurumon2_Deck
    Attribute(
        name="Garurumon2 Deck 1",
        addresses=[0x26a972c],
        number_of_bytes=2,
        possible_values=[New_Garurumon2_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Garurumon2 Deck 2",
        addresses=[0x26a972e,0x26a9730],
        number_of_bytes=2,
        possible_values=[New_Garurumon2_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Garurumon2 Deck 3",
        addresses=[0x26a9732,0x26a9734,0x26a9736,0x26a9738],
        number_of_bytes=2,
        possible_values=[New_Garurumon2_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Garurumon2 Deck 4",
        addresses=[0x26a973a,0x26a973c],
        number_of_bytes=2,
        possible_values=[New_Garurumon2_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Garurumon2 Deck 5",
        addresses=[0x26a973e,0x26a9740],
        number_of_bytes=2,
        possible_values=[New_Garurumon2_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Garurumon2 Deck 6",
		addresses=[0x26a9742,0x26a9744,0x26a9746],
		number_of_bytes=2,
		possible_values=[New_Garurumon2_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Garurumon2 Deck 7",
		addresses=[0x26a9748,0x26a974a,0x26a974c],
		number_of_bytes=2,
		possible_values=[New_Garurumon2_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Garurumon2 Deck 8",
		addresses=[0x26a974e,0x26a9750],
		number_of_bytes=2,
		possible_values=[New_Garurumon2_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Garurumon2 Deck 9",
		addresses=[0x26a9752,0x26a9754,0x26a9756],
		number_of_bytes=2,
		possible_values=[New_Garurumon2_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Garurumon2 Deck 10",
		addresses=[0x26a9758,0x26a975a],
		number_of_bytes=2,
		possible_values=[New_Garurumon2_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Garurumon2 Deck 11",
		addresses=[0x26a975c,0x26a975e],
		number_of_bytes=2,
		possible_values=[New_Garurumon2_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Garurumon2 Deck 12",
		addresses=[0x26a9760,0x26a9762],
		number_of_bytes=2,
		possible_values=[New_Garurumon2_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Garurumon2 Deck 13",
		addresses=[0x26a9764,0x26a9766],
		number_of_bytes=2,
		possible_values=[New_Garurumon2_Deck[12]],
		is_little_endian=True, ),        
#Hagurumon_Deck
    Attribute(
        name="Hagurumon Deck 1",
        addresses=[0x26a5a02],
        number_of_bytes=2,
        possible_values=[New_Hagurumon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Hagurumon Deck 2",
        addresses=[0x26a5a04],
        number_of_bytes=2,
        possible_values=[New_Hagurumon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Hagurumon Deck 3",
        addresses=[0x26a5a06],
        number_of_bytes=2,
        possible_values=[New_Hagurumon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Hagurumon Deck 4",
        addresses=[0x26a5a08,0x26a5a0a],
        number_of_bytes=2,
        possible_values=[New_Hagurumon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Hagurumon Deck 5",
        addresses=[0x26a5a0c,0x26a5a0e],
        number_of_bytes=2,
        possible_values=[New_Hagurumon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Hagurumon Deck 6",
		addresses=[0x26a5a10,0x26a5a12],
		number_of_bytes=2,
		possible_values=[New_Hagurumon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Hagurumon Deck 7",
		addresses=[0x26a5a14,0x26a5a16],
		number_of_bytes=2,
		possible_values=[New_Hagurumon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Hagurumon Deck 8",
		addresses=[0x26a5a18,0x26a5a1a,0x26a5a1c,0x26a5a1e],
		number_of_bytes=2,
		possible_values=[New_Hagurumon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Hagurumon Deck 9",
		addresses=[0x26a5a20, 0x26a5a22],
		number_of_bytes=2,
		possible_values=[New_Hagurumon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Hagurumon Deck 10",
		addresses=[0x26a5a24,0x26a5a26],
		number_of_bytes=2,
		possible_values=[New_Hagurumon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Hagurumon Deck 11",
		addresses=[0x26a5a28,0x26a5a2a],
		number_of_bytes=2,
		possible_values=[New_Hagurumon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Hagurumon Deck 12",
		addresses=[0x26a5a2c,0x26a5a2e],
		number_of_bytes=2,
		possible_values=[New_Hagurumon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Hagurumon Deck 13",
		addresses=[0x26a5a30,0x26a5a32],
		number_of_bytes=2,
		possible_values=[New_Hagurumon_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Hagurumon Deck 14",
		addresses=[0x26a5a34],
		number_of_bytes=2,
		possible_values=[New_Hagurumon_Deck[13]],
		is_little_endian=True, ),
	Attribute(
		name="Hagurumon Deck 15",
		addresses=[0x26a5a36],
		number_of_bytes=2,
		possible_values=[New_Hagurumon_Deck[14]],
		is_little_endian=True, ),
	Attribute(
		name="Hagurumon Deck 16",
		addresses=[0x26a5a38,0x26a5a3a,0x26a5a3c],
		number_of_bytes=2,
		possible_values=[New_Hagurumon_Deck[15]],
		is_little_endian=True, ),
#ShellNumemon_Deck
    Attribute(
        name="ShellNumemon Deck 1",
        addresses=[0x26a5a70,0x26a5a72,0x26a5a74,0x26a5a76],
        number_of_bytes=2,
        possible_values=[New_ShellNumemon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="ShellNumemon Deck 2",
        addresses=[0x26a5a78,0x26a5a7a,0x26a5a7c],
        number_of_bytes=2,
        possible_values=[New_ShellNumemon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="ShellNumemon Deck 3",
        addresses=[0x26a5a7e,0x26a5a80],
        number_of_bytes=2,
        possible_values=[New_ShellNumemon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="ShellNumemon Deck 4",
        addresses=[0x26a5a82,0x26a5a84,0x26a5a86],
        number_of_bytes=2,
        possible_values=[New_ShellNumemon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="ShellNumemon Deck 5",
        addresses=[0x26a5a88,0x26a5a8a,0x26a5a8c],
        number_of_bytes=2,
        possible_values=[New_ShellNumemon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="ShellNumemon Deck 6",
		addresses=[0x26a5a8e,0x26a5a90,0x26a5a92],
		number_of_bytes=2,
		possible_values=[New_ShellNumemon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="ShellNumemon Deck 7",
		addresses=[0x26a5a94,0x26a5a96],
		number_of_bytes=2,
		possible_values=[New_ShellNumemon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="ShellNumemon Deck 8",
		addresses=[0x26a5a98,0x26a5a9a],
		number_of_bytes=2,
		possible_values=[New_ShellNumemon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="ShellNumemon Deck 9",
		addresses=[0x26a5a9c,0x26a5a9e],
		number_of_bytes=2,
		possible_values=[New_ShellNumemon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="ShellNumemon Deck 10",
		addresses=[0x26a5aa0],
		number_of_bytes=2,
		possible_values=[New_ShellNumemon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="ShellNumemon Deck 11",
		addresses=[0x26a5aa2,0x26a5aa4],
		number_of_bytes=2,
		possible_values=[New_ShellNumemon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="ShellNumemon Deck 12",
		addresses=[0x26a5aa6],
		number_of_bytes=2,
		possible_values=[New_ShellNumemon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="ShellNumemon Deck 13",
		addresses=[0x26a5aa8,0x26a5aaa],
		number_of_bytes=2,
		possible_values=[New_ShellNumemon_Deck[12]],
		is_little_endian=True, ),
#KingSukamon_Deck
    Attribute(
        name="KingSukamon Deck 1",
        addresses=[0x26a5ade,0x26a5ae0], 
        number_of_bytes=2,
        possible_values=[New_KingSukamon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="KingSukamon Deck 2",
        addresses=[0x26a5ae2],
        number_of_bytes=2,
        possible_values=[New_KingSukamon_Deck[1]], 
        is_little_endian=True, ),
    Attribute(
        name="KingSukamon Deck 3",
        addresses=[0x26a5ae4,0x26a5ae6,0x26a5ae8,0x26a5aea],
        number_of_bytes=2,
        possible_values=[New_KingSukamon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="KingSukamon Deck 4",
        addresses=[0x26a5aec],
        number_of_bytes=2,
        possible_values=[New_KingSukamon_Deck[3]], 
        is_little_endian=True, ),
    Attribute(
        name="KingSukamon Deck 5",
        addresses=[0x26a5aee,0x26a5af0,0x26a5af2], 
        number_of_bytes=2,
        possible_values=[New_KingSukamon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="KingSukamon Deck 6",
		addresses=[0x26a5af4,0x26a5af6,0x26a5af8,0x26a5afa], 
		number_of_bytes=2,
		possible_values=[New_KingSukamon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="KingSukamon Deck 7",
		addresses=[0x26a5afc,0x26a5afe,0x26a5b00], 
		number_of_bytes=2,
		possible_values=[New_KingSukamon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="KingSukamon Deck 8",
		addresses=[0x26a5b02,0x26a5b04,0x26a5b06],
		number_of_bytes=2,
		possible_values=[New_KingSukamon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="KingSukamon Deck 9",
		addresses=[0x26a5b08,0x26a5b0a],
		number_of_bytes=2,
		possible_values=[New_KingSukamon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="KingSukamon Deck 10",
		addresses=[0x26a5b0c,0x26a5b0e,0x26a5b10,0x26a5b12],
		number_of_bytes=2,
		possible_values=[New_KingSukamon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="KingSukamon Deck 11",
		addresses=[0x26a5b14,0x26a5b16,0x26a5b18],
		number_of_bytes=2,
		possible_values=[New_KingSukamon_Deck[10]],
		is_little_endian=True, ),
#Shadramon_Deck
    Attribute(
        name="Shadramon Deck 1",
        addresses=[0x26a5b4c],
        number_of_bytes=2,
        possible_values=[New_Shadramon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Shadramon Deck 2",
        addresses=[0x26a5b4e],
        number_of_bytes=2,
        possible_values=[New_Shadramon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Shadramon Deck 3",
        addresses=[0x26a5b50,0x26a5b52],
        number_of_bytes=2,
        possible_values=[New_Shadramon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Shadramon Deck 4",
        addresses=[0x26a5b54,0x26a5b56,0x26a5b58],
        number_of_bytes=2,
        possible_values=[New_Shadramon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Shadramon Deck 5",
        addresses=[0x26a5b5a,0x26a5b5c,0x26a5b5e,0x26a5b60],
        number_of_bytes=2,
        possible_values=[New_Shadramon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Shadramon Deck 6",
		addresses=[0x26a5b62,0x26a5b64],
		number_of_bytes=2,
		possible_values=[New_Shadramon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Shadramon Deck 7",
		addresses=[0x26a5b66,0x26a5b68,0x26a5b6a,0x26a5b6c],
		number_of_bytes=2,
		possible_values=[New_Shadramon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Shadramon Deck 8",
		addresses=[0x26a5b6e,0x26a5b70],
		number_of_bytes=2,
		possible_values=[New_Shadramon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Shadramon Deck 9",
		addresses=[0x26a5b72,0x26a5b74],
		number_of_bytes=2,
		possible_values=[New_Shadramon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Shadramon Deck 10",
		addresses=[0x26a5b76,0x26a5b78],
		number_of_bytes=2,
		possible_values=[New_Shadramon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Shadramon Deck 11",
		addresses=[0x26a5b7a],
		number_of_bytes=2,
		possible_values=[New_Shadramon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Shadramon Deck 12",
		addresses=[0x26a5b7c,0x26a5b7e],
		number_of_bytes=2,
		possible_values=[New_Shadramon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Shadramon Deck 13",
		addresses=[0x26a5b80,0x26a5b82],
		number_of_bytes=2,
		possible_values=[New_Shadramon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Shadramon Deck 14",
		addresses=[0x26a5b84, 0x26a5b86],
		number_of_bytes=2,
		possible_values=[New_Shadramon_Deck[12]],
		is_little_endian=True, ),
#Wormmon2_Deck
    Attribute(
        name="Wormmon2 Deck 1",
        addresses=[0x26a5cea],
        number_of_bytes=2,
        possible_values=[New_Wormmon2_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Wormmon2 Deck 2",
        addresses=[0x26a5cec],
        number_of_bytes=2,
        possible_values=[New_Wormmon2_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Wormmon2 Deck 3",
        addresses=[0x26a5cee,0x26a5cf0],
        number_of_bytes=2,
        possible_values=[New_Wormmon2_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Wormmon2 Deck 4",
        addresses=[0x26a5cf2,0x26a5cf4],
        number_of_bytes=2,
        possible_values=[New_Wormmon2_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Wormmon2 Deck 5",
        addresses=[0x26a5cf6,0x26a5cf8],
        number_of_bytes=2,
        possible_values=[New_Wormmon2_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Wormmon2 Deck 6",
		addresses=[0x26a5cfa],
		number_of_bytes=2,
		possible_values=[New_Wormmon2_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Wormmon2 Deck 7",
		addresses=[0x26a5cfc,0x26a5cfe,0x26a5d00],
		number_of_bytes=2,
		possible_values=[New_Wormmon2_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Wormmon2 Deck 8",
		addresses=[0x26a5d02,0x26a5d04],
		number_of_bytes=2,
		possible_values=[New_Wormmon2_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Wormmon2 Deck 9",
		addresses=[0x26a5d06,0x26a5d08,0x26a5d0a],
		number_of_bytes=2,
		possible_values=[New_Wormmon2_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Wormmon2 Deck 10",
		addresses=[0x26a5d0c,0x26a5d0e],
		number_of_bytes=2,
		possible_values=[New_Wormmon2_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Wormmon2 Deck 11",
		addresses=[0x26a5d10],
		number_of_bytes=2,
		possible_values=[New_Wormmon2_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Wormmon2 Deck 12",
		addresses=[0x26a5d12,0x26a5d14],
		number_of_bytes=2,
		possible_values=[New_Wormmon2_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Wormmon2 Deck 13",
		addresses=[0x26a5d16,0x26a5d18],
		number_of_bytes=2,
		possible_values=[New_Wormmon2_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Wormmon2 Deck 14",
		addresses=[0x26a5d1a,0x26a5d1c],
		number_of_bytes=2,
		possible_values=[New_Wormmon2_Deck[13]],
		is_little_endian=True, ),
	Attribute(
		name="Wormmon2 Deck 15",
		addresses=[0x26a5d1e,0x26a5d20],
		number_of_bytes=2,
		possible_values=[New_Wormmon2_Deck[14]],
		is_little_endian=True, ),
	Attribute(
		name="Wormmon2 Deck 16",
		addresses=[0x26a5d22],
		number_of_bytes=2,
		possible_values=[New_Wormmon2_Deck[15]],
		is_little_endian=True, ),
	Attribute(
		name="Wormmon2 Deck 17",
		addresses=[0x26a5d24],
		number_of_bytes=2,
		possible_values=[New_Wormmon2_Deck[16]],
		is_little_endian=True, ),
#Stingmon2_Deck
    Attribute(
        name="Stingmon2 Deck 1",
        addresses=[0x26a5d58,0x26a5d5a],
        number_of_bytes=2,
        possible_values=[New_Stingmon2_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Stingmon2 Deck 2",
        addresses=[0x26a5d5c,0x26a5d5e],
        number_of_bytes=2,
        possible_values=[New_Stingmon2_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Stingmon2 Deck 3",
        addresses=[0x26a5d60,0x26a5d62,0x26a5d64,0x26a5d66],
        number_of_bytes=2,
        possible_values=[New_Stingmon2_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Stingmon2 Deck 4",
        addresses=[0x26a5d68],
        number_of_bytes=2,
        possible_values=[New_Stingmon2_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Stingmon2 Deck 5",
        addresses=[0x26a5d6a,0x26a5d6c],
        number_of_bytes=2,
        possible_values=[New_Stingmon2_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Stingmon2 Deck 6",
		addresses=[0x26a5d6e,0x26a5d70],
		number_of_bytes=2,
		possible_values=[New_Stingmon2_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Stingmon2 Deck 7",
		addresses=[0x26a5d72,0x26a5d74,0x26a5d76,0x26a5d78],
		number_of_bytes=2,
		possible_values=[New_Stingmon2_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Stingmon2 Deck 8",
		addresses=[0x26a5d7a,0x26a5d7c,0x26a5d7e],
		number_of_bytes=2,
		possible_values=[New_Stingmon2_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Stingmon2 Deck 9",
		addresses=[0x26a5d80],
		number_of_bytes=2,
		possible_values=[New_Stingmon2_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Stingmon2 Deck 10",
		addresses=[0x26a5d82],
		number_of_bytes=2,
		possible_values=[New_Stingmon2_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Stingmon2 Deck 11",
		addresses=[0x26a5d84],
		number_of_bytes=2,
		possible_values=[New_Stingmon2_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Stingmon2 Deck 12",
		addresses=[0x26a5d86],
		number_of_bytes=2,
		possible_values=[New_Stingmon2_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Stingmon2 Deck 13",
		addresses=[0x26a5d88],
		number_of_bytes=2,
		possible_values=[New_Stingmon2_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Stingmon2 Deck 14",
		addresses=[0x26a5d8a],
		number_of_bytes=2,
		possible_values=[New_Stingmon2_Deck[13]],
		is_little_endian=True, ),
	Attribute(
		name="Stingmon2 Deck 15",
		addresses=[0x26a5d8c],
		number_of_bytes=2,
		possible_values=[New_Stingmon2_Deck[14]],
		is_little_endian=True, ),
	Attribute(
		name="Stingmon2 Deck 16",
		addresses=[0x26a5d8e],
		number_of_bytes=2,
		possible_values=[New_Stingmon2_Deck[15]],
		is_little_endian=True, ),
	Attribute(
		name="Stingmon2 Deck 17",
		addresses=[0x26a5d90],
		number_of_bytes=2,
		possible_values=[New_Stingmon2_Deck[16]],
		is_little_endian=True, ),
	Attribute(
		name="Stingmon2 Deck 18",
		addresses=[0x26a5d92,0x26a5d94],
		number_of_bytes=2,
		possible_values=[New_Stingmon2_Deck[17]],
		is_little_endian=True, ),
#Shadramon2_Deck
    Attribute(
        name="Shadramon2 Deck 1",
        addresses=[0x26a5dc4],
        number_of_bytes=2,
        possible_values=[New_Shadramon2_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Shadramon2 Deck 2",
        addresses=[0x26a5dc6,0x26a5dc8],
        number_of_bytes=2,
        possible_values=[New_Shadramon2_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Shadramon2 Deck 3",
        addresses=[0x26a5dca],
        number_of_bytes=2,
        possible_values=[New_Shadramon2_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Shadramon2 Deck 4",
        addresses=[0x26a5dcc,0x26a5dce],
        number_of_bytes=2,
        possible_values=[New_Shadramon2_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Shadramon2 Deck 5",
        addresses=[0x26a5dd0,0x26a5dd2,0x26a5dd4],
        number_of_bytes=2,
        possible_values=[New_Shadramon2_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Shadramon2 Deck 6",
		addresses=[0x26a5dd6,0x26a5dd8],
		number_of_bytes=2,
		possible_values=[New_Shadramon2_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Shadramon2 Deck 7",
		addresses=[0x26a5dda,0x26a5ddc,0x26a5dde,0x26a5de0],
		number_of_bytes=2,
		possible_values=[New_Shadramon2_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Shadramon2 Deck 8",
		addresses=[0x26a5de2,0x26a5de4],
		number_of_bytes=2,
		possible_values=[New_Shadramon2_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Shadramon2 Deck 9",
		addresses=[0x26a5de6],
		number_of_bytes=2,
		possible_values=[New_Shadramon2_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Shadramon2 Deck 10",
		addresses=[0x26a5de8,0x26a5dea],
		number_of_bytes=2,
		possible_values=[New_Shadramon2_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Shadramon2 Deck 11",
		addresses=[0x26a5dec],
		number_of_bytes=2,
		possible_values=[New_Shadramon2_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Shadramon2 Deck 12",
		addresses=[0x26a5dee,0x26a5df0],
		number_of_bytes=2,
		possible_values=[New_Shadramon2_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Shadramon2 Deck 13",
		addresses=[0x26a5df2,0x26a5df4],
		number_of_bytes=2,
		possible_values=[New_Shadramon2_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Shadramon2 Deck 14",
		addresses=[0x26a5df6],
		number_of_bytes=2,
		possible_values=[New_Shadramon2_Deck[13]],
		is_little_endian=True, ),
	Attribute(
		name="Shadramon2 Deck 15",
		addresses=[0x26a5df8,0x26a5dfa],
		number_of_bytes=2,
		possible_values=[New_Shadramon2_Deck[14]],
		is_little_endian=True, ),
	Attribute(
		name="Shadramon2 Deck 16",
		addresses=[0x26a5dfc,0x26a5dfe],
		number_of_bytes=2,
		possible_values=[New_Shadramon2_Deck[15]],
		is_little_endian=True, ),
#Quetzalmon_Deck
    Attribute(
        name="Quetzalmon Deck 1",
        addresses=[0x26a5e34,0x26a5e36],
        number_of_bytes=2,
        possible_values=[New_Quetzalmon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Quetzalmon Deck 2",
        addresses=[0x26a5e38,0x26a5e3a],
        number_of_bytes=2,
        possible_values=[New_Quetzalmon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Quetzalmon Deck 3",
        addresses=[0x26a5e3c],
        number_of_bytes=2,
        possible_values=[New_Quetzalmon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Quetzalmon Deck 4",
        addresses=[0x26a5e3e,0x26a5e40],
        number_of_bytes=2,
        possible_values=[New_Quetzalmon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Quetzalmon Deck 5",
        addresses=[0x26a5e42],
        number_of_bytes=2,
        possible_values=[New_Quetzalmon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Quetzalmon Deck 6",
		addresses=[0x26a5e44,0x26a5e46],
		number_of_bytes=2,
		possible_values=[New_Quetzalmon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Quetzalmon Deck 7",
		addresses=[0x26a5e48,0x26a5e4a,0x26a5e4c],
		number_of_bytes=2,
		possible_values=[New_Quetzalmon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Quetzalmon Deck 8",
		addresses=[0x26a5e4e,0x26a5e50,0x26a5e52,0x26a5e54],
		number_of_bytes=2,
		possible_values=[New_Quetzalmon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Quetzalmon Deck 9",
		addresses=[0x26a5e56,0x26a5e58],
		number_of_bytes=2,
		possible_values=[New_Quetzalmon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Quetzalmon Deck 10",
		addresses=[0x26a5e5a,0x26a5e5c,0x26a5e5e],
		number_of_bytes=2,
		possible_values=[New_Quetzalmon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Quetzalmon Deck 11",
		addresses=[0x26a5e60],
		number_of_bytes=2,
		possible_values=[New_Quetzalmon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Quetzalmon Deck 12",
		addresses=[0x26a5e62],
		number_of_bytes=2,
		possible_values=[New_Quetzalmon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Quetzalmon Deck 13",
		addresses=[0x26a5e64,0x26a5e66],
		number_of_bytes=2,
		possible_values=[New_Quetzalmon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Quetzalmon Deck 14",
		addresses=[0x26a5e68,0x26a5e6a],
		number_of_bytes=2,
		possible_values=[New_Quetzalmon_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Quetzalmon Deck 15",
		addresses=[0x26a5e6c,0x26a5e6e],
		number_of_bytes=2,
		possible_values=[New_Quetzalmon_Deck[13]],
		is_little_endian=True, ),
#Digimon_Emperor_Deck
    Attribute(
        name="Digimon_Emperor Deck 1",
        addresses=[0x26a5ea2,0x26a5ea4],
        number_of_bytes=2,
        possible_values=[New_Digimon_Emperor_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Digimon_Emperor Deck 2",
        addresses=[0x26a5ea6],
        number_of_bytes=2,
        possible_values=[New_Digimon_Emperor_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Digimon_Emperor Deck 3",
        addresses=[0x26a5ea8,0x26a5eaa,0x26a5eac],
        number_of_bytes=2,
        possible_values=[New_Digimon_Emperor_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Digimon_Emperor Deck 4",
        addresses=[0x26a5eae,0x26a5eb0],
        number_of_bytes=2,
        possible_values=[New_Digimon_Emperor_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Digimon_Emperor Deck 5",
        addresses=[0x26a5eb2],
        number_of_bytes=2,
        possible_values=[New_Digimon_Emperor_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Digimon_Emperor Deck 6",
		addresses=[0x26a5eb4,0x26a5eb6],
		number_of_bytes=2,
		possible_values=[New_Digimon_Emperor_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Digimon_Emperor Deck 7",
		addresses=[0x26a5eb8,0x26a5eba],
		number_of_bytes=2,
		possible_values=[New_Digimon_Emperor_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Digimon_Emperor Deck 8",
		addresses=[0x26a5ebc,0x26a5ebe],
		number_of_bytes=2,
		possible_values=[New_Digimon_Emperor_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Digimon_Emperor Deck 9",
		addresses=[0x26a5ec0,0x26a5ec2,0x26a5ec4,0x26a5ec6],
		number_of_bytes=2,
		possible_values=[New_Digimon_Emperor_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Digimon_Emperor Deck 10",
		addresses=[0x26a5ec8],
		number_of_bytes=2,
		possible_values=[New_Digimon_Emperor_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Digimon_Emperor Deck 11",
		addresses=[0x26a5eca,0x26a5ecc],
		number_of_bytes=2,
		possible_values=[New_Digimon_Emperor_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Digimon_Emperor Deck 12",
		addresses=[0x26a5ece,0x26a5ed0,0x26a5ed2,0x26a5ed4],
		number_of_bytes=2,
		possible_values=[New_Digimon_Emperor_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Digimon_Emperor Deck 13",
		addresses=[0x26a5ed6,0x26a5ed8],
		number_of_bytes=2,
		possible_values=[New_Digimon_Emperor_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Digimon_Emperor Deck 14",
		addresses=[0x26a5eda,0x26a5edc],
		number_of_bytes=2,
		possible_values=[New_Digimon_Emperor_Deck[12]],
		is_little_endian=True, ),
#Centarumon_Deck
    Attribute(
        name="Centarumon Deck 1",
        addresses=[0x26a5f10,0x26a5f12,0x26a5f14],
        number_of_bytes=2,
        possible_values=[New_Centarumon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Centarumon Deck 2",
        addresses=[0x26a5f16,0x26a5f18],
        number_of_bytes=2,
        possible_values=[New_Centarumon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Centarumon Deck 3",
        addresses=[0x26a5f1a,0x26a5f1c,0x26a5f1e],
        number_of_bytes=2,
        possible_values=[New_Centarumon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Centarumon Deck 4",
        addresses=[0x26a5f20,0x26a5f22],
        number_of_bytes=2,
        possible_values=[New_Centarumon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Centarumon Deck 5",
        addresses=[0x26a5f24],
        number_of_bytes=2,
        possible_values=[New_Centarumon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Centarumon Deck 6",
		addresses=[0x26a5f26,0x26a5f28,0x26a5f2a,0x26a5f2c],
		number_of_bytes=2,
		possible_values=[New_Centarumon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Centarumon Deck 7",
		addresses=[0x26a5f2e,0x26a5f30,0x26a5f32,0x26a5f34],
		number_of_bytes=2,
		possible_values=[New_Centarumon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Centarumon Deck 8",
		addresses=[0x26a5f36,0x26a5f38],
		number_of_bytes=2,
		possible_values=[New_Centarumon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Centarumon Deck 9",
		addresses=[0x26a5f3a,0x26a5f3c,0x26a5f3e],
		number_of_bytes=2,
		possible_values=[New_Centarumon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Centarumon Deck 10",
		addresses=[0x26a5f40,0x26a5f42,0x26a5f44],
		number_of_bytes=2,
		possible_values=[New_Centarumon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Centarumon Deck 11",
		addresses=[0x26a5f42,0x26a5f44,0x26a5f46],
		number_of_bytes=2,
		possible_values=[New_Centarumon_Deck[10]],
		is_little_endian=True, ),
#Tyrannomon_Deck
    Attribute(
        name="Tyrannomon Deck 1",
        addresses=[0x26a5f7e,0x26a5f80,0x26a5f82],
        number_of_bytes=2,
        possible_values=[New_Tyrannomon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Tyrannomon Deck 2",
        addresses=[0x26a5f84],
        number_of_bytes=2,
        possible_values=[New_Tyrannomon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Tyrannomon Deck 3",
        addresses=[0x26a5f86,0x26a5f88,0x26a5f8a,0x26a5f8c],
        number_of_bytes=2,
        possible_values=[New_Tyrannomon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Tyrannomon Deck 4",
        addresses=[0x26a5f8e],
        number_of_bytes=2,
        possible_values=[New_Tyrannomon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Tyrannomon Deck 5",
        addresses=[0x26a5f90,0x26a5f92],
        number_of_bytes=2,
        possible_values=[New_Tyrannomon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Tyrannomon Deck 6",
		addresses=[0x26a5f94,0x26a5f96],
		number_of_bytes=2,
		possible_values=[New_Tyrannomon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Tyrannomon Deck 7",
		addresses=[0x26a5f98,0x26a5f9a,0x26a5f9c],
		number_of_bytes=2,
		possible_values=[New_Tyrannomon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Tyrannomon Deck 8",
		addresses=[0x26a5f9e,0x26a5fa0],
		number_of_bytes=2,
		possible_values=[New_Tyrannomon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Tyrannomon Deck 9",
		addresses=[0x26a5fa2,0x26a5fa4],
		number_of_bytes=2,
		possible_values=[New_Tyrannomon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Tyrannomon Deck 10",
		addresses=[0x26a5fa6,0x26a5fa8],
		number_of_bytes=2,
		possible_values=[New_Tyrannomon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Tyrannomon Deck 11",
		addresses=[0x26a5faa,0x26a5fac,0x26a5fae],
		number_of_bytes=2,
		possible_values=[New_Tyrannomon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Tyrannomon Deck 12",
		addresses=[0x26a5fb0,0x26a5fb2,0x26a5fb4],
		number_of_bytes=2,
		possible_values=[New_Tyrannomon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Tyrannomon Deck 13",
		addresses=[0x26a5fb6,0x26a5fb8],
		number_of_bytes=2,
		possible_values=[New_Tyrannomon_Deck[12]],
		is_little_endian=True, ),
#Angemon_Deck
    Attribute(
        name="Angemon Deck 1",
        addresses=[0x26a5fec],
        number_of_bytes=2,
        possible_values=[New_Angemon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Angemon Deck 2",
        addresses=[0x26a5fee,0x26a5ff0],
        number_of_bytes=2,
        possible_values=[New_Angemon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Angemon Deck 3",
        addresses=[0x26a5ff2,0x26a5ff4,0x26a5ff6,0x26a5ff8],
        number_of_bytes=2,
        possible_values=[New_Angemon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Angemon Deck 4",
        addresses=[0x26a5ffa,0x26a5ffc],
        number_of_bytes=2,
        possible_values=[New_Angemon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Angemon Deck 5",
        addresses=[0x26a5ffe,0x26a6000],
        number_of_bytes=2,
        possible_values=[New_Angemon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Angemon Deck 6",
		addresses=[0x26a6002,0x26a6004,0x26a6006],
		number_of_bytes=2,
		possible_values=[New_Angemon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Angemon Deck 7",
		addresses=[0x26a6008,0x26a600a,0x26a600c],
		number_of_bytes=2,
		possible_values=[New_Angemon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Angemon Deck 8",
		addresses=[0x26a600e,0x26a6010,0x26a6012,0x26a6014],
		number_of_bytes=2,
		possible_values=[New_Angemon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Angemon Deck 9",
		addresses=[0x26a6016,0x26a6018,0x26a601a],
		number_of_bytes=2,
		possible_values=[New_Angemon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Angemon Deck 10",
		addresses=[0x26a601c,0x26a601e,0x26a6020],
		number_of_bytes=2,
		possible_values=[New_Angemon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Angemon Deck 11",
		addresses=[0x26a6022,0x26a6024,0x26a6026],
		number_of_bytes=2,
		possible_values=[New_Angemon_Deck[10]],
		is_little_endian=True, ),
#Davis_Deck
    Attribute(
        name="Davis Deck 1",
        addresses=[0x26a6058,0x26a605a],
        number_of_bytes=2,
        possible_values=[New_Davis_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Davis Deck 2",
        addresses=[0x26a605c],
        number_of_bytes=2,
        possible_values=[New_Davis_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Davis Deck 3",
        addresses=[0x26a605e,0x26a6060,0x26a6062],
        number_of_bytes=2,
        possible_values=[New_Davis_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Davis Deck 4",
        addresses=[0x26a6064,0x26a6066],
        number_of_bytes=2,
        possible_values=[New_Davis_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Davis Deck 5",
        addresses=[0x26a6068],
        number_of_bytes=2,
        possible_values=[New_Davis_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Davis Deck 6",
		addresses=[0x26a606a],
		number_of_bytes=2,
		possible_values=[New_Davis_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Davis Deck 7",
		addresses=[0x26a606c,0x26a606e,0x26a6070],
		number_of_bytes=2,
		possible_values=[New_Davis_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Davis Deck 8",
		addresses=[0x26a6072,0x26a6074,0x26a6076],
		number_of_bytes=2,
		possible_values=[New_Davis_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Davis Deck 9",
		addresses=[0x26a6078,0x26a607a],
		number_of_bytes=2,
		possible_values=[New_Davis_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Davis Deck 10",
		addresses=[0x26a607c,0x26a607e],
		number_of_bytes=2,
		possible_values=[New_Davis_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Davis Deck 11",
		addresses=[0x26a6080],
		number_of_bytes=2,
		possible_values=[175],
		is_little_endian=True, ),
	Attribute(
		name="Davis Deck 12",
		addresses=[0x26a6082],
		number_of_bytes=2,
		possible_values=[New_Davis_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Davis Deck 13",
		addresses=[0x26a6084,0x26a6086,0x26a6088],
		number_of_bytes=2,
		possible_values=[New_Davis_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Davis Deck 14",
		addresses=[0x26a608a,0x26a608c,0x26a608e],
		number_of_bytes=2,
		possible_values=[New_Davis_Deck[13]],
		is_little_endian=True, ),
	Attribute(
		name="Davis Deck 15",
		addresses=[0x26a6090, 0x26a6092],
		number_of_bytes=2,
		possible_values=[New_Davis_Deck[14]],
		is_little_endian=True, ),
#Keeley_Deck
    Attribute(
        name="Keeley Deck 1",
        addresses=[0x26a60c8,0x26a60ca],
        number_of_bytes=2,
        possible_values=[New_Keeley_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Keeley Deck 2",
        addresses=[0x26a60cc],
        number_of_bytes=2,
        possible_values=[New_Keeley_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Keeley Deck 3",
        addresses=[0x26a60ce,0x26a60d0],
        number_of_bytes=2,
        possible_values=[New_Keeley_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Keeley Deck 4",
        addresses=[0x26a60d2,0x26a60d4,0x26a60d6],
        number_of_bytes=2,
        possible_values=[New_Keeley_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Keeley Deck 5",
        addresses=[0x26a60d8,0x26a60da],
        number_of_bytes=2,
        possible_values=[New_Keeley_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Keeley Deck 6",
		addresses=[0x26a60dc,0x26a60de,0x26a60e0],
		number_of_bytes=2,
		possible_values=[New_Keeley_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Keeley Deck 7",
		addresses=[0x26a60e2,0x26a60e4,0x26a60e6],
		number_of_bytes=2,
		possible_values=[New_Keeley_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Keeley Deck 8",
		addresses=[0x26a60e8,0x26a60ea,0x26a60ec],
		number_of_bytes=2,
		possible_values=[New_Keeley_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Keeley Deck 9",
		addresses=[0x26a60ee],
		number_of_bytes=2,
		possible_values=[182],
		is_little_endian=True, ),
	Attribute(
		name="Keeley Deck 10",
		addresses=[0x26a60f0],
		number_of_bytes=2,
		possible_values=[New_Keeley_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Keeley Deck 11",
		addresses=[0x26a60f2],
		number_of_bytes=2,
		possible_values=[New_Keeley_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Keeley Deck 12",
		addresses=[0x26a60f4],
		number_of_bytes=2,
		possible_values=[New_Keeley_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Keeley Deck 13",
		addresses=[0x26a60f6],
		number_of_bytes=2,
		possible_values=[New_Keeley_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Keeley Deck 14",
		addresses=[0x26a60f8],
		number_of_bytes=2,
		possible_values=[New_Keeley_Deck[13]],
		is_little_endian=True, ),
	Attribute(
		name="Keeley Deck 15",
		addresses=[0x26a60fa],
		number_of_bytes=2,
		possible_values=[New_Keeley_Deck[14]],
		is_little_endian=True, ),
	Attribute(
		name="Keeley Deck 16",
		addresses=[0x26a60fc],
		number_of_bytes=2,
		possible_values=[New_Keeley_Deck[15]],
		is_little_endian=True, ),
	Attribute(
		name="Keeley Deck 17",
		addresses=[0x26a60fe],
		number_of_bytes=2,
		possible_values=[New_Keeley_Deck[16]],
		is_little_endian=True, ),
	Attribute(
		name="Keeley Deck 18",
		addresses=[0x26a6100],
		number_of_bytes=2,
		possible_values=[New_Keeley_Deck[17]],
		is_little_endian=True, ),
	Attribute(
		name="Keeley Deck 19",
		addresses=[0x26a6102],
		number_of_bytes=2,
		possible_values=[New_Keeley_Deck[18]],
		is_little_endian=True, ),
#Cody_Deck
    Attribute(
        name="Cody Deck 1",
        addresses=[0x26a6136,0x26a6138],
        number_of_bytes=2,
        possible_values=[New_Cody_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Cody Deck 2",
        addresses=[0x26a613a],
        number_of_bytes=2,
        possible_values=[New_Cody_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Cody Deck 3",
        addresses=[0x26a613c,0x26a613e,0x26a6140],
        number_of_bytes=2,
        possible_values=[New_Cody_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Cody Deck 4",
        addresses=[0x26a6142,0x26a6144],
        number_of_bytes=2,
        possible_values=[New_Cody_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Cody Deck 5",
        addresses=[0x26a6146,0x26a6148],
        number_of_bytes=2,
        possible_values=[New_Cody_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Cody Deck 6",
		addresses=[0x26a614a,0x26a614c,0x26a614e],
		number_of_bytes=2,
		possible_values=[New_Cody_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Cody Deck 7",
		addresses=[0x26a6150,0x26a6152],
		number_of_bytes=2,
		possible_values=[New_Cody_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Cody Deck 8",
		addresses=[0x26a6154,0x26a6156],
		number_of_bytes=2,
		possible_values=[New_Cody_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Cody Deck 9",
		addresses=[0x26a6158,0x26a615a],
		number_of_bytes=2,
		possible_values=[190],
		is_little_endian=True, ),
	Attribute(
		name="Cody Deck 10",
		addresses=[0x26a615c],
		number_of_bytes=2,
		possible_values=[New_Cody_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Cody Deck 11",
		addresses=[0x26a615e,0x26a6160],
		number_of_bytes=2,
		possible_values=[New_Cody_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Cody Deck 12",
		addresses=[0x26a6162,0x26a6164],
		number_of_bytes=2,
		possible_values=[New_Cody_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Cody Deck 13",
		addresses=[0x26a6166,0x26a6168],
		number_of_bytes=2,
		possible_values=[New_Cody_Deck[12]],
		is_little_endian=True, ),
#TK
    Attribute(
        name="TK Deck 1",
        addresses=[0x26a61a4,0x26a61a6],
        number_of_bytes=2,
        possible_values=[New_TK_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="TK Deck 2",
        addresses=[0x26a61a8],
        number_of_bytes=2,
        possible_values=[New_TK_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="TK Deck 3",
        addresses=[0x26a61aa,0x26a61ac,0x26a61ae],
        number_of_bytes=2,
        possible_values=[New_TK_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="TK Deck 4",
        addresses=[0x26a61b0,0x26a61b2],
        number_of_bytes=2,
        possible_values=[New_TK_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="TK Deck 5",
        addresses=[0x26a61b4,0x26a61b6],
        number_of_bytes=2,
        possible_values=[New_TK_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="TK Deck 6",
		addresses=[0x26a61b8,0x26a61ba,0x26a61bc,0x26a61be],
		number_of_bytes=2,
		possible_values=[New_TK_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="TK Deck 7",
		addresses=[0x26a61c0],
		number_of_bytes=2,
		possible_values=[New_TK_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="TK Deck 8",
		addresses=[0x26a61c2,0x26a61c4,0x26a61c6,0x26a61c8],
		number_of_bytes=2,
		possible_values=[New_TK_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="TK Deck 9",
		addresses=[0x26a61ca],
		number_of_bytes=2,
		possible_values=[183],
		is_little_endian=True, ),
	Attribute(
		name="TK Deck 10",
		addresses=[0x26a61cc,0x26a61ce],
		number_of_bytes=2,
		possible_values=[New_TK_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="TK Deck 11",
		addresses=[0x26a61d0],
		number_of_bytes=2,
		possible_values=[New_TK_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="TK Deck 12",
		addresses=[0x26a61d2,0x26a61d4],
		number_of_bytes=2,
		possible_values=[New_TK_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="TK Deck 13",
		addresses=[0x26a61d6],
		number_of_bytes=2,
		possible_values=[New_TK_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="TK Deck 14",
		addresses=[0x26a61d8,0x26a61da],
		number_of_bytes=2,
		possible_values=[New_TK_Deck[13]],
		is_little_endian=True, ),
	Attribute(
		name="TK Deck 15",
		addresses=[0x26a61dc],
		number_of_bytes=2,
		possible_values=[New_TK_Deck[14]],
		is_little_endian=True, ),
	Attribute(
		name="TK Deck 16",
		addresses=[0x26a61de],
		number_of_bytes=2,
		possible_values=[New_TK_Deck[15]],
		is_little_endian=True, ),
#Wizardmon
    Attribute(
        name="Wizardmon Deck 1",
        addresses=[0x26a6212],
        number_of_bytes=2,
        possible_values=[New_Wizardmon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Wizardmon Deck 2",
        addresses=[0x26a6214,0x26a6216],
        number_of_bytes=2,
        possible_values=[New_Wizardmon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Wizardmon Deck 3",
        addresses=[0x26a6218,0x26a621a],
        number_of_bytes=2,
        possible_values=[New_Wizardmon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Wizardmon Deck 4",
        addresses=[0x26a621c,0x26a621e,0x26a6220,0x26a6222],
        number_of_bytes=2,
        possible_values=[New_Wizardmon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Wizardmon Deck 5",
        addresses=[0x26a6224],
        number_of_bytes=2,
        possible_values=[New_Wizardmon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Wizardmon Deck 6",
		addresses=[0x26a6226,0x26a6228,0x26a622a],
		number_of_bytes=2,
		possible_values=[New_Wizardmon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Wizardmon Deck 7",
		addresses=[0x26a622c,0x26a622e],
		number_of_bytes=2,
		possible_values=[New_Wizardmon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Wizardmon Deck 8",
		addresses=[0x26a6230,0x26a6232],
		number_of_bytes=2,
		possible_values=[New_Wizardmon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Wizardmon Deck 9",
		addresses=[0x26a6234,0x26a6236,0x26a6238],
		number_of_bytes=2,
		possible_values=[New_Wizardmon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Wizardmon Deck 10",
		addresses=[0x26a623a],
		number_of_bytes=2,
		possible_values=[New_Wizardmon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Wizardmon Deck 11",
		addresses=[0x26a623c],
		number_of_bytes=2,
		possible_values=[New_Wizardmon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Wizardmon Deck 12",
		addresses=[0x26a623e],
		number_of_bytes=2,
		possible_values=[New_Wizardmon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Wizardmon Deck 13",
		addresses=[0x26a6240],
		number_of_bytes=2,
		possible_values=[New_Wizardmon_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Wizardmon Deck 14",
		addresses=[0x26a6242],
		number_of_bytes=2,
		possible_values=[New_Wizardmon_Deck[13]],
		is_little_endian=True, ),
	Attribute(
		name="Wizardmon Deck 15",
		addresses=[0x26a6244,0x26a6246],
		number_of_bytes=2,
		possible_values=[New_Wizardmon_Deck[14]],
		is_little_endian=True, ),
	Attribute(
		name="Wizardmon Deck 16",
		addresses=[0x26a6248,0x26a624a],
		number_of_bytes=2,
		possible_values=[New_Wizardmon_Deck[15]],
		is_little_endian=True, ),
	Attribute(
		name="Wizardmon Deck 17",
		addresses=[0x26a624c],
		number_of_bytes=2,
		possible_values=[New_Wizardmon_Deck[16]],
		is_little_endian=True, ),
#AeroVeedramon
    Attribute(
        name="AeroVeedramon Deck 1",
        addresses=[0x26a6280,0x26a6282,0x26a6284,0x26a6286],
        number_of_bytes=2,
        possible_values=[New_AeroVeedramon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="AeroVeedramon Deck 2",
        addresses=[0x26a6288,0x26a628a,0x26a628c,0x26a628e],
        number_of_bytes=2,
        possible_values=[New_AeroVeedramon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="AeroVeedramon Deck 3",
        addresses=[0x26a6290,0x26a6292,0x26a6294],
        number_of_bytes=2,
        possible_values=[New_AeroVeedramon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="AeroVeedramon Deck 4",
        addresses=[0x26a6296,0x26a6298,0x26a629a],
        number_of_bytes=2,
        possible_values=[New_AeroVeedramon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="AeroVeedramon Deck 5",
        addresses=[0x26a629c,0x26a629e,0x26a62a0],
        number_of_bytes=2,
        possible_values=[New_AeroVeedramon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="AeroVeedramon Deck 6",
		addresses=[0x26a62a2],
		number_of_bytes=2,
		possible_values=[New_AeroVeedramon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="AeroVeedramon Deck 7",
		addresses=[0x26a62a4,0x26a62a6,0x26a62a8],
		number_of_bytes=2,
		possible_values=[New_AeroVeedramon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="AeroVeedramon Deck 8",
		addresses=[0x26a62aa,0x26a62ac],
		number_of_bytes=2,
		possible_values=[New_AeroVeedramon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="AeroVeedramon Deck 9",
		addresses=[0x26a6234,0x26a6236,0x26a6238],
		number_of_bytes=2,
		possible_values=[New_AeroVeedramon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="AeroVeedramon Deck 10",
		addresses=[0x26a623a],
		number_of_bytes=2,
		possible_values=[New_AeroVeedramon_Deck[9]],
		is_little_endian=True, ),
#Gatomon
    Attribute(
        name="Gatomon Deck 1",
        addresses=[0x26a62ee,0x26a62f0,0x26a62f2,0x26a62f4],
        number_of_bytes=2,
        possible_values=[New_Gatomon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Gatomon Deck 2",
        addresses=[0x26a62f6,0x26a62f8,0x26a62fa],
        number_of_bytes=2,
        possible_values=[New_Gatomon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Gatomon Deck 3",
        addresses=[0x26a62fc,0x26a62fe],
        number_of_bytes=2,
        possible_values=[New_Gatomon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Gatomon Deck 4",
        addresses=[0x26a6300,0x26a6302,0x26a6304],
        number_of_bytes=2,
        possible_values=[New_Gatomon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Gatomon Deck 5",
        addresses=[0x26a6306,0x26a6308,0x26a630a],
        number_of_bytes=2,
        possible_values=[New_Gatomon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Gatomon Deck 6",
		addresses=[0x26a630c,0x26a630e,0x26a6310,0x26a6312],
		number_of_bytes=2,
		possible_values=[New_Gatomon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Gatomon Deck 7",
		addresses=[0x26a6314,0x26a6316],
		number_of_bytes=2,
		possible_values=[New_Gatomon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Gatomon Deck 8",
		addresses=[0x26a6318,0x26a631a],
		number_of_bytes=2,
		possible_values=[New_Gatomon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Gatomon Deck 9",
		addresses=[0x26a631c,0x26a631e,0x26a6320],
		number_of_bytes=2,
		possible_values=[New_Gatomon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Gatomon Deck 10",
		addresses=[0x26a6322,0x26a6324,0x26a6326,0x26a6328],
		number_of_bytes=2,
		possible_values=[New_Gatomon_Deck[9]],
		is_little_endian=True, ),
#Kari
    Attribute(
        name="Kari Deck 1",
        addresses=[0x26a635c],
        number_of_bytes=2,
        possible_values=[New_Kari_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Kari Deck 2",
        addresses=[0x26a635e,0x26a6360],
        number_of_bytes=2,
        possible_values=[New_Kari_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Kari Deck 3",
        addresses=[0x26a6362],
        number_of_bytes=2,
        possible_values=[New_Kari_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Kari Deck 4",
        addresses=[0x26a6364],
        number_of_bytes=2,
        possible_values=[New_Kari_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Kari Deck 5",
        addresses=[0x26a6366,0x26a6368,0x26a636a],
        number_of_bytes=2,
        possible_values=[New_Kari_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Kari Deck 6",
		addresses=[0x26a636c,0x26a636e,0x26a6370],
		number_of_bytes=2,
		possible_values=[New_Kari_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Kari Deck 7",
		addresses=[0x26a6372],
		number_of_bytes=2,
		possible_values=[New_Kari_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Kari Deck 8",
		addresses=[0x26a6374,0x26a6376,0x26a6378,0x26a637a],
		number_of_bytes=2,
		possible_values=[New_Kari_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Kari Deck 9",
		addresses=[0x26a637c,0x26a637e,0x26a6380,0x26a6382],
		number_of_bytes=2,
		possible_values=[New_Kari_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Kari Deck 10",
		addresses=[0x26a6384],
		number_of_bytes=2,
		possible_values=[184],
		is_little_endian=True, ),
	Attribute(
		name="Kari Deck 11",
		addresses=[0x26a6386,0x26a6388],
		number_of_bytes=2,
		possible_values=[New_Kari_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Kari Deck 12",
		addresses=[0x26a638a,0x26a638c],
		number_of_bytes=2,
		possible_values=[New_Kari_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Kari Deck 13",
		addresses=[0x26a638e,0x26a6390,0x26a6392],
		number_of_bytes=2,
		possible_values=[New_Kari_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Kari Deck 14",
		addresses=[0x26a6394,0x26a6396],
		number_of_bytes=2,
		possible_values=[New_Kari_Deck[13]],
		is_little_endian=True, ),
#Goburimon
    Attribute(
        name="Goburimon Deck 1",
        addresses=[0x26a63ca,0x26a63cc,0x26a63ce],
        number_of_bytes=2,
        possible_values=[New_Goburimon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Goburimon Deck 2",
        addresses=[0x26a63d0,0x26a63d2,0x26a63d4],
        number_of_bytes=2,
        possible_values=[New_Goburimon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Goburimon Deck 3",
        addresses=[0x26a63d6,0x26a63d8,0x26a63da],
        number_of_bytes=2,
        possible_values=[New_Goburimon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Goburimon Deck 4",
        addresses=[0x26a63dc,0x26a63de,0x26a63e0],
        number_of_bytes=2,
        possible_values=[New_Goburimon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Goburimon Deck 5",
        addresses=[0x26a63e2,0x26a63e4,0x26a63e6],
        number_of_bytes=2,
        possible_values=[New_Goburimon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Goburimon Deck 6",
		addresses=[0x26a63e8],
		number_of_bytes=2,
		possible_values=[New_Goburimon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Goburimon Deck 7",
		addresses=[0x26a63ea,0x26a63ec,0x26a63ee,0x26a63f0],
		number_of_bytes=2,
		possible_values=[New_Goburimon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Goburimon Deck 8",
		addresses=[0x26a63f2,0x26a63f4,0x26a63f6,0x26a63f8],
		number_of_bytes=2,
		possible_values=[New_Goburimon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Goburimon Deck 9",
		addresses=[0x26a63fa,0x26a63fc,0x26a63fe,0x26a6400],
		number_of_bytes=2,
		possible_values=[New_Goburimon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Goburimon Deck 10",
		addresses=[0x26a6402,0x26a6404],
		number_of_bytes=2,
		possible_values=[New_Goburimon_Deck[9]],
		is_little_endian=True, ),
#DemiDevimon
    Attribute(
        name="DemiDevimon Deck 1",
        addresses=[0x26A6438],
        number_of_bytes=2,
        possible_values=[New_DemiDevimon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="DemiDevimon Deck 2",
        addresses=[0x26A643a,0x26A643c],
        number_of_bytes=2,
        possible_values=[New_DemiDevimon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="DemiDevimon Deck 3",
        addresses=[0x26A643e,0x26A6440],
        number_of_bytes=2,
        possible_values=[New_DemiDevimon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="DemiDevimon Deck 4",
        addresses=[0x26A6442],
        number_of_bytes=2,
        possible_values=[New_DemiDevimon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="DemiDevimon Deck 5",
        addresses=[0x26A6444,0x26A6446,0x26A6448,0x26A644a],
        number_of_bytes=2,
        possible_values=[New_DemiDevimon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="DemiDevimon Deck 6",
		addresses=[0x26A644c,0x26A644e,0x26A6450,0x26A6452],
		number_of_bytes=2,
		possible_values=[New_DemiDevimon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="DemiDevimon Deck 7",
		addresses=[0x26A6454,0x26A6456,0x26A6458,0x26A645a],
		number_of_bytes=2,
		possible_values=[New_DemiDevimon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="DemiDevimon Deck 8",
		addresses=[0x26A645c,0x26A645e,0x26A6460,0x26A6462],
		number_of_bytes=2,
		possible_values=[New_DemiDevimon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="DemiDevimon Deck 9",
		addresses=[0x26A6464,0x26A6466,0x26A6468,0x26A646a],
		number_of_bytes=2,
		possible_values=[New_DemiDevimon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="DemiDevimon Deck 10",
		addresses=[0x26A646c,0x26A646e,0x26A6470,0x26A6472],
		number_of_bytes=2,
		possible_values=[New_DemiDevimon_Deck[9]],
		is_little_endian=True, ),
#Megadramon
    Attribute(
        name="Megadramon Deck 1",
        addresses=[0x26A64A6,0x26A64A8,0x26A64ba,0x26A64bc],
        number_of_bytes=2,
        possible_values=[New_Megadramon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Megadramon Deck 2",
        addresses=[0x26A64AE,0x26A64b0,0x26A64b2,0x26A64b4],
        number_of_bytes=2,
        possible_values=[New_Megadramon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Megadramon Deck 3",
        addresses=[0x26A64B6,0x26A65E8,0x26A65fa,0x26A65fc],
        number_of_bytes=2,
        possible_values=[New_Megadramon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Megadramon Deck 4",
        addresses=[0x26A65EE,0x26A65f0],
        number_of_bytes=2,
        possible_values=[New_Megadramon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Megadramon Deck 5",
        addresses=[0x26A65F2,0x26A65F4,0x26A65F6,0x26A65F8],
        number_of_bytes=2,
        possible_values=[New_Megadramon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Megadramon Deck 6",
		addresses=[0x26A65Fa,0x26A65Fc,0x26A65Fe,0x26A6600],
		number_of_bytes=2,
		possible_values=[New_Megadramon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Megadramon Deck 7",
		addresses=[0x26A6602,0x26A6604],
		number_of_bytes=2,
		possible_values=[New_Megadramon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Megadramon Deck 8",
		addresses=[0x26A6606,0x26A6608],
		number_of_bytes=2,
		possible_values=[New_Megadramon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Megadramon Deck 9",
		addresses=[0x26A660a,0x26A660c],
		number_of_bytes=2,
		possible_values=[New_Megadramon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Megadramon Deck 10",
		addresses=[0x26A660e,0x26A6610],
		number_of_bytes=2,
		possible_values=[New_Megadramon_Deck[9]],
		is_little_endian=True, ),
#Gigadramon
    Attribute(
        name="Gigadramon Deck 1",
        addresses=[0x26a6644,0x26a6646],
        number_of_bytes=2,
        possible_values=[New_Gigadramon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Gigadramon Deck 2",
        addresses=[0x26a6648,0x26a664a],
        number_of_bytes=2,
        possible_values=[New_Gigadramon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Gigadramon Deck 3",
        addresses=[0x26a664c],
        number_of_bytes=2,
        possible_values=[New_Gigadramon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Gigadramon Deck 4",
        addresses=[0x26a664e,0x26a6650,0x26a6652],
        number_of_bytes=2,
        possible_values=[New_Gigadramon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Gigadramon Deck 5",
        addresses=[0x26a6654,0x26a6656,0x26a6658],
        number_of_bytes=2,
        possible_values=[New_Gigadramon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Gigadramon Deck 6",
		addresses=[0x26a665a],
		number_of_bytes=2,
		possible_values=[New_Gigadramon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Gigadramon Deck 7",
		addresses=[0x26a665c,0x26a665e,0x26a6660],
		number_of_bytes=2,
		possible_values=[New_Gigadramon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Gigadramon Deck 8",
		addresses=[0x26a6662,0x26a6664],
		number_of_bytes=2,
		possible_values=[New_Gigadramon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Gigadramon Deck 9",
		addresses=[0x26a6666,0x26a6668,0x26a666a],
		number_of_bytes=2,
		possible_values=[New_Gigadramon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Gigadramon Deck 10",
		addresses=[0x26a666c,0x26a666e],
		number_of_bytes=2,
		possible_values=[New_Gigadramon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Gigadramon Deck 11",
		addresses=[0x26a6670,0x26a6672],
		number_of_bytes=2,
		possible_values=[New_Gigadramon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Gigadramon Deck 12",
		addresses=[0x26a6674,0x26a6676],
		number_of_bytes=2,
		possible_values=[New_Gigadramon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Gigadramon Deck 13",
		addresses=[0x26a6678,0x26a667a],
		number_of_bytes=2,
		possible_values=[New_Gigadramon_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Gigadramon Deck 14",
		addresses=[0x26a667c,0x26a667e],
		number_of_bytes=2,
		possible_values=[New_Gigadramon_Deck[13]],
		is_little_endian=True, ),
#Togemon
    Attribute(
        name="Togemon Deck 1",
        addresses=[0x26a66b2,0x26a66b4],
        number_of_bytes=2,
        possible_values=[New_Togemon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Togemon Deck 2",
        addresses=[0x26a66b6,0x26a66b8,0x26a66ba,0x26a66bc],
        number_of_bytes=2,
        possible_values=[New_Togemon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Togemon Deck 3",
        addresses=[0x26a66be,0x26a66c0,0x26a66c2],
        number_of_bytes=2,
        possible_values=[New_Togemon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Togemon Deck 4",
        addresses=[0x26a66c4],
        number_of_bytes=2,
        possible_values=[New_Togemon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Togemon Deck 5",
        addresses=[0x26a66c6,0x26a66c8,0x26a66ca,0x26a66cc],
        number_of_bytes=2,
        possible_values=[New_Togemon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Togemon Deck 6",
		addresses=[0x26a66ce,0x26a66d0,0x26a66d2],
		number_of_bytes=2,
		possible_values=[New_Togemon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Togemon Deck 7",
		addresses=[0x26a66d4,0x26a66d6,0x26a66d8],
		number_of_bytes=2,
		possible_values=[New_Togemon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Togemon Deck 8",
		addresses=[0x26a66da,0x26a66dc],
		number_of_bytes=2,
		possible_values=[New_Togemon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Togemon Deck 9",
		addresses=[0x26a66de,0x26a66e0],
		number_of_bytes=2,
		possible_values=[New_Togemon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Togemon Deck 10",
		addresses=[0x26a66e2,0x26a66e4],
		number_of_bytes=2,
		possible_values=[New_Togemon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Togemon Deck 11",
		addresses=[0x26a66e6,0x26a66e8],
		number_of_bytes=2,
		possible_values=[New_Togemon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Togemon Deck 12",
		addresses=[0x26a66ea,0x26a66ec],
		number_of_bytes=2,
		possible_values=[New_Togemon_Deck[11]],
		is_little_endian=True, ),
#Kabuterimon
    Attribute(
        name="Kabuterimon Deck 1",
        addresses=[0x26a6720,0x26a6722],
        number_of_bytes=2,
        possible_values=[New_Kabuterimon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Kabuterimon Deck 2",
        addresses=[0x26a6724,0x26a6726,0x26a6728,0x26a672a],
        number_of_bytes=2,
        possible_values=[New_Kabuterimon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Kabuterimon Deck 3",
        addresses=[0x26a672c,0x26a672e,0x26a6730],
        number_of_bytes=2,
        possible_values=[New_Kabuterimon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Kabuterimon Deck 4",
        addresses=[0x26a6732],
        number_of_bytes=2,
        possible_values=[New_Kabuterimon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Kabuterimon Deck 5",
        addresses=[0x26a6734,0x26a6736,0x26a6738,0x26a673a],
        number_of_bytes=2,
        possible_values=[New_Kabuterimon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Kabuterimon Deck 6",
		addresses=[0x26a673c,0x26a673e,0x26a6740],
		number_of_bytes=2,
		possible_values=[New_Kabuterimon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Kabuterimon Deck 7",
		addresses=[0x26a6742,0x26a6744,0x26a6746],
		number_of_bytes=2,
		possible_values=[New_Kabuterimon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Kabuterimon Deck 8",
		addresses=[0x26a6748,0x26a674a,0x26a674c,0x26a674e],
		number_of_bytes=2,
		possible_values=[New_Kabuterimon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Kabuterimon Deck 9",
		addresses=[0x26a6750,0x26a6752],
		number_of_bytes=2,
		possible_values=[New_Kabuterimon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Kabuterimon Deck 10",
		addresses=[0x26a6754,0x26a6756],
		number_of_bytes=2,
		possible_values=[New_Kabuterimon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Kabuterimon Deck 11",
		addresses=[0x26a6758,0x26a675a],
		number_of_bytes=2,
		possible_values=[New_Kabuterimon_Deck[10]],
		is_little_endian=True, ),
#Ikkakumon
    Attribute(
        name="Ikkakumon Deck 1",
        addresses=[0x26a678e,0x26a6790],
        number_of_bytes=2,
        possible_values=[New_Ikkakumon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Ikkakumon Deck 2",
        addresses=[0x26a6792,0x26a6794,0x26a6796,0x26a6798],
        number_of_bytes=2,
        possible_values=[New_Ikkakumon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Ikkakumon Deck 3",
        addresses=[0x26a679a,0x26a679c,0x26a679e],
        number_of_bytes=2,
        possible_values=[New_Ikkakumon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Ikkakumon Deck 4",
        addresses=[0x26a67a0],
        number_of_bytes=2,
        possible_values=[New_Ikkakumon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Ikkakumon Deck 5",
        addresses=[0x26a67a2,0x26a67a4,0x26a67a6,0x26a67a8],
        number_of_bytes=2,
        possible_values=[New_Ikkakumon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Ikkakumon Deck 6",
		addresses=[0x26a67aa,0x26a67ac,0x26a67ae],
		number_of_bytes=2,
		possible_values=[New_Ikkakumon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Ikkakumon Deck 7",
		addresses=[0x26a67b0,0x26a67b2,0x26a67b4],
		number_of_bytes=2,
		possible_values=[New_Ikkakumon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Ikkakumon Deck 8",
		addresses=[0x26a67b6],
		number_of_bytes=2,
		possible_values=[New_Ikkakumon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Ikkakumon Deck 9",
		addresses=[0x26a67b8,0x26a67ba,0x26a67bc],
		number_of_bytes=2,
		possible_values=[New_Ikkakumon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Ikkakumon Deck 10",
		addresses=[0x26a67be,0x26a67c0,0x26a67c2],
		number_of_bytes=2,
		possible_values=[New_Ikkakumon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Ikkakumon Deck 11",
		addresses=[0x26a67c4,0x26a67c6,0x26a67c8],
		number_of_bytes=2,
		possible_values=[New_Ikkakumon_Deck[10]],
		is_little_endian=True, ),
#Birdramon
    Attribute(
        name="Birdramon Deck 1",
        addresses=[0x26a67fc,0x26a67fe],
        number_of_bytes=2,
        possible_values=[New_Birdramon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Birdramon Deck 2",
        addresses=[0x26a6800,0x26a6802],
        number_of_bytes=2,
        possible_values=[New_Birdramon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Birdramon Deck 3",
        addresses=[0x26a6804,0x26a6806,0x26a6808,0x26a680a],
        number_of_bytes=2,
        possible_values=[New_Birdramon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Birdramon Deck 4",
        addresses=[0x26a680c,0x26a680e],
        number_of_bytes=2,
        possible_values=[New_Birdramon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Birdramon Deck 5",
        addresses=[0x26a6810,0x26a6812,0x26a6814,0x26a6816],
        number_of_bytes=2,
        possible_values=[New_Birdramon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Birdramon Deck 6",
		addresses=[0x26a6818,0x26a681a,0x26a681c],
		number_of_bytes=2,
		possible_values=[New_Birdramon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Birdramon Deck 7",
		addresses=[0x26a681e,0x26a6820,0x26a6822],
		number_of_bytes=2,
		possible_values=[New_Birdramon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Birdramon Deck 8",
		addresses=[0x26a6824,0x26a6826],
		number_of_bytes=2,
		possible_values=[New_Birdramon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Birdramon Deck 9",
		addresses=[0x26a6828,0x26a682a],
		number_of_bytes=2,
		possible_values=[New_Birdramon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Birdramon Deck 10",
		addresses=[0x26a682c,0x26a682e],
		number_of_bytes=2,
		possible_values=[New_Birdramon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Birdramon Deck 11",
		addresses=[0x26a6830,0x26a6832],
		number_of_bytes=2,
		possible_values=[New_Birdramon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Birdramon Deck 12",
		addresses=[0x26a6834,0x26a6836],
		number_of_bytes=2,
		possible_values=[New_Birdramon_Deck[11]],
		is_little_endian=True, ),
#WereGarurumon
    Attribute(
        name="WereGarurumon Deck 1",
        addresses=[0x26a686a,0x26a686c,0x26a686e,0x26a6870],
        number_of_bytes=2,
        possible_values=[New_WereGarurumon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="WereGarurumon Deck 2",
        addresses=[0x26a6872,0x26a6874,0x26a6876,0x26a6878],
        number_of_bytes=2,
        possible_values=[New_WereGarurumon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="WereGarurumon Deck 3",
        addresses=[0x26a687a,0x26a687c],
        number_of_bytes=2,
        possible_values=[New_WereGarurumon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="WereGarurumon Deck 4",
        addresses=[0x26a687e],
        number_of_bytes=2,
        possible_values=[New_WereGarurumon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="WereGarurumon Deck 5",
        addresses=[0x26a6880,0x26a6882,0x26a6884],
        number_of_bytes=2,
        possible_values=[New_WereGarurumon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="WereGarurumon Deck 6",
		addresses=[0x26a6886,0x26a6888,0x26a688a],
		number_of_bytes=2,
		possible_values=[New_WereGarurumon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="WereGarurumon Deck 7",
		addresses=[0x26a688c],
		number_of_bytes=2,
		possible_values=[New_WereGarurumon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="WereGarurumon Deck 8",
		addresses=[0x26a688e,0x26a6890,0x26a6892],
		number_of_bytes=2,
		possible_values=[New_WereGarurumon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="WereGarurumon Deck 9",
		addresses=[0x26a6894,0x26a6896],
		number_of_bytes=2,
		possible_values=[New_WereGarurumon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="WereGarurumon Deck 10",
		addresses=[0x26a6898,0x26a689a,0x26a689c],
		number_of_bytes=2,
		possible_values=[New_WereGarurumon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="WereGarurumon Deck 11",
		addresses=[0x26a689e,0x26a68a0,0x26a68a2],
		number_of_bytes=2,
		possible_values=[New_WereGarurumon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="WereGarurumon Deck 12",
		addresses=[0x26a68a4],
		number_of_bytes=2,
		possible_values=[New_WereGarurumon_Deck[11]],
		is_little_endian=True, ),
#MetalGreymon
    Attribute(
        name="MetalGreymon Deck 1",
        addresses=[0x26a68d8,0x26a68da,0x26a68dc,0x26a68de],
        number_of_bytes=2,
        possible_values=[New_MetalGreymon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="MetalGreymon Deck 2",
        addresses=[0x26a68e0],
        number_of_bytes=2,
        possible_values=[New_MetalGreymon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="MetalGreymon Deck 3",
        addresses=[0x26a68e2],
        number_of_bytes=2,
        possible_values=[New_MetalGreymon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="MetalGreymon Deck 4",
        addresses=[0x26a68e4],
        number_of_bytes=2,
        possible_values=[New_MetalGreymon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="MetalGreymon Deck 5",
        addresses=[0x26a68e6],
        number_of_bytes=2,
        possible_values=[New_MetalGreymon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="MetalGreymon Deck 6",
		addresses=[0x26a68e8],
		number_of_bytes=2,
		possible_values=[New_MetalGreymon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="MetalGreymon Deck 7",
		addresses=[0x26a68ea],
		number_of_bytes=2,
		possible_values=[New_MetalGreymon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="MetalGreymon Deck 8",
		addresses=[0x26a68ec],
		number_of_bytes=2,
		possible_values=[New_MetalGreymon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="MetalGreymon Deck 9",
		addresses=[0x26a68ee,0x26a68f0,0x26a68f2,0x26a68f4],
		number_of_bytes=2,
		possible_values=[New_MetalGreymon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="MetalGreymon Deck 10",
		addresses=[0x26a68f6],
		number_of_bytes=2,
		possible_values=[New_MetalGreymon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="MetalGreymon Deck 11",
		addresses=[0x26a68f8],
		number_of_bytes=2,
		possible_values=[New_MetalGreymon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="MetalGreymon Deck 12",
		addresses=[0x26a68fa],
		number_of_bytes=2,
		possible_values=[New_MetalGreymon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="MetalGreymon Deck 13",
		addresses=[0x26a68fc],
		number_of_bytes=2,
		possible_values=[New_MetalGreymon_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="MetalGreymon Deck 14",
		addresses=[0x26a68fe],
		number_of_bytes=2,
		possible_values=[New_MetalGreymon_Deck[13]],
		is_little_endian=True, ),
	Attribute(
		name="MetalGreymon Deck 15",
		addresses=[0x26a6900],
		number_of_bytes=2,
		possible_values=[New_MetalGreymon_Deck[14]],
		is_little_endian=True, ),
	Attribute(
		name="MetalGreymon Deck 16",
		addresses=[0x26a6902,0x26a6904,0x26a6906],
		number_of_bytes=2,
		possible_values=[New_MetalGreymon_Deck[15]],
		is_little_endian=True, ),
	Attribute(
		name="MetalGreymon Deck 17",
		addresses=[0x26a6908,0x26a690a,0x26a690c,0x26a690e],
		number_of_bytes=2,
		possible_values=[New_MetalGreymon_Deck[16]],
		is_little_endian=True, ),
	Attribute(
		name="MetalGreymon Deck 18",
		addresses=[0x26a6910,0x26a6912],
		number_of_bytes=2,
		possible_values=[New_MetalGreymon_Deck[17]],
		is_little_endian=True, ),
#Tuskmon
    Attribute(
        name="Tuskmon Deck 1",
        addresses=[0x26a6946],
        number_of_bytes=2,
        possible_values=[New_Tuskmon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Tuskmon Deck 2",
        addresses=[0x26a6948,0x26a694a],
        number_of_bytes=2,
        possible_values=[New_Tuskmon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Tuskmon Deck 3",
        addresses=[0x26a694c,0x26a694e,0x26a6950,0x26a6952],
        number_of_bytes=2,
        possible_values=[New_Tuskmon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Tuskmon Deck 4",
        addresses=[0x26a6954],
        number_of_bytes=2,
        possible_values=[New_Tuskmon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Tuskmon Deck 5",
        addresses=[0x26a6956],
        number_of_bytes=2,
        possible_values=[New_Tuskmon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Tuskmon Deck 6",
		addresses=[0x26a6958],
		number_of_bytes=2,
		possible_values=[New_Tuskmon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Tuskmon Deck 7",
		addresses=[0x26a695a,0x26a695c,0x26a695e],
		number_of_bytes=2,
		possible_values=[New_Tuskmon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Tuskmon Deck 8",
		addresses=[0x26a6960,0x26a6962,0x26a6964],
		number_of_bytes=2,
		possible_values=[New_Tuskmon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Tuskmon Deck 9",
		addresses=[0x26a6966,0x26a6968,0x26a696a,0x26a696c],
		number_of_bytes=2,
		possible_values=[New_Tuskmon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Tuskmon Deck 10",
		addresses=[0x26a696e,0x26a6970],
		number_of_bytes=2,
		possible_values=[New_Tuskmon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Tuskmon Deck 11",
		addresses=[0x26a6972,0x26a6974,0x26a6976,0x26a6978],
		number_of_bytes=2,
		possible_values=[New_Tuskmon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Tuskmon Deck 12",
		addresses=[0x26a697a,0x26a697c],
		number_of_bytes=2,
		possible_values=[New_Tuskmon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Tuskmon Deck 13",
		addresses=[0x26a697e,0x26a6980],
		number_of_bytes=2,
		possible_values=[New_Tuskmon_Deck[12]],
		is_little_endian=True, ),
#Phantomon
    Attribute(
        name="Phantomon Deck 1",
        addresses=[0x26a69b4,0x26a69b6,0x26a69b8,0x26a69ba],
        number_of_bytes=2,
        possible_values=[New_Phantomon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Phantomon Deck 2",
        addresses=[0x26a69bc,0x26a69be,0x26a69c0,0x26a69c2],
        number_of_bytes=2,
        possible_values=[New_Phantomon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Phantomon Deck 3",
        addresses=[0x26a69c4,0x26a69c6,0x26a69c8],
        number_of_bytes=2,
        possible_values=[New_Phantomon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Phantomon Deck 4",
        addresses=[0x26a69d0,0x26a69d2,0x26a69d4,0x26a69d6],
        number_of_bytes=2,
        possible_values=[New_Phantomon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Phantomon Deck 5",
        addresses=[0x26a69d8,0x26a69da,0x26a69dc],
        number_of_bytes=2,
        possible_values=[New_Phantomon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Phantomon Deck 6",
		addresses=[0x26a69de,0x26a69e0,0x26a69e2],
		number_of_bytes=2,
		possible_values=[New_Phantomon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Phantomon Deck 7",
		addresses=[0x26a69e4,0x26a69e6],
		number_of_bytes=2,
		possible_values=[New_Phantomon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Phantomon Deck 8",
		addresses=[0x26a69e8,0x26a69ea],
		number_of_bytes=2,
		possible_values=[New_Phantomon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Phantomon Deck 9",
		addresses=[0x26a69ec,0x26a69ee],
		number_of_bytes=2,
		possible_values=[New_Phantomon_Deck[8]],
		is_little_endian=True, ),
#MegaSeadramon
    Attribute(
        name="MegaSeadramon Deck 1",
        addresses=[0x26a6a22,0x26a6a24,0x26a6a26,0x26a6a28],
        number_of_bytes=2,
        possible_values=[New_MegaSeadramon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="MegaSeadramon Deck 2",
        addresses=[0x26a6a2a],
        number_of_bytes=2,
        possible_values=[New_MegaSeadramon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="MegaSeadramon Deck 3",
        addresses=[0x26a6a2c,0x26a6a2e],
        number_of_bytes=2,
        possible_values=[New_MegaSeadramon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="MegaSeadramon Deck 4",
        addresses=[0x26a6a30,0x26a6a32],
        number_of_bytes=2,
        possible_values=[New_MegaSeadramon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="MegaSeadramon Deck 5",
        addresses=[0x26a6a34,0x26a6a36],
        number_of_bytes=2,
        possible_values=[New_MegaSeadramon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="MegaSeadramon Deck 6",
		addresses=[0x26a6a38,0x26a6a3a,0x26a6a3c],
		number_of_bytes=2,
		possible_values=[New_MegaSeadramon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="MegaSeadramon Deck 7",
		addresses=[0x26a6a3e,0x26a6a40,0x26a6a42],
		number_of_bytes=2,
		possible_values=[New_MegaSeadramon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="MegaSeadramon Deck 8",
		addresses=[0x26a6a44,0x26a6a46],
		number_of_bytes=2,
		possible_values=[New_MegaSeadramon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="MegaSeadramon Deck 9",
		addresses=[0x26a6a48,0x26a6a4a,0x26a6a4c],
		number_of_bytes=2,
		possible_values=[New_MegaSeadramon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="MegaSeadramon Deck 10",
		addresses=[0x26a6a4e,0x26a6a50,0x26a6a52,0x26a6a54],
		number_of_bytes=2,
		possible_values=[New_MegaSeadramon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="MegaSeadramon Deck 11",
		addresses=[0x26a6a56,0x26a6a58,0x26a6a5a,0x26a6a5c],
		number_of_bytes=2,
		possible_values=[New_MegaSeadramon_Deck[10]],
		is_little_endian=True, ),
#VenomMyotismon
    Attribute(
        name="VenomMyotismon Deck 1",
        addresses=[0x26a6a90,0x26a6a92,0x26a6a94,0x26a6a96],
        number_of_bytes=2,
        possible_values=[New_VenomMyotismon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="VenomMyotismon Deck 2",
        addresses=[0x26a6a98,0x26a6a9a,0x26a6a9c],
        number_of_bytes=2,
        possible_values=[New_VenomMyotismon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="VenomMyotismon Deck 3",
        addresses=[0x26a6a9e,0x26a6aa0],
        number_of_bytes=2,
        possible_values=[New_VenomMyotismon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="VenomMyotismon Deck 4",
        addresses=[0x26a6aa2,0x26a6aa4],
        number_of_bytes=2,
        possible_values=[New_VenomMyotismon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="VenomMyotismon Deck 5",
        addresses=[0x26a6aa6,0x26a6aa8,0x26a6aaa,0x26a6aac],
        number_of_bytes=2,
        possible_values=[New_VenomMyotismon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="VenomMyotismon Deck 6",
		addresses=[0x26a6aae,0x26a6ab0,0x26a6ab2],
		number_of_bytes=2,
		possible_values=[New_VenomMyotismon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="VenomMyotismon Deck 7",
		addresses=[0x26a6ab4,0x26a6ab6,0x26a6ab8],
		number_of_bytes=2,
		possible_values=[New_VenomMyotismon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="VenomMyotismon Deck 8",
		addresses=[0x26a6aba,0x26a6abc,0x26a6abe],
		number_of_bytes=2,
		possible_values=[New_VenomMyotismon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="VenomMyotismon Deck 9",
		addresses=[0x26a6ac0,0x26a6ac2],
		number_of_bytes=2,
		possible_values=[New_VenomMyotismon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="VenomMyotismon Deck 10",
		addresses=[0x26a6ac4,0x26a6ac6],
		number_of_bytes=2,
		possible_values=[New_VenomMyotismon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="VenomMyotismon Deck 11",
		addresses=[0x26a6ac8,0x26a6aca],
		number_of_bytes=2,
		possible_values=[New_VenomMyotismon_Deck[10]],
		is_little_endian=True, ),
#Leomon
    Attribute(
        name="Leomon Deck 1",
        addresses=[0x26a6afe,0x26a6b00,0x26a6b02,0x26a6b04],
        number_of_bytes=2,
        possible_values=[New_Leomon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Leomon Deck 2",
        addresses=[0x26a6b06,0x26a6b08],
        number_of_bytes=2,
        possible_values=[New_Leomon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Leomon Deck 3",
        addresses=[0x26a6b0a,0x26a6b0c,0x26a6b0e],
        number_of_bytes=2,
        possible_values=[New_Leomon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Leomon Deck 4",
        addresses=[0x26a6b10,0x26a6b12,0x26a6b14],
        number_of_bytes=2,
        possible_values=[New_Leomon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Leomon Deck 5",
        addresses=[0x26a6b16,0x26a6b18],
        number_of_bytes=2,
        possible_values=[New_Leomon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Leomon Deck 6",
		addresses=[0x26a6b1a],
		number_of_bytes=2,
		possible_values=[New_Leomon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Leomon Deck 7",
		addresses=[0x26a6b1c,0x26a6b1e,0x26a6b20],
		number_of_bytes=2,
		possible_values=[New_Leomon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Leomon Deck 8",
		addresses=[0x26a6b22],
		number_of_bytes=2,
		possible_values=[New_Leomon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Leomon Deck 9",
		addresses=[0x26a6b24,0x26a6b26,0x26a6b28],
		number_of_bytes=2,
		possible_values=[New_Leomon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Leomon Deck 10",
		addresses=[0x26a6b2a,0x26a6b2c,0x26a6b2e],
		number_of_bytes=2,
		possible_values=[New_Leomon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Leomon Deck 11",
		addresses=[0x26a6b30,0x26a6b32,0x26a6b34],
		number_of_bytes=2,
		possible_values=[New_Leomon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Leomon Deck 12",
		addresses=[0x26a6b36,0x26a6b38],
		number_of_bytes=2,
		possible_values=[New_Leomon_Deck[11]],
		is_little_endian=True, ),
#Devimon
    Attribute(
        name="Devimon Deck 1",
        addresses=[0x26a6b6c,0x26a6b6e,0x26a6b70,0x26a6b72],
        number_of_bytes=2,
        possible_values=[New_Devimon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Devimon Deck 2",
        addresses=[0x26a6b74,0x26a6b76,0x26a6b78,0x26a6b7a],
        number_of_bytes=2,
        possible_values=[New_Devimon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Devimon Deck 3",
        addresses=[0x26a6b7c,0x26a6b7e],
        number_of_bytes=2,
        possible_values=[New_Devimon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Devimon Deck 4",
        addresses=[0x26a6b80,0x26a6b82,0x26a6b84,0x26a6b86],
        number_of_bytes=2,
        possible_values=[New_Devimon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Devimon Deck 5",
        addresses=[0x26a6b88,0x26a6b8a,0x26a6b8c,0x26a6b8e],
        number_of_bytes=2,
        possible_values=[New_Devimon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Devimon Deck 6",
		addresses=[0x26a6b90,0x26a6b92],
		number_of_bytes=2,
		possible_values=[New_Devimon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Devimon Deck 7",
		addresses=[0x26a6b94,0x26a6b96],
		number_of_bytes=2,
		possible_values=[New_Devimon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Devimon Deck 8",
		addresses=[0x26a6b98,0x26a6b9a],
		number_of_bytes=2,
		possible_values=[New_Devimon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Devimon Deck 9",
		addresses=[0x26a6b9c,0x26a6b9e,0x26a6ba0],
		number_of_bytes=2,
		possible_values=[New_Devimon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Devimon Deck 10",
		addresses=[0x26a6ba2,0x26a6ba4,0x26a6ba6],
		number_of_bytes=2,
		possible_values=[New_Devimon_Deck[9]],
		is_little_endian=True, ),
#MetalEtemon
    Attribute(
        name="MetalEtemon Deck 1",
        addresses=[0x26a6bda,0x26a6bdc,0x26a6bde],
        number_of_bytes=2,
        possible_values=[New_MetalEtemon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="MetalEtemon Deck 2",
        addresses=[0x26a6be0,0x26a6be2],
        number_of_bytes=2,
        possible_values=[New_MetalEtemon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="MetalEtemon Deck 3",
        addresses=[0x26a6be4,0x26a6be6],
        number_of_bytes=2,
        possible_values=[New_MetalEtemon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="MetalEtemon Deck 4",
        addresses=[0x26a6be8,0x26a6bea],
        number_of_bytes=2,
        possible_values=[New_MetalEtemon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="MetalEtemon Deck 5",
        addresses=[0x26a6bec,0x26a6bee],
        number_of_bytes=2,
        possible_values=[New_MetalEtemon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="MetalEtemon Deck 6",
		addresses=[0x26a6bf0,0x26a6bf2,0x26a6bf4],
		number_of_bytes=2,
		possible_values=[New_MetalEtemon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="MetalEtemon Deck 7",
		addresses=[0x26a6bf6,0x26a6bf8,0x26a6bfa],
		number_of_bytes=2,
		possible_values=[New_MetalEtemon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="MetalEtemon Deck 8",
		addresses=[0x26a6bfc,0x26a6bfe,0x26a6c00],
		number_of_bytes=2,
		possible_values=[New_MetalEtemon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="MetalEtemon Deck 9",
		addresses=[0x26a6c02,0x26a6c04],
		number_of_bytes=2,
		possible_values=[New_MetalEtemon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="MetalEtemon Deck 10",
		addresses=[0x26a6c06,0x26a6c08],
		number_of_bytes=2,
		possible_values=[New_MetalEtemon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="MetalEtemon Deck 11",
		addresses=[0x26a6c0a,0x26a6c0c],
		number_of_bytes=2,
		possible_values=[New_MetalEtemon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="MetalEtemon Deck 12",
		addresses=[0x26a6c0e,0x26a6c10],
		number_of_bytes=2,
		possible_values=[New_MetalEtemon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="MetalEtemon Deck 13",
		addresses=[0x26a6c12,0x26a6c14],
		number_of_bytes=2,
		possible_values=[New_MetalEtemon_Deck[12]],
		is_little_endian=True, ),
#Myotismon
    Attribute(
        name="Myotismon Deck 1",
        addresses=[0x26a6c48,0x26a6c4a,0x26a6c4c,0x26a6c4e],
        number_of_bytes=2,
        possible_values=[New_Myotismon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Myotismon Deck 2",
        addresses=[0x26a6c50,0x26a6c52,0x26a6c54],
        number_of_bytes=2,
        possible_values=[New_Myotismon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Myotismon Deck 3",
        addresses=[0x26a6c56,0x26a6c58],
        number_of_bytes=2,
        possible_values=[New_Myotismon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Myotismon Deck 4",
        addresses=[0x26a6c5a,0x26a6c5c],
        number_of_bytes=2,
        possible_values=[New_Myotismon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Myotismon Deck 5",
        addresses=[0x26a6c5e,0x26a6c60,0x26a6c62,0x26a6c64],
        number_of_bytes=2,
        possible_values=[New_Myotismon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Myotismon Deck 6",
		addresses=[0x26a6c66,0x26a6c68,0x26a6c6a],
		number_of_bytes=2,
		possible_values=[New_Myotismon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Myotismon Deck 7",
		addresses=[0x26a6c6c,0x26a6c6e,0x26a6c70],
		number_of_bytes=2,
		possible_values=[New_Myotismon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Myotismon Deck 8",
		addresses=[0x26a6c72,0x26a6c74,0x26a6c76],
		number_of_bytes=2,
		possible_values=[New_Myotismon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Myotismon Deck 9",
		addresses=[0x26a6c78,0x26a6c7a],
		number_of_bytes=2,
		possible_values=[New_Myotismon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Myotismon Deck 10",
		addresses=[0x26a6c7c,0x26a6c7e],
		number_of_bytes=2,
		possible_values=[New_Myotismon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Myotismon Deck 11",
		addresses=[0x26a6c80,0x26a6c82],
		number_of_bytes=2,
		possible_values=[New_Myotismon_Deck[10]],
		is_little_endian=True, ),
#Greymon
    Attribute(
        name="Greymon Deck 1",
        addresses=[0x26a6cb6,0x26a6cb8,0x26a6cba,0x26a6cbc],
        number_of_bytes=2,
        possible_values=[New_Greymon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Greymon Deck 2",
        addresses=[0x26a6cbe,0x26a6cc0,0x26a6cc2,0x26a6cc4],
        number_of_bytes=2,
        possible_values=[New_Greymon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Greymon Deck 3",
        addresses=[0x26a6cc6,0x26a6cc8],
        number_of_bytes=2,
        possible_values=[New_Greymon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Greymon Deck 4",
        addresses=[0x26a6cca,0x26a6ccc,0x26a6cce,0x26a6cd0],
        number_of_bytes=2,
        possible_values=[New_Greymon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Greymon Deck 5",
        addresses=[0x26a6cd2,0x26a6cd4,0x26a6cd6,0x26a6cd8],
        number_of_bytes=2,
        possible_values=[New_Greymon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Greymon Deck 6",
		addresses=[0x26a6cda,0x26a6cdc],
		number_of_bytes=2,
		possible_values=[New_Greymon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Greymon Deck 7",
		addresses=[0x26a6cde,0x26a6ce0],
		number_of_bytes=2,
		possible_values=[New_Greymon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Greymon Deck 8",
		addresses=[0x26a6ce2,0x26a6ce4],
		number_of_bytes=2,
		possible_values=[New_Greymon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Greymon Deck 9",
		addresses=[0x26a6ce6,0x26a6ce8],
		number_of_bytes=2,
		possible_values=[New_Greymon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Greymon Deck 10",
		addresses=[0x26a6cea,0x26a6cec,0x26a6cee,0x26a6cf0],
		number_of_bytes=2,
		possible_values=[New_Greymon_Deck[9]],
		is_little_endian=True, ),
#ExVeemon
    Attribute(
        name="ExVeemon Deck 1",
        addresses=[0x26a6d24,0x26a6d26,0x26a6d28,0x26a6d2a],
        number_of_bytes=2,
        possible_values=[New_ExVeemon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="ExVeemon Deck 2",
        addresses=[0x26a6d2c,0x26a6d2e],
        number_of_bytes=2,
        possible_values=[New_ExVeemon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="ExVeemon Deck 3",
        addresses=[0x26a6d30,0x26a6d32],
        number_of_bytes=2,
        possible_values=[New_ExVeemon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="ExVeemon Deck 4",
        addresses=[0x26a6d34,0x26a6d36,0x26a6d38,0x26a6d3a],
        number_of_bytes=2,
        possible_values=[New_ExVeemon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="ExVeemon Deck 5",
        addresses=[0x26a6d3c,0x26a6d3e,0x26a6d40],
        number_of_bytes=2,
        possible_values=[New_ExVeemon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="ExVeemon Deck 6",
		addresses=[0x26a6d42,0x26a6d44,0x26a6d46],
		number_of_bytes=2,
		possible_values=[New_ExVeemon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="ExVeemon Deck 7",
		addresses=[0x26a6d48,0x26a6d4a,0x26a6d4c],
		number_of_bytes=2,
		possible_values=[New_ExVeemon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="ExVeemon Deck 8",
		addresses=[0x26a6d4e,0x26a6d50,0x26a6d52],
		number_of_bytes=2,
		possible_values=[New_ExVeemon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="ExVeemon Deck 9",
		addresses=[0x26a6d54,0x26a6d56,0x26a6d58],
		number_of_bytes=2,
		possible_values=[New_ExVeemon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="ExVeemon Deck 10",
		addresses=[0x26a6d5a,0x26a6d5c,0x26a6d5e],
		number_of_bytes=2,
		possible_values=[New_ExVeemon_Deck[9]],
		is_little_endian=True, ),
#Flamedramon
    Attribute(
        name="Flamedramon Deck 1",
        addresses=[0x26a6d92,0x26a6d94],
        number_of_bytes=2,
        possible_values=[New_Flamedramon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Flamedramon Deck 2",
        addresses=[0x26a6d96,0x26a6d98],
        number_of_bytes=2,
        possible_values=[New_Flamedramon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Flamedramon Deck 3",
        addresses=[0x26a6d9a],
        number_of_bytes=2,
        possible_values=[New_Flamedramon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Flamedramon Deck 4",
        addresses=[0x26a6d9c,0x26a6d9e,0x26a6da0,0x26a6da2],
        number_of_bytes=2,
        possible_values=[New_Flamedramon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Flamedramon Deck 5",
        addresses=[0x26a6da4],
        number_of_bytes=2,
        possible_values=[New_Flamedramon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Flamedramon Deck 6",
		addresses=[0x26a6da6,0x26a6da8,0x26a6daa,0x26a6dac],
		number_of_bytes=2,
		possible_values=[New_Flamedramon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Flamedramon Deck 7",
		addresses=[0x26a6dae,0x26a6db0,0x26a6db2],
		number_of_bytes=2,
		possible_values=[New_Flamedramon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Flamedramon Deck 8",
		addresses=[0x26a6db4,0x26a6db6],
		number_of_bytes=2,
		possible_values=[New_Flamedramon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Flamedramon Deck 9",
		addresses=[0x26a6db8],
		number_of_bytes=2,
		possible_values=[175],
		is_little_endian=True, ),
	Attribute(
		name="Flamedramon Deck 10",
		addresses=[0x26a6dba,0x26a6dbc],
		number_of_bytes=2,
		possible_values=[New_Flamedramon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Flamedramon Deck 11",
		addresses=[0x26a6dbe,0x26a6dc0],
		number_of_bytes=2,
		possible_values=[New_Flamedramon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Flamedramon Deck 12",
		addresses=[0x26a6dc2,0x26a6dc4,0x26a6dc6],
		number_of_bytes=2,
		possible_values=[New_Flamedramon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Flamedramon Deck 13",
		addresses=[0x26a6dc8,0x26a6dca,0x26a6dcc],
		number_of_bytes=2,
		possible_values=[New_Flamedramon_Deck[12]],
		is_little_endian=True, ),
#Raidramon
    Attribute(
        name="Raidramon Deck 1",
        addresses=[0x26a6f30,0x26a6f32,0x26a6f34],
        number_of_bytes=2,
        possible_values=[New_Raidramon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Raidramon Deck 2",
        addresses=[0x26a6f36],
        number_of_bytes=2,
        possible_values=[New_Raidramon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Raidramon Deck 3",
        addresses=[0x26a6f38,0x26a6f3a,0x26a6f3c],
        number_of_bytes=2,
        possible_values=[New_Raidramon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Raidramon Deck 4",
        addresses=[0x26a6f3e],
        number_of_bytes=2,
        possible_values=[New_Raidramon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Raidramon Deck 5",
        addresses=[0x26a6f40,0x26a6f42,0x26a6f44],
        number_of_bytes=2,
        possible_values=[New_Raidramon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Raidramon Deck 6",
		addresses=[0x26a6f46,0x26a6f48],
		number_of_bytes=2,
		possible_values=[New_Raidramon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Raidramon Deck 7",
		addresses=[0x26a6f4a,0x26a6f4c,0x26a6f4e],
		number_of_bytes=2,
		possible_values=[New_Raidramon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Raidramon Deck 8",
		addresses=[0x26a6f50,0x26a6f52],
		number_of_bytes=2,
		possible_values=[New_Raidramon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Raidramon Deck 9",
		addresses=[0x26a6f54],
		number_of_bytes=2,
		possible_values=[175],
		is_little_endian=True, ),
	Attribute(
		name="Raidramon Deck 10",
		addresses=[0x26a6f56,0x26a6f58,0x26a6f5a],
		number_of_bytes=2,
		possible_values=[New_Raidramon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Raidramon Deck 11",
		addresses=[0x26a6f5c,0x26a6f5e,0x26a6f60],
		number_of_bytes=2,
		possible_values=[New_Raidramon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Raidramon Deck 12",
		addresses=[0x26a6f62],
		number_of_bytes=2,
		possible_values=[New_Raidramon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Raidramon Deck 13",
		addresses=[0x26a6f64,0x26a6f66],
		number_of_bytes=2,
		possible_values=[New_Raidramon_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Raidramon Deck 14",
		addresses=[0x26a6f68],
		number_of_bytes=2,
		possible_values=[New_Raidramon_Deck[13]],
		is_little_endian=True, ),
	Attribute(
		name="Raidramon Deck 15",
		addresses=[0x26a6f6a],
		number_of_bytes=2,
		possible_values=[New_Raidramon_Deck[14]],
		is_little_endian=True, ),
#Hawkmon
    Attribute(
        name="Hawkmon Deck 1",
        addresses=[0x26a6f9e,0x26a6fa0],
        number_of_bytes=2,
        possible_values=[New_Hawkmon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Hawkmon Deck 2",
        addresses=[0x26a6fa2],
        number_of_bytes=2,
        possible_values=[New_Hawkmon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Hawkmon Deck 3",
        addresses=[0x26a6fa4,0x26a6fa6,0x26a6fa8],
        number_of_bytes=2,
        possible_values=[New_Hawkmon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Hawkmon Deck 4",
        addresses=[0x26a6faa,0x26a6fac,0x26a6fae],
        number_of_bytes=2,
        possible_values=[New_Hawkmon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Hawkmon Deck 5",
        addresses=[0x26a6fb0,0x26a6fb2,0x26a6fb4,0x26a6fb6],
        number_of_bytes=2,
        possible_values=[New_Hawkmon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Hawkmon Deck 6",
		addresses=[0x26a6fb8,0x26a6fba,0x26a6fbc,0x26a6fbe],
		number_of_bytes=2,
		possible_values=[New_Hawkmon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Hawkmon Deck 7",
		addresses=[0x26a6fc0,0x26a6fc2],
		number_of_bytes=2,
		possible_values=[New_Hawkmon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Hawkmon Deck 8",
		addresses=[0x26a6fc4],
		number_of_bytes=2,
		possible_values=[182],
		is_little_endian=True, ),
	Attribute(
		name="Hawkmon Deck 9",
		addresses=[0x26a6fc6],
		number_of_bytes=2,
		possible_values=[New_Hawkmon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Hawkmon Deck 10",
		addresses=[0x26a6fc8],
		number_of_bytes=2,
		possible_values=[New_Hawkmon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Hawkmon Deck 11",
		addresses=[0x26a6fca],
		number_of_bytes=2,
		possible_values=[New_Hawkmon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Hawkmon Deck 12",
		addresses=[0x26a6fcc],
		number_of_bytes=2,
		possible_values=[New_Hawkmon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Hawkmon Deck 13",
		addresses=[0x26a6fce],
		number_of_bytes=2,
		possible_values=[New_Hawkmon_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Hawkmon Deck 14",
		addresses=[0x26a6fd0,0x26a6fd2,0x26a6fd4,0x26a6fd6],
		number_of_bytes=2,
		possible_values=[New_Hawkmon_Deck[13]],
		is_little_endian=True, ),
	Attribute(
		name="Hawkmon Deck 15",
		addresses=[0x26a6fd8],
		number_of_bytes=2,
		possible_values=[New_Hawkmon_Deck[14]],
		is_little_endian=True, ),
#Aquilamon
    Attribute(
        name="Aquilamon Deck 1",
        addresses=[0x26a700c,0x26a700e],
        number_of_bytes=2,
        possible_values=[New_Aquilamon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Aquilamon Deck 2",
        addresses=[0x26a7010,0x26a7012],
        number_of_bytes=2,
        possible_values=[New_Aquilamon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Aquilamon Deck 3",
        addresses=[0x26a7014,0x26a7016],
        number_of_bytes=2,
        possible_values=[New_Aquilamon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Aquilamon Deck 4",
        addresses=[0x26a7018,0x26a701a],
        number_of_bytes=2,
        possible_values=[New_Aquilamon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Aquilamon Deck 5",
        addresses=[0x26a701c,0x26a701e],
        number_of_bytes=2,
        possible_values=[New_Aquilamon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Aquilamon Deck 6",
		addresses=[0x26a7020,0x26a7022],
		number_of_bytes=2,
		possible_values=[New_Aquilamon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Aquilamon Deck 7",
		addresses=[0x26a7024],
		number_of_bytes=2,
		possible_values=[New_Aquilamon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Aquilamon Deck 8",
		addresses=[0x26a7026,0x26a7028,0x26a702a,0x26a702c],
		number_of_bytes=2,
		possible_values=[New_Aquilamon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Aquilamon Deck 9",
		addresses=[0x26a702e,0x26a7030,0x26a7032],
		number_of_bytes=2,
		possible_values=[New_Aquilamon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Aquilamon Deck 10",
		addresses=[0x26a7034],
		number_of_bytes=2,
		possible_values=[New_Aquilamon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Aquilamon Deck 11",
		addresses=[0x26a7036],
		number_of_bytes=2,
		possible_values=[182],
		is_little_endian=True, ),
	Attribute(
		name="Aquilamon Deck 12",
		addresses=[0x26a7038,0x26a703a],
		number_of_bytes=2,
		possible_values=[New_Aquilamon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Aquilamon Deck 13",
		addresses=[0x26a703c,0x26a703e],
		number_of_bytes=2,
		possible_values=[New_Aquilamon_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Aquilamon Deck 14",
		addresses=[0x26a7040,0x26a7042],
		number_of_bytes=2,
		possible_values=[New_Aquilamon_Deck[13]],
		is_little_endian=True, ),
	Attribute(
		name="Aquilamon Deck 15",
		addresses=[0x26a7044,0x26a7046],
		number_of_bytes=2,
		possible_values=[New_Aquilamon_Deck[14]],
		is_little_endian=True, ),
#Halsemon
    Attribute(
        name="Halsemon Deck 1",
        addresses=[0x26a707a,0x26a707c,0x26a707e],
        number_of_bytes=2,
        possible_values=[New_Halsemon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Halsemon Deck 2",
        addresses=[0x26a7080,0x26a7082],
        number_of_bytes=2,
        possible_values=[New_Halsemon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Halsemon Deck 3",
        addresses=[0x26a7084,0x26a7086,0x26a7088],
        number_of_bytes=2,
        possible_values=[New_Halsemon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Halsemon Deck 4",
        addresses=[0x26a708a,0x26a708c],
        number_of_bytes=2,
        possible_values=[New_Halsemon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Halsemon Deck 5",
        addresses=[0x26a708e,0x26a7090,0x26a7092],
        number_of_bytes=2,
        possible_values=[New_Halsemon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Halsemon Deck 6",
		addresses=[0x26a7094,0x26a7096,0x26a7098],
		number_of_bytes=2,
		possible_values=[New_Halsemon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Halsemon Deck 7",
		addresses=[0x26a709a,0x26a709c,0x26a709e],
		number_of_bytes=2,
		possible_values=[New_Halsemon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Halsemon Deck 8",
		addresses=[0x26a70a0],
		number_of_bytes=2,
		possible_values=[182],
		is_little_endian=True, ),
	Attribute(
		name="Halsemon Deck 9",
		addresses=[0x26a70a2,0x26a70a4,0x26a70a6],
		number_of_bytes=2,
		possible_values=[New_Halsemon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Halsemon Deck 10",
		addresses=[0x26a70a8,0x26a70aa,0x26a70ac],
		number_of_bytes=2,
		possible_values=[New_Halsemon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Halsemon Deck 11",
		addresses=[0x26a70ae,0x26a70b0,0x26a70b2],
		number_of_bytes=2,
		possible_values=[New_Halsemon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Halsemon Deck 12",
		addresses=[0x26a70b4],
		number_of_bytes=2,
		possible_values=[New_Halsemon_Deck[11]],
		is_little_endian=True, ),
#Penguinmon
    Attribute(
        name="Penguinmon Deck 1",
        addresses=[0x26a546c],
        number_of_bytes=2,
        possible_values=[New_Penguinmon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Penguinmon Deck 2",
        addresses=[0x26a546e,0x26a5470],
        number_of_bytes=2,
        possible_values=[New_Penguinmon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Penguinmon Deck 3",
        addresses=[0x26a5472,0x26a5474],
        number_of_bytes=2,
        possible_values=[New_Penguinmon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Penguinmon Deck 4",
        addresses=[0x26a5476],
        number_of_bytes=2,
        possible_values=[New_Penguinmon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Penguinmon Deck 5",
        addresses=[0x26a5478,0x26a547a],
        number_of_bytes=2,
        possible_values=[New_Penguinmon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Penguinmon Deck 6",
		addresses=[0x26a547c],
		number_of_bytes=2,
		possible_values=[New_Penguinmon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Penguinmon Deck 7",
		addresses=[0x26a547e,0x26a5480],
		number_of_bytes=2,
		possible_values=[New_Penguinmon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Penguinmon Deck 8",
		addresses=[0x26a5482,0x26a5484,0x26a5486],
		number_of_bytes=2,
		possible_values=[New_Penguinmon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Penguinmon Deck 9",
		addresses=[0x26a5488,0x26a548a,0x26a548c,0x26a548e],
		number_of_bytes=2,
		possible_values=[New_Penguinmon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Penguinmon Deck 10",
		addresses=[0x26a5490,0x26a5492],
		number_of_bytes=2,
		possible_values=[New_Penguinmon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Penguinmon Deck 11",
		addresses=[0x26a5494,0x26a5496],
		number_of_bytes=2,
		possible_values=[New_Penguinmon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Penguinmon Deck 12",
		addresses=[0x26a5498,0x26a549a],
		number_of_bytes=2,
		possible_values=[New_Penguinmon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Penguinmon Deck 13",
		addresses=[0x26a549e,0x26a54a0],
		number_of_bytes=2,
		possible_values=[New_Penguinmon_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Penguinmon Deck 14",
		addresses=[0x26a54a2,0x26a54a4],
		number_of_bytes=2,
		possible_values=[New_Penguinmon_Deck[13]],
		is_little_endian=True, ),
	Attribute(
		name="Penguinmon Deck 15",
		addresses=[0x26a54a6],
		number_of_bytes=2,
		possible_values=[New_Penguinmon_Deck[14]],
		is_little_endian=True, ),
#Rosemon
    Attribute(
        name="Rosemon Deck 1",
        addresses=[0x26a8d64,0x26a8d66,0x26a8d68],
        number_of_bytes=2,
        possible_values=[New_Rosemon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Rosemon Deck 2",
        addresses=[0x26a8d6a,0x26a8d6c],
        number_of_bytes=2,
        possible_values=[New_Rosemon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Rosemon Deck 3",
        addresses=[0x26a8d6e,0x26a8d70],
        number_of_bytes=2,
        possible_values=[New_Rosemon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Rosemon Deck 4",
        addresses=[0x26a8d72,0x26a8d74],
        number_of_bytes=2,
        possible_values=[New_Rosemon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Rosemon Deck 5",
        addresses=[0x26a8d76],
        number_of_bytes=2,
        possible_values=[New_Rosemon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Rosemon Deck 6",
		addresses=[0x26a8d78,0x26a8d7a,0x26a8d7c,0x26a8d7e],
		number_of_bytes=2,
		possible_values=[New_Rosemon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Rosemon Deck 7",
		addresses=[0x26a8d80,0x26a8d82,0x26a8d84],
		number_of_bytes=2,
		possible_values=[New_Rosemon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Rosemon Deck 8",
		addresses=[0x26a8d86,0x26a8d88,0x26a8d8a],
		number_of_bytes=2,
		possible_values=[New_Rosemon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Rosemon Deck 9",
		addresses=[0x26a8d8c,0x26a8d8e],
		number_of_bytes=2,
		possible_values=[New_Rosemon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Rosemon Deck 10",
		addresses=[0x26a8d90],
		number_of_bytes=2,
		possible_values=[New_Rosemon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Rosemon Deck 11",
		addresses=[0x26a8d92,0x26a8d94],
		number_of_bytes=2,
		possible_values=[New_Rosemon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Rosemon Deck 12",
		addresses=[0x26a8d96],
		number_of_bytes=2,
		possible_values=[New_Rosemon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Rosemon Deck 13",
		addresses=[0x26a8d98,0x26a8d9a],
		number_of_bytes=2,
		possible_values=[New_Rosemon_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Rosemon Deck 14",
		addresses=[0x26a8d9c,0x26a8d9e],
		number_of_bytes=2,
		possible_values=[New_Rosemon_Deck[13]],
		is_little_endian=True, ),
#Armadillomon
    Attribute(
        name="Armadillomon Deck 1",
        addresses=[0x26a70e8,0x26a70ea,0x26a70ec,0x26a70ee],
        number_of_bytes=2,
        possible_values=[New_Armadillomon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Armadillomon Deck 2",
        addresses=[0x26a70f0,0x26a70f2],
        number_of_bytes=2,
        possible_values=[New_Armadillomon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Armadillomon Deck 3",
        addresses=[0x26a70f4,0x26a70f6,0x26a70f8],
        number_of_bytes=2,
        possible_values=[New_Armadillomon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Armadillomon Deck 4",
        addresses=[0x26a70fa,0x26a70fc],
        number_of_bytes=2,
        possible_values=[New_Armadillomon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Armadillomon Deck 5",
        addresses=[0x26a70fe,0x26a7100,0x26a7102],
        number_of_bytes=2,
        possible_values=[New_Armadillomon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Armadillomon Deck 6",
		addresses=[0x26a7104],
		number_of_bytes=2,
		possible_values=[190],
		is_little_endian=True, ),
	Attribute(
		name="Armadillomon Deck 7",
		addresses=[0x26a7106,0x26a7108],
		number_of_bytes=2,
		possible_values=[New_Armadillomon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Armadillomon Deck 8",
		addresses=[0x26a710a,0x26a710c],
		number_of_bytes=2,
		possible_values=[New_Armadillomon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Armadillomon Deck 9",
		addresses=[0x26a710e,0x26a7110,0x26a7112],
		number_of_bytes=2,
		possible_values=[New_Armadillomon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Armadillomon Deck 10",
		addresses=[0x26a7114,0x26a7116],
		number_of_bytes=2,
		possible_values=[New_Armadillomon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Armadillomon Deck 11",
		addresses=[0x26a7118,0x26a711a,0x26a711c,0x26a711e],
		number_of_bytes=2,
		possible_values=[New_Armadillomon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Armadillomon Deck 12",
		addresses=[0x26a7120,0x26a7122],
		number_of_bytes=2,
		possible_values=[New_Armadillomon_Deck[11]],
		is_little_endian=True, ),
#Ankylomon
    Attribute(
        name="Ankylomon Deck 1",
        addresses=[0x26a7156,0x26a7158,0x26a715a],
        number_of_bytes=2,
        possible_values=[New_Ankylomon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Ankylomon Deck 2",
        addresses=[0x26a715c,0x26a715e,0x26a7160,0x26a7162],
        number_of_bytes=2,
        possible_values=[New_Ankylomon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Ankylomon Deck 3",
        addresses=[0x26a7164,0x26a7166],
        number_of_bytes=2,
        possible_values=[New_Ankylomon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Ankylomon Deck 4",
        addresses=[0x26a7168,0x26a716a],
        number_of_bytes=2,
        possible_values=[New_Ankylomon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Ankylomon Deck 5",
        addresses=[0x26a716c,0x26a716e,0x26a7170],
        number_of_bytes=2,
        possible_values=[New_Ankylomon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Ankylomon Deck 6",
		addresses=[0x26a7172,0x26a7174],
		number_of_bytes=2,
		possible_values=[New_Ankylomon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Ankylomon Deck 7",
		addresses=[0x26a7176,0x26a7178],
		number_of_bytes=2,
		possible_values=[New_Ankylomon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Ankylomon Deck 8",
		addresses=[0x26a717a,0x26a717c,0x26a717e],
		number_of_bytes=2,
		possible_values=[New_Ankylomon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Ankylomon Deck 9",
		addresses=[0x26a7180,0x26a7182,0x26a7184],
		number_of_bytes=2,
		possible_values=[New_Ankylomon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Ankylomon Deck 10",
		addresses=[0x26a7186,0x26a7188,0x26a718a],
		number_of_bytes=2,
		possible_values=[New_Ankylomon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Ankylomon Deck 11",
		addresses=[0x26a718c,0x26a718e,0x26a7190],
		number_of_bytes=2,
		possible_values=[New_Ankylomon_Deck[10]],
		is_little_endian=True, ),
#Digmon
    Attribute(
        name="Digmon Deck 1",
        addresses=[0x26a71c4,0x26a71c6],
        number_of_bytes=2,
        possible_values=[New_Digmon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Digmon Deck 2",
        addresses=[0x26a71c8,0x26a71ca,0x26a71cc,0x26a71ce],
        number_of_bytes=2,
        possible_values=[New_Digmon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Digmon Deck 3",
        addresses=[0x26a71d0,0x26a71d2],
        number_of_bytes=2,
        possible_values=[New_Digmon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Digmon Deck 4",
        addresses=[0x26a71d4,0x26a71d6,0x26a71d8],
        number_of_bytes=2,
        possible_values=[New_Digmon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Digmon Deck 5",
        addresses=[0x26a71da,0x26a71dc],
        number_of_bytes=2,
        possible_values=[New_Digmon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Digmon Deck 6",
		addresses=[0x26a71de,0x26a71e0],
		number_of_bytes=2,
		possible_values=[190],
		is_little_endian=True, ),
	Attribute(
		name="Digmon Deck 7",
		addresses=[0x26a71e2],
		number_of_bytes=2,
		possible_values=[190],
		is_little_endian=True, ),
	Attribute(
		name="Digmon Deck 8",
		addresses=[0x26a71e4,0x26a71e6],
		number_of_bytes=2,
		possible_values=[New_Digmon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Digmon Deck 9",
		addresses=[0x26a71e8],
		number_of_bytes=2,
		possible_values=[New_Digmon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Digmon Deck 10",
		addresses=[0x26a71ea,0x26a71ec],
		number_of_bytes=2,
		possible_values=[New_Digmon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Digmon Deck 11",
		addresses=[0x26a71ee,0x26a71f0,0x26a71f2],
		number_of_bytes=2,
		possible_values=[New_Digmon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Digmon Deck 12",
		addresses=[0x26a71f4,0x26a71f6],
		number_of_bytes=2,
		possible_values=[New_Digmon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Digmon Deck 13",
		addresses=[0x26a71f8,0x26a71fa,0x26a71fc,0x26a71fe],
		number_of_bytes=2,
		possible_values=[New_Digmon_Deck[12]],
		is_little_endian=True, ),
#Thundermon
    Attribute(
        name="Thundermon Deck 1",
        addresses=[0x26a7232,0x26a7234,0x26a7236],
        number_of_bytes=2,
        possible_values=[New_Thundermon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Thundermon Deck 2",
        addresses=[0x26a7238,0x26a723a,0x26a723c,0x26a723e],
        number_of_bytes=2,
        possible_values=[New_Thundermon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Thundermon Deck 3",
        addresses=[0x26a7240,0x26a7242],
        number_of_bytes=2,
        possible_values=[New_Thundermon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Thundermon Deck 4",
        addresses=[0x26a7244,0x26a7246,0x26a7248,0x26a724a],
        number_of_bytes=2,
        possible_values=[New_Thundermon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Thundermon Deck 5",
        addresses=[0x26a724c,0x26a724e,0x26a7250,0x26a7252],
        number_of_bytes=2,
        possible_values=[New_Thundermon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Thundermon Deck 6",
		addresses=[0x26a7254,0x26a7256],
		number_of_bytes=2,
		possible_values=[New_Thundermon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Thundermon Deck 7",
		addresses=[0x26a7258,0x26a725a],
		number_of_bytes=2,
		possible_values=[New_Thundermon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Thundermon Deck 8",
		addresses=[0x26a725c,0x26a725e],
		number_of_bytes=2,
		possible_values=[New_Thundermon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Thundermon Deck 9",
		addresses=[0x26a7260,0x26a7262],
		number_of_bytes=2,
		possible_values=[New_Thundermon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Thundermon Deck 10",
		addresses=[0x26a7264,0x26a7266],
		number_of_bytes=2,
		possible_values=[New_Thundermon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Thundermon Deck 11",
		addresses=[0x26a7268],
		number_of_bytes=2,
		possible_values=[New_Thundermon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Thundermon Deck 12",
		addresses=[0x26a726a,0x26a726c],
		number_of_bytes=2,
		possible_values=[New_Thundermon_Deck[11]],
		is_little_endian=True, ),
#MetalMamemon
    Attribute(
        name="MetalMamemon Deck 1",
        addresses=[0x26a72a0,0x26a72a2],
        number_of_bytes=2,
        possible_values=[New_MetalMamemon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="MetalMamemon Deck 2",
        addresses=[0x26a72a4,0x26a72a6],
        number_of_bytes=2,
        possible_values=[New_MetalMamemon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="MetalMamemon Deck 3",
        addresses=[0x26a72a8,0x26a72aa],
        number_of_bytes=2,
        possible_values=[New_MetalMamemon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="MetalMamemon Deck 4",
        addresses=[0x26a72ac,0x26a72ae,0x26a72b0],
        number_of_bytes=2,
        possible_values=[New_MetalMamemon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="MetalMamemon Deck 5",
        addresses=[0x26a72b2,0x26a72b4],
        number_of_bytes=2,
        possible_values=[New_MetalMamemon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="MetalMamemon Deck 6",
		addresses=[0x26a72b6,0x26a72b8],
		number_of_bytes=2,
		possible_values=[New_MetalMamemon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="MetalMamemon Deck 7",
		addresses=[0x26a72ba,0x26a72bc],
		number_of_bytes=2,
		possible_values=[New_MetalMamemon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="MetalMamemon Deck 8",
		addresses=[0x26a72be,0x26a72c0],
		number_of_bytes=2,
		possible_values=[New_MetalMamemon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="MetalMamemon Deck 9",
		addresses=[0x26a72c2,0x26a72c4,0x26a72c6],
		number_of_bytes=2,
		possible_values=[New_MetalMamemon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="MetalMamemon Deck 10",
		addresses=[0x26a72c8,0x26a72ca,0x26a72cc],
		number_of_bytes=2,
		possible_values=[New_MetalMamemon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="MetalMamemon Deck 11",
		addresses=[0x26a72ce,0x26a72d0,0x26a72d2],
		number_of_bytes=2,
		possible_values=[New_MetalMamemon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="MetalMamemon Deck 12",
		addresses=[0x26a72d4,0x26a72d6],
		number_of_bytes=2,
		possible_values=[New_MetalMamemon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="MetalMamemon Deck 13",
		addresses=[0x26a72d8,0x26a72da],
		number_of_bytes=2,
		possible_values=[New_MetalMamemon_Deck[12]],
		is_little_endian=True, ),
#SuperStarmon
    Attribute(
        name="SuperStarmon Deck 1",
        addresses=[0x26a730e,0x26a7310,0x26a7312,0x26a7314],
        number_of_bytes=2,
        possible_values=[New_SuperStarmon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="SuperStarmon Deck 2",
        addresses=[0x26a7316],
        number_of_bytes=2,
        possible_values=[New_SuperStarmon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="SuperStarmon Deck 3",
        addresses=[0x26a7318,0x26a731a,0x26a731c,0x26a731e],
        number_of_bytes=2,
        possible_values=[New_SuperStarmon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="SuperStarmon Deck 4",
        addresses=[0x26a7320,0x26a7322,0x26a7324,0x26a7326],
        number_of_bytes=2,
        possible_values=[New_SuperStarmon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="SuperStarmon Deck 5",
        addresses=[0x26a7328,0x26a732a,0x26a732c,0x26a732e],
        number_of_bytes=2,
        possible_values=[New_SuperStarmon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="SuperStarmon Deck 6",
		addresses=[0x26a7330,0x26a7332,0x26a7334],
		number_of_bytes=2,
		possible_values=[New_SuperStarmon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="SuperStarmon Deck 7",
		addresses=[0x26a7336,0x26a7338,0x26a733a,0x26a733c],
		number_of_bytes=2,
		possible_values=[New_SuperStarmon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="SuperStarmon Deck 8",
		addresses=[0x26a733e,0x26a7340],
		number_of_bytes=2,
		possible_values=[New_SuperStarmon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="SuperStarmon Deck 9",
		addresses=[0x26a7342,0x26a7344],
		number_of_bytes=2,
		possible_values=[New_SuperStarmon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="SuperStarmon Deck 10",
		addresses=[0x26a7346,0x26a7348],
		number_of_bytes=2,
		possible_values=[New_SuperStarmon_Deck[9]],
		is_little_endian=True, ),
#Bakemon
	# Bakemon
	Attribute(
		name="Bakemon Deck 1",
		addresses=[0x26a737c, 0x26a737e, 0x26a7380, 0x26a7382],
		number_of_bytes=2,
		possible_values=[New_Bakemon_Deck[0]],
		is_little_endian=True, ),
	Attribute(
		name="Bakemon Deck 2",
		addresses=[0x26a7384, 0x26a7386, 0x26a7388, 0x26a738a],
		number_of_bytes=2,
		possible_values=[New_Bakemon_Deck[1]],
		is_little_endian=True, ),
	Attribute(
		name="Bakemon Deck 3",
		addresses=[0x26a738c, 0x26a738e, 0x26a7390],
		number_of_bytes=2,
		possible_values=[New_Bakemon_Deck[2]],
		is_little_endian=True, ),
	Attribute(
		name="Bakemon Deck 4",
		addresses=[0x26a7392, 0x26a7394, 0x26a7396],
		number_of_bytes=2,
		possible_values=[New_Bakemon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Bakemon Deck 5",
		addresses=[0x26a7398, 0x26a739a, 0x26a739c, 0x26a739e],
		number_of_bytes=2,
		possible_values=[New_Bakemon_Deck[4]],
		is_little_endian=True, ),
	Attribute(
		name="Bakemon Deck 6",
		addresses=[0x26a73a0],
		number_of_bytes=2,
		possible_values=[New_Bakemon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Bakemon Deck 7",
		addresses=[0x26a73a2, 0x26a73a4, 0x26a73a6],
		number_of_bytes=2,
		possible_values=[New_Bakemon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Bakemon Deck 8",
		addresses=[0x26a73a8, 0x26a73aa, 0x26a73ac, 0x26a73ae],
		number_of_bytes=2,
		possible_values=[New_Bakemon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Bakemon Deck 9",
		addresses=[0x26a73b0, 0x26a73b2, 0x26a73b4, 0x26a73b6],
		number_of_bytes=2,
		possible_values=[New_Bakemon_Deck[8]],
		is_little_endian=True, ),
#Devimon2
    Attribute(
        name="Devimon2 Deck 1",
        addresses=[0x26a73ea,0x26a73ec],
        number_of_bytes=2,
        possible_values=[New_Devimon2_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Devimon2 Deck 2",
        addresses=[0x26a73ee,0x26a73f0],
        number_of_bytes=2,
        possible_values=[New_Devimon2_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Devimon2 Deck 3",
        addresses=[0x26a73f2,0x26a73f4,0x26a73f6,0x26a73f8],
        number_of_bytes=2,
        possible_values=[New_Devimon2_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Devimon2 Deck 4",
        addresses=[0x26a73fa,0x26a73fc],
        number_of_bytes=2,
        possible_values=[New_Devimon2_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Devimon2 Deck 5",
        addresses=[0x26a73fe,0x26a7400,0x26a7402,0x26a7404],
        number_of_bytes=2,
        possible_values=[New_Devimon2_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Devimon2 Deck 6",
		addresses=[0x26a7406,0x26a7408,0x26a740a],
		number_of_bytes=2,
		possible_values=[New_Devimon2_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Devimon2 Deck 7",
		addresses=[0x26a740c,0x26a740e,0x26a7410],
		number_of_bytes=2,
		possible_values=[New_Devimon2_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Devimon2 Deck 8",
		addresses=[0x26a7412,0x26a7414,0x26a7416,0x26a7418],
		number_of_bytes=2,
		possible_values=[New_Devimon2_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Devimon2 Deck 9",
		addresses=[0x26a741a,0x26a741c],
		number_of_bytes=2,
		possible_values=[New_Devimon2_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Devimon2 Deck 10",
		addresses=[0x26a741e,0x26a7420],
		number_of_bytes=2,
		possible_values=[New_Devimon2_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Devimon2 Deck 11",
		addresses=[0x26a7422,0x26a7424],
		number_of_bytes=2,
		possible_values=[New_Devimon2_Deck[10]],
		is_little_endian=True, ),
#SkullGreymon
    Attribute(
        name="SkullGreymon Deck 1",
        addresses=[0x26a7458,0x26a745a,0x26a745c,0x26a745e],
        number_of_bytes=2,
        possible_values=[New_SkullGreymon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="SkullGreymon Deck 2",
        addresses=[0x26a7460,0x26a7462,0x26a7464],
        number_of_bytes=2,
        possible_values=[New_SkullGreymon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="SkullGreymon Deck 3",
        addresses=[0x26a7466,0x26a7468],
        number_of_bytes=2,
        possible_values=[New_SkullGreymon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="SkullGreymon Deck 4",
        addresses=[0x26a746a,0x26a746c],
        number_of_bytes=2,
        possible_values=[New_SkullGreymon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="SkullGreymon Deck 5",
        addresses=[0x26a746e,0x26a7470,0x26a7472,0x26a7474],
        number_of_bytes=2,
        possible_values=[New_SkullGreymon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="SkullGreymon Deck 6",
		addresses=[0x26a7476,0x26a7478,0x26a747a],
		number_of_bytes=2,
		possible_values=[New_SkullGreymon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="SkullGreymon Deck 7",
		addresses=[0x26a747c,0x26a747e,0x26a7480],
		number_of_bytes=2,
		possible_values=[New_SkullGreymon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="SkullGreymon Deck 8",
		addresses=[0x26a7482,0x26a7484,0x26a7486],
		number_of_bytes=2,
		possible_values=[New_SkullGreymon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="SkullGreymon Deck 9",
		addresses=[0x26a7488,0x26a748a,0x26a748c],
		number_of_bytes=2,
		possible_values=[New_SkullGreymon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="SkullGreymon Deck 10",
		addresses=[0x26a748e,0x26a7490,0x26a7492],
		number_of_bytes=2,
		possible_values=[New_SkullGreymon_Deck[9]],
		is_little_endian=True, ),
#Myotismon2
    Attribute(
        name="Myotismon2 Deck 1",
        addresses=[0x26a74c6,0x26a74c8,0x26a74ca,0x26a74cc],
        number_of_bytes=2,
        possible_values=[New_Myotismon2_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Myotismon2 Deck 2",
        addresses=[0x26a74ce,0x26a74d0,0x26a74d2,0x26a74d4],
        number_of_bytes=2,
        possible_values=[New_Myotismon2_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Myotismon2 Deck 3",
        addresses=[0x26a74d6,0x26a74d8,0x26a74da],
        number_of_bytes=2,
        possible_values=[New_Myotismon2_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Myotismon2 Deck 4",
        addresses=[0x26a74dc,0x26a74de,0x26a74e0],
        number_of_bytes=2,
        possible_values=[New_Myotismon2_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Myotismon2 Deck 5",
        addresses=[0x26a74e2,0x26a74e4,0x26a74e6,0x26a74e8],
        number_of_bytes=2,
        possible_values=[New_Myotismon2_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Myotismon2 Deck 6",
		addresses=[0x26a74ea,0x26a74ec,0x26a74ee],
		number_of_bytes=2,
		possible_values=[New_Myotismon2_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Myotismon2 Deck 7",
		addresses=[0x26a74f0,0x26a74f2],
		number_of_bytes=2,
		possible_values=[New_Myotismon2_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Myotismon2 Deck 8",
		addresses=[0x26a74f4],
		number_of_bytes=2,
		possible_values=[New_Myotismon2_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Myotismon2 Deck 9",
		addresses=[0x26a74f6],
		number_of_bytes=2,
		possible_values=[New_Myotismon2_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Myotismon2 Deck 10",
		addresses=[0x26a74f8],
		number_of_bytes=2,
		possible_values=[New_Myotismon2_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Myotismon2 Deck 11",
		addresses=[0x26a74fa,0x26a74fc],
		number_of_bytes=2,
		possible_values=[New_Myotismon2_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Myotismon2 Deck 12",
		addresses=[0x26a74fe],
		number_of_bytes=2,
		possible_values=[New_Myotismon2_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Myotismon2 Deck 13",
		addresses=[0x26a7500],
		number_of_bytes=2,
		possible_values=[New_Myotismon2_Deck[12]],
		is_little_endian=True, ),
#Patamon
    Attribute(
        name="Patamon Deck 1",
        addresses=[0x26a7534,0x26a7536],
        number_of_bytes=2,
        possible_values=[New_Patamon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Patamon Deck 2",
        addresses=[0x26a7538,0x26a753a],
        number_of_bytes=2,
        possible_values=[New_Patamon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Patamon Deck 3",
        addresses=[0x26a753c,0x26a753e],
        number_of_bytes=2,
        possible_values=[New_Patamon_Deck[2]],
        is_little_endian=True, ),
    Attribute(
        name="Patamon Deck 4",
        addresses=[0x26a7540,0x26a7542],
        number_of_bytes=2,
        possible_values=[New_Patamon_Deck[3]],
        is_little_endian=True, ),
    Attribute(
        name="Patamon Deck 5",
        addresses=[0x26a7544,0x26a7546],
        number_of_bytes=2,
        possible_values=[New_Patamon_Deck[4]],
        is_little_endian=True, ),
	Attribute(
		name="Patamon Deck 6",
		addresses=[0x26a7548,0x26a754a],
		number_of_bytes=2,
		possible_values=[New_Patamon_Deck[5]],
		is_little_endian=True, ),
	Attribute(
		name="Patamon Deck 7",
		addresses=[0x26a754c],
		number_of_bytes=2,
		possible_values=[183],
		is_little_endian=True, ),
	Attribute(
		name="Patamon Deck 8",
		addresses=[0x26a754e,0x26a7550,0x26a7552,0x26a7554],
		number_of_bytes=2,
		possible_values=[New_Patamon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Patamon Deck 9",
		addresses=[0x26a7556],
		number_of_bytes=2,
		possible_values=[New_Patamon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Patamon Deck 10",
		addresses=[0x26a7558,0x26a755a,0x26a755c,0x26a755e],
		number_of_bytes=2,
		possible_values=[New_Patamon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Patamon Deck 11",
		addresses=[0x26a7560,0x26a7562,0x26a7564,0x26a7566],
		number_of_bytes=2,
		possible_values=[New_Patamon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Patamon Deck 12",
		addresses=[0x26a7568,0x26a756a,0x26a756c,0x26a756e],
		number_of_bytes=2,
		possible_values=[New_Patamon_Deck[11]],
		is_little_endian=True, ),
#Baronmon
    Attribute(
        name="Baronmon Deck 1",
        addresses=[0x26a75a2,0x26a75a4],
        number_of_bytes=2,
        possible_values=[New_Baronmon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Baronmon Deck 2",
        addresses=[0x26a75a6,0x26a75a8],
        number_of_bytes=2,
        possible_values=[New_Baronmon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Baronmon Deck 3",
        addresses=[0x26a75aa,0x26a75ac,0x26a75ae],
        number_of_bytes=2,
        possible_values=[New_Baronmon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Baronmon Deck 4",
		addresses=[0x26a75b0, 0x26a75b2, 0x26a75b4],
		number_of_bytes=2,
		possible_values=[New_Baronmon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Baronmon Deck 5",
		addresses=[0x26a75b6, 0x26a75b8, 0x26a75ba],
		number_of_bytes=2,
		possible_values=[New_Baronmon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Baronmon Deck 6",
        addresses=[0x26a75bc,0x26a75be],
        number_of_bytes=2,
        possible_values=[New_Baronmon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Baronmon Deck 7",
		addresses=[0x26a75c0,0x26a75c2],
		number_of_bytes=2,
		possible_values=[New_Baronmon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Baronmon Deck 8",
		addresses=[0x26a75c4,0x26a75c6,0x26a75c8],
		number_of_bytes=2,
		possible_values=[New_Baronmon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Baronmon Deck 9",
		addresses=[0x26a75ca],
		number_of_bytes=2,
		possible_values=[183],
		is_little_endian=True, ),
	Attribute(
		name="Baronmon Deck 10",
		addresses=[0x26a75cc,0x26a75ce,0x26a75d0],
		number_of_bytes=2,
		possible_values=[New_Baronmon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Baronmon Deck 11",
		addresses=[0x26a75d2,0x26a75d4,0x26a75d6],
		number_of_bytes=2,
		possible_values=[New_Baronmon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Baronmon Deck 12",
		addresses=[0x26a75d8,0x26a75da],
		number_of_bytes=2,
		possible_values=[New_Baronmon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Baronmon Deck 13",
		addresses=[0x26a75dc],
		number_of_bytes=2,
		possible_values=[New_Baronmon_Deck[12]],
		is_little_endian=True, ),
#Pegasusmon
    Attribute(
        name="Pegasusmon Deck 1",
        addresses=[0x26a7610,0x26a7612],
        number_of_bytes=2,
        possible_values=[New_Pegasusmon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Pegasusmon Deck 2",
        addresses=[0x26a7614,0x26a7616],
        number_of_bytes=2,
        possible_values=[New_Pegasusmon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Pegasusmon Deck 3",
        addresses=[0x26a7618,0x26a761a,0x26a761c],
        number_of_bytes=2,
        possible_values=[New_Pegasusmon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Pegasusmon Deck 4",
		addresses=[0x26a761e,0x26a7620],
		number_of_bytes=2,
		possible_values=[New_Pegasusmon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Pegasusmon Deck 5",
		addresses=[0x26a7622,0x26a7624],
		number_of_bytes=2,
		possible_values=[New_Pegasusmon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Pegasusmon Deck 6",
        addresses=[0x26a7626,0x26a7628,0x26a762a,0x26a762c],
        number_of_bytes=2,
        possible_values=[New_Pegasusmon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Pegasusmon Deck 7",
		addresses=[0x26a762e],
		number_of_bytes=2,
		possible_values=[New_Pegasusmon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Pegasusmon Deck 8",
		addresses=[0x26a7630,0x26a7632,0x26a7634,0x26a7636],
		number_of_bytes=2,
		possible_values=[New_Pegasusmon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Pegasusmon Deck 9",
		addresses=[0x26a7638],
		number_of_bytes=2,
		possible_values=[183],
		is_little_endian=True, ),
	Attribute(
		name="Pegasusmon Deck 10",
		addresses=[0x26a763a,0x26a763c],
		number_of_bytes=2,
		possible_values=[New_Pegasusmon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Pegasusmon Deck 11",
		addresses=[0x26a763e,0x26a7640],
		number_of_bytes=2,
		possible_values=[New_Pegasusmon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Pegasusmon Deck 12",
		addresses=[0x26a7642],
		number_of_bytes=2,
		possible_values=[New_Pegasusmon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Pegasusmon Deck 13",
		addresses=[0x26a7644,0x26a7646],
		number_of_bytes=2,
		possible_values=[New_Pegasusmon_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Pegasusmon Deck 14",
		addresses=[0x26a7648],
		number_of_bytes=2,
		possible_values=[New_Pegasusmon_Deck[13]],
		is_little_endian=True, ),
	Attribute(
		name="Pegasusmon Deck 15",
		addresses=[0x26a764a],
		number_of_bytes=2,
		possible_values=[New_Pegasusmon_Deck[14]],
		is_little_endian=True, ),
#Gatomon2
    Attribute(
        name="Gatomon2 Deck 1",
        addresses=[0x26a767e,0x26a7680],
        number_of_bytes=2,
        possible_values=[New_Gatomon2_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Gatomon2 Deck 2",
        addresses=[0x26a7682,0x26a7684,0x26a7686],
        number_of_bytes=2,
        possible_values=[New_Gatomon2_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Gatomon2 Deck 3",
        addresses=[0x26a7688,0x26a768a],
        number_of_bytes=2,
        possible_values=[New_Gatomon2_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Gatomon2 Deck 4",
		addresses=[0x26a768c,0x26a768e,0x26a7690],
		number_of_bytes=2,
		possible_values=[New_Gatomon2_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Gatomon2 Deck 5",
		addresses=[0x26a7692,0x26a7694,0x26a7696],
		number_of_bytes=2,
		possible_values=[New_Gatomon2_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Gatomon2 Deck 6",
        addresses=[0x26a7698,0x26a769a,0x26a769c],
        number_of_bytes=2,
        possible_values=[New_Gatomon2_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Gatomon2 Deck 7",
		addresses=[0x26a769e],
		number_of_bytes=2,
		possible_values=[184],
		is_little_endian=True, ),
	Attribute(
		name="Gatomon2 Deck 8",
		addresses=[0x26a76a0,0x26a76a2],
		number_of_bytes=2,
		possible_values=[New_Gatomon2_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Gatomon2 Deck 9",
		addresses=[0x26a76a4,0x26a76a6],
		number_of_bytes=2,
		possible_values=[New_Gatomon2_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Gatomon2 Deck 10",
		addresses=[0x26a76a8,0x26a76aa],
		number_of_bytes=2,
		possible_values=[New_Gatomon2_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Gatomon2 Deck 11",
		addresses=[0x26a76ac,0x26a76ae],
		number_of_bytes=2,
		possible_values=[New_Gatomon2_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Gatomon2 Deck 12",
		addresses=[0x26a76b0,0x26a76b2],
		number_of_bytes=2,
		possible_values=[New_Gatomon2_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Gatomon2 Deck 13",
		addresses=[0x26a76b4],
		number_of_bytes=2,
		possible_values=[New_Gatomon2_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Gatomon2 Deck 14",
		addresses=[0x26a76b6,0x26a76b8],
		number_of_bytes=2,
		possible_values=[New_Gatomon2_Deck[13]],
		is_little_endian=True, ),
#Nefertimon
    Attribute(
        name="Nefertimon Deck 1",
        addresses=[0x26a76ec,0x26a76ee],
        number_of_bytes=2,
        possible_values=[New_Nefertimon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Nefertimon Deck 2",
        addresses=[0x26a76f0,0x26a76f2],
        number_of_bytes=2,
        possible_values=[New_Nefertimon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Nefertimon Deck 3",
        addresses=[0x26a76f4,0x26a76f6,0x26a76f8],
        number_of_bytes=2,
        possible_values=[New_Nefertimon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Nefertimon Deck 4",
		addresses=[0x26a76fa,0x26a76fc,0x26a76fe],
		number_of_bytes=2,
		possible_values=[New_Nefertimon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Nefertimon Deck 5",
		addresses=[0x26a7700,0x26a7702],
		number_of_bytes=2,
		possible_values=[New_Nefertimon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Nefertimon Deck 6",
        addresses=[0x26a7704,0x26a7706,0x26a7708,0x26a770a],
        number_of_bytes=2,
        possible_values=[New_Nefertimon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Nefertimon Deck 7",
		addresses=[0x26a770c,0x26a770e,0x26a7710],
		number_of_bytes=2,
		possible_values=[New_Nefertimon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Nefertimon Deck 8",
		addresses=[0x26a7712],
		number_of_bytes=2,
		possible_values=[184],
		is_little_endian=True, ),
	Attribute(
		name="Nefertimon Deck 9",
		addresses=[0x26a7714,0x26a7716, 0x26A7848],
		number_of_bytes=2,
		possible_values=[New_Nefertimon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Nefertimon Deck 10",
		addresses=[0x26A784a,0x26A784c],
		number_of_bytes=2,
		possible_values=[New_Nefertimon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Nefertimon Deck 11",
		addresses=[0x26A784e],
		number_of_bytes=2,
		possible_values=[New_Nefertimon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Nefertimon Deck 12",
		addresses=[0x26A7850,0x26A7852],
		number_of_bytes=2,
		possible_values=[New_Nefertimon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Nefertimon Deck 13",
		addresses=[0x26A7854],
		number_of_bytes=2,
		possible_values=[New_Nefertimon_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Nefertimon Deck 14",
		addresses=[0x26A7856],
		number_of_bytes=2,
		possible_values=[New_Nefertimon_Deck[13]],
		is_little_endian=True, ),
#Tylomon
    Attribute(
        name="Tylomon Deck 1",
        addresses=[0x26a788a,0x26a788c],
        number_of_bytes=2,
        possible_values=[New_Tylomon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Tylomon Deck 2",
        addresses=[0x26a788e,0x26a7890],
        number_of_bytes=2,
        possible_values=[New_Tylomon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Tylomon Deck 3",
        addresses=[0x26a7892,0x26a7894],
        number_of_bytes=2,
        possible_values=[New_Tylomon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Tylomon Deck 4",
		addresses=[0x26a7896],
		number_of_bytes=2,
		possible_values=[New_Tylomon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Tylomon Deck 5",
		addresses=[0x26a7898,0x26a789a],
		number_of_bytes=2,
		possible_values=[New_Tylomon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Tylomon Deck 6",
        addresses=[0x26a789c],
        number_of_bytes=2,
        possible_values=[New_Tylomon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Tylomon Deck 7",
		addresses=[0x26a789e,0x26a78a0,0x26a78a2],
		number_of_bytes=2,
		possible_values=[New_Tylomon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Tylomon Deck 8",
		addresses=[0x26a78a4,0x26a78a6],
		number_of_bytes=2,
		possible_values=[New_Tylomon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Tylomon Deck 9",
		addresses=[0x26a78a8,0x26a78aa,0x26a78ac],
		number_of_bytes=2,
		possible_values=[New_Tylomon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Tylomon Deck 10",
		addresses=[0x26a78ae],
		number_of_bytes=2,
		possible_values=[New_Tylomon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Tylomon Deck 11",
		addresses=[0x26a78b0],
		number_of_bytes=2,
		possible_values=[184],
		is_little_endian=True, ),
	Attribute(
		name="Tylomon Deck 12",
		addresses=[0x26a78b2,0x26a78b4],
		number_of_bytes=2,
		possible_values=[New_Tylomon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Tylomon Deck 13",
		addresses=[0x26a78b6,0x26a78b8],
		number_of_bytes=2,
		possible_values=[New_Tylomon_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Tylomon Deck 14",
		addresses=[0x26a78ba,0x26a78bc],
		number_of_bytes=2,
		possible_values=[New_Tylomon_Deck[13]],
		is_little_endian=True, ),
	Attribute(
		name="Tylomon Deck 15",
		addresses=[0x26a78be,0x26a78c0],
		number_of_bytes=2,
		possible_values=[New_Tylomon_Deck[14]],
		is_little_endian=True, ),
	Attribute(
		name="Tylomon Deck 16",
		addresses=[0x26a78c2],
		number_of_bytes=2,
		possible_values=[New_Tylomon_Deck[15]],
		is_little_endian=True, ),
	Attribute(
		name="Tylomon Deck 17",
		addresses=[0x26a78c4],
		number_of_bytes=2,
		possible_values=[New_Tylomon_Deck[16]],
		is_little_endian=True, ),
#Tentomon
    Attribute(
        name="Tentomon Deck 1",
        addresses=[0x26a78f8,0x26a78fa],
        number_of_bytes=2,
        possible_values=[New_Tentomon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Tentomon Deck 2",
        addresses=[0x26a78fc,0x26a78fe],
        number_of_bytes=2,
        possible_values=[New_Tentomon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Tentomon Deck 3",
        addresses=[0x26a7900,0x26a7902],
        number_of_bytes=2,
        possible_values=[New_Tentomon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Tentomon Deck 4",
		addresses=[0x26a7904,0x26a7906,0x26a7908,0x26a790a],
		number_of_bytes=2,
		possible_values=[New_Tentomon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Tentomon Deck 5",
		addresses=[0x26a790c,0x26a790e,0x26a7910,0x26a7912],
		number_of_bytes=2,
		possible_values=[New_Tentomon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Tentomon Deck 6",
        addresses=[0x26a7914,0x26a7916],
        number_of_bytes=2,
        possible_values=[New_Tentomon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Tentomon Deck 7",
		addresses=[0x26a7918,0x26a791a,0x26a791c,0x26a791e],
		number_of_bytes=2,
		possible_values=[New_Tentomon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Tentomon Deck 8",
		addresses=[0x26a7920,0x26a7922],
		number_of_bytes=2,
		possible_values=[New_Tentomon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Tentomon Deck 9",
		addresses=[0x26a7924,0x26a7926],
		number_of_bytes=2,
		possible_values=[New_Tentomon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Tentomon Deck 10",
		addresses=[0x26a7928,0x26a792a],
		number_of_bytes=2,
		possible_values=[New_Tentomon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Tentomon Deck 11",
		addresses=[0x26a792c,0x26a792e],
		number_of_bytes=2,
		possible_values=[New_Tentomon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Tentomon Deck 12",
		addresses=[0x26a7930,0x26a7932],
		number_of_bytes=2,
		possible_values=[New_Tentomon_Deck[11]],
		is_little_endian=True, ),
#Kuwagamon
    Attribute(
        name="Kuwagamon Deck 1",
        addresses=[0x26a7966],
        number_of_bytes=2,
        possible_values=[New_Kuwagamon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Kuwagamon Deck 2",
        addresses=[0x26a7968,0x26a796a,0x26a796c,0x26a796e],
        number_of_bytes=2,
        possible_values=[New_Kuwagamon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Kuwagamon Deck 3",
        addresses=[0x26a7970,0x26a7972],
        number_of_bytes=2,
        possible_values=[New_Kuwagamon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Kuwagamon Deck 4",
		addresses=[0x26a7974,0x26a7976,0x26a7978,0x26a797a],
		number_of_bytes=2,
		possible_values=[New_Kuwagamon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Kuwagamon Deck 5",
		addresses=[0x26a797c,0x26a797e,0x26a7980],
		number_of_bytes=2,
		possible_values=[New_Kuwagamon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Kuwagamon Deck 6",
        addresses=[0x26a7982,0x26a7984,0x26a7986],
        number_of_bytes=2,
        possible_values=[New_Kuwagamon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Kuwagamon Deck 7",
		addresses=[0x26a7988],
		number_of_bytes=2,
		possible_values=[New_Kuwagamon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Kuwagamon Deck 8",
		addresses=[0x26a798a],
		number_of_bytes=2,
		possible_values=[New_Kuwagamon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Kuwagamon Deck 9",
		addresses=[0x26a798c,0x26a798e],
		number_of_bytes=2,
		possible_values=[New_Kuwagamon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Kuwagamon Deck 10",
		addresses=[0x26a7990,0x26a7992],
		number_of_bytes=2,
		possible_values=[New_Kuwagamon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Kuwagamon Deck 11",
		addresses=[0x26a7994,0x26a7996],
		number_of_bytes=2,
		possible_values=[New_Kuwagamon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Kuwagamon Deck 12",
		addresses=[0x26a7998],
		number_of_bytes=2,
		possible_values=[New_Kuwagamon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Kuwagamon Deck 13",
		addresses=[0x26a799a,0x26a799c],
		number_of_bytes=2,
		possible_values=[New_Kuwagamon_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Kuwagamon Deck 14",
		addresses=[0x26a799e,0x26a79a0],
		number_of_bytes=2,
		possible_values=[New_Kuwagamon_Deck[13]],
		is_little_endian=True, ),
#HerculesKabuterimon
    Attribute(
        name="HerculesKabuterimon Deck 1",
        addresses=[0x26a79d4,0x26a79d6,0x26a79d8,0x26a79da],
        number_of_bytes=2,
        possible_values=[New_HerculesKabuterimon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="HerculesKabuterimon Deck 2",
        addresses=[0x26a79dc],
        number_of_bytes=2,
        possible_values=[New_HerculesKabuterimon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="HerculesKabuterimon Deck 3",
        addresses=[0x26a79de,0x26a79e0],
        number_of_bytes=2,
        possible_values=[New_HerculesKabuterimon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="HerculesKabuterimon Deck 4",
		addresses=[0x26a79e2,0x26a79e4],
		number_of_bytes=2,
		possible_values=[New_HerculesKabuterimon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="HerculesKabuterimon Deck 5",
		addresses=[0x26a79e6],
		number_of_bytes=2,
		possible_values=[New_HerculesKabuterimon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="HerculesKabuterimon Deck 6",
        addresses=[0x26a79e8,0x26a79ea,0x26a79ec],
        number_of_bytes=2,
        possible_values=[New_HerculesKabuterimon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="HerculesKabuterimon Deck 7",
		addresses=[0x26a79ee,0x26a79f0,0x26a79f2],
		number_of_bytes=2,
		possible_values=[New_HerculesKabuterimon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="HerculesKabuterimon Deck 8",
		addresses=[0x26a79f4,0x26a79f6,0x26a79f8],
		number_of_bytes=2,
		possible_values=[New_HerculesKabuterimon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="HerculesKabuterimon Deck 9",
		addresses=[0x26a79fa,0x26a79fc],
		number_of_bytes=2,
		possible_values=[New_HerculesKabuterimon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="HerculesKabuterimon Deck 10",
		addresses=[0x26a79fe,0x26a7a00],
		number_of_bytes=2,
		possible_values=[New_HerculesKabuterimon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="HerculesKabuterimon Deck 11",
		addresses=[0x26a7a02,0x26a7a04,0x26a7a06],
		number_of_bytes=2,
		possible_values=[New_HerculesKabuterimon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="HerculesKabuterimon Deck 12",
		addresses=[0x26a7a08,0x26a7a0a],
		number_of_bytes=2,
		possible_values=[New_HerculesKabuterimon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="HerculesKabuterimon Deck 13",
		addresses=[0x26a7a0c,0x26a7a0e],
		number_of_bytes=2,
		possible_values=[New_HerculesKabuterimon_Deck[12]],
		is_little_endian=True, ),
#Wargreymon
    Attribute(
        name="Wargreymon Deck 1",
        addresses=[0x26a7a42,0x26a7a44,0x26a7a46,0x26a7a48],
        number_of_bytes=2,
        possible_values=[New_Wargreymon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Wargreymon Deck 2",
        addresses=[0x26a7a4a],
        number_of_bytes=2,
        possible_values=[New_Wargreymon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Wargreymon Deck 3",
        addresses=[0x26a7a4c,0x26a7a4e,0x26a7a50,0x26a7a52],
        number_of_bytes=2,
        possible_values=[New_Wargreymon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Wargreymon Deck 4",
		addresses=[0x26a7a54,0x26a7a56],
		number_of_bytes=2,
		possible_values=[New_Wargreymon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Wargreymon Deck 5",
		addresses=[0x26a7a58],
		number_of_bytes=2,
		possible_values=[New_Wargreymon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Wargreymon Deck 6",
        addresses=[0x26a7a5a,0x26a7a5c,0x26a7a5e,0x26a7a60],
        number_of_bytes=2,
        possible_values=[New_Wargreymon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Wargreymon Deck 7",
		addresses=[0x26a7a62,0x26a7a64,0x26a7a66,0x26a7a68],
		number_of_bytes=2,
		possible_values=[New_Wargreymon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Wargreymon Deck 8",
		addresses=[0x26a7a6a,0x26a7a6c],
		number_of_bytes=2,
		possible_values=[New_Wargreymon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Wargreymon Deck 9",
		addresses=[0x26a7a6e,0x26a7a70],
		number_of_bytes=2,
		possible_values=[New_Wargreymon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Wargreymon Deck 10",
		addresses=[0x26a7a72,0x26a7a74],
		number_of_bytes=2,
		possible_values=[New_Wargreymon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Wargreymon Deck 11",
		addresses=[0x26a7a76,0x26a7a78],
		number_of_bytes=2,
		possible_values=[New_Wargreymon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Wargreymon Deck 12",
		addresses=[0x26a7a7a,0x26a7a7c],
		number_of_bytes=2,
		possible_values=[New_Wargreymon_Deck[11]],
		is_little_endian=True, ),
#Tai
    Attribute(
        name="Tai Deck 1",
        addresses=[0x26a7ab0],
        number_of_bytes=2,
        possible_values=[New_Tai_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Tai Deck 2",
        addresses=[0x26a7ab2,0x26a7ab4,0x26a7ab6],
        number_of_bytes=2,
        possible_values=[New_Tai_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Tai Deck 3",
        addresses=[0x26a7ab8,0x26a7aba,0x26a7abc],
        number_of_bytes=2,
        possible_values=[New_Tai_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Tai Deck 4",
		addresses=[0x26a7abe,0x26a7ac0,0x26a7ac2,0x26a7ac4],
		number_of_bytes=2,
		possible_values=[New_Tai_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Tai Deck 5",
		addresses=[0x26a7ac6,0x26a7ac8,0x26a7aca],
		number_of_bytes=2,
		possible_values=[New_Tai_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Tai Deck 6",
        addresses=[0x26a7acc,0x26a7ace],
        number_of_bytes=2,
        possible_values=[New_Tai_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Tai Deck 7",
		addresses=[0x26a7ad0,0x26a7ad2],
		number_of_bytes=2,
		possible_values=[New_Tai_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Tai Deck 8",
		addresses=[0x26a7ad4,0x26a7ad6,0x26a7ad8],
		number_of_bytes=2,
		possible_values=[New_Tai_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Tai Deck 9",
		addresses=[0x26a7ada,0x26a7adc,0x26a7ade],
		number_of_bytes=2,
		possible_values=[New_Tai_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Tai Deck 10",
		addresses=[0x26a7ae0,0x26a7ae2],
		number_of_bytes=2,
		possible_values=[New_Tai_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Tai Deck 11",
		addresses=[0x26a7ae4,0x26a7ae6,0x26a7ae8,0x26a7aea],
		number_of_bytes=2,
		possible_values=[New_Tai_Deck[10]],
		is_little_endian=True, ),
#Paildramon
    Attribute(
        name="Paildramon Deck 1",
        addresses=[0x26a7b1e,0x26a7b20,0x26a7b22,0x26a7b24],
        number_of_bytes=2,
        possible_values=[New_Paildramon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Paildramon Deck 2",
        addresses=[0x26a7b26,0x26a7b28,0x26a7b2a],
        number_of_bytes=2,
        possible_values=[New_Paildramon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Paildramon Deck 3",
        addresses=[0x26a7b2c,0x26a7b2e],
        number_of_bytes=2,
        possible_values=[New_Paildramon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Paildramon Deck 4",
		addresses=[0x26a7b30,0x26a7b32,0x26a7b34,0x26a7b36],
		number_of_bytes=2,
		possible_values=[New_Paildramon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Paildramon Deck 5",
		addresses=[0x26a7b38,0x26a7b3a,0x26a7b3c],
		number_of_bytes=2,
		possible_values=[New_Paildramon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Paildramon Deck 6",
        addresses=[0x26a7b3e,0x26a7b40,0x26a7b42],
        number_of_bytes=2,
        possible_values=[New_Paildramon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Paildramon Deck 7",
		addresses=[0x26a7b44,0x26a7b46,0x26a7b48],
		number_of_bytes=2,
		possible_values=[New_Paildramon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Paildramon Deck 8",
		addresses=[0x26a7b4a,0x26a7b4c,0x26a7b4e],
		number_of_bytes=2,
		possible_values=[New_Paildramon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Paildramon Deck 9",
		addresses=[0x26a7b50,0x26a7b52,0x26a7b54],
		number_of_bytes=2,
		possible_values=[New_Paildramon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Paildramon Deck 10",
		addresses=[0x26a7b56,0x26a7b58],
		number_of_bytes=2,
		possible_values=[New_Paildramon_Deck[9]],
		is_little_endian=True, ),
#Rosemon2
    Attribute(
        name="Rosemon2 Deck 1",
        addresses=[0x26a8d64,0x26a8d66,0x26a8d68],
        number_of_bytes=2,
        possible_values=[New_Rosemon2_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Rosemon2 Deck 2",
        addresses=[0x26a8d6a,0x26a8d6c],
        number_of_bytes=2,
        possible_values=[New_Rosemon2_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Rosemon2 Deck 3",
        addresses=[0x26a8d6e,0x26a8d70],
        number_of_bytes=2,
        possible_values=[New_Rosemon2_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Rosemon2 Deck 4",
		addresses=[0x26a8d72,0x26a8d74],
		number_of_bytes=2,
		possible_values=[New_Rosemon2_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Rosemon2 Deck 5",
		addresses=[0x26a8d76],
		number_of_bytes=2,
		possible_values=[New_Rosemon2_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Rosemon2 Deck 6",
        addresses=[0x26a8d78,0x26a8d7a,0x26a8d7c,0x26a8d7e],
        number_of_bytes=2,
        possible_values=[New_Rosemon2_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Rosemon2 Deck 7",
		addresses=[0x26a8d80,0x26a8d82,0x26a8d84],
		number_of_bytes=2,
		possible_values=[New_Rosemon2_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Rosemon2 Deck 8",
		addresses=[0x26a8d86,0x26a8d88,0x26a8d8a],
		number_of_bytes=2,
		possible_values=[New_Rosemon2_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Rosemon2 Deck 9",
		addresses=[0x26a8d8c,0x26a8d8e],
		number_of_bytes=2,
		possible_values=[New_Rosemon2_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Rosemon2 Deck 10",
		addresses=[0x26a8d90],
		number_of_bytes=2,
		possible_values=[New_Rosemon2_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Rosemon2 Deck 11",
		addresses=[0x26a8d92,0x26a8d94],
		number_of_bytes=2,
		possible_values=[New_Rosemon2_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Rosemon2 Deck 12",
		addresses=[0x26a8d96],
		number_of_bytes=2,
		possible_values=[New_Rosemon2_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Rosemon2 Deck 13",
		addresses=[0x26a8d98,0x26a8d9a],
		number_of_bytes=2,
		possible_values=[New_Rosemon2_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Rosemon2 Deck 14",
		addresses=[0x26a8d9c,0x26a8d9e],
		number_of_bytes=2,
		possible_values=[New_Rosemon2_Deck[13]],
		is_little_endian=True, ),
#Garudamon
    Attribute(
        name="Garudamon Deck 1",
        addresses=[0x26a7b8c,0x26a7b8e,0x26a7b90,0x26a7b92],
        number_of_bytes=2,
        possible_values=[New_Garudamon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Garudamon Deck 2",
        addresses=[0x26a7b94,0x26a7b96,0x26a7b98],
        number_of_bytes=2,
        possible_values=[New_Garudamon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Garudamon Deck 3",
        addresses=[0x26a7b9a,0x26a7b9c,0x26a7b9e,0x26a7ba0],
        number_of_bytes=2,
        possible_values=[New_Garudamon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Garudamon Deck 4",
		addresses=[0x26a7ba2,0x26a7ba4,0x26a7ba6],
		number_of_bytes=2,
		possible_values=[New_Garudamon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Garudamon Deck 5",
		addresses=[0x26a7ba8,0x26a7baa,0x26a7bac,0x26a7bae],
		number_of_bytes=2,
		possible_values=[New_Garudamon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Garudamon Deck 6",
        addresses=[0x26a7bb0,0x26a7bb2,0x26a7bb4,0x26a7bb6],
        number_of_bytes=2,
        possible_values=[New_Garudamon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Garudamon Deck 7",
		addresses=[0x26a7bb8,0x26a7bba,0x26a7bbc,0x26a7bbe],
		number_of_bytes=2,
		possible_values=[New_Garudamon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Garudamon Deck 8",
		addresses=[0x26a7bc0,0x26a7bc2,0x26a7bc4,0x26a7bc6],
		number_of_bytes=2,
		possible_values=[New_Garudamon_Deck[7]],
		is_little_endian=True, ),
#Sora
    Attribute(
        name="Sora Deck 1",
        addresses=[0x26a7bfa,0x26a7bfc,0x26a7bfe,0x26a7c00],
        number_of_bytes=2,
        possible_values=[New_Sora_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Sora Deck 2",
        addresses=[0x26a7c02,0x26a7c04,0x26a7c06,0x26a7c08],
        number_of_bytes=2,
        possible_values=[New_Sora_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Sora Deck 3",
        addresses=[0x26a7c0a,0x26a7c0c],
        number_of_bytes=2,
        possible_values=[New_Sora_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Sora Deck 4",
		addresses=[0x26a7c0e,0x26a7c10,0x26a7c12],
		number_of_bytes=2,
		possible_values=[New_Sora_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Sora Deck 5",
		addresses=[0x26a7c14,0x26a7c16,0x26a7c18,0x26a7c1a],
		number_of_bytes=2,
		possible_values=[New_Sora_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Sora Deck 6",
        addresses=[0x26a7c1c,0x26a7c1e,0x26a7c20],
        number_of_bytes=2,
        possible_values=[New_Sora_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Sora Deck 7",
		addresses=[0x26a7c22,0x26a7c24],
		number_of_bytes=2,
		possible_values=[New_Sora_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Sora Deck 8",
		addresses=[0x26a7c26,0x26a7c28],
		number_of_bytes=2,
		possible_values=[New_Sora_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Sora Deck 9",
		addresses=[0x26a7c2a,0x26a7c2c],
		number_of_bytes=2,
		possible_values=[New_Sora_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Sora Deck 10",
		addresses=[0x26a7c2e,0x26a7c30,0x26a7c32],
		number_of_bytes=2,
		possible_values=[New_Sora_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Sora Deck 11",
		addresses=[0x26a7c34],
		number_of_bytes=2,
		possible_values=[New_Sora_Deck[10]],
		is_little_endian=True, ),
#Shurimon
    Attribute(
        name="Shurimon Deck 1",
        addresses=[0x26a7c68,0x26a7c6a],
        number_of_bytes=2,
        possible_values=[New_Shurimon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Shurimon Deck 2",
        addresses=[0x26a7c6c,0x26a7c6e,0x26a7c70],
        number_of_bytes=2,
        possible_values=[New_Shurimon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Shurimon Deck 3",
        addresses=[0x26a7c72,0x26a7c74,0x26a7c76],
        number_of_bytes=2,
        possible_values=[New_Shurimon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Shurimon Deck 4",
		addresses=[0x26a7c78,0x26a7c7a],
		number_of_bytes=2,
		possible_values=[New_Shurimon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Shurimon Deck 5",
		addresses=[0x26a7c7c,0x26a7c7e],
		number_of_bytes=2,
		possible_values=[New_Shurimon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Shurimon Deck 6",
        addresses=[0x26a7c80,0x26a7c82],
        number_of_bytes=2,
        possible_values=[New_Shurimon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Shurimon Deck 7",
		addresses=[0x26a7c84,0x26a7c86,0x26a7c88],
		number_of_bytes=2,
		possible_values=[New_Shurimon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Shurimon Deck 8",
		addresses=[0x26a7c8a],
		number_of_bytes=2,
		possible_values=[New_Shurimon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Shurimon Deck 9",
		addresses=[0x26a7c8c,0x26a7c8e,0x26a7c90],
		number_of_bytes=2,
		possible_values=[New_Shurimon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Shurimon Deck 10",
		addresses=[0x26a7c92,0x26a7c94],
		number_of_bytes=2,
		possible_values=[New_Shurimon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Shurimon Deck 11",
		addresses=[0x26a7c96,0x26a7c98,0x26a7c9a],
		number_of_bytes=2,
		possible_values=[New_Shurimon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Shurimon Deck 12",
		addresses=[0x26a7c9c,0x26a7c9e],
		number_of_bytes=2,
		possible_values=[New_Shurimon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Shurimon Deck 13",
		addresses=[0x26a7ca0,0x26a7ca2],
		number_of_bytes=2,
		possible_values=[New_Shurimon_Deck[12]],
		is_little_endian=True, ),
#Lillymon
    Attribute(
        name="Lillymon Deck 1",
        addresses=[0x26a7cd6],
        number_of_bytes=2,
        possible_values=[New_Lillymon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Lillymon Deck 2",
        addresses=[0x26a7cd8,0x26a7cda,0x26a7cdc,0x26a7cde],
        number_of_bytes=2,
        possible_values=[New_Lillymon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Lillymon Deck 3",
        addresses=[0x26a7ce0,0x26a7ce2],
        number_of_bytes=2,
        possible_values=[New_Lillymon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Lillymon Deck 4",
		addresses=[0x26a7ce4],
		number_of_bytes=2,
		possible_values=[New_Lillymon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Lillymon Deck 5",
		addresses=[0x26a7ce6,0x26a7ce8,0x26a7cea,0x26a7cec],
		number_of_bytes=2,
		possible_values=[New_Lillymon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Lillymon Deck 6",
        addresses=[0x26a7cee,0x26a7cf0],
        number_of_bytes=2,
        possible_values=[New_Lillymon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Lillymon Deck 7",
		addresses=[0x26a7cf2,0x26a7cf4,0x26a7cf6],
		number_of_bytes=2,
		possible_values=[New_Lillymon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Lillymon Deck 8",
		addresses=[0x26a7cf8,0x26a7cfa,0x26a7cfc],
		number_of_bytes=2,
		possible_values=[New_Lillymon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Lillymon Deck 9",
		addresses=[0x26a7cfe,0x26a7d00,0x26a7d02,0x26a7d04],
		number_of_bytes=2,
		possible_values=[New_Lillymon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Lillymon Deck 10",
		addresses=[0x26a7d06,0x26a7d08],
		number_of_bytes=2,
		possible_values=[New_Lillymon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Lillymon Deck 11",
		addresses=[0x26a7d0a,0x26a7d0c],
		number_of_bytes=2,
		possible_values=[New_Lillymon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Lillymon Deck 12",
		addresses=[0x26a7d0e,0x26a7d10],
		number_of_bytes=2,
		possible_values=[New_Lillymon_Deck[11]],
		is_little_endian=True, ),
#Mimi
    Attribute(
        name="Mimi Deck 1",
        addresses=[0x26a7d44,0x26a7d46,0x26a7d48,0x26a7d4a],
        number_of_bytes=2,
        possible_values=[New_Mimi_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Mimi Deck 2",
        addresses=[0x26a7d4c,0x26a7d4e],
        number_of_bytes=2,
        possible_values=[New_Mimi_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Mimi Deck 3",
        addresses=[0x26a7d50,0x26a7d52,0x26a7d54],
        number_of_bytes=2,
        possible_values=[New_Mimi_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Mimi Deck 4",
		addresses=[0x26a7d56],
		number_of_bytes=2,
		possible_values=[New_Mimi_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Mimi Deck 5",
		addresses=[0x26a7d58],
		number_of_bytes=2,
		possible_values=[New_Mimi_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Mimi Deck 6",
        addresses=[0x26a7d5a],
        number_of_bytes=2,
        possible_values=[New_Mimi_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Mimi Deck 7",
		addresses=[0x26a7d5c,0x26a7d5e,0x26a7d60],
		number_of_bytes=2,
		possible_values=[New_Mimi_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Mimi Deck 8",
		addresses=[0x26a7d62,0x26a7d64,0x26a7d66,0x26a7d68],
		number_of_bytes=2,
		possible_values=[New_Mimi_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Mimi Deck 9",
		addresses=[0x26a7d6a,0x26a7d6c],
		number_of_bytes=2,
		possible_values=[New_Mimi_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Mimi Deck 10",
		addresses=[0x26a7d6e,0x26a7d70,0x26a7d72],
		number_of_bytes=2,
		possible_values=[New_Mimi_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Mimi Deck 11",
		addresses=[0x26a7d74,0x26a7d76,0x26a7d78],
		number_of_bytes=2,
		possible_values=[New_Mimi_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Mimi Deck 12",
		addresses=[0x26a7d7a,0x26a7d7c],
		number_of_bytes=2,
		possible_values=[New_Mimi_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Mimi Deck 13",
		addresses=[0x26a7d7e],
		number_of_bytes=2,
		possible_values=[New_Mimi_Deck[12]],
		is_little_endian=True, ),
#Submarimon
    Attribute(
        name="Submarimon Deck 1",
        addresses=[0x26a7db2],
        number_of_bytes=2,
        possible_values=[New_Submarimon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Submarimon Deck 2",
        addresses=[0x26a7db4],
        number_of_bytes=2,
        possible_values=[New_Submarimon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Submarimon Deck 3",
        addresses=[0x26a7db6,0x26a7db8],
        number_of_bytes=2,
        possible_values=[New_Submarimon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Submarimon Deck 4",
		addresses=[0x26a7dba,0x26a7dbc],
		number_of_bytes=2,
		possible_values=[New_Submarimon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Submarimon Deck 5",
		addresses=[0x26a7dbe,0x26a7dc0,0x26a7dc2],
		number_of_bytes=2,
		possible_values=[New_Submarimon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Submarimon Deck 6",
        addresses=[0x26a7dc4,0x26a7dc6,0x26a7dc8],
        number_of_bytes=2,
        possible_values=[New_Submarimon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Submarimon Deck 7",
		addresses=[0x26a7dca,0x26a7dcc,0x26a7dce],
		number_of_bytes=2,
		possible_values=[New_Submarimon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Submarimon Deck 8",
		addresses=[0x26a7dd0,0x26a7dd2,0x26a7dd4],
		number_of_bytes=2,
		possible_values=[New_Submarimon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Submarimon Deck 9",
		addresses=[0x26a7dd6],
		number_of_bytes=2,
		possible_values=[190],
		is_little_endian=True, ),
	Attribute(
		name="Submarimon Deck 10",
		addresses=[0x26a7dd8,0x26a7dda,0x26a7ddc],
		number_of_bytes=2,
		possible_values=[New_Submarimon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Submarimon Deck 11",
		addresses=[0x26a7dde,0x26a7de0,0x26a7de2],
		number_of_bytes=2,
		possible_values=[New_Submarimon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Submarimon Deck 12",
		addresses=[0x26a7de4],
		number_of_bytes=2,
		possible_values=[New_Submarimon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Submarimon Deck 13",
		addresses=[0x26a7de6],
		number_of_bytes=2,
		possible_values=[New_Submarimon_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Submarimon Deck 14",
		addresses=[0x26a7de8,0x26a7dea],
		number_of_bytes=2,
		possible_values=[New_Submarimon_Deck[13]],
		is_little_endian=True, ),
#Metalgarurumon
    Attribute(
        name="Metalgarurumon Deck 1",
        addresses=[0x26a7e20,0x26a7e22,0x26a7e24,0x26a7e26],
        number_of_bytes=2,
        possible_values=[New_Metalgarurumon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Metalgarurumon Deck 2",
        addresses=[0x26a7e28],
        number_of_bytes=2,
        possible_values=[New_Metalgarurumon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Metalgarurumon Deck 3",
        addresses=[0x26a7e2a,0x26a7e2c,0x26a7e2e,0x26a7e30],
        number_of_bytes=2,
        possible_values=[New_Metalgarurumon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Metalgarurumon Deck 4",
		addresses=[0x26a7e32,0x26a7e34],
		number_of_bytes=2,
		possible_values=[New_Metalgarurumon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Metalgarurumon Deck 5",
		addresses=[0x26a7e36],
		number_of_bytes=2,
		possible_values=[New_Metalgarurumon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Metalgarurumon Deck 6",
        addresses=[0x26a7e38,0x26a7e3a,0x26a7e3c,0x26a7e3e],
        number_of_bytes=2,
        possible_values=[New_Metalgarurumon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Metalgarurumon Deck 7",
		addresses=[0x26a7e40,0x26a7e42,0x26a7e44],
		number_of_bytes=2,
		possible_values=[New_Metalgarurumon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Metalgarurumon Deck 8",
		addresses=[0x26a7e46,0x26a7e48,0x26a7e4a],
		number_of_bytes=2,
		possible_values=[New_Metalgarurumon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Metalgarurumon Deck 9",
		addresses=[0x26a7e4c],
		number_of_bytes=2,
		possible_values=[New_Metalgarurumon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Metalgarurumon Deck 10",
		addresses=[0x26a7e4e,0x26a7e50],
		number_of_bytes=2,
		possible_values=[New_Metalgarurumon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Metalgarurumon Deck 11",
		addresses=[0x26a7e52,0x26a7e54],
		number_of_bytes=2,
		possible_values=[New_Metalgarurumon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Metalgarurumon Deck 12",
		addresses=[0x26a7e56],
		number_of_bytes=2,
		possible_values=[New_Metalgarurumon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Metalgarurumon Deck 13",
		addresses=[0x26a7e58,0x26a7e5a],
		number_of_bytes=2,
		possible_values=[New_Metalgarurumon_Deck[12]],
		is_little_endian=True, ),
#Matt
    Attribute(
        name="Matt Deck 1",
        addresses=[0x26a7e8e,0x26a7e90,0x26a7e92],
        number_of_bytes=2,
        possible_values=[New_Matt_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Matt Deck 2",
        addresses=[0x26a7e94],
        number_of_bytes=2,
        possible_values=[New_Matt_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Matt Deck 3",
        addresses=[0x26a7e96,0x26a7e98,0x26a7e9a,0x26a7e9c],
        number_of_bytes=2,
        possible_values=[New_Matt_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Matt Deck 4",
		addresses=[0x26a7e9e,0x26a7ea0,0x26a7ea2],
		number_of_bytes=2,
		possible_values=[New_Matt_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Matt Deck 5",
		addresses=[0x26a7ea4,0x26a7ea6,0x26a7ea8,0x26a7eaa],
		number_of_bytes=2,
		possible_values=[New_Matt_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Matt Deck 6",
        addresses=[0x26a7eac,0x26a7eae],
        number_of_bytes=2,
        possible_values=[New_Matt_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Matt Deck 7",
		addresses=[0x26a7eb0,0x26a7eb2,0x26a7eb4],
		number_of_bytes=2,
		possible_values=[New_Matt_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Matt Deck 8",
		addresses=[0x26a7eb6],
		number_of_bytes=2,
		possible_values=[New_Matt_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Matt Deck 9",
		addresses=[0x26a7eb8,0x26a7eba],
		number_of_bytes=2,
		possible_values=[New_Matt_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Matt Deck 10",
		addresses=[0x26a7ebc,0x26a7ebe],
		number_of_bytes=2,
		possible_values=[New_Matt_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Matt Deck 11",
		addresses=[0x26a7ec0,0x26a7ec2],
		number_of_bytes=2,
		possible_values=[New_Matt_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Matt Deck 12",
		addresses=[0x26a7ec4,0x26a7ec6],
		number_of_bytes=2,
		possible_values=[New_Matt_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Matt Deck 13",
		addresses=[0x26a7ec8],
		number_of_bytes=2,
		possible_values=[New_Matt_Deck[12]],
		is_little_endian=True, ),
#Zudomon
    Attribute(
        name="Zudomon Deck 1",
        addresses=[0x26a7efc,0x26a7efe,0x26a7f00,0x26a7f02],
        number_of_bytes=2,
        possible_values=[New_Zudomon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Zudomon Deck 2",
        addresses=[0x26a7f04,0x26a7f06,0x26a7f08,0x26a7f0a],
        number_of_bytes=2,
        possible_values=[New_Zudomon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Zudomon Deck 3",
        addresses=[0x26a7f10],
        number_of_bytes=2,
        possible_values=[New_Zudomon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Zudomon Deck 4",
		addresses=[0x26a7f12],
		number_of_bytes=2,
		possible_values=[New_Zudomon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Zudomon Deck 5",
		addresses=[0x26a7f14,0x26a7f16,0x26a7f18,0x26a7f1a],
		number_of_bytes=2,
		possible_values=[New_Zudomon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Zudomon Deck 6",
        addresses=[0x26a7f1c,0x26a7f1e,0x26a7f20,0x26a7f22],
        number_of_bytes=2,
        possible_values=[New_Zudomon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Zudomon Deck 7",
		addresses=[0x26a7f24,0x26a7f26],
		number_of_bytes=2,
		possible_values=[New_Zudomon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Zudomon Deck 8",
		addresses=[0x26a7f28],
		number_of_bytes=2,
		possible_values=[New_Zudomon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Zudomon Deck 9",
		addresses=[0x26a7f2a],
		number_of_bytes=2,
		possible_values=[New_Zudomon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Zudomon Deck 10",
		addresses=[0x26a7f2c],
		number_of_bytes=2,
		possible_values=[New_Zudomon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Zudomon Deck 11",
		addresses=[0x26a7f2e,0x26a7f30],
		number_of_bytes=2,
		possible_values=[New_Zudomon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Zudomon Deck 12",
		addresses=[0x26a7f32,0x26a7f34],
		number_of_bytes=2,
		possible_values=[New_Zudomon_Deck[11]],
		is_little_endian=True, ),
#Joe
    Attribute(
        name="Joe Deck 1",
        addresses=[0x26a7f6a,0x26a7f6c,0x26a7f6e],
        number_of_bytes=2,
        possible_values=[New_Joe_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Joe Deck 2",
        addresses=[0x26a7f70],
        number_of_bytes=2,
        possible_values=[New_Joe_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Joe Deck 3",
        addresses=[0x26a7f72,0x26a7f74],
        number_of_bytes=2,
        possible_values=[New_Joe_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Joe Deck 4",
		addresses=[0x26a7f76,0x26a7f78,0x26a7f7a],
		number_of_bytes=2,
		possible_values=[New_Joe_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Joe Deck 5",
		addresses=[0x26a7f7c,0x26a7f7e,0x26a7f80],
		number_of_bytes=2,
		possible_values=[New_Joe_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Joe Deck 6",
        addresses=[0x26a7f82,0x26a7f84],
        number_of_bytes=2,
        possible_values=[New_Joe_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Joe Deck 7",
		addresses=[0x26a7f86,0x26a7f88],
		number_of_bytes=2,
		possible_values=[New_Joe_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Joe Deck 8",
		addresses=[0x26a7f8a,0x26a7f8c,0x26a7f8e,0x26a7f90],
		number_of_bytes=2,
		possible_values=[New_Joe_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Joe Deck 9",
		addresses=[0x26a7f92,0x26a7f94,0x26a7f96,0x26a7f98],
		number_of_bytes=2,
		possible_values=[New_Joe_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Joe Deck 10",
		addresses=[0x26a7f9a,0x26a7f9c,0x26a7f9e],
		number_of_bytes=2,
		possible_values=[New_Joe_Deck[9]],
		is_little_endian=True, ),
#MegaKabuterimon
    Attribute(
        name="MegaKabuterimon Deck 1",
        addresses=[0x26a7fd8,0x26a7fda,0x26a7fdc,0x26a7fde],
        number_of_bytes=2,
        possible_values=[New_MegaKabuterimon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="MegaKabuterimon Deck 2",
        addresses=[0x26a7fe0,0x26a7fe2,0x26a7fe4],
        number_of_bytes=2,
        possible_values=[New_MegaKabuterimon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="MegaKabuterimon Deck 3",
        addresses=[0x26a7fe6,0x26a7fe8,0x26a7fea],
        number_of_bytes=2,
        possible_values=[New_MegaKabuterimon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="MegaKabuterimon Deck 4",
		addresses=[0x26a7fec,0x26a7fee,0x26a7ff0],
		number_of_bytes=2,
		possible_values=[New_MegaKabuterimon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="MegaKabuterimon Deck 5",
		addresses=[0x26a7ff2,0x26a7ff4,0x26a7ff6],
		number_of_bytes=2,
		possible_values=[New_MegaKabuterimon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="MegaKabuterimon Deck 6",
        addresses=[0x26a7ff8,0x26a7ffa,0x26a7ffc,0x26a7ffe],
        number_of_bytes=2,
        possible_values=[New_MegaKabuterimon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="MegaKabuterimon Deck 7",
		addresses=[0x26a8000,0x26a8002,0x26a8004],
		number_of_bytes=2,
		possible_values=[New_MegaKabuterimon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="MegaKabuterimon Deck 8",
		addresses=[0x26a8006,0x26a8008,0x26a800a],
		number_of_bytes=2,
		possible_values=[New_MegaKabuterimon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="MegaKabuterimon Deck 9",
		addresses=[0x26a800c,0x26a800e,0x26a8010,0x26a8012],
		number_of_bytes=2,
		possible_values=[New_MegaKabuterimon_Deck[8]],
		is_little_endian=True, ),
#Izzy
    Attribute(
        name="Izzy Deck 1",
        addresses=[0x26a8178,0x26a817a],
        number_of_bytes=2,
        possible_values=[New_Izzy_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Izzy Deck 2",
        addresses=[0x26a817c,0x26a817e,0x26a8180,0x26a8182],
        number_of_bytes=2,
        possible_values=[New_Izzy_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Izzy Deck 3",
        addresses=[0x26a8184,0x26a8186,0x26a8188],
        number_of_bytes=2,
        possible_values=[New_Izzy_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Izzy Deck 4",
		addresses=[0x26a818a,0x26a818c,0x26a818e,0x26a8190],
		number_of_bytes=2,
		possible_values=[New_Izzy_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Izzy Deck 5",
		addresses=[0x26a8192,0x26a8194,0x26a8196],
		number_of_bytes=2,
		possible_values=[New_Izzy_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Izzy Deck 6",
        addresses=[0x26a8198,0x26a819a,0x26a819c],
        number_of_bytes=2,
        possible_values=[New_Izzy_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Izzy Deck 7",
		addresses=[0x26a819e,0x26a81a0],
		number_of_bytes=2,
		possible_values=[New_Izzy_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Izzy Deck 8",
		addresses=[0x26a81a2,0x26a81a4],
		number_of_bytes=2,
		possible_values=[New_Izzy_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Izzy Deck 9",
		addresses=[0x26a81a6,0x26a81a8],
		number_of_bytes=2,
		possible_values=[New_Izzy_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Izzy Deck 10",
		addresses=[0x26a81aa,0x26a81ac],
		number_of_bytes=2,
		possible_values=[New_Izzy_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Izzy Deck 11",
		addresses=[0x26a81ae],
		number_of_bytes=2,
		possible_values=[New_Izzy_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Izzy Deck 12",
		addresses=[0x26a81b0],
		number_of_bytes=2,
		possible_values=[New_Izzy_Deck[11]],
		is_little_endian=True, ),
#MagnaAngemon
    Attribute(
        name="MagnaAngemon Deck 1",
        addresses=[0x26a81e4],
        number_of_bytes=2,
        possible_values=[New_MagnaAngemon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="MagnaAngemon Deck 2",
        addresses=[0x26a81e6,0x26a81e8,0x26a81ea],
        number_of_bytes=2,
        possible_values=[New_MagnaAngemon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="MagnaAngemon Deck 3",
        addresses=[0x26a81ec,0x26a81ee,0x26a81f0,0x26a81f2],
        number_of_bytes=2,
        possible_values=[New_MagnaAngemon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="MagnaAngemon Deck 4",
		addresses=[0x26a81f4,0x26a81f6],
		number_of_bytes=2,
		possible_values=[New_MagnaAngemon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="MagnaAngemon Deck 5",
		addresses=[0x26a81f8],
		number_of_bytes=2,
		possible_values=[New_MagnaAngemon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="MagnaAngemon Deck 6",
        addresses=[0x26a81fa,0x26a81fc],
        number_of_bytes=2,
        possible_values=[New_MagnaAngemon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="MagnaAngemon Deck 7",
		addresses=[0x26a81fe,0x26a8200,0x26a8202],
		number_of_bytes=2,
		possible_values=[New_MagnaAngemon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="MagnaAngemon Deck 8",
		addresses=[0x26a8204,0x26a8206,0x26a8208,0x26a820a],
		number_of_bytes=2,
		possible_values=[New_MagnaAngemon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="MagnaAngemon Deck 9",
		addresses=[0x26a820c],
		number_of_bytes=2,
		possible_values=[New_MagnaAngemon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="MagnaAngemon Deck 10",
		addresses=[0x26a820e,0x26a8210,0x26a8212],
		number_of_bytes=2,
		possible_values=[New_MagnaAngemon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="MagnaAngemon Deck 11",
		addresses=[0x26a8214,0x26a8216,0x26a8218],
		number_of_bytes=2,
		possible_values=[New_MagnaAngemon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="MagnaAngemon Deck 12",
		addresses=[0x26a821a,0x26a821c,0x26a821e],
		number_of_bytes=2,
		possible_values=[New_MagnaAngemon_Deck[11]],
		is_little_endian=True, ),
#Angewomon
    Attribute(
        name="Angewomon Deck 1",
        addresses=[0x26a8252,0x26a8254,0x26a8256,0x26a8258],
        number_of_bytes=2,
        possible_values=[New_Angewomon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Angewomon Deck 2",
        addresses=[0x26a825a,0x26a825c,0x26a825e,0x26a8260],
        number_of_bytes=2,
        possible_values=[New_Angewomon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Angewomon Deck 3",
        addresses=[0x26a8262,0x26a8264],
        number_of_bytes=2,
        possible_values=[New_Angewomon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Angewomon Deck 4",
		addresses=[0x26a8266,0x26a8268],
		number_of_bytes=2,
		possible_values=[New_Angewomon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Angewomon Deck 5",
		addresses=[0x26a826a,0x26a826c,0x26a826e,0x26a8270],
		number_of_bytes=2,
		possible_values=[New_Angewomon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Angewomon Deck 6",
        addresses=[0x26a8272,0x26a8274,0x26a8276],
        number_of_bytes=2,
        possible_values=[New_Angewomon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Angewomon Deck 7",
		addresses=[0x26a8278],
		number_of_bytes=2,
		possible_values=[New_Angewomon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Angewomon Deck 8",
		addresses=[0x26a827a],
		number_of_bytes=2,
		possible_values=[New_Angewomon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Angewomon Deck 9",
		addresses=[0x26a827c],
		number_of_bytes=2,
		possible_values=[New_Angewomon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Angewomon Deck 10",
		addresses=[0x26a827e,0x26a8280],
		number_of_bytes=2,
		possible_values=[New_Angewomon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Angewomon Deck 11",
		addresses=[0x26a8282],
		number_of_bytes=2,
		possible_values=[New_Angewomon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Angewomon Deck 12",
		addresses=[0x26a8284],
		number_of_bytes=2,
		possible_values=[New_Angewomon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Angewomon Deck 13",
		addresses=[0x26a8286],
		number_of_bytes=2,
		possible_values=[New_Angewomon_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Angewomon Deck 14",
		addresses=[0x26a8288],
		number_of_bytes=2,
		possible_values=[New_Angewomon_Deck[13]],
		is_little_endian=True, ),
	Attribute(
		name="Angewomon Deck 15",
		addresses=[0x26a828a],
		number_of_bytes=2,
		possible_values=[New_Angewomon_Deck[14]],
		is_little_endian=True, ),
	Attribute(
		name="Angewomon Deck 16",
		addresses=[0x26a828c],
		number_of_bytes=2,
		possible_values=[New_Angewomon_Deck[15]],
		is_little_endian=True, ),
#GranKuwagamon
    Attribute(
        name="GranKuwagamon Deck 1",
        addresses=[0x26a82c0,0x26a82c2,0x26a82c4,0x26a82c6],
        number_of_bytes=2,
        possible_values=[New_GranKuwagamon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="GranKuwagamon Deck 2",
        addresses=[0x26a82c8,0x26a82ca,0x26a82cc],
        number_of_bytes=2,
        possible_values=[New_GranKuwagamon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="GranKuwagamon Deck 3",
        addresses=[0x26a82d2],
        number_of_bytes=2,
        possible_values=[New_GranKuwagamon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="GranKuwagamon Deck 4",
		addresses=[0x26a82d4,0x26a82d6],
		number_of_bytes=2,
		possible_values=[New_GranKuwagamon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="GranKuwagamon Deck 5",
		addresses=[0x26a82d8,0x26a82da],
		number_of_bytes=2,
		possible_values=[New_GranKuwagamon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="GranKuwagamon Deck 6",
        addresses=[0x26a82dc,0x26a82de],
        number_of_bytes=2,
        possible_values=[New_GranKuwagamon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="GranKuwagamon Deck 7",
		addresses=[0x26a82e0,0x26a82e2,0x26a82e4,0x26a82e6],
		number_of_bytes=2,
		possible_values=[New_GranKuwagamon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="GranKuwagamon Deck 8",
		addresses=[0x26a82e8],
		number_of_bytes=2,
		possible_values=[New_GranKuwagamon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="GranKuwagamon Deck 9",
		addresses=[0x26a82ea,0x26a82ec],
		number_of_bytes=2,
		possible_values=[New_GranKuwagamon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="GranKuwagamon Deck 10",
		addresses=[0x26a82ee,0x26a82f0],
		number_of_bytes=2,
		possible_values=[New_GranKuwagamon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="GranKuwagamon Deck 11",
		addresses=[0x26a82f2],
		number_of_bytes=2,
		possible_values=[New_GranKuwagamon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="GranKuwagamon Deck 12",
		addresses=[0x26a82f4,0x26a82f6],
		number_of_bytes=2,
		possible_values=[New_GranKuwagamon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="GranKuwagamon Deck 13",
		addresses=[0x26a82f8,0x26a82fa],
		number_of_bytes=2,
		possible_values=[New_GranKuwagamon_Deck[12]],
		is_little_endian=True, ),
#GranKuwagamon
    Attribute(
        name="GranKuwagamon Deck 1",
        addresses=[0x26a832e,0x26a8330,0x26a8332],
        number_of_bytes=2,
        possible_values=[New_GranKuwagamon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="GranKuwagamon Deck 2",
        addresses=[0x26a8334,0x26a8336,0x26a8338],
        number_of_bytes=2,
        possible_values=[New_GranKuwagamon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="GranKuwagamon Deck 3",
        addresses=[0x26a833a,0x26a833c],
        number_of_bytes=2,
        possible_values=[New_GranKuwagamon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="GranKuwagamon Deck 4",
		addresses=[0x26a833e],
		number_of_bytes=2,
		possible_values=[New_GranKuwagamon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="GranKuwagamon Deck 5",
		addresses=[0x26a8340,0x26a8342],
		number_of_bytes=2,
		possible_values=[New_GranKuwagamon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="GranKuwagamon Deck 6",
        addresses=[0x26a8344],
        number_of_bytes=2,
        possible_values=[New_GranKuwagamon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="GranKuwagamon Deck 7",
		addresses=[0x26a8346,0x26a8348],
		number_of_bytes=2,
		possible_values=[New_GranKuwagamon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="GranKuwagamon Deck 8",
		addresses=[0x26a834a,0x26a834c,0x26a834e,0x26a8350],
		number_of_bytes=2,
		possible_values=[New_GranKuwagamon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="GranKuwagamon Deck 9",
		addresses=[0x26a8352],
		number_of_bytes=2,
		possible_values=[187],
		is_little_endian=True, ),
	Attribute(
		name="GranKuwagamon Deck 10",
		addresses=[0x26a8354,0x26a8356],
		number_of_bytes=2,
		possible_values=[New_GranKuwagamon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="GranKuwagamon Deck 11",
		addresses=[0x26a8358,0x26a835a,0x26a835c,0x26a835e],
		number_of_bytes=2,
		possible_values=[New_GranKuwagamon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="GranKuwagamon Deck 12",
		addresses=[0x26a8360,0x26a8362],
		number_of_bytes=2,
		possible_values=[New_GranKuwagamon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="GranKuwagamon Deck 13",
		addresses=[0x26a8364],
		number_of_bytes=2,
		possible_values=[New_GranKuwagamon_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="GranKuwagamon Deck 14",
		addresses=[0x26a8366,0x26a8368],
		number_of_bytes=2,
		possible_values=[New_GranKuwagamon_Deck[13]],
		is_little_endian=True, ),
#Ken
    Attribute(
        name="Ken Deck 1",
        addresses=[0x26a832e,0x26a8330,0x26a8332],
        number_of_bytes=2,
        possible_values=[New_Ken_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Ken Deck 2",
        addresses=[0x26a8334,0x26a8336,0x26a8338],
        number_of_bytes=2,
        possible_values=[New_Ken_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Ken Deck 3",
        addresses=[0x26a833a,0x26a833c],
        number_of_bytes=2,
        possible_values=[New_Ken_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Ken Deck 4",
		addresses=[0x26a833e],
		number_of_bytes=2,
		possible_values=[New_Ken_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Ken Deck 5",
		addresses=[0x26a8340,0x26a8342],
		number_of_bytes=2,
		possible_values=[New_Ken_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Ken Deck 6",
        addresses=[0x26a8344],
        number_of_bytes=2,
        possible_values=[New_Ken_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Ken Deck 7",
		addresses=[0x26a8346,0x26a8348],
		number_of_bytes=2,
		possible_values=[New_Ken_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Ken Deck 8",
		addresses=[0x26a834a,0x26a834c,0x26a834e,0x26a8350],
		number_of_bytes=2,
		possible_values=[New_Ken_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Ken Deck 9",
		addresses=[0x26a8352],
		number_of_bytes=2,
		possible_values=[187],
		is_little_endian=True, ),
	Attribute(
		name="Ken Deck 10",
		addresses=[0x26a8354,0x26a8356],
		number_of_bytes=2,
		possible_values=[New_Ken_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Ken Deck 11",
		addresses=[0x26a8358,0x26a835a,0x26a835c,0x26a835e],
		number_of_bytes=2,
		possible_values=[New_Ken_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Ken Deck 12",
		addresses=[0x26a8360,0x26a8362],
		number_of_bytes=2,
		possible_values=[New_Ken_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Ken Deck 13",
		addresses=[0x26a8364],
		number_of_bytes=2,
		possible_values=[New_Ken_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Ken Deck 14",
		addresses=[0x26a8366,0x26a8368],
		number_of_bytes=2,
		possible_values=[New_Ken_Deck[13]],
		is_little_endian=True, ),
#MetalSeadramon
    Attribute(
        name="MetalSeadramon Deck 1",
        addresses=[0x26a839c,0x26a839e,0x26a83a0],
        number_of_bytes=2,
        possible_values=[New_MetalSeadramon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="MetalSeadramon Deck 2",
        addresses=[0x26a83a2],
        number_of_bytes=2,
        possible_values=[New_MetalSeadramon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="MetalSeadramon Deck 3",
        addresses=[0x26a83a4],
        number_of_bytes=2,
        possible_values=[New_MetalSeadramon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="MetalSeadramon Deck 4",
		addresses=[0x26a83a6,0x26a83a8,0x26a83aa],
		number_of_bytes=2,
		possible_values=[New_MetalSeadramon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="MetalSeadramon Deck 5",
		addresses=[0x26a83ac,0x26a83ae],
		number_of_bytes=2,
		possible_values=[New_MetalSeadramon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="MetalSeadramon Deck 6",
        addresses=[0x26a83b0,0x26a83b2],
        number_of_bytes=2,
        possible_values=[New_MetalSeadramon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="MetalSeadramon Deck 7",
		addresses=[0x26a83b4,0x26a83b6,0x26a83b8],
		number_of_bytes=2,
		possible_values=[New_MetalSeadramon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="MetalSeadramon Deck 8",
		addresses=[0x26a83ba,0x26a83bc,0x26a83be,0x26a83c0],
		number_of_bytes=2,
		possible_values=[New_MetalSeadramon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="MetalSeadramon Deck 9",
		addresses=[0x26a83c2,0x26a83c4,0x26a83c6],
		number_of_bytes=2,
		possible_values=[New_MetalSeadramon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="MetalSeadramon Deck 10",
		addresses=[0x26a83c8,0x26a83ca,0x26a83cc],
		number_of_bytes=2,
		possible_values=[New_MetalSeadramon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="MetalSeadramon Deck 11",
		addresses=[0x26a83ce,0x26a83d0],
		number_of_bytes=2,
		possible_values=[New_MetalSeadramon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="MetalSeadramon Deck 12",
		addresses=[0x26a83d2,0x26a83d4,0x26a83d6],
		number_of_bytes=2,
		possible_values=[New_MetalSeadramon_Deck[11]],
		is_little_endian=True, ),
#Puppetmon
    Attribute(
        name="Puppetmon Deck 1",
        addresses=[0x26a840a,0x26a840c,0x26a840e,0x26a8410],
        number_of_bytes=2,
        possible_values=[New_Puppetmon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Puppetmon Deck 2",
        addresses=[0x26a8412],
        number_of_bytes=2,
        possible_values=[New_Puppetmon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Puppetmon Deck 3",
        addresses=[0x26a8414,0x26a8416,0x26a8418,0x26a841a],
        number_of_bytes=2,
        possible_values=[New_Puppetmon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Puppetmon Deck 4",
		addresses=[0x26a841c,0x26a841e,0x26a8420],
		number_of_bytes=2,
		possible_values=[New_Puppetmon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Puppetmon Deck 5",
		addresses=[0x26a8422,0x26a8424],
		number_of_bytes=2,
		possible_values=[New_Puppetmon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Puppetmon Deck 6",
        addresses=[0x26a8426,0x26a8428],
        number_of_bytes=2,
        possible_values=[New_Puppetmon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Puppetmon Deck 7",
		addresses=[0x26a842a,0x26a842c,0x26a842e,0x26a8430],
		number_of_bytes=2,
		possible_values=[New_Puppetmon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Puppetmon Deck 8",
		addresses=[0x26a8432,0x26a8434,0x26a8436],
		number_of_bytes=2,
		possible_values=[New_Puppetmon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Puppetmon Deck 9",
		addresses=[0x26a8438,0x26a843a],
		number_of_bytes=2,
		possible_values=[New_Puppetmon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Puppetmon Deck 10",
		addresses=[0x26a843c,0x26a843e],
		number_of_bytes=2,
		possible_values=[New_Puppetmon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Puppetmon Deck 11",
		addresses=[0x26a8440],
		number_of_bytes=2,
		possible_values=[New_Puppetmon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Puppetmon Deck 12",
		addresses=[0x26a8442,0x26a8444],
		number_of_bytes=2,
		possible_values=[New_Puppetmon_Deck[11]],
		is_little_endian=True, ),
#Machinedramon
    Attribute(
        name="Machinedramon Deck 1",
        addresses=[0x26a8478,0x26a847a,0x26a847c,0x26a847e],
        number_of_bytes=2,
        possible_values=[New_Machinedramon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Machinedramon Deck 2",
        addresses=[0x26a8480],
        number_of_bytes=2,
        possible_values=[New_Machinedramon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Machinedramon Deck 3",
        addresses=[0x26a8482,0x26a8484,0x26a8486,0x26a8488],
        number_of_bytes=2,
        possible_values=[New_Machinedramon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Machinedramon Deck 4",
		addresses=[0x26a848a,0x26a848c,0x26a848e],
		number_of_bytes=2,
		possible_values=[New_Machinedramon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Machinedramon Deck 5",
		addresses=[0x26a8490,0x26a8492,0x26a8494,0x26a8496],
		number_of_bytes=2,
		possible_values=[New_Machinedramon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Machinedramon Deck 6",
        addresses=[0x26a8498,0x26a849a,0x26a849c],
        number_of_bytes=2,
        possible_values=[New_Machinedramon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Machinedramon Deck 7",
		addresses=[0x26a849e,0x26a84a0,0x26a84a2],
		number_of_bytes=2,
		possible_values=[New_Machinedramon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Machinedramon Deck 8",
		addresses=[0x26a84a4,0x26a84a6],
		number_of_bytes=2,
		possible_values=[New_Machinedramon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Machinedramon Deck 9",
		addresses=[0x26a84a8],
		number_of_bytes=2,
		possible_values=[New_Machinedramon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Machinedramon Deck 10",
		addresses=[0x26a84aa,0x26a84ac],
		number_of_bytes=2,
		possible_values=[New_Machinedramon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Machinedramon Deck 11",
		addresses=[0x26a84ac,0x26a84ae,0x26a84b0],
		number_of_bytes=2,
		possible_values=[New_Machinedramon_Deck[10]],
		is_little_endian=True, ),
#LadyDevimon
    Attribute(
        name="LadyDevimon Deck 1",
        addresses=[0x26a84e6,0x26a84e8,0x26a84ea],
        number_of_bytes=2,
        possible_values=[New_LadyDevimon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="LadyDevimon Deck 2",
        addresses=[0x26a84ec,0x26a84ee,0x26a84f0],
        number_of_bytes=2,
        possible_values=[New_LadyDevimon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="LadyDevimon Deck 3",
        addresses=[0x26a84f2,0x26a84f4,0x26a84f6],
        number_of_bytes=2,
        possible_values=[New_LadyDevimon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="LadyDevimon Deck 4",
		addresses=[0x26a84f8,0x26a84fa,0x26a84fc,0x26a84fe],
		number_of_bytes=2,
		possible_values=[New_LadyDevimon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="LadyDevimon Deck 5",
		addresses=[0x26a8500,0x26a8502,0x26a8504],
		number_of_bytes=2,
		possible_values=[New_LadyDevimon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="LadyDevimon Deck 6",
        addresses=[0x26a8506,0x26a8508,0x26a850a,0x26a850c],
        number_of_bytes=2,
        possible_values=[New_LadyDevimon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="LadyDevimon Deck 7",
		addresses=[0x26a850e,0x26a8510],
		number_of_bytes=2,
		possible_values=[New_LadyDevimon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="LadyDevimon Deck 8",
		addresses=[0x26a8512,0x26a8514],
		number_of_bytes=2,
		possible_values=[New_LadyDevimon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="LadyDevimon Deck 9",
		addresses=[0x26a8516,0x26a8518],
		number_of_bytes=2,
		possible_values=[New_LadyDevimon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="LadyDevimon Deck 10",
		addresses=[0x26a851a,0x26a851c],
		number_of_bytes=2,
		possible_values=[New_LadyDevimon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="LadyDevimon Deck 11",
		addresses=[0x26a851e,0x26a8520],
		number_of_bytes=2,
		possible_values=[New_LadyDevimon_Deck[10]],
		is_little_endian=True, ),
#Piedmon
    Attribute(
        name="Piedmon Deck 1",
        addresses=[0x26a8554],
        number_of_bytes=2,
        possible_values=[New_Piedmon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Piedmon Deck 2",
        addresses=[0x26a8556],
        number_of_bytes=2,
        possible_values=[New_Piedmon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Piedmon Deck 3",
        addresses=[0x26a8558],
        number_of_bytes=2,
        possible_values=[New_Piedmon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Piedmon Deck 4",
		addresses=[0x26a855a],
		number_of_bytes=2,
		possible_values=[New_Piedmon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Piedmon Deck 5",
		addresses=[0x26a855c,0x26a855e],
		number_of_bytes=2,
		possible_values=[New_Piedmon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Piedmon Deck 6",
        addresses=[0x26a8560,0x26a8562],
        number_of_bytes=2,
        possible_values=[New_Piedmon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Piedmon Deck 7",
		addresses=[0x26a8564,0x26a8566],
		number_of_bytes=2,
		possible_values=[New_Piedmon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Piedmon Deck 8",
		addresses=[0x26a8568,0x26a856a],
		number_of_bytes=2,
		possible_values=[New_Piedmon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Piedmon Deck 9",
		addresses=[0x26a856c,0x26a856e,0x26a8570],
		number_of_bytes=2,
		possible_values=[New_Piedmon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Piedmon Deck 10",
		addresses=[0x26a8572,0x26a8574,0x26a8576,0x26a8578],
		number_of_bytes=2,
		possible_values=[New_Piedmon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Piedmon Deck 11",
		addresses=[0x26a857a,0x26a857c,0x26a857e],
		number_of_bytes=2,
		possible_values=[New_Piedmon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Piedmon Deck 12",
		addresses=[0x26a8580,0x26a8582],
		number_of_bytes=2,
		possible_values=[New_Piedmon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Piedmon Deck 13",
		addresses=[0x26a8584],
		number_of_bytes=2,
		possible_values=[New_Piedmon_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Piedmon Deck 14",
		addresses=[0x26a8586],
		number_of_bytes=2,
		possible_values=[New_Piedmon_Deck[13]],
		is_little_endian=True, ),
	Attribute(
		name="Piedmon Deck 15",
		addresses=[0x26a8588],
		number_of_bytes=2,
		possible_values=[New_Piedmon_Deck[14]],
		is_little_endian=True, ),
	Attribute(
		name="Piedmon Deck 16",
		addresses=[0x26a858a,0x26a858c,0x26a858e],
		number_of_bytes=2,
		possible_values=[New_Piedmon_Deck[15]],
		is_little_endian=True, ),
#Magnamon
    Attribute(
        name="Magnamon Deck 1",
        addresses=[0x26a85c2,0x26a85c4,0x26a85c6],
        number_of_bytes=2,
        possible_values=[New_Magnamon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Magnamon Deck 2",
        addresses=[0x26a85c8,0x26a85ca,0x26a85cc],
        number_of_bytes=2,
        possible_values=[New_Magnamon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Magnamon Deck 3",
        addresses=[0x26a85ce],
        number_of_bytes=2,
        possible_values=[New_Magnamon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Magnamon Deck 4",
		addresses=[0x26a85d0,0x26a85d2,0x26a85d4],
		number_of_bytes=2,
		possible_values=[New_Magnamon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Magnamon Deck 5",
		addresses=[0x26a85d6,0x26a85d8,0x26a85da,0x26a85dc],
		number_of_bytes=2,
		possible_values=[New_Magnamon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Magnamon Deck 6",
        addresses=[0x26a85de,0x26a85e0,0x26a85e2],
        number_of_bytes=2,
        possible_values=[New_Magnamon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Magnamon Deck 7",
		addresses=[0x26a85e4,0x26a85e6,0x26a85e8],
		number_of_bytes=2,
		possible_values=[New_Magnamon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Magnamon Deck 8",
		addresses=[0x26a85ea],
		number_of_bytes=2,
		possible_values=[175],
		is_little_endian=True, ),
	Attribute(
		name="Magnamon Deck 9",
		addresses=[0x26a85ec,0x26a85ee],
		number_of_bytes=2,
		possible_values=[New_Magnamon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Magnamon Deck 10",
		addresses=[0x26a85f0],
		number_of_bytes=2,
		possible_values=[New_Magnamon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Magnamon Deck 11",
		addresses=[0x26a85f2,0x26a85f4],
		number_of_bytes=2,
		possible_values=[New_Magnamon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Magnamon Deck 12",
		addresses=[0x26a85f6],
		number_of_bytes=2,
		possible_values=[New_Magnamon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Magnamon Deck 13",
		addresses=[0x26a85f8],
		number_of_bytes=2,
		possible_values=[New_Magnamon_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Magnamon Deck 14",
		addresses=[0x26a85fa],
		number_of_bytes=2,
		possible_values=[New_Magnamon_Deck[13]],
		is_little_endian=True, ),
	Attribute(
		name="Magnamon Deck 15",
		addresses=[0x26a85fc],
		number_of_bytes=2,
		possible_values=[New_Magnamon_Deck[14]],
		is_little_endian=True, ),

#Sylphymon
    Attribute(
        name="Sylphymon Deck 1",
        addresses=[0x26a8630,0x26a8632,0x26a8634,0x26a8636],
        number_of_bytes=2,
        possible_values=[New_Sylphymon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Sylphymon Deck 2",
        addresses=[0x26a8638,0x26a863a],
        number_of_bytes=2,
        possible_values=[New_Sylphymon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Sylphymon Deck 3",
        addresses=[0x26a863c,0x26a863e,0x26a8640],
        number_of_bytes=2,
        possible_values=[New_Sylphymon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Sylphymon Deck 4",
		addresses=[0x26a8642,0x26a8644],
		number_of_bytes=2,
		possible_values=[New_Sylphymon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Sylphymon Deck 5",
		addresses=[0x26a8646,0x26a8648,0x26a864a,0x26a864c],
		number_of_bytes=2,
		possible_values=[New_Sylphymon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Sylphymon Deck 6",
        addresses=[0x26a864e,0x26a8650,0x26a8652],
        number_of_bytes=2,
        possible_values=[New_Sylphymon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Sylphymon Deck 7",
		addresses=[0x26a8654,0x26a8656],
		number_of_bytes=2,
		possible_values=[New_Sylphymon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Sylphymon Deck 8",
		addresses=[0x26a8658],
		number_of_bytes=2,
		possible_values=[182],
		is_little_endian=True, ),
	Attribute(
		name="Sylphymon Deck 9",
		addresses=[0x26a865a,0x26a865c],
		number_of_bytes=2,
		possible_values=[New_Sylphymon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Sylphymon Deck 10",
		addresses=[0x26a865e,0x26a8660],
		number_of_bytes=2,
		possible_values=[New_Sylphymon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Sylphymon Deck 11",
		addresses=[0x26a8662],
		number_of_bytes=2,
		possible_values=[New_Sylphymon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Sylphymon Deck 12",
		addresses=[0x26a8664,0x26a8666],
		number_of_bytes=2,
		possible_values=[New_Sylphymon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Sylphymon Deck 13",
		addresses=[0x26a8668],
		number_of_bytes=2,
		possible_values=[New_Sylphymon_Deck[12]],
		is_little_endian=True, ),
	Attribute(
		name="Sylphymon Deck 14",
		addresses=[0x26a866a],
		number_of_bytes=2,
		possible_values=[New_Sylphymon_Deck[13]],
		is_little_endian=True, ),
#Shakkoumon
    Attribute(
        name="Shakkoumon Deck 1",
        addresses=[0x26a869e,0x26a86a0,0x26a86a2],
        number_of_bytes=2,
        possible_values=[New_Shakkoumon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Shakkoumon Deck 2",
        addresses=[0x26a86a4],
        number_of_bytes=2,
        possible_values=[New_Shakkoumon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Shakkoumon Deck 3",
        addresses=[0x26a86a6,0x26a86a8,0x26a86aa],
        number_of_bytes=2,
        possible_values=[New_Shakkoumon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Shakkoumon Deck 4",
		addresses=[0x26a86ac,0x26a86ae],
		number_of_bytes=2,
		possible_values=[New_Shakkoumon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Shakkoumon Deck 5",
		addresses=[0x26a86b0,0x26a86b2],
		number_of_bytes=2,
		possible_values=[New_Shakkoumon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Shakkoumon Deck 6",
        addresses=[0x26a86b4,0x26a86b6,0x26a86b8,0x26a86ba],
        number_of_bytes=2,
        possible_values=[New_Shakkoumon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Shakkoumon Deck 7",
		addresses=[0x26a86bc,0x26a86be,0x26a86c0],
		number_of_bytes=2,
		possible_values=[New_Shakkoumon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Shakkoumon Deck 8",
		addresses=[0x26a86c2,0x26a86c4,0x26a86c6],
		number_of_bytes=2,
		possible_values=[New_Shakkoumon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Shakkoumon Deck 9",
		addresses=[0x26a86c8,0x26a86ca],
		number_of_bytes=2,
		possible_values=[New_Shakkoumon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Shakkoumon Deck 10",
		addresses=[0x26a86cc,0x26a86ce],
		number_of_bytes=2,
		possible_values=[New_Shakkoumon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Shakkoumon Deck 11",
		addresses=[0x26a86d0,0x26a86d2],
		number_of_bytes=2,
		possible_values=[New_Shakkoumon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Shakkoumon Deck 12",
		addresses=[0x26a86d4,0x26a86d6],
		number_of_bytes=2,
		possible_values=[New_Shakkoumon_Deck[11]],
		is_little_endian=True, ),
	Attribute(
		name="Shakkoumon Deck 13",
		addresses=[0x26a86d8],
		number_of_bytes=2,
		possible_values=[New_Shakkoumon_Deck[12]],
		is_little_endian=True, ),
#Seraphimon
    Attribute(
        name="Seraphimon Deck 1",
        addresses=[0x26a870c,0x26a870e,0x26a8710],
        number_of_bytes=2,
        possible_values=[New_Seraphimon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Seraphimon Deck 2",
        addresses=[0x26a8712],
        number_of_bytes=2,
        possible_values=[New_Seraphimon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Seraphimon Deck 3",
        addresses=[0x26a8714,0x26a8716,0x26a8718,0x26a871a],
        number_of_bytes=2,
        possible_values=[New_Seraphimon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Seraphimon Deck 4",
		addresses=[0x26a871c,0x26a871e],
		number_of_bytes=2,
		possible_values=[New_Seraphimon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Seraphimon Deck 5",
		addresses=[0x26a8720],
		number_of_bytes=2,
		possible_values=[New_Seraphimon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Seraphimon Deck 6",
        addresses=[0x26a8722,0x26a8724],
        number_of_bytes=2,
        possible_values=[New_Seraphimon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Seraphimon Deck 7",
		addresses=[0x26a8726,0x26a8728,0x26a872a],
		number_of_bytes=2,
		possible_values=[New_Seraphimon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Seraphimon Deck 8",
		addresses=[0x26a872c,0x26a872e,0x26a8730,0x26a8732],
		number_of_bytes=2,
		possible_values=[New_Seraphimon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Seraphimon Deck 9",
		addresses=[0x26a8734],
		number_of_bytes=2,
		possible_values=[183],
		is_little_endian=True, ),
	Attribute(
		name="Seraphimon Deck 10",
		addresses=[0x26a8736,0x26a8738,0x26a873a],
		number_of_bytes=2,
		possible_values=[New_Seraphimon_Deck[9]],
		is_little_endian=True, ),
	Attribute(
		name="Seraphimon Deck 11",
		addresses=[0x26a873c,0x26a873e,0x26a8740],
		number_of_bytes=2,
		possible_values=[New_Seraphimon_Deck[10]],
		is_little_endian=True, ),
	Attribute(
		name="Seraphimon Deck 12",
		addresses=[0x26a8742,0x26a8744,0x26a8746],
		number_of_bytes=2,
		possible_values=[New_Seraphimon_Deck[11]],
		is_little_endian=True, ),
#Magnadramon
    Attribute(
        name="Magnadramon Deck 1",
        addresses=[0x26a877a,0x26a877c,0x26a877e,0x26a8780],
        number_of_bytes=2,
        possible_values=[New_Magnadramon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Magnadramon Deck 2",
        addresses=[0x26a8782,0x26a8784,0x26a8786,0x26a8788],
        number_of_bytes=2,
        possible_values=[New_Magnadramon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Magnadramon Deck 3",
        addresses=[0x26a878a,0x26a878c],
        number_of_bytes=2,
        possible_values=[New_Magnadramon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Magnadramon Deck 4",
		addresses=[0x26a878e,0x26a8790],
		number_of_bytes=2,
		possible_values=[New_Magnadramon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Magnadramon Deck 5",
		addresses=[0x26a8792,0x26a8794,0x26a8796,0x26a8798],
		number_of_bytes=2,
		possible_values=[New_Magnadramon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Magnadramon Deck 6",
        addresses=[0x26a87a0],
        number_of_bytes=2,
        possible_values=[184],
        is_little_endian=True, ),
	Attribute(
		name="Magnadramon Deck 7",
		addresses=[0x26a87a2,0x26a87a4,0x26a87a6],
		number_of_bytes=2,
		possible_values=[New_Magnadramon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Magnadramon Deck 8",
		addresses=[0x26a87a8,0x26a87aa,0x26a87ac],
		number_of_bytes=2,
		possible_values=[New_Magnadramon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Magnadramon Deck 9",
		addresses=[0x26a87ae,0x26a87b0],
		number_of_bytes=2,
		possible_values=[New_Magnadramon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Magnadramon Deck 10",
		addresses=[0x26a87b2,0x26a87b4],
		number_of_bytes=2,
		possible_values=[New_Magnadramon_Deck[9]],
		is_little_endian=True, ),
#Infermon
    Attribute(
        name="Infermon Deck 1",
        addresses=[0x26a87e8,0x26a87ea,0x26a87ec,0x26a87ee],
        number_of_bytes=2,
        possible_values=[New_Infermon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Infermon Deck 2",
        addresses=[0x26a87f0,0x26a87f2],
        number_of_bytes=2,
        possible_values=[New_Infermon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Infermon Deck 3",
        addresses=[0x26a87f4,0x26a87f6,0x26a87f8,0x26a87fa],
        number_of_bytes=2,
        possible_values=[New_Infermon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Infermon Deck 4",
		addresses=[0x26a87fc,0x26a87fe,0x26a8800,0x26a8802],
		number_of_bytes=2,
		possible_values=[New_Infermon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Infermon Deck 5",
		addresses=[0x26a8804,0x26a8806,0x26a8808,0x26a880a],
		number_of_bytes=2,
		possible_values=[New_Infermon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Infermon Deck 6",
        addresses=[0x26a880c,0x26a880e,0x26a8810,0x26a8812],
        number_of_bytes=2,
        possible_values=[New_Infermon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Infermon Deck 7",
		addresses=[0x26a8814,0x26a8816,0x26a8818,0x26a881a],
		number_of_bytes=2,
		possible_values=[New_Infermon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Infermon Deck 8",
		addresses=[0x26a881c,0x26a881e,0x26a8820,0x26a8822],
		number_of_bytes=2,
		possible_values=[New_Infermon_Deck[7]],
		is_little_endian=True, ),
#Diaboromon
    Attribute(
        name="Diaboromon Deck 1",
        addresses=[0x26a8856,0x26a8858,0x26a885a,0x26a885c],
        number_of_bytes=2,
        possible_values=[New_Diaboromon_Deck[0]],
        is_little_endian=True, ),
    Attribute(
        name="Diaboromon Deck 2",
        addresses=[0x26a885e,0x26a8860,0x26a8862],
        number_of_bytes=2,
        possible_values=[New_Diaboromon_Deck[1]],
        is_little_endian=True, ),
    Attribute(
        name="Diaboromon Deck 3",
        addresses=[0x26a8864,0x26a8866,0x26a8868],
        number_of_bytes=2,
        possible_values=[New_Diaboromon_Deck[2]],
        is_little_endian=True, ),
	Attribute(
		name="Diaboromon Deck 4",
		addresses=[0x26a886a,0x26a886c],
		number_of_bytes=2,
		possible_values=[New_Diaboromon_Deck[3]],
		is_little_endian=True, ),
	Attribute(
		name="Diaboromon Deck 5",
		addresses=[0x26a886e,0x26a8870,0x26a8872,0x26a8874],
		number_of_bytes=2,
		possible_values=[New_Diaboromon_Deck[4]],
		is_little_endian=True, ),
    Attribute(
        name="Diaboromon Deck 6",
        addresses=[0x26a8876,0x26a8878,0x26a887a,0x26a887c],
        number_of_bytes=2,
        possible_values=[New_Diaboromon_Deck[5]],
        is_little_endian=True, ),
	Attribute(
		name="Diaboromon Deck 7",
		addresses=[0x26a887e,0x26a8880],
		number_of_bytes=2,
		possible_values=[New_Diaboromon_Deck[6]],
		is_little_endian=True, ),
	Attribute(
		name="Diaboromon Deck 8",
		addresses=[0x26a8882,0x26a8884],
		number_of_bytes=2,
		possible_values=[New_Diaboromon_Deck[7]],
		is_little_endian=True, ),
	Attribute(
		name="Diaboromon Deck 9",
		addresses=[0x26a8886,0x26a8888,0x26a888a],
		number_of_bytes=2,
		possible_values=[New_Diaboromon_Deck[8]],
		is_little_endian=True, ),
	Attribute(
		name="Diaboromon Deck 10",
		addresses=[0x26a888c,0x26a888e,0x26a8890],
		number_of_bytes=2,
		possible_values=[New_Diaboromon_Deck[9]],
		is_little_endian=True, ),
]
Required_Rules = [

]

Optional_Rulesets = [

]