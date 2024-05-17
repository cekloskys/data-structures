from circle.circle import *

class cylinder(circle):
    """The Cylinder class stores general information about a cylinder.

    Args:
        circle (circle): class that includes general information about
        a circle.
    """    
    def __init__(self, radius: float, height: float):
        """Constructs a cylinder using the specified radius and height.

        :ivar __radius: radius of this cylinder
        :ivar __area: area of this cylinder
        :ivar __circumference: circumference of this cylinder
        :ivar __height: height of this cylinder
        :ivar __volume: volume of this cylinder

        Args:
            radius (float): specified radius
            height (float): specified height

        Raises:
            ValueError: indicates specified height isn't a float
            ValueError: indicates specified height isn't positive
        """        
        super().__init__(radius)
        try:
            if (not isinstance(height, float)):
                raise ValueError("Height must be a float!") 
            if (height < 0.0):
                raise ValueError("Height must be positive!")             
        except ValueError as e:
            exit(e)
        else:
            self.__height = height
            self.__volume = self.__height * self.getArea()

    def getHeight(self):
        """Returns the height of the calling cylinder.

        Returns:
            float: height of the calling cylinder
        """
        return self.__height
    
    def setHeight(self, height: float):
        """Sets the height of the calling cylinder to the specified height and
        recomputes the volume of the calling cylinder.

        Args:
            height (float): specified height

        Raises:
            ValueError: indicates specified height isn't a float
            ValueError: indicates specified height isn't positive
        """
        try:
            if (not isinstance(height, float)):
                raise ValueError("Height must be a float!") 
            if (height < 0.0):
                raise ValueError("Height must be positive!")             
        except ValueError as e:
            exit(e)
        else:
            self.__height = height
            self.__volume = self.__height * self.getArea()

    def getVolume(self):
        """Returns the volume of the calling cylinder.

        Returns:
            float: volume of the calling cylinder
        """
        return self.__volume
    
    def __str__(self):
        """Returns string representation of the calling cylinder.

        Returns:
            str: string representation of the calling cylinder
        """
        return f"radius={self.getRadius()}, area={self.getArea()}, circumference={self.getCircumference()}, height={self.__height}, volume={self.__volume}"
    
    def __eq__(self, other):
        """Tests if the calling cylinder is equal to the specified object.

        Args:
            other: the specified object

        Returns:
            Boolean: True if the cylinder circle is equal to the specified
            object, else False
        """
        if other is not None:
            if isinstance(other, cylinder):
                if other.getRadius() == self.getRadius():
                    if other.getArea() == self.getArea():
                        if other.getCircumference() == self.getCircumference():
                            if other.__height == self.__height:
                                if other.__volume == self.__volume:
                                    return True
        return False