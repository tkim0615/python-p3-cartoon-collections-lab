def roll_call_dwarves(l):
    for name in l:
        print(f'{l.index(name)+1}. {name}')
roll_call_dwarves(["Doc", "Dopey", "Bashful", "Grumpy"])


def summon_captain_planet(l):
    l =[f'{name.title()}!' for name in l]
    return (l)
summon_captain_planet(["earth", "wind", "fire", "water", "heart"])

def long_planeteer_calls(l):
    for name in l:
        if len(name) > 4:
            return(True)
    return False
print(long_planeteer_calls(["Doc", "Dopey", "Bashful", "Grumpy"]))
    


def find_the_cheese(names):
    for name in names:
        if name == 'cheddar' or name == 'gouda' or name == 'camembert':
            return name
    return None
print(find_the_cheese(["tomato soup", "gouda", "oyster crackers", "camembert"]))

# # 
# The find_the_cheese() function should accept a list of strings. It should then look through these strings to find
# and return the first string that is a type of cheese. The types of cheese that appear are "cheddar", "gouda", and "camembert".

# For example:

# snacks = ["crackers", "gouda", "thyme"]
# find_the_cheese(snacks)
# #=> "gouda"

# soup = ["tomato soup", "cheddar", "oyster crackers", "gouda"]
# find_the_cheese(soup)
# #=> "cheddar"
# If, sadly, a list of ingredients does not include cheese, return None:

# ingredients = ["garlic", "rosemary", "bread"]
# find_the_cheese(ingredients)
# #=> None
# You can assume that all strings will be lowercase. Take a look at the inLinks to an external site. 
# keyword for a hint. This function asks you to return a string value instead of printing it so keep that in mind.