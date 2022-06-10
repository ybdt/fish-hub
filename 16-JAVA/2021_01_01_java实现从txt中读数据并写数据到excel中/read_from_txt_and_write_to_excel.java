package package0;

import java.io.BufferedReader;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;

import org.apache.poi.hssf.usermodel.HSSFCell;
import org.apache.poi.hssf.usermodel.HSSFRow;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;

public class ReadTxtWriteExcel {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
            String[][] txt = readTxt("CJ_BJGMD.txt");
            HSSFWorkbook workbook= new HSSFWorkbook(); // create a workbook object
            HSSFSheet sheet1 = workbook.createSheet("sheet1"); // create a sheet1 object
            for (int i = 0; i < 22161; i++) {
            	HSSFRow row = sheet1.createRow(i); // create row object
                for (int j=0; j<8; j++) {
                	HSSFCell cell = row.createCell(j); // create column object
                	cell.setCellValue(txt[i][j]); // set value to the column
                }
            }
            workbook.write(new FileOutputStream("Excel.xls"));
            workbook.close();
		}
		catch (IOException e) {
			e.printStackTrace();
		}
		System.out.println("Data has been write to Excel Successfully!");
	}

	//read data from text to the two-dimensional array
	private static String[][] readTxt(String name) throws IOException {
		BufferedReader in = new BufferedReader(new FileReader(name));
		String[][] doubleArray = new String[22161][8];
		String line;
		for (int i = 0; (line = in.readLine()) != null; i++)
			doubleArray[i] = line.split("\t"); // pass a one-dimensional array to the each-row of the two dimension array
		in.close();
		return doubleArray;
	}

}
