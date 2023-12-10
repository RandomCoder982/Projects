import java.util.Scanner;

public class JavaSurvey {

	public static void main(String[] args) {
	

	Scanner scanner = new Scanner(System.in);
	
	System.out.println("Hello, what's your name");
	String name = scanner.nextLine();
	
	System.out.println("Nice to meet you " + name + " How old are you?");
	int age = scanner.nextInt();
	
	System.out.println("So, " + name + " you're " + age + " years old? Nice, how many family members do you have?");
	int family = scanner.nextInt();
	
	System.out.println("Wow, I didn't know you had " +family+ " family members. How many are boys?");
	int boy = scanner.nextInt();
	
	System.out.println("You have " +boy+ " boys in your family? How about girls?");
	int girl = scanner.nextInt();

	System.out.println("You have " +girl+ " girls in your family? Nice.");

	scanner.close();
	
	}
}