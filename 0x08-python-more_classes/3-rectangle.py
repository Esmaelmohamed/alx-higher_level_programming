#!/usr/bin/python3 
"""Defines a Rectangle class """ 
class Rectangle: 
    def __init__(self, width=0,height=0): 
        """ initlize a new rectangle 
        Arguments: 
        width (int): the width of the rectangle 
        height (int): the height of the new rectangle 

        """ 
        self.width = width 
        self.height = height 

        @property 
        def width(self):
            """Get and Set the width of the Rectangle """ 
            return self.__width 
        
        @width.setter
        def widht(self,vlaue):
            if not isinstance(vlaue,int):
                raise TypeError("width must be an integer ")
            if vlaue < 0: 
                raise ValueError("Width must be >= 0") 
            self.__width = vlaue 

            @property
            def height(self):
                return self.__height 
            
            @height.setter
            def height(self,value):
                if not isinstance(vlaue,int):
                    raise TypeError("the value must be an integer ") 
                if value <0:
                    raise ValueError("height must be >=0 ") 
                self.__height = value 

                def area(self): 
                    """ return the area of the rectangle """
                    return (self.__width *self.__height) 
                def parameter(self):
                    """Return the prarameter of the rectangle """ 
                    if self.__width == 0 or self.__height ==0:
                        return (0) 
                    return ((self.__width * 2) + (self.__height * 2))
                
                def __str__(self):
                    """Return the printable representain of the rectangle object """ 
                    if self.__width == 0 or self.__height ==0:
                        return ("") 
                    rect = [] 
                    for i in range(self.__height):
                        [rect.append("#") for j in range(self.__width)] 
                        if i != self.__height - 1:
                            rect.append("\n") 
                        return("".join(rect)) 
            
             
