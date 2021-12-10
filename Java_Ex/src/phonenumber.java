import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;


public class phonenumber {
	public static void main(String arg[]){
		BufferedReader br = null;
		try {
		String sCurrentLine;
		 
		br = new BufferedReader(new FileReader("C:\\Users\\pkumarasami\\Downloads\\whatsapp-fb-pk.txt"));
		/*while ((sCurrentLine = br.readLine()) != null) {
			System.out.println("<test>");
			System.out.println("<name>"+sCurrentLine+"</name>");
			System.out.println("</test>");
		}*/
		while ((sCurrentLine = br.readLine()) != null) {
			String value[] = sCurrentLine.split(" ");
			if(!value[value.length-1].contains(":")){
			if((value[value.length-1].startsWith("1")) || (value[value.length-1].startsWith("2")) ||(value[value.length-1].startsWith("3")) ||(value[value.length-1].startsWith("4")) ||(value[value.length-1].startsWith("5")) ||(value[value.length-1].startsWith("6")) ||(value[value.length-1].startsWith("7")) ||(value[value.length-1].startsWith("8")) ||(value[value.length-1].startsWith("9")) ||(value[value.length-1].startsWith("0"))){
				//System.out.println(value[value.length-1]);
				System.out.println("BEGIN:VCARD");
				System.out.println("VERSION:2.1");
				System.out.println("TEL;CELL:"+value[value.length-1]);				
				System.out.println("FN:FB PK "+value[0]);
				System.out.println("END:VCARD");
			}
			}
			//System.out.println(value[value.length-1]);
		}
		} catch (IOException e) {
			e.printStackTrace();
		}
		}
	}

