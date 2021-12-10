import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class FindContactHasMobileNoOrEmail {

	public static void main(String[] args) {
		BufferedReader br = null;
		 
		try {
 
			String sCurrentLine;
			String name[],email[],phone[];
			br = new BufferedReader(new FileReader("C:\\Users\\pkumarasami\\Desktop\\Parasu\\00001.vcf"));
			while ((sCurrentLine = br.readLine()) != null) {
				if(sCurrentLine.startsWith("FN:")){
					String fname = sCurrentLine;
					name = fname.split(":");
					int len = name.length;
					System.out.print(name[len-1]+"		");
				}  if(sCurrentLine.startsWith("TEL;")){
					String fname = sCurrentLine;
					email = fname.split(":");
					int len = email.length;
					System.out.print(email[len-1]+"		");
				}  if(sCurrentLine.startsWith("EMAIL;")){
					String fname = sCurrentLine;
					phone = fname.split(":");
					int len = phone.length;
					System.out.println(phone[len-1]+"		");
				}  if(sCurrentLine.startsWith("NOTE")){
					
					String fname = sCurrentLine;
					phone = fname.split(":");
					int len = phone.length;
					if(phone[len-1].startsWith("0")||phone[len-1].startsWith("+")||phone[len-1].startsWith("7")||phone[len-1].startsWith("9")||phone[len-1].startsWith("8")){
					System.out.println(phone[len-1]+"		");
					}
				}  if(sCurrentLine.startsWith("ADR;")){
					String fname = sCurrentLine;
					phone = fname.split(":");
					int len = phone.length;
					if(phone[len-1].startsWith("0")||phone[len-1].startsWith("+")||phone[len-1].startsWith("7")||phone[len-1].startsWith("9")||phone[len-1].startsWith("8")){
						System.out.println(phone[len-1]+"		");
						}
				}
				
			
				
			}
 
		} catch (IOException e) {
			e.printStackTrace();
		} 
	}

}
