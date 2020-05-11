import java.util.ArrayList;
import java.util.List;

/**
 * Created by saumaury on 2/18/17.
 */
public class RoundRobin implements SchedulingAlgorithm {
    int pivot;

    public RoundRobin(){
        pivot = 0;
    }

    @Override
    public int assignLiftToPassenger(Passenger passenger, List<Elevator> elevatorList, DiscreteSimulation currentSimulation) {
        boolean isLiftAssigned = false;
        for(int i = 0;i < elevatorList.size();i++){
            pivot = (pivot + 1)%elevatorList.size();// todo: changed without prateek
            if(elevatorList.get(pivot).getDirection() == passenger.getDirection()){
                Elevator elevator = elevatorList.get(pivot);
                KoneHackUtils.addPassengerToLift(elevator, passenger);
                isLiftAssigned = true;
                break;
            }
        }
        if(!isLiftAssigned){
            System.out.println("I have not been assigned a lift!");
            currentSimulation.hallCallQueue.add(passenger);

            KoneHackUtils.addPassengerToLift(elevatorList.get(pivot),passenger);
            pivot = (pivot + 1)%elevatorList.size();
        }
        return 0;
    }

    @Override
    public int getDirectionOfLift(List<Elevator> elevatorList, Elevator elevator, DiscreteSimulation currentSimulation) {
        if( elevator.getPosition() >= currentSimulation.maxFloor){
            elevator.setDirection(-1);
        } else if(Math.abs(elevator.getPosition()) <= Double.MIN_VALUE ){
            elevator.setDirection(1);
        }
        return elevator.getDirection();
    }

    @Override
    public void optimizeLiftPosition(final List<Elevator> elevatorList, final DiscreteSimulation currentSimulation) {

    }
}
