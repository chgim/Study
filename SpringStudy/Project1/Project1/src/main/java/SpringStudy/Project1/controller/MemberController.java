package SpringStudy.Project1.controller;


import SpringStudy.Project1.domain.Member;
import SpringStudy.Project1.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import java.util.List;

@Controller
public class MemberController { //컨트롤러가 MemberService 를 통해서 회원가입, 데이터 조회. -> 의존관계
    private final MemberService memberService;

    @Autowired
    //생성자에 @Autowired 를 넣으면  MemberController 가 생성될 때 SpringBean에 등록되어 있는 MemberService 객체를 넣어줌. dependency injection
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }

    @GetMapping("/members/new")
    public String createForm(){
        return "members/createMemberForm";
    }
    @PostMapping("/members/new")
    public String create(MemberForm form){
        Member member=new Member();
        member.setName(form.getName());

        memberService.join(member);
        return "redirect:/";
    }
    @GetMapping("/members")
    public String list(Model model){
        List<Member> members=memberService.findMembers();
        model.addAttribute("members", members);
        return "members/memberList";
    }

}
    /* 생성자에 @Autowired 가 있으면 스프링이 연관된 객체를 스프링 컨테이너에서 찾아서 넣어준다. 이렇게
    객체 의존관계를 외부에서 넣어주는 것을 DI (Dependency Injection), 의존성 주입이라 한다.
    이전 테스트에서는 개발자가 직접 주입했고, 여기서는 @Autowired에 의해 스프링이 주입해준다 */

    /*스프링은 스프링 컨테이너에 스프링 빈을 등록할 때, 기본으로 싱글톤으로 등록한다(유일하게 하나만
    등록해서 공유한다) 따라서 같은 스프링 빈이면 모두 같은 인스턴스다.*/

    /*@Component 애노테이션이 있으면 스프링 빈으로 자동 등록된다.
    @Controller 컨트롤러가 스프링 빈으로 자동 등록된 이유도 컴포넌트 스캔 때문이다*/