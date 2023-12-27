# Inheriatnce class practice

# Parent or base class 
class animal:
    def __init__(self, name, color, category):
        self.name = name
        self.color = color 
        self.category = category 


    def charecteristics(self):
        print("This animal is from Unknown Cataegory\n")

    def __str__(self):
        return f"Name: {self.name} \nColor: {self.color} \nCategory: {self.category} \nAnimal Facts:"
    
    """ def show(self):
            print(f"Name: {self.name}, \nColor: {self.color} \nCategory: {self.category} \nAnimal Facts:")
    """  
    

# child, derived or sub classes
class mammals(animal): # inherited the animal class
    def charecteristics(self):
      print("Mammals are characterized by the presence of milk-producing mammary glands for feeding their young\n")

class birds(animal):
     def charecteristics(self):
        print("Birds are characterised by feathers, toothless beaked jaws, the laying of hard-shelled eggs, a high metabolic rate, a four-chambered heart, and a strong yet lightweight skeleton.\n")
       
class fish(animal):
     def charecteristics(self):
        print("Fish or fishes is an aquatic, craniate, gill-bearing animal that lacks limbs with digits. \n")
       
class reptiles(animal):
     def __init__(self, name, color, category, size):
         super().__init__(name, color, category)
         self.size = size
   
     def show(self):
            print(f"Name: {self.name}, \nColor: {self.color} \nCategory: {self.category} \nSize: {self.size} \nAnimal Facts:")
  
     def charecteristics(self):
         print("Reptiles, as commonly defined, are a group of tetrapods with an ectothermic metabolism and amniotic development.\n")
        

# calling the classes and creating objects 
           
animal_obj = animal("Lion","Red", "Mammals")
#animal_obj.show()
print(animal_obj)
animal_obj.charecteristics()


mammals_obj = mammals("Tiger","Blue", "Mammals")
#mammals_obj.show()
print(mammals_obj)
mammals_obj.charecteristics()


birds_obj = birds("Lion","Red", "birds")
#birds_obj.show()
print(birds_obj)
birds_obj.charecteristics()

fish_obj = fish("Grouper","Yellow gold", "fish")
#fish_obj.show()
print(fish_obj)
fish_obj.charecteristics()

reptiles_obj = reptiles("Snake","Green", "reptiles", 12)
reptiles_obj.show()
#print(reptiles_obj)
reptiles_obj.charecteristics()
