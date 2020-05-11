package foo.bar.dataObjects;

import org.springframework.web.multipart.MultipartFile;

/**
 * Created by jainpj on 18/02/17.
 */
public class SimulateAlgoRequest {

    private MultipartFile file;
    private int maxFloors;
    private int liftSpeed;
    private int liftWaitingTimeOnFloor;
    private String algorithmName;
    private int noOfElevators;

    public MultipartFile getFile() {
        return file;
    }

    public void setFile(final MultipartFile file) {
        this.file = file;
    }

    public int getMaxFloors() {
        return maxFloors;
    }

    public void setMaxFloors(final int maxFloors) {
        this.maxFloors = maxFloors;
    }

    public int getLiftSpeed() {
        return liftSpeed;
    }

    public void setLiftSpeed(final int liftSpeed) {
        this.liftSpeed = liftSpeed;
    }

    public int getLiftWaitingTimeOnFloor() {
        return liftWaitingTimeOnFloor;
    }

    public void setLiftWaitingTimeOnFloor(final int liftWaitingTimeOnFloor) {
        this.liftWaitingTimeOnFloor = liftWaitingTimeOnFloor;
    }

    public String getAlgorithmName() {
        return algorithmName;
    }

    public void setAlgorithmName(final String algorithmName) {
        this.algorithmName = algorithmName;
    }

    public int getNoOfElevators() {
        return noOfElevators;
    }

    public void setNoOfElevators(final int noOfElevators) {
        this.noOfElevators = noOfElevators;
    }
}
