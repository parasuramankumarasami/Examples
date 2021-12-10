import java.io.File;

public class Rename_file {

	public static void main(String[] args) {

		File folder = new File(
				"C:\\Users\\pkumarasami\\Desktop\\Parasu\\Tiruvasagam_Songs");
		File[] listOfFiles = folder.listFiles();// listFiles();
		for (int i = 0; i < listOfFiles.length; i++) {
			if (listOfFiles[i].isFile()) {
				listOfFiles[i].renameTo(new File(listOfFiles[i].getParent()
						+ "\\" + listOfFiles[i].getName() + ".mp3"));
			}
		}

	}

}
