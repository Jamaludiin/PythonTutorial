

class animal:
    def __init__(self, name, color, category):
        self.name = name
        self.color = color 
        self.category = category # it can be mammals, birds, fish, reptiles, amphibians


animal_obj = animal("Lion", "Red", "Mammals")

# display the animals on the screen
print("Name:", animal_obj.name, "\nColor:", animal_obj.color, "\nCategory:", animal_obj.category)
