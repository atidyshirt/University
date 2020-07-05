public class LiftoffWatch{
    private double temperature;
    private String weather;
    public double wind;

    public void setTemp(double temperature){
        this.temperature = temperature;
    }

    public void setWeather(String weather){
        this.weather = weather;
    }

    public void setWind(double wind){
        this.wind = wind;
    }

    boolean canWeLaunch(){
        if (temperature >= 16.5 && temperature <= 34.0){
            if ((weather.toLowerCase()).equals("sunny") && wind <= 60.0){
                return true;
            }
            else if ((weather.toLowerCase()).equals("cloudy") && wind <= 45.0){
                return true;
            }
            else{
                return false;
            }
        }

        else{
            return false;
            }
        
    }

    public static void main(String[] args){
        LiftoffWatch launch = new LiftoffWatch();
        launch.setTemp(27.0);
        launch.setWeather("Sunny");
        launch.setWind(53);
        System.out.println(launch.canWeLaunch());
    }

}