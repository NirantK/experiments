package foo.bar.controllers;

import java.util.ArrayList;
import java.util.List;

import javax.annotation.Resource;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.core.Response;

import org.springframework.web.multipart.MultipartFile;
import foo.bar.dataObjects.Elevator;
import foo.bar.dataObjects.Passenger;
import foo.bar.dataObjects.SimulateAlgoRequest;
import foo.bar.liftScheduling.NearestCar;
import foo.bar.liftScheduling.RoundRobin;
import foo.bar.liftScheduling.SchedulingAlgorithm;
import foo.bar.simulation.DiscreteSimulation;

/**
 * Created by jainpj on 18/02/17.
 */
@Path("/simulateAlgo")
public class HackServiceController {

    @Resource(name = "roundRobin")
    private RoundRobin roundRobin;

    @Resource(name = "nearestCar")
    private NearestCar nearestCar;

    @POST
    public Response simulateAlgo(SimulateAlgoRequest request){
        List<Elevator> elevatorList = new ArrayList<>();
        for(int i = 0;i<request.getNoOfElevators();i++) {
            Elevator elevator = new Elevator(0);
            elevatorList.add(elevator);
        }
        DiscreteSimulation discreteSimulation = new DiscreteSimulation(elevatorList, request.getLiftWaitingTimeOnFloor(),
                request.getLiftSpeed(), getSchedulingAlgorithm(request.getAlgorithmName()), request.getMaxFloors());
        List<Passenger> loadData = prepareLoad(request.getFile());
        discreteSimulation.runSimulation(loadData);
        return Response.ok().build();
    }

    private SchedulingAlgorithm getSchedulingAlgorithm(String algorithmName){
        return roundRobin;
    }

    private List<Passenger> prepareLoad(MultipartFile file){
        return new ArrayList<>();
    }
}
