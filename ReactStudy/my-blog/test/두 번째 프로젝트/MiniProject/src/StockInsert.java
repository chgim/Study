import java.awt.FlowLayout;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.Statement;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

import javax.swing.DefaultComboBoxModel;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JDialog;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JSpinner;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;



public class StockInsert extends JDialog {

	private final JPanel contentPanel = new JPanel();
	private JTextField textField;
	private JTextField textField2;
	private JTextField textField3;
	private JComboBox comboBox;
	private JSpinner spinner;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		try {
			StockInsert dialog = new StockInsert();
			dialog.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
			dialog.setVisible(true);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/**
	 * Create the dialog.
	 */
	public StockInsert() {
		setResizable(false);
		setTitle("주식 추가");
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
		
		JLabel lblNewLabel_6 = new JLabel("( 입력 형식 : 2021-12-10 )");
		lblNewLabel_6.setBounds(202, 279, 164, 15);
		contentPanel.add(lblNewLabel_6);
		{
			JPanel buttonPane = new JPanel();
			buttonPane.setBounds(0, 410, 516, 33);
			buttonPane.setLayout(new FlowLayout(FlowLayout.RIGHT));
			getContentPane().add(buttonPane);
			{
				JButton okButton = new JButton("추가");
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
						
						
						/* db구조
						+------------+-------------+------+-----+---------+-------+
						| Field      | Type        | Null | Key | Default | Extra |
						+------------+-------------+------+-----+---------+-------+
						| company    | varchar(20) | NO   |     | NULL    |       |
						| item       | varchar(20) | NO   | PRI | NULL    |       |
						| amount     | int(30)     | YES  |     | NULL    |       |
						| price      | int(30)     | YES  |     | NULL    |       |
						| totalprice | int(30)     | YES  |     | NULL    |       |
						| s_date     | date        | YES  |     | NULL    |       |
						+------------+-------------+------+-----+---------+-------+
						 */
						
						String sql="insert into stock values(?,?,?,?,?,?)";
						pstmt = conn.prepareStatement( sql );
						pstmt.setString(1,company );
						pstmt.setString(2,item);
						pstmt.setInt(3,amount);
						pstmt.setInt(4,price );
						pstmt.setInt(5,totalprice);
						pstmt.setString(6, s_date);
						
						int result =pstmt.executeUpdate();

						if (result == 1) {
							JOptionPane.showMessageDialog(StockInsert.this,"저장이 완료되었습니다"); 
							contentClear();
							StockInsert.this.dispose();
							//StockInfo.tableRefresh();
						} else {
							JOptionPane.showMessageDialog(StockInsert.this, "저장에 실패하였습니다!");
						}

						System.out.println("실행 성공");
					} catch (ClassNotFoundException e1) {
						System.out.println("[에러] " +e1.getMessage());
					} catch (SQLException e1) {
						System.out.println("[에러] " +e1.getMessage());
					}finally {
						if(stmt != null) try {stmt.close();} catch(SQLException e1) {}
						if(conn != null) try {conn.close();} catch(SQLException e1) {}
					}
							
					}

				public void contentClear() 
				{
				comboBox.setSelectedItem("한국투자증권");
				textField.setText("");
				spinner.setValue(0);
				textField2.setText("");
				textField3.setText("");
				} 

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
						StockInsert.this.dispose();
					}
				});
				cancelButton.setActionCommand("Cancel");
				buttonPane.add(cancelButton);
			}
		}
	}
}
