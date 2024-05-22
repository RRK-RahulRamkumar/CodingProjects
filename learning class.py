class ClassName:
    def __init__(self, Parameter1, Parameter2):
        self.para1 = Parameter1
        self.__para2 = Parameter2 # self.__para2 is a private attribute

        # Attributes dont have to be always given a value by the user
        self.testvalue = "parent class text"


    def MethodName(self, MethodPara1, MethodPara2):
        print(f"Para1 was {self.para1}")
        print(f"Para2 was {self.__para2}")
        self.para1 = MethodPara1
        self.__para2 = MethodPara2
        print(f"Para1 now is {self.para1}")
        print(f"Para2 now is {self.__para2}")

class OtherClass(ClassName):
    def __init__(self, Parameter1, Parameter2, ChildClassParameter):
        self.ChildClassPara = ChildClassParameter
        super().__init__(Parameter1, Parameter2)

        # The child class must have the same parameters used in the parentclass for both def __init__() and super().__init__()

    def MethodName(self): # Polymorphism, same function name but changed its "functionality"
        # Look how i changed the value for testvalue from the parent class
        print(f"test value was {self.testvalue}")
        self.testvalue = "child class here"
        print(f"test value now {self.testvalue}")


# ObjectName = ClassName("Argument1", "Argument2")
# ObjectName.MethodName("ChangePara1", "ChangePara2")

ChildClassObjectName = OtherClass("Argument1", "Argument2", "ChildClassArgument")
ChildClassObjectName.MethodName()
