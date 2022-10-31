class Rectangle(object):
    def __init__(self, w, h):
        self.width = w
        self.height = h
    
    def stretch_vertical(self, sf):
        self.height *= sf
    
    def stretch_horizontal(self, sf):
        self.width *= sf

    def draw(self):
        print(("*"*self.width+"\n")*self.height)