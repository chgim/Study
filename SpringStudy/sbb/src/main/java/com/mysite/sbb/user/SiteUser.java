package com.mysite.sbb.user;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@Entity
public class SiteUser {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(unique = true)
    private String username;

    private String password;

    @Column(unique = true)
    private String email;
}
/*엔티티명을 User 대신 SiteUser로 한 이유는 스프링 시큐리티에 이미 User 클래스가 있기 때문이다.
 물론 패키지명이 달라 User라는 이름을 사용할수 있지만 패키지 오용으로 인한 오류가 발생할수 있으므로 이 책에서는 User 대신 SiteUser라는 이름으로 명명*/