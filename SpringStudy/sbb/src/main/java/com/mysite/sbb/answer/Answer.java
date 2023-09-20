package com.mysite.sbb.answer;

import java.time.LocalDateTime;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.ManyToOne;

import com.mysite.sbb.question.Question;
import lombok.Getter;
import lombok.Setter;


@Getter
@Setter
@Entity
public class Answer {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(columnDefinition = "TEXT")
    private String content;

    private LocalDateTime createDate;
    @ManyToOne // 답변은 하나의 질문에 여러개가 달릴 수 있는 구조, @ManyToOne은 N:1 관계. Answer 엔티티의 question 속성과 Question 엔티티가 서로 연결. 실제 데이터베이스에서는 ForeignKey 관계가 생성
    private Question question;
}
/*답변 객체(예:answer)를 통해 질문 객체의 제목을 알고 싶다면 answer.getQuestion().getSubject()처럼 접근할 수 있다.
 하지만 이렇게 속성만 추가하면 안되고 질문 엔티티와 연결된 속성이라는 것을 명시적으로 표시*/