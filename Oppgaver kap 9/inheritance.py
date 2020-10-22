class Mammal:
    def __init__(self):
        pass

    def info(self):
        return 'I have hair on my body '

    def identity_mammal(self):
        print('I am a mammal ')


class Primate(Mammal):
    def info(self):
        return super().info() + 'I have a large brain '

    def identity_primate(self):
        print('I am a primate')

class Human(Primate):
    def info(self):
        return super().info() + 'I am the smartest animal '

    def identity_human(self):
        print('I am a human ')

class Ape(Primate):
    def info(self):
        return super().info() + 'I have thumbs '

    def identity_ape(self):
        print('I am a ape ')

John = Human()
Julius = Ape()

"""
print(f'Info: John: {John.info()} Julius: {Julius.info()}')
John.identity_human(); Julius.identity_human()
John.identity_mammal(); Julius.identity_mammal()
John.identity_primate(); Julius.identity_primate()
John.identity_ape(); Julius.identity_ape()
"""

instances = [Mammal, Primate, Human, Ape]

for i in instances:
    print(f'{i}, John: {isinstance(John, i)} Julius: {isinstance(Julius, i)}')
