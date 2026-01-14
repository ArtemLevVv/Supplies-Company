from .data import (
    change, get, save,
    MINES, SHOP_ITEMS,
    CRAFTING_RECIPES,
    FUEL_VALUES,
    FURNACE_RECIPES,
    REQUIREMENTS_FOR_BUILDING,
    QUESTS,
)
import random

# =========================
# INVENTORY HELPERS
# =========================

def get_inventory(item=None, target='player'):
    try:
        inventory = get(target, 'inventory') or {}
        if item is None:
            return inventory
        return inventory.get(item, 0)
    except Exception as e:
        print(e)
        print('something went wrong')


def add_item(item, amount, target='player'):
    try:
        inventory = get_inventory(target=target)
        inventory[item] = inventory.get(item, 0) + int(amount)
        change(target, 'inventory', inventory)
    except Exception as e:
        print(e)
        print('something went wrong')


def remove_item(item, amount, target='player'):
    try:
        inventory = get_inventory(target=target)

        if item not in inventory:
            print(f"No {item} in {target}'s inventory")
            return False

        if amount > inventory[item]:
            print(f"Not enough {item}")
            return False
        elif amount == inventory[item]:
            inventory.pop(item)
        else:
            inventory[item] -= amount

        change(target, 'inventory', inventory)
        return True
    except Exception as e:
        print(e)
        print('something went wrong')


# =========================
# COMPANY / GAME
# =========================

def set_company_name():
    try:
        if not get('company', 'name'):
            name = input('How will your company be called?: ')
            change('company', 'name', name)
    except Exception as e:
        print(e)
        print('something went wrong')

def get_info():
    try:
        return {
            'town': get('town'),
            'player': get('player'),
            'company': get('company'),
            'mine': get('mine'),
            'workers': get('workers')
        }
    except Exception as e:
        print(e)
        print('something went wrong')


# =========================
# MINING / WOOD
# =========================


def mining(amount_of_work=1, target='player'):
    try:
        mine = get('mine')

        for _ in range(amount_of_work):
            entity = get(target)

            tool = entity.get('tool')
            if mine.get('required_tool') and tool != mine['required_tool']:
                print(f"{target} has wrong tool")
                return

            item = random.choice(mine['items'])
            amount = random.randint(1, mine['max_amount_item'])

            add_item(item, amount, target)
            print(f"{amount} {item} added to {target}")
    except Exception as e:
        print(e)
        print('something went wrong')

def deforestation(amount_of_work=1, target='player'):
    try:
        for _ in range(amount_of_work):
            wood = random.randint(1, 3)
            add_item('wood', wood, target)
            print(f"{wood} wood added to {target}")
    except Exception as e:
        print(e)
        print('something went wrong')

# =========================
# SHOP
# =========================

def sell_everything():
    print('sell_everything')
    inventory = get('player', 'inventory')
    print(inventory)
    for item, amount in inventory.items():
        print(item)
        print(amount)
        sell_to_shop(item, int(amount))
    
    print('everything was sold')


def sell_to_shop(item, amount):
    try:
        amount = int(amount)
        inventory_amount = get_inventory(item)

        if inventory_amount < amount:
            print("Not enough items to sell")
            return

        price = SHOP_ITEMS[item]['sell'] * amount
        remove_item(item, amount)
        change('company', 'budget', get('company', 'budget') + price)

        print(f"Sold {amount}x {item} for {price}$")
    except Exception as e:
        print(e)
        print('something went wrong')


def buy_in_shop(item, amount):
    try:
        amount = int(amount)
        cost = SHOP_ITEMS[item]['buy'] * amount
        budget = get('company', 'budget')

        if budget < cost:
            print("Not enough money")
            return

        add_item(item, amount)
        change('company', 'budget', budget - cost)
        print(f"Bought {amount}x {item}")
    except Exception as e:
        print(e)
        print('something went wrong')


# =========================
# CRAFTING
# =========================

def craft(item, times=1):
    try:
        recipe = CRAFTING_RECIPES.get(item)
        if not recipe:
            print("No such recipe")
            return

        mine_level = get('mine', 'level')
        if recipe.get('required_level', 1) > mine_level:
            print("Mine level too low")
            return

        required_table = recipe.get('required_table')
        if required_table and get_inventory(required_table) == 0:
            print(f"You need {required_table}")
            return

        for ing, amt in recipe['ingredients'].items():
            if get_inventory(ing) < amt * times:
                print(f"Not enough {ing}")
                return

        for ing, amt in recipe['ingredients'].items():
            remove_item(ing, amt * times)

        add_item(item, recipe['output'] * times)
        print(f"Crafted {recipe['output'] * times}x {item}")
    except Exception as e:
        print(e)
        print('something went wrong')

# =========================
# FURNACE
# =========================

def furnace(material, material_amount, fuel, fuel_amount, furnace_level=1):
    try:
        material_amount = int(material_amount)
        fuel_amount = int(fuel_amount)

        if material not in FURNACE_RECIPES:
            print("Wrong material")
            return
        if fuel not in FUEL_VALUES:
            print("Wrong fuel")
            return

        recipe = FURNACE_RECIPES[material]

        if furnace_level < recipe['furnace_level']:
            print("Furnace level too low")
            return

        required_fuel = recipe['fuel'] * material_amount
        available_fuel = FUEL_VALUES[fuel] * fuel_amount

        if available_fuel < required_fuel:
            print("Not enough fuel power")
            return

        if get_inventory(material) < material_amount:
            print("Not enough material")
            return

        remove_item(material, material_amount)
        remove_item(fuel, fuel_amount)

        add_item(recipe['output'], recipe['output_amount'] * material_amount)
        print(f"Smelted {recipe['output_amount'] * material_amount}x {recipe['output']}")
    except Exception as e:
        print(e)
        print('something went wrong')

# =========================
# BUILDINGS / WORKERS
# =========================

def build(building):
    try:
        recipe = REQUIREMENTS_FOR_BUILDING.get(building)
        if not recipe:
            print("No such building")
            return
        if building == 'house':
            people = get('company', 'people')
            level = get('company', 'level')
            max_workers = level * 5

            if people >= max_workers:
                print("Worker limit reached")
                return

            for item, amount in recipe.items():
                if get_inventory(item) < amount:
                    print(f"Not enough {item}")
                    return

            for item, amount in recipe.items():
                remove_item(item, amount)

            change('company', 'people', people + 1)
            change('workers', 'free_workers', get('workers', 'free_workers') + 1)

            print("Worker hired")
        
        elif building == 'warehouse':
            for item, amount in recipe.items():
                if get_inventory(item) < amount:
                    print(f'Not enough {item}')
                    return
                
            for item, amount in recipe.items():
                remove_item(item, amount)
            
            capacity = get('warehouse', 'capacity')
            
            change('warehouse', 'capacity', capacity+100)
    except Exception as e:
        print(e)
        print('something went wrong')

def manage_workers(task, workers, times):
    try:
        workers = int(workers)
        times = int(times)

        free = get('workers', 'free_workers')
        budget = get('company', 'budget')
        salary = 5 * workers * times
        tool = get('workers', 'tool')
        required_tool = get('mine', 'required_tool')
        
        if free < workers:
            print("Not enough free workers")
            return
        if budget < salary:
            print("Not enough money")
            return

        change('workers', 'free_workers', free - workers)

        if task == 'mining':
            mining(workers * times, target='workers')
        elif task == 'deforestation':
            deforestation(workers * times, target='workers')
        else:
            print("Wrong task")
            change('workers', 'free_workers', free)
            return

        change('company', 'budget', budget - salary)
        change('workers', 'free_workers', free)

        print(f"{workers} workers finished {task}, salary paid {salary}$")
    except Exception as e:
        print(e)
        print('something went wrong')

def collect_from_workers():
    try:
        inventory = get_inventory(target='workers')

        for item, amount in list(inventory.items()):
            add_item(item, amount)
            remove_item(item, amount, target='workers')

        print("Resources collected from workers")
    except Exception as e:
        print(e)
        print('something went wrong')

def set_tool_to_worker(tool):
    tool = get_inventory(tool)
    if tool != {}:
        change('workers', 'tool', tool)
        
    remove_item(tool, 1)

def quest(type_of_quest):
    try:
        quests = get('town', 'quest_id')

        if type_of_quest not in quests:
            print('no such quest')
            return

        quest_level = quests[type_of_quest]

        if quest_level not in QUESTS[type_of_quest]:
            print('no more quests in this category')
            return

        materials = QUESTS[type_of_quest][quest_level]

        for item, amount in materials.items():
            if get_inventory(item) < amount:
                print(f'Not enough {item}')
                return

        for item, amount in materials.items():
            remove_item(item, amount)

        boost = get('town', 'boost')
        boost[type_of_quest] += 1
        change('town', 'boost', boost)

        quests[type_of_quest] += 1
        change('town', 'quest_id', quests)

        print(f'{type_of_quest} quest completed!')
    except Exception as e:
        print(e)
        print('something went wrong')

# try except was added to play nonstoply with errors
# expansions of items in shop
# condition was added to check if worker have tool to mine of get wood 
# possibility to sell whole inventory was added
# 