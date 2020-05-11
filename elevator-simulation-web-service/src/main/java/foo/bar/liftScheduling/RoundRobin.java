package foo.bar.liftScheduling;

import java.util.List;

import org.springframework.stereotype.Component;
import foo.bar.dataObjects.*;
import foo.bar.simulation.DiscreteSimulation;
import foo.bar.utils.KoneHackUtils;

/**
 * Created by saumaury on 2/18/17.
 */
@Component("roundRobin")
public class RoundRobin implements SchedulingAlgorithm {
    int pivot;

    public RoundRobin(){
        pivot = 0;
    }

    @Override
    public int assignLiftToPassenger(Passenger passenger, List<Elevator> elevatorList, DiscreteSimulation currentSimulation) {
        for(int i = 0;i < elevatorList.size();i++){
            pivot = (pivot + i)%currentSimulation.getMaxFloor();
            if(elevatorList.get(pivot).getDirection() == passenger.getDirection()){
                Elevator elevator = elevatorList.get(pivot);
                KoneHackUtils.addPassengerToLift(elevator, passenger);
            }
        }
        return 0;
    }

    @Override
    public int getDirectionOfLift(List<Elevator> elevatorList, Elevator elevator, DiscreteSimulation currentSimulation) {
        if(elevator.getPosition() == currentSimulation.getMaxFloor()){
            elevator.setDirection(-1);
        } else if(elevator.getPosition() == 0){
            elevator.setDirection(1);
        }
        return elevator.getDirection();
    }

    @Override
    public void optimizeLiftPosition(final List<Elevator> elevatorList, final DiscreteSimulation currentSimulation) {

    }
}
