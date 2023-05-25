def roll_call_dwarves(dwarves_list):
    i = 1
    for name in dwarves_list:
        print(f'{i}. {name}')
        i += 1

def summon_captain_planet(planeteer_calls):
    calls_list = [f'{call.title()}!' for call in planeteer_calls]
    return calls_list
    # summon_captain_planet(["cat", "dog", "bear"])
    
        

def long_planeteer_calls(short_words):
    for word in short_words:
        if len(word) > 4:
            return True
    
    return False

def find_the_cheese(foods):
    cheeses = ["camembert", "gouda", "cheddar"]
    for food in foods:
        if food in cheeses:
            return food
    return None
