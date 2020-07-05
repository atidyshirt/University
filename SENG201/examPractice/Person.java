public class Person{
  private String name; 
  private float weight;
  private int age;

  public Person(String name, float weight, int age){
    this.name = name;
    this.weight = weight;
    this.age = age;
  }
  
  public String getName(){
    return name;
  }

  public float getWeight(){
    return weight;
  }

  public int getAge(){
    return age;
  }

  public String getMessage(){
    return "A person named " + name + ", who is " + age + " years old.";
  }
}

