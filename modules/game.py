from .data import change, get, save, MINES, SHOP_ITEMS, CRAFTING_RECIPES, FUEL_VALUES, FURNACE_RECIPES, REQUIREMENTS_FOR_BUILDING
import random

def add_item(item, amount):
    inventory = get('player', 'inventory')

    # якщо інвентар порожній або None
    if not inventory:
        inventory = {}

    # додаємо предмет або збільшуємо кількість
    if item in inventory:
        inventory[item] += int(amount)
    else:
        inventory[item] = int(amount)

    # зберігаємо оновлений інвентар
    change('player', 'inventory', inventory)

def remove_item(item: str, amount: int):
    inventory = get('player', 'inventory') or {}

    if item in inventory:
        if amount >= inventory[item]:
            # видаляємо предмет повністю, якщо видаляємо більше або рівно
            inventory.pop(item)
        else:
            # зменшуємо кількість
            inventory[item] -= amount

        # зберігаємо оновлений інвентар
        change('player', 'inventory', inventory)
    else:
        print(f"No {item} in inventory")

def upgrade_mining():
    budget = get('company', 'budget')
    price = get('mine', 'to_upgrade')
    mine_level = get('mine', 'level')
    
    if budget >= price:
        change('mine', value=MINES[mine_level+1])
        budget = budget-price
        change('company', 'budget', budget)
        price('mine was upgraded')
    else:
        print('not enough money')

def set_company_name():
    if not get('company', 'name'):
        name = input('how will called your SC: ')
        change('company', 'name', name)

def mining(amount_of_work=1, target='player'):
    for _ in range(amount_of_work):
        player_data = get(target)  # тепер target може бути 'workers'
        mine = get('mine')
        items = mine['item']
        max_amount = mine['max_amount_item']
        
        # перевірка інструменту
        if mine['required_tools'] == player_data.get('tool', None):
            item = random.choice(items)
            amount = random.randint(1, max_amount)
            
            # додаємо в інвентар target
            inv = get_inventory(target=target)
            inv[item] = inv.get(item, 0) + amount
            change(target, 'inventory', inv)
            
            print(f"{amount} {item} was added to {target}'s inventory")

def get_inventory(item=None, target='player'):
    inv = get(target, 'inventory')
    if not item:
        return inv
    return inv.get(item, 0)

def sell_to_shop(item, amount): 
    inventory = get('player', 'inventory') or {}
    budget = get('company', 'budget') or 0
    amount = int(amount)
    if item in inventory:
        if inventory[item] >= amount:
            remove_item(item, amount)  # зменшуємо інвентар
            revenue = SHOP_ITEMS[item]['sell'] * amount
            budget += revenue
            change('company', 'budget', budget)
            print(f"You sold {amount}x {item} for {revenue}$")
        else:
            print(f"Not enough {item} to sell!")
    else:
        print(f"You don't have any {item} in inventory!")

def buy_in_shop(item, amount):
    inventory = get('player', 'inventory')
    budget = get('company', 'budget')
    
    if budget >= float(SHOP_ITEMS[item]['buy'] * amount):
        add_item(item, amount)
        budget = budget - float(SHOP_ITEMS[item]['buy'] * amount)
        change('company', 'budget', budget)
        print(f'{item} was add to your Inventory in mount of {amount}')
    else:
        print("you don't have enough money")

def get_info():
    player = get('player')
    company = get('company')
    return player, company

def craft(item, times=1):
    recipe = CRAFTING_RECIPES.get(item)
    if not recipe:
        print("No such recipe")
        return

    # перевірка рівня гравця або шахти
    mine_level = get('mine', 'level')
    if recipe.get('required_level', 1) > mine_level:
        print(f"You need mine level {recipe['required_level']} to craft {item}")
        return

    # перевірка крафтінг столу
    required_table = recipe.get('required_table')
    inventory = get('player', 'inventory') or {}
    if required_table and required_table not in inventory:
        print(f"You need {required_table} to craft {item}")
        return

    # перевірка інгредієнтів
    for ing, amt in recipe['ingredients'].items():
        if inventory.get(ing, 0) < amt * times:
            print(f"Not enough {ing} to craft {item}")
            return

    # віднімаємо інгредієнти
    for ing, amt in recipe['ingredients'].items():
        remove_item(ing, amt * times)

    # додаємо вихідний предмет
    add_item(item, recipe['output'] * times)
    print(f"Crafted {recipe['output'] * times}x {item}!")

def deforestation(amount_of_work=1, target='player'):
    for _ in range(amount_of_work):
        wood_amount = random.randint(1, 3)
        
        # отримуємо інвентар target
        inv = get_inventory(target=target)
        
        # додаємо деревину
        inv['wood'] = inv.get('wood', 0) + wood_amount
        
        # зберігаємо назад
        change(target, 'inventory', inv)
        
        print(f"{wood_amount} wood was added to {target}'s inventory")

def furnace(material, material_amount, fuel, fuel_amount, furnace_level=1):
    if material not in FURNACE_RECIPES:
        print('wrong material')
        return
    if fuel not in FUEL_VALUES:
        print('wrong fuel')
        return
    
    fuel_in_inventory = get_inventory(fuel)
    
    if fuel_in_inventory < fuel_amount:
        print("you don't have enough in yor inventory")
        return
        
    required_fuel = FURNACE_RECIPES[material]['fuel'] * material_amount
    current_fuel = FUEL_VALUES[fuel] * fuel_amount
    
    if current_fuel < required_fuel:
        print('not enough fuel')
        return
    if furnace_level < FURNACE_RECIPES[material]['furnace_level']:
        print('low rank of furnace')
        return
    
    remove_item(material, material_amount)
    remove_item(fuel, fuel_amount)
    
    add_item(FURNACE_RECIPES[material]['output'], FURNACE_RECIPES[material]['output_amount'] * material_amount)
    print(f"you get {FURNACE_RECIPES[material]['output']} x{FURNACE_RECIPES[material]['output_amount'] * material_amount}")

def build(building):
    keys= REQUIREMENTS_FOR_BUILDING[building].keys()
    people = get('company', 'people')
    level = get('company', 'level')
    max_worker = level*5
    if level >= 2:
        max_worker = max_worker * 2 
    
    for material in keys:
        if get_inventory(material) < REQUIREMENTS_FOR_BUILDING[building][material]:
            print(f"you don't have enough {material}")
            return
        if people >= level*5:
            print('you have max amount of worker[s], you need to upgrade company')
            return
        
        remove_item(material, REQUIREMENTS_FOR_BUILDING[building][material])
    people = people + 1
    change('company', 'people', people)
    print('worker was heired')

def manage_workers(task, amount_of_workers, times):
    free_workers = get('workers', 'free_workers')
    budget = get('company', 'budget')
    
    if free_workers < amount_of_workers:
        print("Not enough free workers")
        return
    
    salary = 5 * amount_of_workers * times
    if salary > budget:
        print(f"Not enough money, you miss {salary - budget}$")
        return
    
    # виділяємо робітників
    change('workers', 'free_workers', free_workers - amount_of_workers)
    
    # виконання завдання з target='workers'
    if task == 'mining':
        mining(amount_of_work=amount_of_workers * times, target='workers')
    elif task == 'deforestation':
        deforestation(amount_of_work=amount_of_workers * times, target='workers')
    else:
        change('workers', 'free_workers', free_workers)
        print("Wrong task")
        return
    
    change('company', 'budget', budget - salary)
    print(f"{amount_of_workers} worker(s) finished {task} for {times} times, salary {salary}$")

