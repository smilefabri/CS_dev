"""Vector class

""" 
from math import sqrt


class Vector2(object):
    x: float
    y: float

    def __init__(self,x_,y_) -> None:
        self.x = x_
        self.y = y_

    #set and get

    def Magnitude(self)->float:
        return sqrt( self.x**2+self.y**2)

    def set_Magnitude(self):
        pass
    def Normalize(self)->None:
        mag = self.Magnitude()
        if mag != 0:
            self.x = self.x  / mag
            self.y = self.y / mag

    def limit(self,max:float)->None:
        pass


    #Magic function
    def __str__(self)-> str:
        return str(( round(self.x,2) ,round(self.y,2)))

    def __add__(self,other:'Vector2')-> 'Vector2':
        assert isinstance(other,Vector2), f"{other} in not a {Vector2}"
        return Vector2(self.x +other.x,self.y +other.y)

    def __sub__(self,other:'Vector2')-> 'Vector2':
        assert isinstance(other,Vector2), f"{other} in not a {Vector2}"
        return Vector2(self.x -other.x,self.y -other.y)
    
    def __mul__(self,other)-> 'Vector2':
        assert not isinstance(other,Vector2), f"{other} must not be {Vector2} "
        return Vector2(self.x * other,self.y * other)
    
    def __truediv__(self,other)-> 'Vector2':
        assert not isinstance(other,Vector2), f"{other} must not be {Vector2} "
        return Vector2(self.x / other,self.y / other)

    
        

def main():
    posizione:Vector2 = Vector2(5,5)

    posizione.x = 40

    posizione.Normalize()

    
    print(posizione)
    print(posizione.Magnitude())

    
    

if __name__ =="__main__":
    
    main()








