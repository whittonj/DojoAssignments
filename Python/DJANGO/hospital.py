from datetime import datetime
class Patient(object):
    num_pat = 0
    def __init__(self,pat_name, pat_allergies,):
        self.id = Patient.num_pat
        self.pat_name = pat_name
        self.pat_allergies = pat_allergies
        self.pat_bed = 0
        Patient.num_pat += 1

    def display(self):
        print self.id
        print self.pat_name
        print self.pat_allergies
        print self.pat_bed
        return self

class Hospital(object):
    def __init__(self, name, cap):
        self.patients = []
        self.name = name
        self.capacity = cap
        self.beds = self.initialize_beds()
    def initialize_beds(self):
        beds = []
        for i in range (1, self.capacity+1):
            beds.append({
                "bed_id": i,
                "Available": True
            })
        return beds
    def admit(self,new_pat):
        print "Patients:", len(self.patients)
        print "Beds: ", len(self.beds)
        print "admitting: ", new_pat.pat_name
        if len(self.patients) >= len(self.beds):
            print "All beds full"
        else:
            for q in range (0, len(self.beds)):
                if self.beds[q]["Available"] == True:
                    new_pat.pat_bed = self.beds[q]["bed_id"]
                    self.beds[q]["Available"] = False
                    print "Patient in bed: ", self.beds[q]["bed_id"]
                    self.patients.append(new_pat)
                    break

    
    def discharge(self,dis_pat):
        #remove a patent add bed back jsut liek add but work off patient"ID" to figure out what bed to free up
        print self.name
    def info(self):
        print self.name
        print "-------------------------------------"
        for patient in self.patients:
            print patient.pat_name, " | Room: ", patient.pat_bed


c1 = Patient('Jeff Whitton', "food")
c2 = Patient('Jerry Herd', "drugs")
c3 = Patient('Harry Hood', "drugs")
c4 = Patient('Mary Nerd', "drugs")
c5 = Patient('Dairy Herd', "drugs")
c6 = Patient('Hon Doe', "drugs")
c7 = Patient('Mancy', "drugs")
c8 = Patient('Lichtenstein Mcdaverd', "drugs")

c1.display()

ER = Hospital('The Emergency Room', 5)
ER.admit(c1)
ER.admit(c2)
ER.admit(c3)
ER.admit(c4)
ER.admit(c5)
ER.admit(c6)
ER.admit(c7)
ER.admit(c8)
ER.info()







