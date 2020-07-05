enum MarsActivities {
    MOUNTAINS, VALLEYS, ICE_CAPS, CURIOSITY, RED_SAND 
}

public class MarsHoliday{
    public void activityChooser(MarsActivities state){
        switch (state) {
            case MOUNTAINS:
            System.out.println("The air is no different up here than on the ground");
            break;

            case VALLEYS:
            System.out.println("Did I just see a Martian?");
            break;

            case ICE_CAPS:
            System.out.println("Maybe I can drink this");
            break;

            case CURIOSITY:
            System.out.println("Lets pat Curiosity");
            patCuriosity();
            break;

            case RED_SAND:
            System.out.println("That's hot!");
            break;
        }
    }

    public void patCuriosity(){
        System.out.println("Pat pat pat\nCuriosity seems happy");
    }
    
    public static void main(String[] args){
        MarsHoliday holiday = new MarsHoliday();
        holiday.activityChooser(MarsActivities.MOUNTAINS);
        holiday.activityChooser(MarsActivities.VALLEYS);
        holiday.activityChooser(MarsActivities.ICE_CAPS);
        holiday.activityChooser(MarsActivities.CURIOSITY);
        holiday.activityChooser(MarsActivities.RED_SAND);
    }
}
