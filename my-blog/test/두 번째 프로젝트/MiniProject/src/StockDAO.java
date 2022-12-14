import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JOptionPane;


public class StockDAO {

	private Connection conn;
	
	public StockDAO() {
		String url = "jdbc:mysql://localhost:3306/sample";
		String user = "sample";
		String password = "1234";		
		
		try {
			Class.forName( "org.mariadb.jdbc.Driver" );
			this.conn = DriverManager.getConnection(url, user, password);
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			System.out.println( "[에러] " + e.getMessage() );
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			System.out.println( "[에러] " + e.getMessage() );
		}
	}

	public ArrayList<StockTO> listStock(String strCompany) {
	//public ArrayList<StockTO> listStock() {
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		
		ArrayList<StockTO> listStock = new ArrayList<StockTO>();
		try {
			String sql = "select company,item, amount, price, totalprice,s_date from stock where company = ?";
			pstmt = conn.prepareStatement( sql );
			
			pstmt.setString(1, strCompany);
			
			rs=pstmt.executeQuery();
			while(rs.next())
			{
				StockTO to=new StockTO();
				to.setCompany(rs.getString("company"));;
				to.setItem(rs.getString("item"));
				to.setAmount(rs.getInt("amount"));
				to.setPrice(rs.getInt("price"));
				to.setTotalprice(rs.getInt("totalprice"));
				to.setS_date(rs.getDate("s_date"));
				listStock.add(to);		
			}
		} catch (SQLException e) {
			System.out.println( "[에러] " + e.getMessage() );
		} finally {
			if ( rs != null ) try { rs.close(); } catch( SQLException e ) {}
			if ( pstmt != null ) try { pstmt.close(); } catch( SQLException e ) {}
			if ( conn != null ) try { conn.close(); } catch( SQLException e ) {}			
		}
		return listStock;
	}
	/*
	public List<StockTO> memberAllselect() {
		// 선택한 레코드를 보관할 컬렉션
		List<StockTO> lst = new ArrayList<StockTO>();
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		try {
			
			String sql = "select * from stock ";
			
			pstmt = conn.prepareStatement(sql);
			
			rs = pstmt.executeQuery();
			
			while(rs.next()){
				
				StockTO to=new StockTO();
				to.setCompany(rs.getString("company"));;
				to.setItem(rs.getString("item"));
				to.setAmount(rs.getInt("amount"));
				to.setPrice(rs.getInt("price"));
				to.setTotalprice(rs.getInt("totalprice"));
				to.setS_date(rs.getDate("s_date"));	
				lst.add(to);
			}
		}catch(Exception e) {
			e.printStackTrace();
		}finally {
			if ( rs != null ) try { rs.close(); } catch( SQLException e ) {}
			if ( pstmt != null ) try { pstmt.close(); } catch( SQLException e ) {}
			if ( conn != null ) try { conn.close(); } catch( SQLException e ) {}	
		}
		return lst;
	}*/



	
	
	/*
	   public int UpdateStock(StockTO stockto) {
		   Connection conn=null;
		   PreparedStatement pstmt = null;
			ResultSet rs = null;
	        int result = 0;
	        
	        String sql = "update stock set company=?, amount=?, price=?, totalprice=(amount*price), s_date=?  where item=?" ;
	 
	        try {
	            pstmt = conn.prepareStatement(sql);

	            StockTO to=new StockTO();
				pstmt = conn.prepareStatement( sql );
				pstmt.setString(1,to.getCompany() );
				
				pstmt.setInt(2,to.getAmount());
				pstmt.setInt(3,to.getPrice());
				
				//pstmt.setInt(4,to.totalprice);
				pstmt.setString(4, to.getS_date().toString());
				pstmt.setString(5,to.getItem());
				
	 
	            // 실행하기
	            result = pstmt.executeUpdate();
 
	           
	        } catch (SQLException e) {
	        	System.out.println( "[에러] " + e.getMessage() );
	        } finally {
	        	if ( rs != null ) try { rs.close(); } catch( SQLException e ) {}
				if ( pstmt != null ) try { pstmt.close(); } catch( SQLException e ) {}
				if ( conn != null ) try { conn.close(); } catch( SQLException e ) {}
	        }
	        return result;
	    }
	   
	   public int DeleteStock(StockTO to) {
		    Connection conn=null;
		    PreparedStatement pstmt = null;
			ResultSet rs = null;
	        int result = 0;
	        
	        String sql = "delete from stock where item=?";
	        try {
	        	   pstmt = conn.prepareStatement(sql);
	        	   //StockTO to=new StockTO();

	        	   pstmt.setString(1, to.getItem());
	        	   result = pstmt.executeUpdate();
	 
	        } catch (SQLException e) {
	        	System.out.println( "[에러] " + e.getMessage() );
	        }finally {
	        	if ( rs != null ) try { rs.close(); } catch( SQLException e ) {}
				if ( pstmt != null ) try { pstmt.close(); } catch( SQLException e ) {}
				if ( conn != null ) try { conn.close(); } catch( SQLException e ) {}		
	        }
	 
	        return result;
	    }*/

	
}
