# Simple class which has attributes and method

class animal:
    def __init__(self, name, color, category): # the self parameter is used to access the variables declared inside the class. It is not compulsory to be named self, you can use other names but it has to be at the first parameter in any function found in the class 
        self.name = name
        self.color = color 
        self.category = category # it can be mammals, birds, fish, reptiles, amphibians
        
        self.animal_facts = self.animal_facts()


    # Animal charecteristics are stated also after these conditions are matched
    def animal_facts(self):
        if self.category == "mammals" or self.category == "Mammals":
            return "Mammals are characterized by the presence of milk-producing mammary glands for feeding their young"
        elif self.category == "birds" or self.category == "Birds":
            return "Birds are characterised by feathers, toothless beaked jaws, the laying of hard-shelled eggs, a high metabolic rate, a four-chambered heart, and a strong yet lightweight skeleton."
        elif self.category == "fish" or self.category == "Fish":
            return "Fish or fishes is an aquatic, craniate, gill-bearing animal that lacks limbs with digits. "
        elif self.category == "reptiles" or self.category == "Reptiles":
            return "Reptiles, as commonly defined, are a group of tetrapods with an ectothermic metabolism and amniotic development."
        elif self.category == "amphibians" or self.category == "Amphibians":
            return "Amphibians are ectothermic, anamniotic, four-limbed vertebrate animals that constitute the class Amphibia."
        else:
            return "This animal is from Unknown Cataegory"


    # __str__() Function controls what should be returned when the class object is represented as a string.
    def __str__(self): 
        return f"Name: {self.name}, \nColor: {self.color} \nCategory: {self.category} \nAnimal Facts: {self.animal_facts} \n"


# outside of the class 
animal_obj = animal("Snake", "Yellow", "Reptiles")
"""# display the animals on the screen
print("Name:", animal_obj.name, "\nColor:", animal_obj.color, "\nCategory:", animal_obj.category, "\nAnimal Facts:", animal_obj.animal_facts,"\n")
"""
print(animal_obj)

animal_obj = animal("Lion", "Red", "Mammals")
"""# display the animals on the screen
print("Name:", animal_obj.name, "\nColor:", animal_obj.color, "\nCategory:", animal_obj.category, "\nAnimal Facts:", animal_obj.animal_facts,"\n")
"""
print(animal_obj)

animal_obj = animal("Alien", "Dark", "Carnivals")
"""# display the animals on the screen
print("Name:", animal_obj.name, "\nColor:", animal_obj.color, "\nCategory:", animal_obj.category, "\nAnimal Facts:", animal_obj.animal_facts,"\n")
"""
print(animal_obj)


# more concepts

# modify object properties
animal_obj.name = "Tiger"

# delete object property 
del animal_obj.name

# delete object
del animal_obj

# using pass statement inside the class: normally classes must not be empty, thus, using pass statement it can be empty and reuse later
class empty_class:
    pass