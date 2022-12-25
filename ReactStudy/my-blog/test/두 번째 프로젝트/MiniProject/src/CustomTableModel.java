import java.text.SimpleDateFormat;
import java.util.ArrayList;

import javax.swing.table.AbstractTableModel;

public class CustomTableModel extends AbstractTableModel {
	private ArrayList<StockTO> datas;
	private String[] columnNames=new String[] {
			"\uC99D\uAD8C\uC0AC", "\uC885\uBAA9\uBA85", "\uAD6C\uB9E4\uC218\uB7C9", "\uB9E4\uC785\uB2E8\uAC00", "\uB9E4\uC218\uAE08\uC561", "\uAD6C\uB9E4\uB0A0\uC9DC"};
	
	public CustomTableModel(String strCompany) {
		// TODO Auto-generated constructor stub
		StockDAO dao = new StockDAO();
		datas = dao.listStock(strCompany);
	}
	@Override
	public String getColumnName(int column) {
		// TODO Auto-generated method stub
		return columnNames[column];
	}
	@Override
	public int getRowCount() {
		// TODO Auto-generated method stub
		return datas.size();
	}

	@Override
	public int getColumnCount() {
		// TODO Auto-generated method stub
		return 6;
	}

	@Override
	public Object getValueAt(int rowIndex, int columnIndex) {
		// TODO Auto-generated method stub
		String result = "";
        StockTO to = datas.get(rowIndex);
		switch( columnIndex ) {
		case 0:
			result = to.getCompany();
			break;
		case 1:
			result = to.getItem();
			break;
		case 2:
			result = Integer.toString(to.getAmount());
			break;
		case 3:
			result = Integer.toString(to.getPrice());
			break;
		case 4:
			result = Integer.toString(to.getTotalprice());
			break;
		case 5:
			String dateToStr = String.format("%1$tY-%1$tm-%1$td", to.getS_date());
			result = dateToStr;
			break;
			
		}
		return result;
	}
}
