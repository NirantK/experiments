import java.util.ArrayList;
import java.util.List;

/**
 * Created by jainpj on 19/02/17.
 */
public class KoneHackUtils {

    public static void addPassengerToLift(Elevator elevator, Passenger passenger){
        List<Floor> floorList = elevator.getFloorsGoToList();
        int j = 0;
        while(j < floorList.size() && floorList.get(j).getFloorNumber() < passenger.getStartFloor()){
            j++;
        }
        if(j >= floorList.size()){
            Floor floor = new Floor(passenger.getStartFloor());
//            floor.setFloorNumber();
//            floor.setIncomingPassengerList();
            floor.addPassengerToFloor(passenger);
            elevator.getFloorsGoToList().add(floor);
        }else if(floorList.get(j).getFloorNumber() == passenger.getStartFloor()){
            floorList.get(j).getIncomingPassengerList().add(passenger);
        }else if(floorList.get(j).getFloorNumber() > passenger.getStartFloor()){
            Floor floor = new Floor(passenger.getStartFloor());
            floor.addPassengerToFloor(passenger);
//            floor.setFloorNumber(passenger.getStartFloor());
//            floor.setIncomingPassengerList(new ArrayList<>());
//            floor.setIncomingPassengerList().add(passenger);
            elevator.getFloorsGoToList().add(j, floor);
        }
    }
}
