import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;


public class TestStatus_ROD {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		String logfile = "C:\\Users\\pkumarasami\\Desktop\\ShoreTel\\Selenium\\Workspace\\Java_Ex\\log_for_html.log";
		BufferedReader br = null;
		 
		try {
 
			String sCurrentLine;
 
			br = new BufferedReader(new FileReader(logfile));
 
			while ((sCurrentLine = br.readLine()) != null) {
				if(sCurrentLine.startsWith("Test Name   : ") || sCurrentLine.startsWith("Test Status : "))
				System.out.println(sCurrentLine);
			}
 
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				if (br != null)br.close();
			} catch (IOException ex) {
				ex.printStackTrace();
			}
		}
 

	}

}
