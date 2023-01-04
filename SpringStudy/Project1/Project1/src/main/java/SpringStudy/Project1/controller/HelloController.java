package SpringStudy.Project1.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class HelloController {
    @GetMapping("hello") //url 에 /hello
    public String hello(Model model) {
        model.addAttribute("data", "hello!!");
        return "hello"; //resources / templates / hello 로 넘겨주기
    }//컨트롤러에서 리턴 값으로 문자를 반환하면 뷰 리졸버( viewResolver )가 화면을 찾아서 처리한다

    @GetMapping("hello-mvc")
    public String helloMvc(@RequestParam(value = "name") String name, Model model) {
        model.addAttribute("name", name);
        return "hello-template";
    }//http://localhost:8080/hello-mvc?name=spring  <-- 링크 name=에 값 넣기

    @GetMapping("hello-string")
    @ResponseBody
    public String helloString(@RequestParam("name") String name) {
        return "hello" + name; //hello spring
        //view 가 없고 그대로 데이터를 내려줌

    }

    @GetMapping("hello-api")
    @ResponseBody
    public Hello helloApi(@RequestParam("name") String name) {
        Hello hello = new Hello();
        hello.setName(name);
        return hello; //객체를 반환. json 방식으로 데이터 만들어서 html 에 반환
    }

    static class Hello {
        private String name;

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }
        
    }
//@ResponseBody 를 사용하면 뷰 리졸버( viewResolver )를 사용하지 않음
//대신에 HTTP의 BODY에 문자 내용을 직접 반환(HTML BODY TAG를 말하는 것이 아님)
//@ResponseBody 를 사용하고, 객체를 반환하면 객체가 JSON으로 변환됨
}

