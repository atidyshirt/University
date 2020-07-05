public class PracticeExam {
  public static void main(String [] args){
    checkPassword("xxx123", "@xxx123#");
  }

  public static void checkPassword(String username, String password){
    String error1 = "";
    String error2 = "";
    String error3 = "";
    String error = "";
    if (username.length() < 1){
      error1 = "You need a username";
    }
    if (password.contains(username)){
      error2 = "Your username can't be contained in your password";

    }
    if (password.length() < 12){
      error3 = "the length of your password must be at least 12";
    }
    
    if (error1.length() > 0){
      error = error1;
      if (error2.length() > 0){
        error = error + " and " + error2;
      }
      if (error3.length() > 0){
        error = error + " and " + error3;
      }

    }
    else if (error2.length() > 0){
      error = error2;
      if (error1.length() > 0){
        error = error + " and " + error1;
      }
      if (error3.length() > 0){
        error = error + " and " + error3;
      }
    }
    else if (error3.length() > 0){
      error = error3;
      if (error2.length() > 0){
        error = error + " and " + error2;
      }
      if (error1.length() > 0){
        error = error + " and " + error1;
      }

    }
    else {
      error = "The password is OK";
    }
    System.out.println(error);
  }

  }

  
