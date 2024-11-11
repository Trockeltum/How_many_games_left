import math
def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def get_valid_input(prompt, valid_options):
    response = input(prompt).strip().lower()
    while response not in valid_options:
        print(f"Invalid input. Please enter one of the following: {', '.join(valid_options)}")
        response = input(prompt).strip().lower()
    return response

levels_chart = {
    1: 144, 2: 144, 3: 192, 4: 240, 5: 336, 6: 432, 7: 528, 8: 624, 9: 720, 10: 816,
    11: 912, 12: 984, 13: 1056, 14: 1128, 15: 1344, 16: 1440, 17: 1536, 18: 1680, 19: 1824,
    20: 1968, 21: 2112, 22: 2208, 23: 2304, 24: 2304, 25: 2496, 26: 2496, 27: 2592, 28: 2688,
    29: 2688, 30: 2688, 31: 2688, 32: 2688, 33: 2784, 34: 2784, 35: 2784, 36: 2880, 37: 2880,
    38: 2880, 39: 3072, 40: 3072, 41: 3168, 42: 3168, 43: 3264, 44: 3264, 45: 3360, 46: 3360,
    47: 3456, 48: 3456, 49: 3456
}

levels_chart_25 = {
    0: 2592, 1: 2688, 2: 2688, 3: 2688, 4: 2688, 5: 2880, 6: 2880, 7: 2880, 8: 3072, 9: 3072,
    10: 3072, 11: 3264, 12: 3264, 13: 3264, 14: 3360, 15: 3360, 16: 3360, 17: 3456, 18: 3456, 19: 3456,
    20: 3456, 21: 3552, 22: 3552, 23: 3648, 24: 3648
}

lvl_goal = get_integer_input("Enter the level you want to reach (as a number): ")
level = get_integer_input("Enter your current level (as a number): ")
xp = get_integer_input("Enter your current XP (as a number): ")
summoner = get_valid_input("Which mode are you playing (type 'aram' or 'summoner')? ", {"aram", "summoner"})
xp_boost = get_integer_input("How much XP boost do you have? (enter as a number): ")

print("\n" * 20)
if level == 0:
    print("You can't be lvl 0")
    exit()

goal = 0
goal_extra = 0
level_extra = 0
if lvl_goal > 50:
    goal_extra = lvl_goal - 50
    lvl_goal = 50
    level_extra = level-50
for i in range(int(level), int(lvl_goal)):
    goal += levels_chart[i]
for i in range(int(level_extra),goal_extra):
    goal += levels_chart_25[i%25]
if xp_boost < 1:
    xp_boost = 1
if xp_boost > 1:
    xp_boost = 1 + xp_boost / 100

if summoner == "aram":
    game_len = ((15 + 20) / 2) * 60
if summoner == "summoner":
    game_len = ((25 + 45) / 2) * 60

xp_left = goal - xp
wins = xp_left / 0.11
loss = xp_left / 0.09
avrage = xp_left / ((0.11 + 0.09) / 2)

games_win, games_loss, games_avrage = xp_left, xp_left, xp_left
won, losses, avrages = 0, 0, 0

while games_win > 0:
    games_win -= 0.11 * game_len * xp_boost + 6.6
    won += 1
while games_loss > 0:
    games_loss -= 0.09 * game_len * xp_boost + 5.4
    losses += 1
while games_avrage > 0:
    games_avrage -= ((0.11 + 0.09) / 2) * game_len * xp_boost + (6.6 + 5.4) / 2
    avrages += 1

print(f"Hours needed in game on a winst, {math.ceil(won*game_len/(60*60))}")
print(f"Hours needed in game on a loss, {math.ceil(losses*game_len/(60*60))}")
print(f"Hours needed in game when avraging, {math.ceil(avrages*game_len/(60*60))}")
print(f"Matches needed of {summoner} on only winsts, {won}")
print(f"Matches needed of {summoner} on only losses, {losses}")
print(f"Matches needed of {summoner} on only avraging, {avrages}")
print(f"with {math.ceil((xp_boost-1)*100)}% xp boost active")
print(f"Good luck on reaching lvl {lvl_goal+goal_extra}")
