import java.io.*;

public class bf {

	// BufferedReader 사용 시 예외처리 필수!
	public static void main(String[] args) throws Exception {
    	// 콘솔 입력 시 BufferedReader 객체 생성
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // readLine() 매서드 리턴값은 String이어서 숫자 입력시 형변환 필수!
        int N = Integer.parseInt(br.readLine());
        
        String line = "";
        // 더 이상 입력값이 없을 때까지 1줄씩 읽는다.
       	for(int i=0; (line=br.readLine()) != null; i++) {
        	System.out.println(line);
         }
	}
}
