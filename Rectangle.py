class Rectangle(object):
    def __init__(self, w, h):
        self.width = w
        self.height = h
    
    def stretchVertical(self, sf):
        self.height *= sf
    
    def stretchHorizontal(self, sf):
        self.width *= sf

    def draw(self):
        print(("#"*self.width+"\n")*self.height)

class FramedRectangle(Rectangle):
    def __init__(self, w, h, symbol="*"):
        super().__init__(w,h)
        self.frame_symbol = symbol
    
    def draw(self):
        frame = self.frame_symbol
        print(frame*(self.width+2))
        print((frame+"#"*self.width+frame+"\n")*self.height, end="")
        print(frame*(self.width+2))