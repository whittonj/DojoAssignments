from datetime import datetime
class Call(object):
    num_calls = 0
    def __init__(self,caller_name, caller_phone, call_time, reason):
        self.id = Call.num_calls
        self.caller_name = caller_name
        self.caller_phone = caller_phone
        self.call_time = datetime.now()
        self.reason = reason
        Call.num_calls += 1

    def display(self):
        print self.id
        print self.caller_name
        print self.caller_phone
        print self.call_time
        print self.reason
class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = len(self.calls)
    def add(self,new_call):
        self.calls.append(new_call)
    def remove(self,rem_call):
        self.calls.remove(rem_call)
    def info(self):
            print self.calls
        # all names in queue print names, phones and count them

c1 = Call('Jeff Whitton', 2066229840, "1PM", "I like calling people")
c2 = Call('Jack Herioc', 2061111111, "2PM", "I am sick")

queue_one = CallCenter()
queue_one.add(c1)
queue_one.add(c2)
queue_one.info()







