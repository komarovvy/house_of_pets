class Pet:
    def __init__(self, kind, age, sex, name):
        self.kind = kind
        self.age = age
        self.sex = sex
        self.name = name

    def info(self):
        print(f"{self.name}: {self.kind}, {self.age} years old, {self.sex}")


class Cat(Pet):
    kind = 'cat'

    def __init__(self, coat_length, age, sex, name):
        self.coat_len = coat_length
        self.age = age
        self.sex = sex
        self.name = name

if __name__ == '__main__':
    test_pet = Pet(kind='dog', age=5, sex='female', name='Rex')
    test_pet.info()
    test_cat = Cat(coat_length='long', age=2, sex='male', name='Sam')
    test_cat.info()