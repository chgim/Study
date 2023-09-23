package com.mysite.sbb;

import com.mysite.sbb.answer.Answer;
import com.mysite.sbb.answer.AnswerRepository;
import com.mysite.sbb.question.Question;
import com.mysite.sbb.question.QuestionRepository;
import com.mysite.sbb.question.QuestionService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import static org.junit.jupiter.api.Assertions.assertEquals;

import static org.junit.jupiter.api.Assertions.assertTrue;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

@SpringBootTest // SbbApplicationTests 클래스가 스프링부트 테스트 클래스임을 의미
class SbbApplicationTests {

	@Autowired // 스프링의 DI 기능으로 questionRepository 객체를 스프링이 자동으로 생성.
	private QuestionRepository questionRepository;
	// DI(Dependency Injection) - 스프링이 객체를 대신 생성하여 주입한다.
//	@Autowired
//	private AnswerRepository answerRepository;

	@Autowired
	private QuestionService questionService;

	@Test //  testJpa 메서드가 테스트 메서드임을 나타낸다.
	void testJpa() {
//		for (int i = 1; i <= 300; i++) {
//			String subject = String.format("테스트 데이터입니다:[%03d]", i);
//			String content = "내용무";
//			this.questionService.create(subject, content,null);
//	}
//		Question q1 = new Question();
//		q1.setSubject("sbb가 무엇인가요?");
//		q1.setContent("sbb에 대해서 알고 싶습니다.");
//		q1.setCreateDate(LocalDateTime.now());
//		this.questionRepository.save(q1);  // 첫번째 질문 저장
//
//		Question q2 = new Question();
//		q2.setSubject("스프링부트 모델 질문입니다.");
//		q2.setContent("id는 자동으로 생성되나요?");
//		q2.setCreateDate(LocalDateTime.now());
//		this.questionRepository.save(q2);  // 두번째 질문 저장

//		Optional<Question> oq = this.questionRepository.findById(2);
//		assertTrue(oq.isPresent());
//		Question q = oq.get();
//
//		Answer a = new Answer();
//		a.setContent("네 자동으로 생성됩니다.");
//		a.setQuestion(q);  // 어떤 질문의 답변인지 알기위해서 Question 객체가 필요하다.
//		a.setCreateDate(LocalDateTime.now());
//		this.answerRepository.save(a);
/*
		List<Question> all = this.questionRepository.findAll();
		assertEquals(2, all.size());

		Question q = all.get(0);
		assertEquals("sbb가 무엇인가요?", q.getSubject());
*/

	}
}
/*@Autowired
객체를 주입하기 위해 사용하는 스프링의 애너테이션이다.
객체를 주입하는 방식에는 @Autowired 외에 Setter 또는 생성자를 사용하는 방식이 있다.
순환참조 문제와 같은 이유로 @Autowired 보다는 생성자를 통한 객체 주입방식이 권장된다.
하지만 테스트 코드의 경우에는 생성자를 통한 객체의 주입이 불가능하므로 테스트 코드 작성시에만 @Autowired를 사용하고 실제 코드 작성시에는 생성자를 통한 객체 주입방식을 사용하겠다.*/