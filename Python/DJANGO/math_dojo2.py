class MathDojo(object):
    def __init__(self):
        self.total = 0

    def add(self, *args):
        # unpack args
        for arg in args:
            if type(arg) ==list or type(arg) == tuple:
                for value in arg:
                   self.total += value
            else:
                self.total += arg
        return self

    def subtract(self, *args):
        for arg in args:
            if type(arg) == list or type(arg) == tuple:
                for value in arg:
                    self.total -= value
            else:
                self.total -= arg
        return self

    def results(self):
        print self.total
    
md = MathDojo()
md.add(1,2,3).results

