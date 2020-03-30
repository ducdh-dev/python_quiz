class MethodTypes:
    name = "Ragnar"

    # This method can only be called if the class has been instantiated
    # An instance method is capable of creating, getting and setting new instance attributes and calling other instance,
    # class and static methods
    def instance_method(self):
        # Creates an instance atribute through keyword self
        self.last_name = "Lothbrock"
        print(self.name)
        print(self.last_name)

    # They can be called without having an instance of the class
    # The difference relies on the capability to access other methods and class attributes but no instance attributes
    @classmethod
    def class_method(cls):
        # Access a class atribute through keyword cls
        cls.name = "Lagertha"
        print(cls.name)
        print(cls.static_method())

    # You probably won’t need an specific instance to call that method so you could use a static method.
    @staticmethod
    def static_method():
        print("This is a static method")


# Creates an instance of the class
m = MethodTypes()
# Calls instance method
m.instance_method()

MethodTypes.class_method()
MethodTypes.static_method()
