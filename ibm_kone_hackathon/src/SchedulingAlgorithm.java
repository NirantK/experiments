import java.util.List;

/**
 * Created by jainpj on 18/02/17.
 */
public interface SchedulingAlgorithm {

    int assignLiftToPassenger(Passenger passenger, List<Elevator> elevatorList, DiscreteSimulation currentSimulation);
    int getDirectionOfLift(List<Elevator> elevatorList, Elevator elevator, DiscreteSimulation currentSimulation);
    void optimizeLiftPosition(List<Elevator> elevatorList, DiscreteSimulation currentSimulation);

}
