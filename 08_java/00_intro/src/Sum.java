
public class Sum {

	public static void main(String[] args) {
		int s = 0, i = 0 ;
		
		do {
			i++;
			s = s + i ;
		} while ( i < 10 ) ;
		System.out.println("1에서 " + i + "까지의 합은 " + s);
		// while 조건에 만족하는 동안 do 내부 코드 반복
	}

}
