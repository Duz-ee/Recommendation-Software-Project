from Windsor_Bars_Data import sorted_live_music_lst
from Windsor_Bars_Data import sorted_noLive_music_lst


print("\t\t\tWelcome to Windsor Bars!\n\n")
print("This is a bar recommendation software for bars in Windsor Ontario\n")
print("Windsor can boast of a bouyant night life\n")
print("We would love for you to have a good time in the city, by sharing in this experience\n")
print("This program gives you restauarant suggestions based on the number of days you would like to spend in the city, and the atmosphere you prefer.\n")
user_input_1 = input("How many days will you be in Windsor? Your answer should be from 1 to 10 ")
while user_input_1 not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
    user_input_1 = input("How many days will you be in Windsor? Your answer should be from 1 to 10 ")
user_input_2 = input("Okay, what kind of atmosphere are you looking for in the bar? Answer 1) for live music or 2) for no live music ")
while user_input_2 not in ["1", "2"]:
    user_input_2 = input("Okay, what kind of atmosphere are you looking for in the bar? Answer 1) for live music or 2) for no live music ")

    


if user_input_2 == "1":
    bars_for_you = "\n".join(sorted_live_music_lst[-int(user_input_1):])
    print("You should check out the following bars:\n", bars_for_you)
elif user_input_2 == "2":
    bars_for_you = "\n".join(sorted_noLive_music_lst[-int(user_input_1):])
    print("You should check out the following bars:\n", bars_for_you)