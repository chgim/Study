package SpringStudy.Project1;

import SpringStudy.Project1.aop.TimeTraceAop;
import SpringStudy.Project1.repository.*;
import SpringStudy.Project1.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.persistence.EntityManager;
import javax.sql.DataSource;


//자바 코드로 직접 스프링 빈 등록하기
@Configuration
public class SpringConfig { //SpringBean 에 등록. 등록된 memberRepository 를 memberService 에 넣어줌

//    private DataSource dataSource;
//
//    @Autowired
//    public SpringConfig(DataSource dataSource){
//        this.dataSource=dataSource;
//    }Jdbc 까지만 씀


//    private EntityManager em;
//    @Autowired
//    public SpringConfig(EntityManager em) {
//        this.em = em;
//    } jpa 에서 사용

    private final MemberRepository memberRepository;

    @Autowired
    public SpringConfig(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }

//    @Bean
//    public MemberService memberService(){
//        return new MemberService(memberRepository());
//    } spring data jpa 전까지

    @Bean
    public MemberService memberService(){
        return new MemberService(memberRepository);
    }

//    @Bean
//    public MemberRepository memberRepository(){
////        return new MemoryMemberRepository();
////        return new JdbcMemberRepository(dataSource);
////        return new JdbcTemplateMemberRepository(dataSource);
////        return new JpaMemberRepository(em);
//
//    }
    @Bean
    public TimeTraceAop timeTraceAop(){
        return new TimeTraceAop();
    }

}
//실무에서는 주로 정형화된 컨트롤러, 서비스, 리포지토리 같은 코드는 컴포넌트 스캔을 사용한다.
//그리고 정형화 되지 않거나, 상황에 따라 구현 클래스를 변경해야 하면 설정을 통해 스프링 빈으로 등록한다. ex) 데이터 저장소(repository 변경)
//DataSource 는 데이터베이스 커넥션을 획득할 때 사용하는 객체다. 스프링 부트는 데이터베이스 커넥션
//정보를 바탕으로 DataSource 를 생성하고 스프링 빈으로 만들어둔다. 그래서 DI를 받을 수 있다.
//개방-폐쇄 원칙(OCP, Open-Closed Principle): 확장에는 열려있고, 수정, 변경에는 닫혀있다.
//스프링의 DI (Dependencies Injection)을 사용하면 기존 코드를 전혀 손대지 않고, 설정만으로 구현 클래스를 변경할 수 있다.