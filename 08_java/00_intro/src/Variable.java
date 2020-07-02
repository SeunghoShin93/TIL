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
	/* Data Type	Size	Description
	byte	1 byte	Stores whole numbers from -128 to 127
	short	2 bytes	Stores whole numbers from -32,768 to 32,767
	int		4 bytes	Stores whole numbers from -2,147,483,648 to 2,147,483,647 || -21.47억 부터 21.47억
	long	8 bytes	Stores whole numbers from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 
	float	4 bytes	Stores fractional numbers. Sufficient for storing 6 to 7 decimal digits
	double	8 bytes	Stores fractional numbers. Sufficient for storing 15 decimal digits
	boolean	1 bit	Stores true or false values
	char	2 bytes	Stores a single character/letter or ASCII values */
}