class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health =150
    def walk(self):
        self.health = self.health - 1
        print "walking"
        return self
    def run(self):
        self.health = self.health -5
        print "running"
        return self
    def display(self):
        print self.health
        return self
class Dog(Animal):
    def pet(self):
        self.health = self.health + 5
        return self
class Dragon(Animal):
    def __init__(self):
        self.health = 170
    def fly(self):
        self.health = self.health -10
        return self
    def display(self):
        super(Dragon, self).display()
        print "I'm a dragon!"

d= Dog("Dog")
d.walk()
d.walk()
d.walk()
d.run()
d.run()
d.display()

z=Dragon()
z.display()
z.fly()
z.fly()
z.fly()
z.fly()
z.display()

 #   def display(self):
 #       super(Dragon,self).__init__(self)
 #       print "I am a dragon!"
  #      return self
  #    self.health = 170