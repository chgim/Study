import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JComboBox;
import javax.swing.JDialog;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.JScrollPane;
import javax.swing.JSpinner;
import javax.swing.table.DefaultTableModel;



import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.sql.Connection;
import java.sql.Date;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Vector;

import javax.swing.JCheckBox;
import javax.swing.AbstractButton;
import javax.swing.ComboBoxModel;
import javax.swing.DefaultComboBoxModel;
import java.awt.event.ItemListener;
import java.awt.event.ItemEvent;
import javax.swing.ScrollPaneConstants;

public class StockInfo extends JFrame {

	protected static final StockTO StockTO = null;
	private JPanel contentPane;
	private JScrollPane scrollPane;
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
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					StockInfo frame = new StockInfo();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public StockInfo() {
		setTitle("주식 관리 프로그램");
		setResizable(false);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 640, 480);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JComboBox comboBox = new JComboBox();
		comboBox.addItemListener(new ItemListener() {
			public void itemStateChanged(ItemEvent e) {
				
				String strCompany="";
				if(e.getStateChange() == ItemEvent.SELECTED) {
					
					strCompany=(String)comboBox.getSelectedItem();
					table.setModel(new CustomTableModel(strCompany));
					
				}


			}
		});
		comboBox.setModel(new DefaultComboBoxModel(new String[] {"한국투자증권", "삼성증권", "미래에셋증권"}));
		comboBox.setBounds(58, 23, 198, 23);
		contentPane.add(comboBox);
		
		JButton btn1 = new JButton("주식 추가");
		btn1.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				StockInsert insert = new StockInsert();
				insert.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
				insert.setVisible(true);
				//String strDong=textField.getText();
			}
		});
		btn1.setBounds(317, 23, 91, 23);
		contentPane.add(btn1);
		
		JButton btn2 = new JButton("주식 수정");
		btn2.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				 
				 int rowIndex = table.getSelectedRow();
				// System.out.println(rowIndex);
				 
				 String strCompany =table.getValueAt(rowIndex, 0).toString();
				 String strItem=table.getValueAt(rowIndex, 1).toString() ;
				 int strAmount=Integer.parseInt(table.getValueAt(rowIndex, 2).toString()) ;
				 String strPrice=table.getValueAt(rowIndex, 3).toString() ;
				 String strS_date=table.getValueAt(rowIndex, 5).toString() ;
					//System.out.println(strItem);
				 
				 //StockUpdate update=new StockUpdate();
				 StockUpdate update = new StockUpdate(strCompany,strItem,strAmount,strPrice,strS_date); 
				 update.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
				 update.setVisible(true);
				// tableRefresh();
				
					

			}

			

			
		});
		btn2.setBounds(420, 23, 91, 23);
		contentPane.add(btn2);
		
		JButton btn3 = new JButton("주식 삭제");
		btn3.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				
				 int rowIndex = table.getSelectedRow();
				// System.out.println(rowIndex);
				 
				 String strCompany =table.getValueAt(rowIndex, 0).toString();
				 String strItem=table.getValueAt(rowIndex, 1).toString() ;
				 int strAmount=Integer.parseInt(table.getValueAt(rowIndex, 2).toString()) ;
				 String strPrice=table.getValueAt(rowIndex, 3).toString() ;
				 String strS_date=table.getValueAt(rowIndex, 5).toString() ;
					//System.out.println(strItem);
				 
				 StockDelete delete = new StockDelete(strCompany,strItem,strAmount,strPrice,strS_date); 
				// StockDelete delete = new StockDelete(); 
				 delete.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
				 delete.setVisible(true);
								
					
					
			}

				
		});
		btn3.setBounds(525, 23, 91, 23);
		contentPane.add(btn3);
		
		JPanel panel = new JPanel();
		panel.setBounds(0, 66, 626, 367);
		contentPane.add(panel);
		
		scrollPane = new JScrollPane();
		scrollPane.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
		panel.add(scrollPane);
		
		table = new JTable();
		table.setModel(new DefaultTableModel(
			new Object[][] {
				{null, null, null, null, null, null},
			},
			new String[] {
				"\uC99D\uAD8C\uC0AC", "\uC885\uBAA9\uBA85", "\uAD6C\uB9E4\uC218\uB7C9", "\uB9E4\uC785\uB2E8\uAC00", "\uB9E4\uC218\uAE08\uC561", "\uAD6C\uB9E4\uB0A0\uC9DC"
			}
		) {
			boolean[] columnEditables = new boolean[] {
				false, false, false, false, false, false
			};
			public boolean isCellEditable(int row, int column) {
				return columnEditables[column];
			}
		});
		scrollPane.setViewportView(table);
		
		JLabel lbl = new JLabel("증권사: ");
		lbl.setBounds(12, 27, 50, 15);
		contentPane.add(lbl);
		
		
	}
}
