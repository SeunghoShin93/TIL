
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
			System.out.println("a�� b���� ũ��.");
			break ;
		case 0:
			System.out.println("a�� b���� �۰ų� ����.");
			break ;
//		default :
//			System.out.println("haha");
//			break ;
		}

	}

}
