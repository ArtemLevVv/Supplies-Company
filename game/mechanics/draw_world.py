from ..classes.tree import Tree
from .data import get, CHUNK_SIZE, world_parts


tree = Tree(x= 0, y= 0)
BLOCK_SIZE = 64  # або як у тебе

def draw_world(chunks_ids: list, surface):
    for chunk_id in chunks_ids:
        chunk = get(f'chunk{chunk_id}')  # отримуємо 2D список

        for y, row in enumerate(chunk):  # проходимо по рядках
            for x, value in enumerate(row):  # проходимо по колонках
                if value == 1:
                    tree.X= x
                    tree.Y= y
                    tree.draw_tree(surface=surface, tree_type='TREE')
                elif value == 2:
                    tree.X= x
                    tree.Y= y
                    tree.draw_tree(surface=surface, tree_type='SPRUCE')
                elif value == 3:
                    tree.X= x
                    tree.Y= y
                    tree.draw_tree(surface=surface, tree_type='OLD_TREE')
