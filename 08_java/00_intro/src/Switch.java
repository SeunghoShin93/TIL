
public class Switch {

	public static void main(String[] args) {
		int a = 3;
		int b = 5;
		int x;
		if (a > b) {
			x = 1;
		}
		else {
			x = 0;
		}
		switch (x) {
		case 1:
			System.out.println("a가 b보다 크다.");
			break ;
		case 0:
			System.out.println("a가 b보다 작거나 같다.");
			break ;
//		default :
//			System.out.println("haha");
//			break ;
		}

	}

}
