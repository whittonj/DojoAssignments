class Bike(object):
    def __init__(self, price, max_speed,miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles
        
    def ride(self):
        self.miles = self.miles + 10
        return self

    def reverse(self):
        self.miles = self.miles -5
        return self

schwinn = Bike(100,20,5)
mongoose = Bike(200,100,0)
huffy = Bike(10,10,10)

schwinn.displayInfo()
schwinn.ride()
schwinn.ride()
schwinn.ride()
schwinn.reverse()
schwinn.displayInfo()

huffy.reverse()
huffy.reverse()
huffy.reverse()
huffy.displayInfo()


