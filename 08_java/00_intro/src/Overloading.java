
public class Overloading {
	static String add(String a, String b) {
		return a + b;
		
	}
	
	static int add(int a, int b) {
		return a + b;
	}
	
	public static void main(String[] args) {
		// �̸��� ������ return ���� �ٸ� �Լ� => �Ű� ������ ���� ó����
		System.out.println(add("Hello ", "Java"));
		System.out.println(add(3, 5));
	}

}
