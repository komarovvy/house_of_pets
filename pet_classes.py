class Pet:
    def __init__(self, kind, age, sex, name):
        self.kind = kind
        self.age = age
        self.sex = sex
        self.name = name

    def info(self):
        print(f"{self.name}: {self.kind}, {self.age} years old, {self.sex}")


if __name__ == '__main__':
    test_pet = Pet(kind='dog', age=5, sex='male', name='Rex')
    test_pet.info()