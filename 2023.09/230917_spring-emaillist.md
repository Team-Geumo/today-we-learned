```
package com.poscodx.emaillist.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import com.poscodx.emaillist.repository.EmailListRepository;
import com.poscodx.emaillist.vo.EmailListVo;

@Controller
public class EmaillistController {
	
	@Autowired // Root Application context에서 wire 해옴
	private EmailListRepository emailListRepository;
	@RequestMapping("/")
	public String main(Model model) {
		List<EmailListVo> list = emailListRepository.findAll();
		model.addAttribute("list", list);
		return "index";
	}
	
	@RequestMapping(value="/add",method=RequestMethod.GET)
	public String add() {
		return "add";
	}
	
	@RequestMapping(value="/add",method=RequestMethod.POST)
	public String add(EmailListVo vo) {
		emailListRepository.insert(vo);
		return "redirect:/";
	}
	
}

```
```
package com.poscodx.emaillist.repository;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Repository;

import com.poscodx.emaillist.vo.EmailListVo;

@Repository
public class EmailListRepository {

	public List<EmailListVo> findAll() {
		List<EmailListVo> result = new ArrayList<EmailListVo>();
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;
		try {
			// 1. JDBC Driver Class 로딩
			Class.forName("org.mariadb.jdbc.Driver");
			// 2. 연결하기
			String url = "jdbc:mariadb://192.168.0.174:3307/webdb?chraset=utf8";
			// getConnection (url, 계정이름, 비밀번호)
			conn = DriverManager.getConnection(url, "webdb", "webdb");
			System.out.println("연결 성공");
			// 3. sql 준비
			String sql = "select no, first_name, last_name, email from emaillist order by no desc";
			pstmt = conn.prepareStatement(sql);

			// 5. sql 실행

			rs = pstmt.executeQuery();

			// 6. 결과처리
			while (rs.next()) {
				Long no = rs.getLong(1);
				String firstName = rs.getString(2);
				String lastName = rs.getString(3);
				String email = rs.getString(4);

				EmailListVo vo = new EmailListVo();
				vo.setNo(no);
				vo.setFirstName(firstName);
				vo.setLastName(lastName);
				vo.setEmail(email);

				result.add(vo);
//				System.out.println(empNo + " : " +  firstName + lastName);

			}
		} catch (ClassNotFoundException e) {
			System.out.println("드라이버 로딩 실패:" + e);
		} catch (SQLException e) {
			System.out.println("error:" + e);
		} finally {
			try {
				// 7. 자원 처리
				if (rs != null) {
					rs.close();
				}
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

	public void insert(EmailListVo vo) {
		Connection conn = null;
		PreparedStatement pstmt = null;
		try {
			conn = getConnection();
			// 3. sql 준비
			String sql = "insert into emaillist values(null, ?, ?, ?)";
			pstmt = conn.prepareStatement(sql);

			// 4. binding
			pstmt.setString(1, vo.getFirstName());
			pstmt.setString(2, vo.getLastName());
			pstmt.setString(3, vo.getEmail());

			// 5. sql 실행
			pstmt.executeQuery();

			// 6. 결과처리 생략
//			while (rs.next()) {
//				Long no = rs.getLong(1);
//				String firstName = rs.getString(2);
//				String lastName = rs.getString(3);
//				String email = rs.getString(4);
//
//				EmailListVo vo = new EmailListVo();
//				vo.setNo(no);
//				vo.setFirstName(firstName);
//				vo.setLastName(lastName);
//				vo.setEmail(email);
//
//				result.add(vo);
////						System.out.println(empNo + " : " +  firstName + lastName);
//
//			}
		} catch (SQLException e) {
			System.out.println("error:" + e);
		} finally {
			try {
				// 7. 자원 처리
//				if (rs != null) {
//					rs.close();
//				}
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
	}

	public void deleteByEmail(String email) {
		Connection conn = null;
		PreparedStatement pstmt = null;
		try {
			// 1. JDBC Driver Class 로딩
			Class.forName("org.mariadb.jdbc.Driver");
			// 2. 연결하기
			String url = "jdbc:mariadb://192.168.0.174:3307/webdb?chraset=utf8";
			// getConnection (url, 계정이름, 비밀번호)
			conn = DriverManager.getConnection(url, "webdb", "webdb");
			System.out.println("연결 성공");
			// 3. sql 준비
			String sql = "delete from emaillist where email=?";
			pstmt = conn.prepareStatement(sql);
			// 4. binding
			pstmt.setString(1, email);
			// 5. sql 실행
			pstmt.executeQuery();

			// 6. 결과처리 생략
//			while (rs.next()) {
//				Long no = rs.getLong(1);
//				String firstName = rs.getString(2);
//				String lastName = rs.getString(3);
//				String email = rs.getString(4);
//
//				EmailListVo vo = new EmailListVo();
//				vo.setNo(no);
//				vo.setFirstName(firstName);
//				vo.setLastName(lastName);
//				vo.setEmail(email);
//
//				result.add(vo);
////						System.out.println(empNo + " : " +  firstName + lastName);
//
//			}
		} catch (ClassNotFoundException e) {
			System.out.println("드라이버 로딩 실패:" + e);
		} catch (SQLException e) {
			System.out.println("error:" + e);
		} finally {
			try {
				// 7. 자원 처리
//				if (rs != null) {
//					rs.close();
//				}
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
	}
	
	// 위에서 sqlexception 처리하므로, 던져버리기
	private Connection getConnection() throws SQLException {
		Connection conn = null;
		// 1. JDBC Driver Class 로딩
		try {
			Class.forName("org.mariadb.jdbc.Driver");
			// 2. 연결하기
			String url = "jdbc:mariadb://192.168.0.174:3307/webdb?charset=utf8";
			// getConnection (url, 계정이름, 비밀번호)
			conn = DriverManager.getConnection(url, "webdb", "webdb");
			System.out.println("연결 성공");
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} 
		return conn;
	}
}

```

```
package com.poscodx.emaillist.vo;

import javax.print.event.PrintJobAttributeEvent;

public class EmailListVo {
	private Long no;
	private String firstName;
	private String lastName;
	private String email;
	public Long getNo() {
		return no;
	}
	public void setNo(Long no) {
		this.no = no;
	}
	public String getFirstName() {
		return firstName;
	}
	public void setFirstName(String firstName) {
		this.firstName = firstName;
	}
	public String getLastName() {
		return lastName;
	}
	public void setLastName(String lastName) {
		this.lastName = lastName;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	@Override
	public String toString() {
		return "EmailListVo [no=" + no + ", firstName=" + firstName + ", lastName=" + lastName + ", email=" + email
				+ "]";
	}
}

```

```
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fn"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>

<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h1>메일 리스트에 가입되었습니다.</h1>
	<p>입력한 정보 내역입니다.</p>
	<!-- 메일정보 리스트 -->

	<c:forEach items="${list }" var="vo">
		<table border="1" cellpadding="5" cellspacing="2">
			<tr>
				<td align=right>First name:</td>
				<td>${vo.firstName }</td>
			</tr>
			<tr>
				<td align=right width="110">Last name:</td>
				<td width="110">${vo.lastName}</td>
			</tr>
			<tr>
				<td align=right>Email address:</td>
				<td>${vo.email}</td>
			</tr>
		</table>
		<br>
	</c:forEach>
	<p>
		<a href="/${pageContext.request.contextPath }/add">추가메일 등록</a>
	</p>
	<br>
</body>
</html>
```

