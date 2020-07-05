public class Astronaut{
  //DATA FIELDS
  private String name;
  private int age;
  private String rocketShip;
  private String poweredBy;
  private boolean inSpace;

  //Astronaut empty constructor
  Astronaut(){
    name = "Starman";
    age = 1;
    rocketShip = "Falcon Heavy";
    poweredBy = "Electricity";
    inSpace = true;
  }

  Astronaut(String name, int age, String ship, String power, boolean inSpace){
    this.name = name;
    this.age = age;
    ship = rocketShip;
    power = poweredBy;
    this.inSpace = inSpace;

  }
  public void printName(){
    System.out.println("Hello, my name is " + name);
  }

  public void printAge(){
    System.out.println("I am " + age + " years old");
  }

  public void printRocket(){
    System.out.println("My rocket is " + rocketShip + " and it is powered by " + poweredBy);
  }

  public boolean isInSpace(){
    return inSpace;
  }

  public static void main(String[] args){
    Astronaut starman = new Astronaut();
    Astronaut test = new Astronaut("John", 12, "Jameship", "fuel", false);
    starman.printName();
    starman.printAge();
    starman.printRocket();
    test.printName();
    System.out.println(starman.isInSpace());
  }

} 
