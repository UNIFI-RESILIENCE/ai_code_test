Here's the Java code to implement the unit tests in the provided file:

```java
package hotel;

import java.util.ArrayList;
import java.util.List;

public class RoomControllerTest {

    private RoomRepository roomRepository;
    private RoomView roomView;
    private RoomController roomController;

    @Before
    public void setup() {
        roomRepository = Mockito.mock(RoomRepository.class);
        roomView = Mockito.mock(RoomView.class);
        roomController = new RoomController(roomRepository, roomView);
    }

    @Test
    public void testAllRooms() {
        List<Room> rooms = new ArrayList<>();
        rooms.add(new Room());
        Mockito.when(roomRepository.findAll()).thenReturn(rooms);

        roomController.allRooms();

        Mockito.verify(roomView).showAllRooms(rooms);
    }

    @Test
    public void testNewRoomWhenRoomDoesNotAlreadyExist() {
        Room room = new Room("1", "test");
        Mockito.when(roomRepository.findById("1")).thenReturn(null);

        roomController.newRoom(room);

        InOrder inOrder = Mockito.inOrder(roomRepository, roomView);
        inOrder.verify(roomRepository).save(room);
        inOrder.verify(roomView).roomAdded(room);
    }

    @Test
    public void testNewRoomWhenRoomAlreadyExists() {
        Room roomToAdd = new Room("1", "test");
        Room existingRoom = new Room("1", "name");
        Mockito.when(roomRepository.findById("1")).thenReturn(existingRoom);

        roomController.newRoom(roomToAdd);

        Mockito.verify(roomView).showError("Room already exist 1", roomToAdd);
        Mockito.verifyNoMoreInteractions(Mockito.ignoreStubs(roomRepository));
    }

    @Test
    public void testDeleteRoomWhenRoomExists() {
        Room roomToDelete = new Room("1", "test");
        Mockito.when(roomRepository.findById("1")).thenReturn(roomToDelete);

        roomController.deleteRoom(roomToDelete);

        InOrder inOrder = Mockito.inOrder(roomRepository, roomView);
        inOrder.verify(roomRepository).delete("1");
        inOrder.verify(roomView).roomRemoved(roomToDelete);
    }

    @Test
    public void testdeleteRoomWhenRoomDoesNotExist() {
        Room room = new Room("1", "test");
        Mockito.when(roomRepository.findById("1")).thenReturn(null);

        roomController.deleteRoom(room);

        Mockito.verify(roomView).showError("Room not found 1", room);
        Mockito.verifyNoMoreInteractions(Mockito.ignoreStubs(roomRepository));
    }
}
```

In this implementation, we're using the Mockito library for creating mock objects and setting up the expectations and verifications for the test cases.

Here's a breakdown of the code:

1. In the `setup` method, we create mock objects for `RoomRepository` and `RoomView` using `Mockito.mock(Class)`. We also create an instance of `RoomController` by passing these mock objects as dependencies.

2. In the `testAllRooms` method, we create a list of rooms and set up the expectation that when `roomRepository.findAll()` is called, it should return this list of rooms. We then call `roomController.allRooms()` and verify that `roomView.showAllRooms(rooms)` is called with the expected list of rooms.

3. In the `testNewRoomWhenRoomDoesNotAlreadyExist` method, we create a new `Room` object and set up the expectation that when `roomRepository.findById("1")` is called, it should return `null`. We then call `roomController.newRoom(room)` and verify that `roomRepository.save(room