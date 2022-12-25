package com.springbook.biz.board;

import java.util.List;

import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.GenericXmlApplicationContext;

public class BoardServiceClient {

	public static void main(String[] args) {
		//������ �����̳ʸ� ����
		AbstractApplicationContext container=
				new GenericXmlApplicationContext("applicationContext.xml");
		//������ �����̳ʷκ��� BoardServiceImpl ��ü�� Lookup�Ѵ�.
		BoardService boardService=(BoardService) container.getBean("boardService");
		//�� ��� ��� �׽�Ʈ
		BoardVO vo=new BoardVO();
		vo.setTitle("�����λ�");
		vo.setWriter("������");
		vo.setContent("�ߺ�Ź�帳�ϴ�.......");
		boardService.insertBoard(vo);
		//�� ��� �˻� ��� �׽�Ʈ
		List<BoardVO> boardList=boardService.getBoardList(vo);
		for(BoardVO board:boardList) {
			System.out.println("--->"+board.toString());
		}
		//������ �����̳� ����
		container.close();

	}

}
