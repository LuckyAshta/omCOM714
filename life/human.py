class Human:
    #class attributes - each is a constant
    MAX_ENERGY = 100
    MOVE_ENERGY = 10
    REPRODUCE_ENERGY = 20
    # initialise the state of the instance
    def __init__(self, name: str, age: int = 0, energy: int = 100) -> None:
        # instance attributes/variables
        self.name = name
        self.age = age
        self.energy = energy

    def __repr__(self) -> str:
        return f'human(name={self.name}, age={self.age}, energy={self.energy})'

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old and has an energy level {self.energy}.'

    def eat(self, amount) -> int:
        potential_energy = self.energy + amount

        if (potential_energy >= Human.MAX_ENERGY):
            self.energy = Human.MAX_ENERGY
            return (potential_energy - Human.MAX_ENERGY)
        else:
            self.energy = potential_energy
            return self.energy - Human.MAX_ENERGY

    def grow(self) -> None:
        self.age = self.age + 1

    def move(self, distance: int) -> bool:
        potential_energy = self.energy - distance

        if (potential_energy >= Human.MOVE_ENERGY):
            self.energy = potential_energy
            return True
        else:
            return False

    def reproduce(self) -> bool:
        potential_energy = self.energy - Human.REPRODUCE_ENERGY

        if (potential_energy >= Human.REPRODUCE_ENERGY):
            self.energy = potential_energy
            return True
        else:
            return False