package hello2.core.scan.filter;


import java.lang.annotation.*;

@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface MyExcludeComponent {
        

}

//includeFilters : 컴포넌트 스캔 대상을 추가로 지정한다.
//excludeFilters : 컴포넌트 스캔에서 제외할 대상을 지정한다.