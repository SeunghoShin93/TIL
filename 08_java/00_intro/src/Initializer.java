class Book {
	int price ;
	int num = 0 ;
	String title ;
	
	Book(String t, int p) {
		title = t ;
		price = p ;
	}
	
	void print() {
		System.out.println("���� : " + title);
		System.out.println("���� : " + price);
		System.out.println("�ֹ� ���� : " + num);
		System.out.println("�� ��  : " + price * num);
	}
}

class Initializer {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Book book = new Book("C�� ���̴� �׸�å", 12000) ;
		book.num = 10 ;
		book.print();
	}

}
