package com.example.loginpractice.config;

import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.authentication.AuthenticationProvider;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@Configuration
@RequiredArgsConstructor
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    private final AuthenticationProvider authenticationProvider;

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        // http basic 방식 사용함
        http
                .cors().disable()
                .csrf().disable()

                .httpBasic().disable();

        // 엔드포인트 권한 설정
        http.authorizeRequests()
                .mvcMatchers("/").permitAll()
                .mvcMatchers("/login").permitAll()
                .anyRequest().authenticated();

        // FormLogin
        http.formLogin()
                .loginPage("/login")
                .loginProcessingUrl("/auth/login")
                .usernameParameter("email")
                .passwordParameter("password");

        // .loginPage("/login") // 사용자 커스텀한 로그인 페이지 URL 지정
        // // /auth/login < AuthenticationFilter
        // .loginProcessingUrl("/auth/login");

    }

    @Override //custom 하겠다. customAuthenticationProvider 사용
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        auth.authenticationProvider(authenticationProvider);

    }

}