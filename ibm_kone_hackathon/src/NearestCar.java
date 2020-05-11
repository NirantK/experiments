import java.util.List;

/**
 * Created by roycharu on 2/18/17.
 */
public class NearestCar implements SchedulingAlgorithm {

    @Override
    public int assignLiftToPassenger(Passenger passenger, List<Elevator> elevatorList, DiscreteSimulation currentSimulation) {
        double minimum = Double.MAX_VALUE;
        for(Elevator elevator: elevatorList){
            double difference = passenger.getStartFloor() - elevator.getPosition();
            if (minimum < difference){
                minimum = difference;
                String elevatorID = elevator.getElevatorID();
                passenger.setElevatorID(elevatorID);
            }
        }
        return 0;
    }

    @Override
    public int getDirectionOfLift(List<Elevator> elevatorList, Elevator elevator,  DiscreteSimulation currentSimulation) {


        return 0;
    }

    @Override
    public void optimizeLiftPosition(final List<Elevator> elevatorList, final DiscreteSimulation currentSimulation) {

    }
}
