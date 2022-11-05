package hello2.core;


import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.FilterType;

@Configuration
@ComponentScan(
        excludeFilters = @ComponentScan.Filter(type= FilterType.ANNOTATION, classes = Configuration.class)
)
public class AutoAppConfig {

}
//컴포넌트 스캔을 사용하려면 먼저 @ComponentScan 을 설정 정보에 붙여주면 된다.
//기존의 AppConfig와는 다르게 @Bean으로 등록한 클래스가 하나도 없다
//@Controller : 스프링 MVC 컨트롤러로 인식
//@Repository : 스프링 데이터 접근 계층으로 인식하고, 데이터 계층의 예외를 스프링 예외로 변환해준다.
//@Configuration : 앞서 보았듯이 스프링 설정 정보로 인식하고, 스프링 빈이 싱글톤을 유지하도록 추가
//처리를 한다.
//@Service : 사실 @Service 는 특별한 처리를 하지 않는다. 대신 개발자들이 핵심 비즈니스 로직이 여기에
//있겠구나 라고 비즈니스 계층을 인식하는데 도움이 된다
//의존관계 자동 주입은 스프링 컨테이너가 관리하는 스프링 빈이어야
//동작한다. 스프링 빈이 아닌 Member 같은 클래스에서 @Autowired 코드를 적용해도 아무 기능도
//동작하지 않는다.