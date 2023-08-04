package com.example.loginpractice.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import com.example.loginpractice.domain.user.User;

import java.util.Optional;

public interface UserRepo extends JpaRepository<User, Long> {
    Optional<User> findByEmail(String email);
}
