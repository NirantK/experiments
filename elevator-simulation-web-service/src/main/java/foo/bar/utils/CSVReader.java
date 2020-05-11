package foo.bar.utils; /**
 * Created by roycharu on 2/18/17.
 */
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import foo.bar.dataObjects.Passenger;

public class CSVReader {

    public List<Passenger> readCsv(String filePath) {

        String csvFile = filePath;
        BufferedReader br = null;
        String line = "";
        String cvsSplitBy = ",";
        List<Passenger> passengerList = new ArrayList<Passenger>();
        try {

            br = new BufferedReader(new FileReader(csvFile));
            while ((line = br.readLine()) != null) {

                // use comma as separator
                String[] passenger_row = line.split(cvsSplitBy);

                // System.out.println(passenger_row[0] + "," + passenger_row[1] );
                int startTime = Integer.parseInt(passenger_row[1]);
                int startFloor = Integer.parseInt(passenger_row[2]);
                int endFloor = Integer.parseInt(passenger_row[3]);
                String passengerId = passenger_row[0];

                Passenger p = new Passenger(startFloor,endFloor,startTime);
                p.setPassengerId(passengerId);
                passengerList.add(p);
            }



        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (br != null) {
                try {
                    br.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
        return passengerList;

    }
}
