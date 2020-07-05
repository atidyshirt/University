public class GreenAlien {
	private String name;
	private int eyeCount;
	private String favouriteCandy;
	
	public String toString() {
		return "This Alien is called " + name + " and has " + eyeCount + " eyes. Gross. It seems to enjoy eating " + favouriteCandy;
	}
	
	public GreenAlien() {
		//default constructor
		name = "Kloup";
		eyeCount = 6;
		favouriteCandy = "Lollypops";
	}
	
	public GreenAlien(String name, int eyeCount, String favouriteCandy) {
		//default constructor
		this.name = name;
		this.eyeCount = eyeCount;
		this.favouriteCandy = favouriteCandy;
	}
} 