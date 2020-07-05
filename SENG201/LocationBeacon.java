public class LocationBeacon{
    private int hours;
    private int minutes;
    private int distance; //in KM

    public void heartBeat(int startHour, int startMinute, int startDistance, int speed, int duration){
        System.out.println( "[" + startHour + ":" + startMinute + "] Starman is <distance>km away from Earth");
    }

    public static void main(String [] args){
      LocationBeacon beacon = new LocationBeacon();
      beacon.heartBeat(14, 31, 300000, 60000, 60);
    }
}
