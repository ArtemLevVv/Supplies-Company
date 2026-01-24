import random, json, os

# 0 = air, 1 = tree
world_parts = ['air', 'tree', 'spruce', 'old_tree']

AIR = 0
TREE = 1
SPRUCE = 2
OLD_TREE = 3


CHUNK_SIZE = 8  # 8x8 blocks

world = {
    "chunk0": [],
    "chunk10": [],
    "chunk01": [],
    "chunk11": [],
}

FILE_PATH_WORLD = f'{__file__}/../../data/data.json'

def random_chunk():
    return [
        [random.randint(AIR, OLD_TREE) for _ in range(CHUNK_SIZE)]
        for _ in range(CHUNK_SIZE)
    ]

def init_data():
    print('init_data_world')
    if not os.path.exists(FILE_PATH_WORLD):
        for chunk_key in world:
            print(f"Generating {chunk_key}")
            world[chunk_key] = random_chunk()
        with open(FILE_PATH_WORLD, 'w', encoding='utf-8') as file:
            json.dump(world, file, ensure_ascii=False, indent=4)
        print('create initial world file')
    else:
        print('initial file was created before')

def get(object_name=None, key=None):
    with open(FILE_PATH_WORLD, 'r', encoding='utf-8') as file:
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