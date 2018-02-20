class MathDojo(object):
    def __init__(self):
        self.total = 0
    
    def add(self, *args):
        for arg in args:
            if type(arg) == list or type(arg) == tuple:
                for value in arg:
                    self.total += value
                    print self.total
            else:
                self.total += arg
                print self.total
        return self

    def sub(self, *args):
        for arg in args:
            if type(arg) == list or type(arg) == tuple:
                for value in arg:
                    self.total -= value
                    print self.total
            else:
                self.total -= arg
                print self.total
        return self

    def res(self):
        print "TOTAL: ", self.total

mad = MathDojo()
mad.add(1,2,3,4,5,6).add(45,3,3.66).sub(1000).res()


