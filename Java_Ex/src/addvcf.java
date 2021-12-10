import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class addvcf {
	public static void main(String arg[]){
		BufferedReader br = null;
		try {
			String sCurrentLine;
			br = new BufferedReader(new FileReader("C:\\Users\\pkumarasami\\Desktop\\date.txt"));
			while ((sCurrentLine = br.readLine()) != null) {
				sCurrentLine=sCurrentLine.replace(",", "");
				String value[] = sCurrentLine.split(" ");
				String month = null;
				if(value[0].equalsIgnoreCase("Jan")){
					month = "01";
				}else if(value[0].equalsIgnoreCase("Feb")){
					month = "02";
				}else if(value[0].equalsIgnoreCase("mar")){
					month = "03";
				}else if(value[0].equalsIgnoreCase("apr")){
					month = "04";
				}else if(value[0].equalsIgnoreCase("may")){
					month = "05";
				}else if(value[0].equalsIgnoreCase("jun")){
					month = "06";
				}else if(value[0].equalsIgnoreCase("jul")){
					month = "07";
				}else if(value[0].equalsIgnoreCase("aug")){
					month = "08";
				}else if(value[0].equalsIgnoreCase("sep")){
					month = "09";
				}else if(value[0].equalsIgnoreCase("oct")){
					month = "10";
				}else if(value[0].equalsIgnoreCase("nov")){
					month = "11";
				}else if(value[0].equalsIgnoreCase("dec")){
					month = "12";
				}
				System.out.println(value[1]+"-"+month+"-"+value[2]);
				//System.out.println("BEGIN:VCARD");
				//System.out.println("VERSION:2.1");
				//System.out.println("Note:"+value[0]);
				//value[1]=value[1].replace("\"", "");
				//System.out.println("FN: PR "+value[0].trim());
				//System.out.println("ADR;WORK:"+value[3]+", "+value[4]);
				//System.out.println("TEL;CELL:"+sCurrentLine);
				//System.out.println("END:VCARD");
				/*String value[] = sCurrentLine.split(" ");
				System.out.println("BEGIN:VCARD");
				System.out.println("VERSION:2.1");
				System.out.println("TEL;CELL:"+sCurrentLine);
				//System.out.println(sCurrentLine);
				//System.out.println("FN:PR "+value[0]);
				System.out.println("END:VCARD");*/
			}
			/*while ((sCurrentLine = br.readLine()) != null) {
				String[] arr = sCurrentLine.split("	");
				if (arr.length>1)
				System.out.println(sCurrentLine);
			}*/
		} catch (IOException e) {
			e.printStackTrace();
		} 
	}
}
