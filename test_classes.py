from pet_classes import Cat

cats = []
cats.append(Cat(coat_length='long', age=2, sex='male', name='Sam'))
cats.append(Cat(coat_length='long', age=2, sex='male', name='Baron'))

for cat in cats:
    cat.info()
