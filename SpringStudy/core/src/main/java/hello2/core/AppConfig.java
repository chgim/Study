package hello2.core;

import hello2.core.discount.DiscountPolicy;
import hello2.core.discount.FixDiscountPolicy;
import hello2.core.discount.RateDiscountPolicy;
import hello2.core.member.MemberRepository;
import hello2.core.member.MemberService;
import hello2.core.member.MemberServiceImpl;
import hello2.core.member.MemoryMemberRepository;
import hello2.core.order.OrderService;
import hello2.core.order.OrderServiceImpl;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration//@Configuration 애노테이션을 사용하면 가시적으로 설정파일이야 ~ , Bean 등록할꺼야 ~ 라는건 알수있다.(설정 정보)
public class AppConfig {//AppConfig 를 통해서 관심사를 확실하게 분리
//프로그램의 제어 흐름을 직접 제어하는 것이 아니라 외부에서 관리하는것을 제어의 역전 loC 라고 한다.
    @Bean//스프링 컨테이너 등록
    public MemberService memberService(){
        System.out.println("call AppConfig.memberService");
        return new MemberServiceImpl(memberRepository());
    }
    @Bean
    public MemberRepository memberRepository(){
        System.out.println("call AppConfig.memberRepository");
        return new MemoryMemberRepository();
    }
    @Bean
    public OrderService orderService(){
        System.out.println("call AppConfig.orderService");
        return new OrderServiceImpl(memberRepository(),discountPolicy());
    }
    @Bean
    public DiscountPolicy discountPolicy(){
        return new RateDiscountPolicy();
    }


}
//@Bean이 붙은 메서드마다 이미 스프링 빈이 존재하면 존재하는 빈을 반환하고, 스프링 빈이 없으면
//생성해서 스프링 빈으로 등록하고 반환하는 코드가 동적으로 만들어진다.
//덕분에 싱글톤이 보장되는 것이다.
//@Bean만 사용해도 스프링 빈으로 등록되지만, 싱글톤을 보장하지 않는다.
//memberRepository() 처럼 의존관계 주입이 필요해서 메서드를 직접 호출할 때 싱글톤을 보장하지
//않는다.
//크게 고민할 것이 없다. 스프링 설정 정보는 항상 @Configuration 을 사용하자