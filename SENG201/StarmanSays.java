public class StarmanSays {
	
	/**
	* Member variables are normally placed at the top
	* of the class, right below the class name.
	*/
	public String hello = "Hello";
	public static String helloStatic = "Hello";
	public static final String HELLO_FINAL = "Hello";
	
	public String sayHello() {
		return hello;
	}
	
	public static void main(String[] args) {
	
		// Make two objects
		StarmanSays starman = new StarmanSays();
		StarmanSays starwoman = new StarmanSays();
		
    // Say hello
		System.out.println(starman.sayHello());
		// Say hello
		System.out.println(starwoman.sayHello());
		
		// Change to Goodbye for object 1
		starman.hello = "Goodbye";
		// Say goodbye
		System.out.println(starman.sayHello());
		// Say hello
		System.out.println(starwoman.sayHello());
		
		// Say to the stars
		StarmanSays.helloStatic = "To the stars!";
		System.out.println(StarmanSays.helloStatic);
		System.out.println(StarmanSays.helloStatic);
		
		// Attempt to modify
		// starman.HELLO_FINAL = "Goodbye"; // compile error, comment out.
		System.out.println(StarmanSays.HELLO_FINAL);
		System.out.println(StarmanSays.HELLO_FINAL);
	}
}
