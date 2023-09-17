package com.mysite.sbb;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller //스프링부트 프레임워크가 컨트롤러로 인식
public class HelloController {
    @GetMapping("/hello") //http://localhost:8080/hello URL 요청이 발생하면 hello 메서드가 실행, Get 방식의 URL 요청은 GetMapping을 사용하고 Post 방식의 URL 요청은 PostMapping을 사용
    @ResponseBody // hello 메서드의 응답 결과가 문자열 그 자체임을 나타냄
    public String hello() {
        return "Hello";
    }
}
