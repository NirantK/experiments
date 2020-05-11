package foo.bar.utils;

import java.util.ArrayList;
import java.util.List;

import foo.bar.dataObjects.*;

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
            Floor floor = new Floor();
            floor.setFloorNumber(passenger.getStartFloor());
            floor.setIncomingPassengerList(new ArrayList<>());
            floor.getIncomingPassengerList().add(passenger);
            elevator.getFloorsGoToList().add(floor);
        }else if(floorList.get(j).getFloorNumber() == passenger.getStartFloor()){
            floorList.get(j).getIncomingPassengerList().add(passenger);
        }else if(floorList.get(j).getFloorNumber() > passenger.getStartFloor()){
            Floor floor = new Floor();
            floor.setFloorNumber(passenger.getStartFloor());
            floor.setIncomingPassengerList(new ArrayList<>());
            floor.getIncomingPassengerList().add(passenger);
            elevator.getFloorsGoToList().add(j, floor);
        }
    }
}
