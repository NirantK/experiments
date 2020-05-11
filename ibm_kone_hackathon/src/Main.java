import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        System.out.println("Hello World!");
        CSVReader csv1 = new CSVReader();
        List<Passenger> passengerList = csv1.readCsv("data/sample_data.csv");

        Elevator elevator1 = new Elevator(0);
        elevator1.capacity = 5;
        elevator1.elevatorID = "One";
        Elevator elevator2 = new Elevator(88);
        elevator2.setDirection(-1);
        elevator2.capacity = 5;
        elevator2.elevatorID = "Two";

        List<Elevator> elevatorList = new ArrayList<Elevator>();
        elevatorList.add(elevator1);
        elevatorList.add(elevator2);

        DiscreteSimulation discreteSimulation = new DiscreteSimulation(elevatorList, 5, 2, new RoundRobin(), 100);
        discreteSimulation.runSimulation(passengerList);
        discreteSimulation.computeRelevantStats(passengerList);

    }
}
