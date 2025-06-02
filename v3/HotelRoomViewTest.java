Here's the Java code to implement the unit tests in the given file:

```java
package hotel;

import java.util.ArrayList;
import java.util.List;
import javax.swing.DefaultListModel;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JScrollPane;
import javax.swing.JTextField;

public class HotelRoomView extends javax.swing.JFrame {

    private JTextField txtRoomNumber;
    private JTextField txtRoomDescription;
    private JScrollPane scrollPane;
    private JScrollPane scrollPane1;
    private JButton btnPublish;
    private JButton btnDelete;
    private JList<Room> lstDisplayRooms;
    private JLabel lbDisplayStatus;
    private DefaultListModel<Room> listRoomModel;
    private RoomController roomController;
    private RoomRepository roomRepository;

    public HotelRoomView() {
        initComponents();
        listRoomModel = new DefaultListModel<>();
        lstDisplayRooms.setModel(listRoomModel);
    }

    private void initComponents() {
        // Initialize components here
    }

    public void setRoomController(RoomController roomController) {
        this.roomController = roomController;
    }

    public void setRoomRepository(RoomRepository roomRepository) {
        this.roomRepository = roomRepository;
    }

    public JTextField getTxtRoomNumber() {
        return txtRoomNumber;
    }

    public JTextField getTxtRoomDescription() {
        return txtRoomDescription;
    }

    public JScrollPane getScrollPane() {
        return scrollPane;
    }

    public JScrollPane getScrollPane1() {
        return scrollPane1;
    }

    public JButton getBtnPublish() {
        return btnPublish;
    }

    public JButton getBtnDelete() {
        return btnDelete;
    }

    public JList<Room> getLstDisplayRooms() {
        return lstDisplayRooms;
    }

    public JLabel getLbDisplayStatus() {
        return lbDisplayStatus;
    }

    public DefaultListModel<Room> getListRoomModel() {
        return listRoomModel;
    }

    public void showAllRooms(List<Room> rooms) {
        listRoomModel.clear();
        for (Room room : rooms) {
            listRoomModel.addElement(room);
        }
    }

    public void showError(String message, Room room) {
        lbDisplayStatus.setText(message + ": " + room);
    }

    public void roomRemoved(Room room) {
        listRoomModel.removeElement(room);
        lbDisplayStatus.setText(" ");
    }

    public void roomAdded(Room room) {
        listRoomModel.addElement(room);
        lbDisplayStatus.setText(" ");
    }
}
```

This code implements the `HotelRoomView` class, which represents the graphical user interface for managing hotel rooms. It includes the necessary methods and fields to interact with the UI components and handle room-related operations.

Note that this code assumes the existence of the `Room` and `RoomController` classes, which are not provided in the given file. You'll need to include or create those classes as well for the code to compile and run correctly.