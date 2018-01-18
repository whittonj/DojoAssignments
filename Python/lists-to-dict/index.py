name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
  new_dict = zip(name,favorite_animal)
  return new_dict

print make_dict(name,favorite_animal)

#to do by length do an if conditional by len(list1) vs len(list2) zip in the order by longest