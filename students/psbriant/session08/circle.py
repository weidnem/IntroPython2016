class Circle:
    def __init__(self, radius):
        """

        """
        self.radius = radius

        self.diameter = radius * 2

        @property
        def diameter(self):
            return self.radius * 2
        @diameter.setter
        def diameter(self, value):
            self.radius = value / 2
            
