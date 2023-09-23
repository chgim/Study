package com.mysite.sbb.user;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
@Service
public class UserService {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;
    public SiteUser create(String username, String email, String password) {
        SiteUser user = new SiteUser();
        user.setUsername(username);
        user.setEmail(email);
        // BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();
        // user.setPassword(passwordEncoder.encode(password));
        user.setPassword(passwordEncoder.encode(password));
        this.userRepository.save(user);
        return user;
    }
}
/*User 서비스에는 User 리포지터리를 사용하여 User 데이터를 생성하는 create 메서드를 추가했다.
이 때 사용자의 비밀번호는 보안을 위해 반드시 암호화하여 저장해야 한다. 암호화를 위해 시큐리티의 BCryptPasswordEncoder 클래스를 사용하여 암호화하여 비밀번호를 저장했다.
BCryptPasswordEncoder는 BCrypt 해싱 함수(BCrypt hashing function)를 사용해서 비밀번호를 암호화한다.
하지만 이렇게 BCryptPasswordEncoder 객체를 직접 new로 생성하는 방식보다는 PasswordEncoder 빈(bean)으로 등록해서 사용하는 것이 좋다. 왜냐하면 암호화 방식을 변경하면 BCryptPasswordEncoder를 사용한 모든 프로그램을 일일이 찾아서 수정해야 하기 때문이다.*/
// BCryptPasswordEncoder 객체를 직접 생성하여 사용하지 않고 빈으로 등록한 PasswordEncoder 객체를 주입받아 사용