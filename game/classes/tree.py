from .settings import Setting

class Tree(Setting):
    def __init__(self, x, y, width= 450, height= 400, step= 0, hp= 100, file_name= 'tree.png', folder_name = 'world', count_trees = 3):
        self.X= x
        self.Y= y
        self.WIDTH= width
        self.HEIGHT= height
        self.STEP= step
        self.HP= hp
        self.FOLDER_NAME= folder_name
        self.FILE_NAME= file_name
        self.COUNT_TREES = count_trees
        self.load_image()
        self.load_tree()
        
    def load_tree(self):
        third_width = self.WIDTH // self.COUNT_TREES
        self.TREES = {
            "TREE": self.IMAGE.subsurface(0, 0, third_width, self.HEIGHT),
            "SPRUCE": self.IMAGE.subsurface(third_width, 0, third_width, self.HEIGHT),
            "OLD_TREE": self.IMAGE.subsurface(third_width * 2, 0, third_width, self.HEIGHT)
        }

    def draw_tree(self, surface, tree_type= 'TREE'):
        surface.blit(self.TREES['TREE'], (self.X, self.Y))
        