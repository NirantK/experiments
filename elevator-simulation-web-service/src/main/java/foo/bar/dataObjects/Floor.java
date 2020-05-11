package foo.bar.dataObjects;

import java.util.List;

/**
 * Created by jainpj on 19/02/17.
 */
public class Floor {
    private int floorNumber;
    private List<Passenger> incomingPassengerList;

    public int getFloorNumber() {
        return floorNumber;
    }

    public void setFloorNumber(final int floorNumber) {
        this.floorNumber = floorNumber;
    }

    public List<Passenger> getIncomingPassengerList() {
        return incomingPassengerList;
    }

    public void setIncomingPassengerList(final List<Passenger> incomingPassengerList) {
        this.incomingPassengerList = incomingPassengerList;
    }
}
