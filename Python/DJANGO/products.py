class Product(object):
    def __init__(self, price, item_name,weight, brand, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
        self.tax =.10
        
        self.displayInfo()

    def displayInfo(self):
        print self
        print self.item_name
        print "$", self.price
        print self.weight, "lbs"
        print self.brand
        print self.status
        print self.tax, "%"
        
    def gettax(self):
        cost_with_tax = (self.tax + 1) * self.price
        print "total with tax $", cost_with_tax 
        return self
    def sale(self):
        self.status = "sold"
        print "SOLD"
        return self

    def returny(self):
        self.status = "used"
        print "RETURNED"
        self.price = self.price * .8
        return self

Napkin = Product(10000, "Napkin", 5000, "Housey", "nfs")

Napkin.gettax()
Napkin.sale()
Napkin.displayInfo()
Napkin.returny()
Napkin.displayInfo()


