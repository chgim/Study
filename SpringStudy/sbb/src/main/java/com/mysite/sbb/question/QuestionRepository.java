package com.mysite.sbb.question;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;
public interface QuestionRepository extends JpaRepository<Question, Integer> {
    Question findBySubject(String subject);
    Question findBySubjectAndContent(String subject, String content);

    List<Question> findBySubjectLike(String subject);
    Page<Question> findAll(Pageable pageable);
}
/*JpaRepository를 상속할 때는 제네릭스 타입으로 <Question, Integer> 처럼 리포지터리의 대상이 되는 엔티티의 타입(Question)과 해당 엔티티의 PK의 속성 타입(Integer)을 지정해야 한다.
 이것은 JpaRepository를 생성하기 위한 규칙이다.*/

/*
항목	          |                예제	              |            설명
And	findBySubjectAndContent(String subject, String content)	여러 컬럼을 and 로 검색
Or	findBySubjectOrContent(String subject, String content)	여러 컬럼을 or 로 검색
Between	findByCreateDateBetween(LocalDateTime fromDate, LocalDateTime toDate)	컬럼을 between으로 검색
LessThan	findByIdLessThan(Integer id)	작은 항목 검색
GreaterThanEqual	findByIdGraterThanEqual(Integer id)	크거나 같은 항목 검색
Like	findBySubjectLike(String subject)	like 검색
In	findBySubjectIn(String[] subjects)	여러 값중에 하나인 항목 검색
OrderBy	findBySubjectOrderByCreateDateAsc(String subject)	검색 결과를 정렬하여 전달
*/

// 쿼리 생성 규칙에 대한 다음의 공식문서를 참고
/*페이징을 구현하기 위해 추가로 설치해야 하는 라이브러리는 없다. JPA 환경 구축시 설치했던 JPA 관련 라이브러리에 이미 페이징을 위한 패키지들이 들어있기 때문이다.

다음의 클래스들을 이용하면 페이징을 쉽게 구현할 수 있다.

org.springframework.data.domain.Page
org.springframework.data.domain.PageRequest
org.springframework.data.domain.Pageable*/