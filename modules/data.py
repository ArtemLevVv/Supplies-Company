import json, os

BASE_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(BASE_DIR, 'data', 'data.json')

WOODEN_PICKAXE_ITEMS = [
    'dirt',
    'sand',
    'gravel',
    'clay',
    'stone',
    'coal',
    'peat',
]

STONE_PICKAXE_ITEMS = [
    'copper',
    'tin',
    'zinc',
    'limestone',
]

IRON_PICKAXE_ITEMS = [
    'iron',
    'lead',
    'nickel',
    'sulfur',
]

STEEL_PICKAXE_ITEMS = [
    'bauxite',      
    'chromium',
    'manganese',
]

ELECTRIC_DRILL_ITEMS = [
    'aluminum',
    'silicon',
    'lithium',
    'graphite',
]

INDUSTRIAL_ITEMS = [
    'uranium',
    'thorium',
    'titanium',
    'tungsten',
]

HIGH_TECH_ITEMS = [
    'platinum',
    'iridium',
    'rare_earth_elements',
]

PICKAXE_TIERS = {
    'wooden': WOODEN_PICKAXE_ITEMS,
    'stone': STONE_PICKAXE_ITEMS,
    'iron': IRON_PICKAXE_ITEMS,
    'steel': STEEL_PICKAXE_ITEMS,
    'electric': ELECTRIC_DRILL_ITEMS,
}

MINES = {
    1: {
        'level': 1,
        'tier': 'wooden',
        'items': PICKAXE_TIERS['wooden'],
        'required_tool': 'wooden_pickaxe',
        'max_amount_item': 2,
        'depth': 5,
        'to_upgrade': 1000
    },
    2: {
        'level': 2,
        'tier': 'stone',
        'items': PICKAXE_TIERS['stone'],
        'required_tool': 'stone_pickaxe',
        'max_amount_item': 3,
        'depth': 10,
        'to_upgrade': 10000
    },
    3: {
        'level': 3,
        'tier': 'iron',
        'items': PICKAXE_TIERS['iron'],
        'required_tool': 'iron_pickaxe',
        'max_amount_item': 4,
        'depth': 15,
        'to_upgrade': 25000
    },
    4: {
        'level': 4,
        'tier': 'steel',
        'items': PICKAXE_TIERS['steel'],
        'required_tool': 'steel_pickaxe',
        'max_amount_item': 5,
        'depth': 20,
        'to_upgrade': 50000
    },
    5: {
        'level': 5,
        'tier': 'electric',
        'items': PICKAXE_TIERS['electric'],
        'required_tool': 'electric_drill',
        'max_amount_item': 6,
        'depth': 25,
        'to_upgrade': 100000
    },
}

FOREST = {
    'required_tool': 'axe',
    'items': ['wood'],
    'min_amount': 1,
    'max_amount': 3,
}

SHOP_ITEMS = {
    # =========================
    # БАЗОВІ РЕСУРСИ (СТАРТ)
    # =========================
    'wood': {'buy': 3, 'sell': 2},
    'board': {'buy': 6, 'sell': 4},
    'stick': {'buy': 2, 'sell': 1},
    'torch': {'buy': 4, 'sell': 2},

    'dirt': {'buy': 1, 'sell': 0.5},
    'sand': {'buy': 2, 'sell': 1},
    'gravel': {'buy': 2, 'sell': 1},
    'clay': {'buy': 3, 'sell': 1.5},
    'stone': {'buy': 3, 'sell': 1.5},

    # =========================
    # ПАЛИВО
    # =========================
    'coal': {'buy': 5, 'sell': 2.5},
    'peat': {'buy': 4, 'sell': 2},
    'charcoal': {'buy': 6, 'sell': 3},

    # =========================
    # БУДІВЕЛЬНІ МАТЕРІАЛИ
    # =========================
    'brick': {'buy': 6, 'sell': 4},
    'brick_wall': {'buy': 12, 'sell': 8},
    'glass': {'buy': 8, 'sell': 5},

    'wooden_chest': {'buy': 15, 'sell': 10},
    'camp_fire': {'buy': 20, 'sell': 14},
    'door': {'buy': 10, 'sell': 6},

    # =========================
    # РАННІ МЕТАЛИ
    # =========================
    'copper': {'buy': 10, 'sell': 7},
    'tin': {'buy': 8, 'sell': 5},
    'zinc': {'buy': 9, 'sell': 6},
    'limestone': {'buy': 5, 'sell': 3},

    'bronze': {'buy': 18, 'sell': 12},

    # =========================
    # СЕРЕДНІ МЕТАЛИ
    # =========================
    'iron': {'buy': 15, 'sell': 10},
    'lead': {'buy': 12, 'sell': 8},
    'nickel': {'buy': 14, 'sell': 9},
    'sulfur': {'buy': 10, 'sell': 6},

    'steel': {'buy': 25, 'sell': 18},

    # =========================
    # ПРОСУНУТІ МАТЕРІАЛИ
    # =========================
    'bauxite': {'buy': 18, 'sell': 12},
    'chromium': {'buy': 20, 'sell': 14},
    'manganese': {'buy': 16, 'sell': 11},

    'aluminum': {'buy': 25, 'sell': 18},

    # =========================
    # ЕЛЕКТРО / ХАЙ-ТЕК
    # =========================
    'silicon': {'buy': 30, 'sell': 20},
    'graphite': {'buy': 28, 'sell': 20},
    'lithium': {'buy': 35, 'sell': 25},

    'battery': {'buy': 50, 'sell': 35},
    'wire': {'buy': 12, 'sell': 8},
    'circuit': {'buy': 80, 'sell': 55},

    # =========================
    # ПРОМИСЛОВІ
    # =========================
    'titanium': {'buy': 55, 'sell': 40},
    'tungsten': {'buy': 60, 'sell': 45},
    'uranium': {'buy': 50, 'sell': 35},
    'thorium': {'buy': 45, 'sell': 30},

    # =========================
    # ХАЙ-ТЕК / ЛЕЙТ
    # =========================
    'platinum': {'buy': 100, 'sell': 70},
    'iridium': {'buy': 120, 'sell': 85},
    'rare_earth_elements': {'buy': 150, 'sell': 100},
}

CRAFTING_RECIPES = {
    'clay_block': {
        'ingredients': {'sand': 2, 'clay': 1},
        'output': 1,
        'required_level': 1,
    },
    'handful_peat': {
        'ingredients': {'peat': 3},
        'output': 1,
        'required_level': 1,
    },
    'boards': {
        'ingredients': {'wood': 1},
        'output': 2,
        'required_level': 1,
    },
    'stick': {
        'ingredients': {'boards': 1},
        'output': 2,
        'required_level': 1,
    },
    'wooden_pickaxe': {
        'ingredients': {'boards': 3, 'stick': 2},
        'output': 1,
        'required_level': 1,
        'required_table': 'crafting_table', 
    },
    'torch': {
        'ingredients': {'stick': 1, 'coal': 1},
        'output': 4,
        'required_level': 1,
    },
    'crafting_table': {
        'ingredients': {'boards': 4},
        'output': 1,
        'required_level': 1,
    },
    'wooden_sword': {
        'ingredients': {'boards': 2, 'stick': 1},
        'output': 1,
        'required_table': 'crafting_table',
    },
    'wooden_shovel': {
        'ingredients': {'boards': 1, 'stick': 2},
        'output': 1,
        'required_table': 'crafting_table',
    },
    'wooden_slab': {
        'ingredients': {'boards': 3},
        'output': 6,
        'required_level': 1,
    },
    'wooden_axe': {
        'ingredients': {'stick': 2, 'boards': 3},
        'output': 1,
        'required_table': 'crafting_table',
        'required_level': 1,
    },
    'wooden_chest':{
        'ingredients': {'boards': 8},
        'output': 1,
        'required_table': 'crafting_table',
        'required_level': 1,
    },
    'campfire':{
        'ingredients': {'boards': 3, 'coal': 3},
        'output': 1,
        'required_level': 1,
    },
    'brick_furnace':{
        'ingredients': {'stone': 8},
        'output': 1,
        'required_level': 1,
        'required_table': 'crafting_table',
    },
    'brick_wall':{
        'ingredients': {'brick': 12},
        'output': 1,
        'required_level': 1,
        'required_table': 'crafting_table',
    },
}

# fuel = required fuel units to process 1 input item

FURNACE_RECIPES = {
    'clay_block': {
        'fuel':1,
        'output': 'brick',
        'output_amount':1,
        'furnace_level': 1,
    },
    'handful_peat': {
        'fuel': 1,
        'output': 'dried_peat',
        'output_amount': 1,
        'furnace_level': 1,
    },
    'sand': {
        'fuel': 0.5,
        'output': 'glass',
        'output_amount': 1,
        'furnace_level': 2,
    },
}

FUEL_VALUES = {
    # дрібне паливо
    'stick': 0.25,
    'boards': 1,
    'wood': 2,
    'wooden_slab': 1.5,

    # органіка
    'handful_peat': 1,
    'peat_block': 10,
    'dried_peat': 4,

    # вугілля
    'coal': 8,

    # дерев'яні предмети
    'wooden_pickaxe': 1.5,
    'wooden_axe': 1.5,
    'wooden_shovel': 1.25,
    'wooden_sword': 1.25,
    'wooden_chest': 3,
    'crafting_table': 2,
}

ALL_ITEMS = [
    # ранній рівень (дерев'яний кайло)
    'boards',
    'stick',
    'dirt',
    'sand',
    'gravel',
    'clay',
    'stone',
    'coal',
    'peat',
    'wood',  # доданий базовий ресурс

    # кам'яний кайло
    'copper',
    'tin',
    'zinc',
    'limestone',

    # залізне кайло
    'iron',
    'lead',
    'nickel',
    'sulfur',

    # сталеве кайло
    'bauxite',
    'chromium',
    'manganese',

    # електро-інструменти
    'aluminum',
    'silicon',
    'lithium',
    'graphite',

    # промислові
    'uranium',
    'thorium',
    'titanium',
    'tungsten',

    # хай-тек
    'platinum',
    'iridium',
    'rare_earth_elements',

    # крафтові предмети
    'brick',
    'clay_block',
    'furnace',
    'fuel_block',
]

REQUIREMENTS_FOR_BUILDING= {
    'house':{
        'brick_wall': 4,
        'door': 1,
        'glass': 5,
        'board': 20,
        'torch': 5,
        'wooden_chest':2,
        'camp_fire':1,
    },
    'warehouse':{
        'brick_wall':8,
        'door':2,
        'glass':8,
        'board':30,
        'torch':12,
        'wooden_chest':10,
    }
}

QUESTS = {
    'infrastructure':{
            1:{
                'stone':20,
                'torch':10,
            }
        },
    'social':{
            1:{
                'brick_wall':4,
                'glass':2,
                'torch':2,
            }
        },
    'administrative':{
            1:{
                'brick_wall':4,
                'glass':2,
                'torch':2,
                'wooden_chest':2,
            }
        },
    'industrial':{
            1:{
                'handful_peat':10,
                'coal':10,
            }
        },
}

TOOLS ={
    'wooden_pickaxe':{
        'health': 200,
        'damage': 1,
    },
    'wooden_axe':{
        'heath': 200,
        'damage':1,
    }
}

initial_data = {
    'town':{
        'quest_id':{
            'infrastructure':1,
            'social':1,
            'administrative':1,
            'industrial':1,
        },
        'boost':{
            'infrastructure':0,
            'social':0,
            'administrative':0,
            'industrial':0,
        }
    },
    'warehouse':{
        'capacity': 150
    },
    'player': {
        'tool': {
            'wooden_pickaxe': 200,
            'wooden_axe': 200,
        },
        'inventory': {
            
        },
    },
    "workers":{
        "inventory":{
            
        },
        "tool":"",
        "salary":5,
        "free_workers":0
    },
    'company':{
        'name':'',
        'budget':100,
        'people':0,
        'level':1
    },
    'mine':MINES[1],
}

def get(object_name=None, key=None):
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # якщо не передали — явно
    if not object_name:
        return data
    
    # якщо передали, але такого нема — теж без крашу
    obj = data.get(object_name)
    
    if not obj:
        return data
    
    if not key:
        return obj
    
    return obj.get(key, obj)

def save(data):
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii= False, indent= 4)

def init_data():
    try:
        if not os.path.exists(FILE_PATH):
            with open(FILE_PATH, 'w', encoding='utf-8') as file:
                json.dump(initial_data, file, ensure_ascii=False, indent=4)
            print('create initial file')
        else:
            print('initial file was created before')
    except Exception as e:
        print('something went wrong')
        print(e)            

def change(object_name, key=None, value=None):
    try:
        data = get()  # беремо весь JSON

        if not object_name:
            return  # нічого не міняємо

        if key is None:
            # змінюємо весь об'єкт
            data[object_name] = value
        else:
            if object_name not in data:
                data[object_name] = {}
            data[object_name][key] = value

        save(data)

    except Exception as e:
        print('something went wrong')
        print(e)
