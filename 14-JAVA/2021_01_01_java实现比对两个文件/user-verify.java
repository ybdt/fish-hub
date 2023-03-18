package package0;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class UserVerify {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			String[] name1 = readIni("AccInfo229.ini"); // invoke readIni func
			String[] name2 = readIni("AccInfo243.ini"); // invoke readIni func
			int sum = 0;
			for (String item1 : name1) {
				// here if is to skip the null in name1
				if (item1.equals(null)) { 
					continue;
				}
				for (String item2 : name2) {
					if (item1.equals(item2)) {
						System.out.println("Found the same account: " + item1);
						sum += 1;
					}
				}
			}
			System.out.println("Finish the check, the count is: " + sum);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	private static String[] readIni(String name) throws IOException {
		BufferedReader in = new BufferedReader(new FileReader(name));
		
		String line;
		String[] nameArray = new String[27];
		int i = 0;
		while ((line = in.readLine()) != null) {
			if (line.charAt(0) == 'U' && line.charAt(4) == 'N') {
				nameArray[i] = line; // read the whole line to the array
				i++;
			}
		}
		
		in.close();
		return nameArray;
	}
	
}
