package foo.bar.dataObjects;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by jainpj on 18/02/17.
 */
public class Elevator {

    private double position; //

    public String elevatorID;
    private int direction;
    private int waitingFor; //

    public int capacity; //input

    private List<Passenger> onboardedPassengerList;
    private List<Floor> floorsGoToList;

    public List<Floor> getFloorsGoToList() {
        return floorsGoToList;
    }

    public void setFloorsGoToList(final List<Floor> floorsGoToList) {
        this.floorsGoToList = floorsGoToList;
    }

    public String getElevatorID() {
        return elevatorID;
    }

    public void setElevatorID(String elevatorID) {
        this.elevatorID = elevatorID;
    }

    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }

    public Elevator(double position) {
        floorsGoToList = new ArrayList<>();
        onboardedPassengerList = new ArrayList<>();
        this.position = position;

    }

    public List<Passenger> getOnboardedPassengerList() {
        return onboardedPassengerList;
    }

    public void setOnboardedPassengerList(final List<Passenger> onboardedPassengerList) {
        this.onboardedPassengerList = onboardedPassengerList;
    }

    public double getPosition() {
        return position;
    }

    public void setPosition(final double position) {
        this.position = position;
    }

    public int getDirection() {
        return direction;
    }

    public void setDirection(final int direction) {
        this.direction = direction;
    }

    public int getWaitingFor() {
        return waitingFor;
    }

    public void setWaitingFor(final int waitingFor) {
        this.waitingFor = waitingFor;
    }

    @Override
    public String toString() {
        return elevatorID;
    }
}
