import java.io.*;

public class bf {

	// BufferedReader ��� �� ����ó�� �ʼ�!
	public static void main(String[] args) throws Exception {
    	// �ܼ� �Է� �� BufferedReader ��ü ����
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // readLine() �ż��� ���ϰ��� String�̾ ���� �Է½� ����ȯ �ʼ�!
        int N = Integer.parseInt(br.readLine());
        
        String line = "";
        // �� �̻� �Է°��� ���� ������ 1�پ� �д´�.
       	for(int i=0; (line=br.readLine()) != null; i++) {
        	System.out.println(line);
         }
	}
}
