package com.mysite.sbb.question;

import java.time.LocalDateTime;
import java.util.List;
// 스프링부트 3.x 버전일 경우 jakarta. 사용,  스프링부트 2.x 버전일 경우 javax. 사용
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.ManyToOne;
import com.mysite.sbb.user.SiteUser;
import javax.persistence.CascadeType;
import javax.persistence.OneToMany;

import com.mysite.sbb.answer.Answer;
import lombok.Getter;
import lombok.Setter;

@Getter // Getter, Setter 메서드를 자동으로 생성
@Setter // Getter, Setter 메서드를 자동으로 생성
@Entity // @Entity 애너테이션을 적용해야 JPA가 엔티티로 인식
public class Question {
    @Id //  id 속성을 기본 키로 지정
    @GeneratedValue(strategy = GenerationType.IDENTITY) // 데이터를 저장할 때 해당 속성에 값을 따로 세팅하지 않아도 1씩 자동으로 증가하여 저장.strategy는 고유번호를 생성하는 옵션으로 GenerationType.IDENTITY는 해당 컬럼만의 독립적인 시퀀스를 생성하여 번호를 증가시킬 때 사용
    private Integer id;

    @ManyToOne
    private SiteUser author;

    @Column(length = 200) // 엔티티의 속성은 테이블의 컬럼명과 일치하는데 컬럼의 세부 설정을 위해 @Column 애너테이션을 사용
    private String subject;

    @Column(columnDefinition = "TEXT") // columnDefinition은 컬럼의 속성을 정의할 때 사용한다. columnDefinition = "TEXT"은 "내용"처럼 글자 수를 제한할 수 없는 경우에 사용
    private String content;

    private LocalDateTime createDate;
    //  createDate 속성의 실제 테이블의 컬럼명은 create_date가 된다. 즉 createDate처럼 대소문자 형태의 카멜케이스(Camel Case) 이름은
    //  create_date 처럼 모두 소문자로 변경되고 언더바(_)로 단어가 구분되어 실제 테이블 컬럼명이 된다.

    @OneToMany(mappedBy = "question", cascade = CascadeType.REMOVE)
    private List<Answer> answerList;
}
/*일반적으로 엔티티에는 Setter 메서드를 구현하지 않고 사용하기를 권한다. 왜냐하면 엔티티는 데이터베이스와 바로 연결되어 있으므로 데이터를 자유롭게 변경할 수 있는 Setter 메서드를 허용하는 것이 안전하지 않다고 판단하기 때문이다.

그렇다면 Setter 메서드 없이 어떻게 엔티티에 값을 저장할 수 있을까?

엔티티를 생성할 경우에는 롬복의 @Builder 어노테이션을 통한 빌드패턴을 사용하고, 데이터를 변경해야 할 경우에는 그에 해당되는 메서드를 엔티티에 추가하여 데이터를 변경하면 된다.*/

/*답변과 질문이 N:1의 관계라면 질문과 답변은 1:N의 관계라고 할 수 있다. 이런경우에는 @ManyToOne이 아닌 @OneToMany애너테이션을 사용한다.
Question 하나에 Answer는 여러개이므로 Question 엔티티에 추가할 답변의 속성은 List 형태로 구성*/

/* 질문 객체(예:question)에서 답변을 참조하려면 question.getAnswerList()를 호출하면 된다. @OneToMany 애너테이션에 사용된 mappedBy는 참조 엔티티의 속성명을 의미한다.
즉, Answer 엔티티에서 Question 엔티티를 참조한 속성명 question을 mappedBy에 전달해야 한다.*/

