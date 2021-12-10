import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;


public class logbyappid {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		BufferedReader br = null;
		 
		try {
 
			String sCurrentLine;
 
			br = new BufferedReader(new FileReader("C:\\Users\\pkumarasami\\Desktop\\ShoreTel\\logcats5.txt"));
 
			while ((sCurrentLine = br.readLine()) != null) {
				if(sCurrentLine.contains("/Dialer")){
					System.out.println(sCurrentLine);
					
				}
			}
 
		} catch (IOException e) {
			e.printStackTrace();
		} 

	}

}
