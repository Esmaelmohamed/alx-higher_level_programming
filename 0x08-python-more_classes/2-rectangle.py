#!/usr/bin/python3
"""Defines a Rectangle Class """
 
class Rectangle:
    """Represent a rectangle """
    def __init__(self,width=0,height=0):
      """  inti a new rectangle. 
        Arguments: 
        width (int): the width of the new rectangle 
        height (int): the height of the new rectangle 
     """ 
      self.width = width 
      self.height = height 

      @property
      def width(self):
         """Get and Set the width o the rectangle """ 
         return self.__width 
      
      @width.setter
      def width(self,value):
         if not isinstance(value,int):
            raise TypeError("Width must be an integer") 
         if value <0:
            raise ValueError("Width must be >=0 ") 
         self.__width = value 

         @property
         def height(self):
            """Get and set of the height """ 
            return self.__height 
         
         @height.setter
         def height(self,value):
            if not isinstance(value,int):
               raise TypeError("height must be an integer") 
            if value<0:
               raise ValueError("height must be >=0 ")
            self.__height = value 

            def area(self):
               """Retrun the area of the Rectangle """ 
               return (self.__width * self.__height)
            def parameter(self):
               """Return the area of the Rectangle """ 
               if self.__width == 0 or self.__height == 0:
                  return (0) 
               return ((self.__wdith * 2 ) + (self.__height * 2)) 
            
                  
      

