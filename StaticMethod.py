class Book:

    staticVariable = "songOfIceAndFire"

print(Book.staticVariable)

instance = Book()
print(instance.staticVariable)

instance.staticVariable = "LordOfRing"

print(instance.staticVariable)
print(Book.staticVariable)
