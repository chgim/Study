

import java.util.ArrayList;

import javax.swing.DefaultComboBoxModel;

public class CustomComboBoxModel extends DefaultComboBoxModel<String> {
	//실제 데이터
	private ArrayList<String> companys=new ArrayList<String>();
	
	public CustomComboBoxModel() {
		companys.add("한국투자증권");
		companys.add("미래에셋증권");
		companys.add("삼성증권");
	}
	//데이터를 가져올 때 필요한 메서드
	@Override
	public int getSize() {
		//System.out.println("getSize 호출");
		return companys.size();
	}
	@Override
	public String getElementAt(int index) {
		//System.out.println("getElementAt 호출");
		return companys.get(index);
	}
}
