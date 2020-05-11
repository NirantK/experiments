import java.util.ArrayList;
import java.util.List;

/**
 * Created by jainpj on 19/02/17.
 */
public class Floor {


    private int floorNumber;
    private List<Passenger> incomingPassengerList;

    public Floor (int floorNumber){
        this.setFloorNumber(floorNumber);
        this.incomingPassengerList = new ArrayList<>();
    }
    public int getFloorNumber() {
        return floorNumber;
    }

    public void setFloorNumber(final int floorNumber) {
        this.floorNumber = floorNumber;
    }

    public List<Passenger> getIncomingPassengerList() {
        return incomingPassengerList;
    }

    public void addPassengerToFloor(Passenger passenger){
        this.incomingPassengerList.add(passenger);
    }
    public void setIncomingPassengerList(final List<Passenger> incomingPassengerList) {
        this.incomingPassengerList = incomingPassengerList;
    }
}
