package SpringStudy.Project1;

import SpringStudy.Project1.repository.MemberRepository;
import SpringStudy.Project1.repository.MemoryMemberRepository;
import SpringStudy.Project1.service.MemberService;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;


//자바 코드로 직접 스프링 빈 등록하기
@Configuration
public class SpringConfig { //SpringBean 에 등록. 등록된 memberRepository 를 memberService 에 넣어줌
    @Bean
    public MemberService memberService(){
        return new MemberService(memberRepository());
    }
    @Bean
    public MemberRepository memberRepository(){
        return new MemoryMemberRepository();
    }
}
//실무에서는 주로 정형화된 컨트롤러, 서비스, 리포지토리 같은 코드는 컴포넌트 스캔을 사용한다.
//그리고 정형화 되지 않거나, 상황에 따라 구현 클래스를 변경해야 하면 설정을 통해 스프링 빈으로 등록한다. ex) 데이터 저장소(repository 변경)
