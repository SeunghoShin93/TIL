/**
 * 
 */

/**
 * @author Seungho
 *
 */
public class Variable {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String myName = "Seungho";
		int myAge = 27;
		// declare many variables
		int x = 5, y = 6, z = 50;
		char myBloodType = 'B';
		boolean married = false;
		final boolean isHuman = true; 
		// final == unchangeable and read-only
		System.out.println("Hello " + myName);
		System.out.println("I am " + myAge + " years old.");
		System.out.println("My blood type is " + myBloodType);
		System.out.println("Did I get married? The answer is " +married);
		System.out.println("Am I human ? The answer is " + isHuman);
		System.out.println(x + y + z);
	}
}