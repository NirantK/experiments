/**
 * Created by jainpj on 18/02/17.
 */
public class Passenger {
    private int startFloor; //input
    private int endFloor; //input
    private int entryTime; //start of journey
    private int startTime; //time when person request elevator //input
    private int endTime;
    private int liftNumber;
    public int direction;

    public Passenger(int startFloor,int endFloor, int startTime){
        this.startFloor = startFloor;
        this.endFloor = endFloor;
        this.startTime = startTime;
        this.direction = startFloor < endFloor ? 1: -1;
    }

    public String getElevatorID() {
        return ElevatorID;
    }

    public void setElevatorID(String elevatorID) {
        ElevatorID = elevatorID;
    }

    private String ElevatorID;

    public String getPassengerId() {
        return passengerId;
    }

    public void setPassengerId(String passengerId) {
        this.passengerId = passengerId;
    }

    private String passengerId;

    public int getStartFloor() {
        return startFloor;
    }

    public void setStartFloor(final int startFloor) {
        this.startFloor = startFloor;
    }

    public int getEndFloor() {
        return endFloor;
    }

    public void setEndFloor(final int endFloor) {
        this.endFloor = endFloor;
    }

    public int getEntryTime() {
        return entryTime;
    }

    public void setEntryTime(final int entryTime) {
        this.entryTime = entryTime;
    }

    public int getStartTime() {
        return startTime;
    }

    public void setStartTime(final int startTime) {
        this.startTime = startTime;
    }

    public int getEndTime() {
        return endTime;
    }

    public void setEndTime(final int endTime) {
        this.endTime = endTime;
    }

    public int getLiftNumber() {
        return liftNumber;
    }

    public void setLiftNumber(final int liftNumber) {
        this.liftNumber = liftNumber;
    }

    public int getDirection() {
        return direction;
    }

}
