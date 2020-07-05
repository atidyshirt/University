import java.util.ArrayList;

import jdk.internal.net.http.websocket.Transport;
import sun.net.TransferProtocolClient;

public class GreenAlienTransporter {
	private ArrayList<GreenAlien> transporter;

    public GreenAlienTransporter(String name){
        transporter = new GreenAlienTransporter(name);
    }
 
    public boolean addPassenger(GreenAlien alien){
        for (int i = 0; i <= transporter.size(); i++){
            if (alien == transporter.get(i)){
                return true;
            }
            else{
                transporter.add(alien);
                return false;
            }
        }
    }

    public boolean removePassanger(GreenAlien alien){
        for (int i = 0; i <= transporter.size(); i++){
            if (alien == transporter.get(i)){
                transporter.remove(transporter.get(i));
                return true;
            } 
            else {
                return false;
            }
            
        }
    }
    
    public void listPassasngers(){
        System.out.println("The passengers on " + transporter + "are:")
        for (int i = 0; i < transporter.size(); i++){ 
            System.out.println(transporter.get(i)); 
        }
    }


	public static void main(String[] args) {
        GreenAlienTransporter transporter = new GreenAlienTransporter("Fun Club");

        GreenAlien kloup = new GreenAlien("Kloup", 9, "Biscuits");
        GreenAlien gwerp = new GreenAlien("Gwerp", 4, "Marshmellows");
        GreenAlien blarg = new GreenAlien("Blarg", 3, "Pop Rocks");
        GreenAlien lesap = new GreenAlien("Lesap", 5, "Chocolate");
        GreenAlien hugso = new GreenAlien("Hugso", 2, "Pop Rocks");

        transporter.addPassenger(kloup);
        transporter.addPassenger(gwerp);
        transporter.addPassenger(blarg);
        transporter.addPassenger(lesap);
        transporter.addPassenger(hugso);

        //transporter.printDetails();
        System.out,println(transporter);
		
	}
}
