
public class Overloading {
	static String add(String a, String b) {
		return a + b;
		
	}
	
	static int add(int a, int b) {
		return a + b;
	}
	
	public static void main(String[] args) {
		// 이름이 같지만 return 값이 다른 함수 => 매개 변수에 따라 처리함
		System.out.println(add("Hello ", "Java"));
		System.out.println(add(3, 5));
	}

}
