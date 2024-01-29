#!/usr/bin/bash 
"""Defines a Rectangle class """ 

class Rectangle:
    """Represent a rectangle . """ 

    def __init__(self,width=0,height=0):
        """ Initialize a New  rectangle
         arguments: 
         width (int) : the width of the rectangle 
         height (int) : the height of the rectangle 
          
           """
        self.width = width 
        self.height = height 

        @property
        def width(self):
            """the getter of the width """ 
            return self.__width 
        @width.setter
        def width(self,value):
            if not isinstance(value,int):
                raise TypeError("width must be an integer ") 
            if value<0:
                raise ValueError("width musr be >=0 ") 
            self.__width = value 

            @property
            def height(self):
                """the height getter and setter  """ 
                return self.__height 
            @height.setter
            def height(self,vlaue):
                if not isinstance(value , int):
                    raise TypeError("height must be an integer ") 
                if value <0:
                    raise ValueError("height must be >=0 ")
                self.__height = vlaue 

            def area(self):
                """Return the parameter of the rectangle """ 
                if self.__width == 0 or self.__height == 0:
                    return (0) 
                return ((self.__width * 2) + (self.__height * 2)) 
            def __str__(self):
                """Return the printable representaion of the rectangle object """ 
                if self.__width == 0 or self.__height == 0:
                    return("") 
                react = [] 
                for i in range(self.__height):
                    [react.append('#') for j in range (self.__width)]
                    if i != self.__height - 1:
                        react.append("\n") 
                    return ("".join(react)) 
            
        def __repr__(self):
            """Return the string representation of the Rectangle."""
            rect = "Rectangle(" + str(self.__width)
            rect += ", " + str(self.__height) + ")"
            return (rect)
                
            