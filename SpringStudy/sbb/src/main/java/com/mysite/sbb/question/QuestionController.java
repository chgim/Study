package com.mysite.sbb.question;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.data.domain.Page;
import java.util.List;
import org.springframework.security.access.prepost.PreAuthorize;
import java.security.Principal;
import com.mysite.sbb.user.SiteUser;
import com.mysite.sbb.user.UserService;
import javax.validation.Valid;
import org.springframework.validation.BindingResult;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import com.mysite.sbb.answer.AnswerForm;
@RequestMapping("/question")
@Controller
@RequiredArgsConstructor // questionRepository 속성을 포함하는 생성자를 생성. 롬복이 제공하는 애너테이션으로 final이 붙은 속성을 포함하는 생성자를 자동으로 생성
public class QuestionController {

    private final QuestionService questionService;
    private final UserService userService;

    @GetMapping("/list")
    public String list(Model model, @RequestParam(value="page", defaultValue="0") int page) {
        Page<Question> paging = this.questionService.getList(page);
        model.addAttribute("paging", paging);
        return "question_list";
    }
//http://localhost:8080/question/list?page=0 처럼 GET 방식으로 요청된 URL에서 page값을 가져오기 위해 @RequestParam(value="page", defaultValue="0") int page 매개변수가 list 메서드에 추가되었다. URL에 페이지 파라미터 page가 전달되지 않은 경우 디폴트 값으로 0이 되도록 설정했다.
    @GetMapping(value = "/detail/{id}")
    public String detail(Model model, @PathVariable("id") Integer id,  AnswerForm answerForm) { // 변하는 id 값을 얻을 때에는 위와 같이 @PathVariable 애너테이션을 사용. @GetMapping(value = "/question/detail/{id}") 에서 사용한 id와 @PathVariable("id")의 매개변수 이름이 동일해야 한다.
        Question question = this.questionService.getQuestion(id);
        model.addAttribute("question", question);
        return "question_detail";
    }
// QuestionController의 GetMapping으로 매핑한 메서드도 다음과 같이 변경해야 한다. 왜냐하면 question_form.html 템플릿은 "질문 등록하기" 버튼을 통해 GET 방식으로 요청되더라도 th:object에 의해 QuestionForm 객체가 필요하기 때문이다.
// GET 방식에서도 question_form 템플릿에 QuestionForm 객체가 전달될 것이다.
    @PreAuthorize("isAuthenticated()")
    @GetMapping("/create")
    public String questionCreate(QuestionForm questionForm) {
        return "question_form";
    }
    @PreAuthorize("isAuthenticated()")
    @PostMapping("/create")
    public String questionCreate(@Valid QuestionForm questionForm, BindingResult bindingResult, Principal principal) { // questionCreate 메서드의 매개변수를 subject, content 대신 QuestionForm 객체로 변경했다. subject, content 항목을 지닌 폼이 전송되면 QuestionForm의 subject, content 속성이 자동으로 바인딩 된다. 이것은 스프링 프레임워크의 바인딩 기능이다.
        if (bindingResult.hasErrors()) {
            return "question_form";
        }
        SiteUser siteUser = this.userService.getUser(principal.getName());
        this.questionService.create(questionForm.getSubject(), questionForm.getContent(),siteUser);
        return "redirect:/question/list";
    }
//@GetMapping("/question/list")
//public String list() {
//    return "question_list";
//}
}
/*스프링의 의존성 주입(Dependency Injection) 방식 3가지
@Autowired 속성 - 속성에 @Autowired 애너테이션을 적용하여 객체를 주입하는 방식
생성자 - 생성자를 작성하여 객체를 주입하는 방식 (권장하는 방식)
Setter - Setter 메서드를 작성하여 객체를 주입하는 방식 (메서드에 @Autowired 애너테이션 적용이 필요하다.)*/

// Model 객체는 따로 생성할 필요없이 컨트롤러 메서드의 매개변수로 지정하기만 하면 스프링부트가 자동으로 Model 객체를 생성

/*Valid 애너테이션을 적용하면 QuestionForm의 @NotEmpty, @Size 등으로 설정한 검증 기능이 동작한다.
 그리고 이어지는 BindingResult 매개변수는 @Valid 애너테이션으로 인해 검증이 수행된 결과를 의미하는 객체이다.*/