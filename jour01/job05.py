class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display_points(self):
        return (f"The axis are {self.x} and {self.y}")
    
    def display_x(self):
        return (f"The x axis is {self.x}")
    def display_y(self):
        return (f"The y axis is {self.y}")



all_axis = Point(20, 30)
x_axis = Point(20, 30)
y_axis = Point(20, 30)

print(all_axis.display_points())
print(x_axis.display_x())
print(y_axis.display_y())
