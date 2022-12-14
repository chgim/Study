import java.awt.FlowLayout;
import java.awt.Frame;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

import javax.swing.DefaultComboBoxModel;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JDialog;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JSpinner;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;
import javax.swing.table.DefaultTableModel;



public class StockUpdate extends JDialog {

	private final JPanel contentPanel = new JPanel();
	private JTextField textField;
	private JTextField textField2;
	private JTextField textField3;
	private JComboBox comboBox;
	private JSpinner spinner;
	private Frame rowIndex;
	

	JTable table;
	JTextField item, price,totalprice,s_date;
	JComboBox company;
	JSpinner amount;
	StockDAO stockDAO;
	StockTO stockTO;
	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		try {
			StockUpdate dialog = new StockUpdate();
			dialog.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
			dialog.setVisible(true);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/**
	 * Create the dialog.
	 * @param index 
	 */
	public StockUpdate(String strCompany,String strItem,int strAmount,String strPrice,String strS_date) {
		setResizable(false);
		setTitle("주식 수정");
		setBounds(100, 100,535 , 480);
		getContentPane().setLayout(null);
		contentPanel.setBounds(0, 0, 516, 410);
		contentPanel.setBorder(new EmptyBorder(5, 5, 5, 5));
		getContentPane().add(contentPanel);
		contentPanel.setLayout(null);
		{
			JLabel lblNewLabel = new JLabel("증권사");
			lblNewLabel.setBounds(120, 91, 50, 15);
			contentPanel.add(lblNewLabel);
		}
		{
			textField = new JTextField();
			textField.setBounds(182, 127, 210, 21);
			contentPanel.add(textField);
			textField.setColumns(10);
		}
		{
			comboBox = new JComboBox();
			comboBox.setModel(new DefaultComboBoxModel(new String[] {"한국투자증권", "삼성증권", "미래에셋증권"}));
			comboBox.setSelectedIndex(0);
			comboBox.setBounds(182, 87, 210, 23);
			contentPanel.add(comboBox);
		}
		{
			JLabel lblNewLabel_1 = new JLabel("종목명");
			lblNewLabel_1.setBounds(120, 130, 50, 15);
			contentPanel.add(lblNewLabel_1);
		}
		{
			JLabel lblNewLabel_2 = new JLabel("구매수량");
			lblNewLabel_2.setBounds(120, 171, 50, 15);
			contentPanel.add(lblNewLabel_2);
		}
		{
			JLabel lblNewLabel_3 = new JLabel("매입단가");
			lblNewLabel_3.setBounds(120, 211, 50, 15);
			contentPanel.add(lblNewLabel_3);
		}
		{
			textField2 = new JTextField();
			textField2.setBounds(182, 208, 184, 21);
			contentPanel.add(textField2);
			textField2.setColumns(10);
		}
		{
			JLabel lblNewLabel_4 = new JLabel("구매날짜");
			lblNewLabel_4.setBounds(120, 251, 50, 15);
			contentPanel.add(lblNewLabel_4);
		}
		{
			JLabel lblNewLabel_5 = new JLabel("원");
			lblNewLabel_5.setBounds(378, 211, 50, 15);
			contentPanel.add(lblNewLabel_5);
		}
		{
			spinner = new JSpinner();
			spinner.setBounds(182, 168, 61, 21);
			contentPanel.add(spinner);
		}
		
		textField3 = new JTextField();
		textField3.setBounds(182, 248, 184, 21);
		contentPanel.add(textField3);
		textField3.setColumns(10);
		{
			JPanel buttonPane = new JPanel();
			buttonPane.setBounds(0, 410, 516, 33);
			buttonPane.setLayout(new FlowLayout(FlowLayout.RIGHT));
			getContentPane().add(buttonPane);
			{
				JButton okButton = new JButton("수정");
				okButton.addMouseListener(new MouseAdapter() {
					@Override
					public void mouseClicked(MouseEvent e) {
						 
						String url="jdbc:mysql://localhost:3306/sample";
						String user="sample";
						String password="1234";
						
						Connection conn=null;
						Statement stmt =null;
						PreparedStatement pstmt=null;
						
						try {
							Class.forName("org.mariadb.jdbc.Driver");
							System.out.println("드라이버 로딩 성공");
							
							conn=DriverManager.getConnection(url,user,password);
							System.out.println("연결 성공");
							
							stmt=conn.createStatement();
							
							String company=(String) comboBox.getSelectedItem();
							String item=textField.getText();
							int amount=(int) spinner.getValue();
							int price= Integer.parseInt(textField2.getText());
							int totalprice=(amount*price);
							String s_date=textField3.getText();
							
							 String sql = "update stock set company=?, amount=?, price=?, totalprice=?, s_date=?  where item=?" ;
							 
						        
						            pstmt = conn.prepareStatement(sql);

						           
									pstmt.setString(1,company );	
									pstmt.setInt(2,amount);
									pstmt.setInt(3,price );
									pstmt.setInt(4,totalprice);
									pstmt.setString(5, s_date);
									pstmt.setString(6,item);

						            // 실행하기
						            int result = pstmt.executeUpdate();
					 

							if (result == 1) {
								JOptionPane.showMessageDialog(StockUpdate.this,"수정이 완료되었습니다"); 
								StockUpdate.this.dispose();
									
							} else {
								JOptionPane.showMessageDialog(StockUpdate.this, "수정에 실패하였습니다!");
							}
						        
						} catch (ClassNotFoundException e1) {
							JOptionPane.showMessageDialog(StockUpdate.this, "수정에 실패하였습니다!");
						} catch (SQLException e1) {
							JOptionPane.showMessageDialog(StockUpdate.this, "수정에 실패하였습니다!");
						}finally {
							if(stmt != null) try {stmt.close();} catch(SQLException e1) {}
							if(conn != null) try {conn.close();} catch(SQLException e1) {}
						}
								
						
					}//mouseClick	
				});
				okButton.setActionCommand("OK");
				buttonPane.add(okButton);
				getRootPane().setDefaultButton(okButton);
			}
			{
				JButton cancelButton = new JButton("취소");
				cancelButton.addMouseListener(new MouseAdapter() {
					@Override
					public void mouseClicked(MouseEvent e) {
						StockUpdate.this.dispose();
					}
				});
				cancelButton.setActionCommand("Cancel");
				buttonPane.add(cancelButton);
			}
		}
		
		 comboBox.setSelectedItem(strCompany);
		 textField.setText(strItem);
		 spinner.setValue(strAmount);
		 textField2.setText(strPrice);
		 textField3.setText(strS_date);
		// System.out.println(strCompany);
		
	}

	
	
	public StockUpdate() {
				
		
	}
	
		
}
		
	




