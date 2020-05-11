
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Created by jainpj on 18/02/17.
 */
public class DiscreteSimulation {

    int currentTime;
    int timeBetweenFloors;
    int waitTimeOnFloor;
    int passengerCounter;
    List<Elevator> elevatorList;
    SchedulingAlgorithm scheduler;
    int meanWaitingTime;
    int maxFloor;
    public final Queue<Passenger> hallCallQueue = new LinkedList<Passenger>();


    public DiscreteSimulation(List<Elevator> elevatorList, int waitTimeOnFloor, int timeBetweenFloors, SchedulingAlgorithm scheduler, int maxFloor){
        this.elevatorList = elevatorList;
        currentTime = 0;
        passengerCounter = 0;
        this.waitTimeOnFloor = waitTimeOnFloor;
        this.timeBetweenFloors = timeBetweenFloors;
        this.scheduler = scheduler;
        this.maxFloor = maxFloor;
    }

    public void runSimulation(final List<Passenger> passengerEntryList){
        Passenger processingPassenger;
        while(true){
            if(currentTime > 3000){break;}
            while(passengerCounter < passengerEntryList.size() && currentTime == passengerEntryList.get(passengerCounter).getStartTime()){
                processingPassenger = passengerEntryList.get(passengerCounter);
                scheduler.assignLiftToPassenger(processingPassenger, elevatorList, this); // We call implementation
                passengerCounter++;
            }
            updateElevatorsState(currentTime);
            System.out.println("Simulation done for time: " + currentTime);
            scheduler.optimizeLiftPosition(elevatorList, this);
            currentTime++;
        }
    }

    private void updateElevatorsState(int currentTime){
        for(Elevator elevator : this.elevatorList){
            if(elevator.getWaitingFor() >= 0){
                elevator.setWaitingFor(elevator.getWaitingFor() + 1);
                if(elevator.getWaitingFor() > waitTimeOnFloor) {
                    elevator.setWaitingFor(-1);
                }
                if(elevator.getWaitingFor() == waitTimeOnFloor) {
                    if(elevator.getOnboardedPassengerList().size() == elevator.getCapacity()){
                        for(Passenger passenger : elevator.getFloorsGoToList().get(0).getIncomingPassengerList()){
                            scheduler.assignLiftToPassenger(passenger, elevatorList, this);
                        }
                        elevator.getFloorsGoToList().remove(0);
                        elevator.setDirection(scheduler.getDirectionOfLift(elevatorList, elevator, this));
                    }
                }
            }else{
                int dir = scheduler.getDirectionOfLift(elevatorList, elevator, this);
                updatePosition(elevator, dir);
                if(elevator.getWaitingFor() == 0 ){
                    int c = 0;
                    List<Passenger> passengerList = elevator.getOnboardedPassengerList();
                    while(c < passengerList.size()){
                        if(passengerList.get(c).getEndFloor() == elevator.getPosition()){
                            passengerList.get(c).setEndTime(currentTime);
                            passengerList.remove(c);
                            System.out.println("I've reached here!");
                        }else{
                            c++;
                        }
                    }
                    List<Floor> floorList = elevator.getFloorsGoToList();

                    passengerList = floorList.get(0).getIncomingPassengerList();
                    while(passengerList.size() > 0){
                        System.out.println("I never expected to be here!");
                        if(elevator.getOnboardedPassengerList().size() == elevator.getCapacity()){
                            break;
                        }
                        elevator.getOnboardedPassengerList().add(passengerList.get(0));
                        passengerList.remove(0);
                    }
                }
            }
        }
    }

    private void updatePosition(Elevator elevator, int direction){
        if(direction == 1){
            double newVal = elevator.getPosition() + (1.0/timeBetweenFloors);
            if(newVal >= maxFloor){
                System.out.println("Reset elevator position. Too high!");
                elevator.setPosition(maxFloor);
                elevator.setWaitingFor(0);
                return;
            }
            if(elevator.getOnboardedPassengerList().isEmpty()){
                elevator.setPosition(newVal);
                return;
            }
            if(newVal > Math.ceil(elevator.getPosition())){
                if(((int)Math.ceil(elevator.getPosition()) == elevator.getOnboardedPassengerList().get(0).getEndFloor())
                        || ((int)Math.ceil(elevator.getPosition()) == elevator.getFloorsGoToList().get(0).getFloorNumber())){
                    elevator.setPosition(Math.ceil(elevator.getPosition()));
                    elevator.setWaitingFor(0);
                }else{
                    elevator.setPosition(newVal);
                }
            } else{
                elevator.setPosition(newVal);
            }
        } else if(direction == -1){
            double newVal = elevator.getPosition() - (1.0/timeBetweenFloors);
            if(newVal <= 0){
                elevator.setPosition(0);
                elevator.setWaitingFor(0);
                return;
            }
            if(elevator.getOnboardedPassengerList().isEmpty()){
                elevator.setPosition(newVal);
                return;
            }
            if(newVal < Math.floor(elevator.getPosition())){
                if(((int)Math.floor(elevator.getPosition()) == elevator.getOnboardedPassengerList().get(0).getEndFloor())
                        || ((int)Math.floor(elevator.getPosition()) == elevator.getFloorsGoToList().get(0).getFloorNumber())){
                    elevator.setPosition(Math.floor(elevator.getPosition()));
                    elevator.setWaitingFor(0);
                }else{
                    elevator.setPosition(newVal);
                }
            } else{
                elevator.setPosition(newVal);
            }
        }
    }

    private void updateEndTime(List<Passenger> passengerList, int currentTime){

    }

    public void computeRelevantStats(List<Passenger> passengerList) {
        double averageWaitingTime = 0;
        double averageTravelTime = 0;
        double averageDistanceTravelled = 0;
        for(Passenger passenger: passengerList){
            int waitingTime = passenger.getEntryTime() - passenger.getStartTime();
            int travelTime =  passenger.getEndTime() - passenger.getEntryTime();
            System.out.println("Waiting time for this passenger: " + waitingTime);
            System.out.println("Travel time for this passenger: " + travelTime);
            averageTravelTime += travelTime;
            averageWaitingTime += waitingTime;
        }
        averageTravelTime /= passengerList.size();
        averageWaitingTime /= passengerList.size();
        System.out.println("Average waiting time: " + averageWaitingTime);
        System.out.println("Average travel time:  " + averageTravelTime);
    }
}
