class Book {
	int price ;
	int num = 0 ;
	String title ;
	
	Book(String t, int p) {
		title = t ;
		price = p ;
	}
	
	void print() {
		System.out.println("제목 : " + title);
		System.out.println("가격 : " + price);
		System.out.println("주문 수량 : " + num);
		System.out.println("총 액  : " + price * num);
	}
}

class Initializer {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Book book = new Book("C가 보이는 그림책", 12000) ;
		book.num = 10 ;
		book.print();
	}

}
