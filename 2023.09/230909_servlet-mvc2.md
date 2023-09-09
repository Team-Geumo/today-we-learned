# Factory를 통한 객체지향 설계

```
package com.poscodx.mysite.controller;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.poscodx.mysite.web.mvc.guestbook.GuestbookActionFactory;

import com.poscodx.web.mvc.Action;

public class GuestbookController extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		String actionName = request.getParameter("a");
		Action action = new GuestbookActionFactory().getAction(actionName);
		action.execute(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {

		doGet(request, response);
	}

}
```

```
package com.poscodx.mysite.web.mvc.guestbook;

import java.io.IOException;
import java.util.List;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.poscodx.mysite.dao.GuestBookDao;
import com.poscodx.mysite.vo.GuestBookVo;
import com.poscodx.web.mvc.Action;

public class MainGuestbookAction implements Action {

	@Override
	public void execute(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
		List<GuestBookVo> list = new GuestBookDao().guestBookfindAll();
		request.setAttribute("list", list);
		RequestDispatcher rd = request.getRequestDispatcher("/WEB-INF/views/guestbook/index.jsp");
		rd.forward(request, response);
	}

}
```

```
package com.poscodx.mysite.web.mvc.guestbook;

import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.poscodx.mysite.dao.GuestBookDao;
import com.poscodx.mysite.vo.GuestBookVo;
import com.poscodx.web.mvc.Action;

public class InsertGuestbook implements Action {

	@Override
	public void execute(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
		String name = request.getParameter("name");
		String password = request.getParameter("password");
		String message = request.getParameter("content");
		Date currentDate = new Date();
		SimpleDateFormat formatter = new SimpleDateFormat("yyyyMMddHHmmss");
		String reg_Date = formatter.format(currentDate);

		GuestBookVo vo = new GuestBookVo();
		vo.setName(name);
		vo.setPassword(password);
		vo.setContents(message);
		vo.setDate(reg_Date);
		new GuestBookDao().guestBookInsert(vo);

		response.sendRedirect("/mysite02/guestbook");
	}

}
```

```
package com.poscodx.mysite.web.mvc.guestbook;

import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.poscodx.mysite.dao.GuestBookDao;
import com.poscodx.mysite.vo.GuestBookVo;
import com.poscodx.web.mvc.Action;

public class InsertGuestbook implements Action {

	@Override
	public void execute(HttpServletRequest request, HttpServletResponse response) throws IOException, ServletException {
		String name = request.getParameter("name");
		String password = request.getParameter("password");
		String message = request.getParameter("content");
		Date currentDate = new Date();
		SimpleDateFormat formatter = new SimpleDateFormat("yyyyMMddHHmmss");
		String reg_Date = formatter.format(currentDate);

		GuestBookVo vo = new GuestBookVo();
		vo.setName(name);
		vo.setPassword(password);
		vo.setContents(message);
		vo.setDate(reg_Date);
		new GuestBookDao().guestBookInsert(vo);

		response.sendRedirect("/mysite02/guestbook");
	}

}
```

```
<%@page import="com.poscodx.mysite.vo.GuestBookVo"%>
<%@page import="java.util.List"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%
List<GuestBookVo> list = (List<GuestBookVo>) request.getAttribute("list");
%>
<!DOCTYPE html>
<html>
<head>
<title>mysite</title>
<meta http-equiv="content-type" content="text/html; charset=utf-8">
<link href="<%=request.getContextPath()%>/assets/css/guestbook.css"
	rel="stylesheet" type="text/css">
</head>
<body>
	<div id="container">
		<jsp:include page="/WEB-INF/views/includes/header.jsp"/>
		<div id="content">
			<div id="guestbook">
				<form action="/mysite02/guestbook" method="post">
					<input type="hidden" name="a" value="insert">
					<table>
						<tr>
							<td>이름</td>
							<td><input type="text" name="name"></td>
							<td>비밀번호</td>
							<td><input type="password" name="password"></td>
						</tr>
						<tr>
							<td colspan=4><textarea name="content" id="content"></textarea></td>
						</tr>
						<tr>
							<td colspan=4 align=right><input type="submit" VALUE="확인"></td>
						</tr>
					</table>
				</form>
				<ul>
				<% for(GuestBookVo vo : list){ %>
					<li>
						<table>
							<tr>
								<td><%= list.size() %></td>
								<td><%= vo.getName() %></td>
								<td><%= vo.getDate() %></td>
								<td><a href="/mysite02/guestbook?a=deleteform&no=<%= vo.getNo() %>">삭제</a></td>
							</tr>
							<tr>
								<td colspan=4><%= vo.getContents() %></td>
							</tr>
						</table> <br>
					</li>
					<% } %>
				</ul>
			</div>
		</div>
		<jsp:include page="/WEB-INF/views/includes/navigation.jsp"/>
      	<jsp:include page="/WEB-INF/views/includes/footer.jsp"/>
	</div>
</body>
</html>
```
