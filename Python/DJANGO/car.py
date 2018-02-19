class Car(object):
    def __init__(self, price, max_speed,fuel, miles, tax):
        self.price = price
        self.max_speed = max_speed
        self.fuel = fuel
        self.miles = miles
        self.tax = .12
        self.gettax()
        self.displayInfo()

    def displayInfo(self):
        print self
        print "$", self.price
        print self.max_speed, "mph"
        print self.fuel
        print self.miles, "mpg"
        print self.tax
        
    def gettax(self):
        if self.price>10000:
            self.tax =.15
        return self

buick = Car(10000,200,'half full',10,0)
Land_Rover = Car(50000,200,'half full',10,0)
PT = Car(1000,100,'full',10,0)
Big = Car(1000000,2010,'empty',100000,0)
Round = Car(10000,200,'half full',10,0)
Good = Car(10000,200,'half full',10,0)


