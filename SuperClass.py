class Math:
    
    def __init__(self,x):
        self.x = x
        
    def sample(self):
        print("this is base sample")
        
class Science(Math):
    
    def __init__(self,x,y):
        
        super(Science, self).__init__(x)
        self.y =y
        super(Science, self).sample() # with help of this line we can display the base class sample method.

    def sample(self):
        print("this is derived sample")
        print(self.x,self.y)

a = Science(23,90)
a.sample()
