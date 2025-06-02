To implement the unit tests in the provided file, we need to create a `Room` class in the `hotel` package. Here's an example implementation of the `Room` class that satisfies the requirements of the unit tests:

```java
package hotel;

import java.util.Objects;

public class Room {
    private final String id;
    private final String description;

    public Room(String id, String description) {
        this.id = id;
        this.description = description;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Room room = (Room) o;
        return Objects.equals(id, room.id) && Objects.equals(description, room.description);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, description);
    }

    @Override
    public String toString() {
        return "Room{" +
                "id='" + id + '\'' +
                ", description='" + description + '\'' +
                '}';
    }
}
```

In this implementation, we have the following:

1. `Room` class with two fields: `id` and `description`.
2. A constructor that takes `id` and `description` as parameters and initializes the corresponding fields.
3. An implementation of the `equals` method that compares the `id` and `description` fields of two `Room` objects for equality.
4. An implementation of the `hashCode` method that calculates a hash code based on the `id` and `description` fields.
5. An implementation of the `toString` method that returns a string representation of the `Room` object.

With this `Room` class implementation, the provided unit tests should pass without any modifications.

Note: The `Objects` class from the `java.util` package is used to provide null-safe implementations of the `equals` and `hashCode` methods.