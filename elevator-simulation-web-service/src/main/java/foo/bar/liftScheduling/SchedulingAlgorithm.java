package foo.bar.liftScheduling;

import java.util.List;

import foo.bar.dataObjects.*;
import foo.bar.simulation.DiscreteSimulation;

/**
 * Created by jainpj on 18/02/17.
 */
public interface SchedulingAlgorithm {

    int assignLiftToPassenger(Passenger passenger, List<Elevator> elevatorList, DiscreteSimulation currentSimulation);
    int getDirectionOfLift(List<Elevator> elevatorList, Elevator elevator, DiscreteSimulation currentSimulation);
    void optimizeLiftPosition(List<Elevator> elevatorList, DiscreteSimulation currentSimulation);

}
