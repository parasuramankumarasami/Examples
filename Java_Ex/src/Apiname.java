import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;


public class Apiname {

	public static void main(String[] args) {
		
		BufferedReader br = null;
		 
		try {
 
			String sCurrentLine;
			//br = new BufferedReader(new FileReader("C:\\Shared\\239_MHClient\\MHClient\\lib\\WebAgentComponent.py"));
			//br = new BufferedReader(new FileReader("C:\\Shared\\239_MHClient\\MHClient\\lib\\HighBallComponent.py"));
			br = new BufferedReader(new FileReader("C:\\Users\\pkumarasami\\Downloads\\PR.vcf"));
			while ((sCurrentLine = br.readLine()) != null) {
				if(sCurrentLine.startsWith("    def ")){
					System.out.println(sCurrentLine);
					
				} else if(sCurrentLine.startsWith("FN:")){
					String value[] = sCurrentLine.split(":");
					System.out.println(value[value.length-1]);
				} 
			}
 
		} catch (IOException e) {
			e.printStackTrace();
		} 
	}

}
