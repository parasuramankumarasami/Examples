import java.io.File;


public class scriptname {
	public static void main(String[] args) {
		File folder = new File("C:\\Users\\pkumarasami\\Desktop\\Scripts");
		String[] listOfFiles = folder.list();//listFiles();
		for (int i=0; i<=listOfFiles.length;i++)
			System.out.println(listOfFiles[i]);
	}

}
