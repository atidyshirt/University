public class FallTime {
  public static void main(String [] args){
    // test cases
    FallTime fallTime = new FallTime();
    List<Double> gravity = Arrays.asList(3.70, 8.87);
    System.out.println(fallTime.calculateTime(3, gravity));
  }
  
  public List<Double> calculateTime(double height, List<Double> gravity){
    double time;
    List<Double> result;
    for (int i = 0; i < gravity.length(); i++){
      time = Math.sqrt(Math.pow(height, 2) / gravity[i]);
      if (gravity == 0){
        time = Double.POSITIVE_INFINITY;
      }
      result.append(time);
    }
    return result;
  }
  

}
