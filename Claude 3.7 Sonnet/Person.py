class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
```

In this implementation:

1. The `__init__` method is the constructor method that initializes the `name` and `age` attributes when creating a new `Person` object.
2. The `display_info` method is an instance method that prints the person's name and age using the `print` function and string formatting (`f-strings`).

Here's an example of how you can use this class:

```python
# Create a Person object
person1 = Person("Alice", 25)

# Call the display_info method
person1.display_info()  # Output: Name: Alice, Age: 25
```

You can also create multiple `Person` objects and call their methods:

```python
# Create more Person objects
person2 = Person("Bob", 30)
person3 = Person("Charlie", 35)

# Call the display_info method for each object
person2.display_info()  # Output: Name: Bob, Age: 30
person3.display_info()  # Output: Name: Charlie, Age: 35