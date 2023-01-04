package SpringStudy.Project1.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HelloController {
    @GetMapping("hello") //url 에 /hello
    public String hello(Model model){
    model.addAttribute("data", "hello!!");
    return "hello"; //resources / templates / hello 로 넘겨주기
    }
}
