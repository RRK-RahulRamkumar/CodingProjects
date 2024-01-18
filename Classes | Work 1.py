class employee:
    def __init__(self, name, staffno):
        self.name = name
        self.staffno = staffno
        self.fullTimeStaff = True

    def showDetails(self):
        print(f"Employee name : {self.name}")
        print(f"Employee number: {self.staffno}")
    
class partTime(employee):
    def __init__(self, name, staffno):
        super().__init__(name, staffno)
        self.fullTimeStaff = False
        self.hoursWorked = 0

    
    def getHoursWorked(self):
        return self.hoursWorked
    

class fullTime(employee):
    def __init__(self, name, staffno):
        super().__init__(name, staffno)
        self.fullTimeStaff = True
        self.yearlySalary = 0

    def getYearlySalary(self):
        return self.yearlySalary
    
permanentStaff = fullTime("Eric Jones", 72)
permanentStaff.showDetails()
temporaryStaff = partTime("Alice Hue", 1017)
temporaryStaff.showDetails()

# When using super() use __init__(), when using classname, use __init__(self)