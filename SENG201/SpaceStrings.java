public class SpaceStrings{

  public int getStringLength(String s){
    return s.length();
  }

  public int getLetterPosition(String s, char v){
    return s.indexOf(v);
  }

  public String makeAllCaps(String s){
    return s.toUpperCase();
  }

  public String makeAllLower(String s){
    return s.toLowerCase();
  }

  //concat function
  public String makeHugeString(String s1, String s2){
    return s1 + s2;
  }

  public static void main(String[] args){
    SpaceStrings space = new SpaceStrings();
		
    String starman = "Starman Sez";
    String rocketship = "Red Tesla";

    System.out.println(space.getStringLength(starman));
    System.out.println(space.getLetterPosition(starman, 'r'));
    System.out.println(space.makeAllCaps(starman));
    System.out.println(space.makeAllLower(starman));
    System.out.println(space.makeHugeString(starman, rocketship));
  }
}
