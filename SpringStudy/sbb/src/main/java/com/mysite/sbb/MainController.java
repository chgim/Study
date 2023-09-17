package com.mysite.sbb;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;
@Controller
public class MainController {
// @ResponseBody 애너테이션은 URL 요청에 대한 응답으로 문자열을 리턴하라는 의미
// 만약 @ResponseBody 애너테이션을 생략한다면 "index"라는 이름의 템플릿 파일을 찾게 됨
    @GetMapping("/sbb")
    @ResponseBody
    public String index() {
        return "index";
    }
}