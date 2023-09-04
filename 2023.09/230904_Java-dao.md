```
package bookmall.vo;

public class CategoryVo {
	private int categoryNo;
	private String name;
	
	public int getCategoryNo() {
		return categoryNo;
	}
	public void setCategoryNo(int categoryNo) {
		this.categoryNo = categoryNo;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	@Override
	public String toString() {
		return "CategoryVo [categoryNo=" + categoryNo + ", name=" + name + "]";
	}
	
}

```

```
package bookmall.dao.test;

import bookmall.dao.BookDao;
import bookmall.vo.BookVo;

public class BookDaoTest {

	public static void main(String[] args) {
		bookInsertTest();
	}

	private static void bookInsertTest() {
		BookVo bookVo =  new BookVo();
		BookDao bookDao = new BookDao();
		
		bookVo.setBookNo(1);
		bookVo.setTitle("총,균,쇠");
		bookVo.setPrice(30000);
		bookVo.setCategory_no(1);
		bookDao.bookInsert(bookVo);
		
		bookVo.setBookNo(2);
		bookVo.setTitle("이것이 Java다");
		bookVo.setPrice(40000);
		bookVo.setCategory_no(2);
		bookDao.bookInsert(bookVo);
		
		bookVo.setBookNo(3);
		bookVo.setTitle("무소유");
		bookVo.setPrice(15000);
		bookVo.setCategory_no(3);
		bookDao.bookInsert(bookVo);
	}

}

```

```
package bookmall.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import bookmall.vo.CategoryVo;

public class CategoryDao {

	public boolean categoryInsert(CategoryVo categoryVo) {
		PreparedStatement pstmt = null;
		Connection conn = null;
		boolean result = false;
		try {
			Class.forName("org.mariadb.jdbc.Driver");
			String url = "jdbc:mariadb://192.168.0.174:3307/bookmall?charset=utf8";
			conn = DriverManager.getConnection(url, "bookmall", "bookmall");

			String sql = "insert into category values(null,?)";
			pstmt = conn.prepareStatement(sql);

			pstmt.setString(1, categoryVo.getName());

			int count = pstmt.executeUpdate();

			result = (count == 1);
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {

			try {
				if (pstmt != null) {
					pstmt.close();
				}
				if (conn != null) {
					conn.close();
				}
			} catch (SQLException e) {
				e.printStackTrace();
			}
		}
		return result;
	}
}

```