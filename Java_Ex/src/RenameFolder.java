import java.io.File;


public class RenameFolder {

	public static void main(String[] args) {
		
		File folder = new File("C:\\Users\\pkumarasami\\Desktop\\Parasu\\BWW");
		File[] listOfFiles = folder.listFiles();//listFiles();
		for(int i=0;i<listOfFiles.length;i++){
			if(listOfFiles[i].isDirectory()){
				System.out.println(listOfFiles[i].getParent());
				System.out.println(listOfFiles[i].getName().replace("_", " & "));
				File dir = new File(listOfFiles[i].getParent()+"\\"+listOfFiles[i].getName().replace("_", " & "));
				listOfFiles[i].renameTo(dir);
			}
		}
	}

}
