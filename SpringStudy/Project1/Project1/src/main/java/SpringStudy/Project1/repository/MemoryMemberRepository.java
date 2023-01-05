package SpringStudy.Project1.repository;

import SpringStudy.Project1.domain.Member;
import org.springframework.stereotype.Repository;

import java.util.*;

//@Repository
public class MemoryMemberRepository implements MemberRepository{

    private static Map<Long, Member> store=new HashMap<>();
    private static long sequence=0L; //0,1,2 key 값 생성

    @Override
    public Member save(Member member) {
        member.setId(++sequence);
        store.put(member.getId(), member);
        return member;
    }

    @Override
    public Optional<Member> findById(Long id) {
        return Optional.ofNullable(store.get(id));
    }

    @Override
    public Optional<Member> findByName(String name) {
        return store.values().stream()
                    .filter(member->member.getName().equals(name)) //member.getName() 이 파라미터로 넘어온 name 과 같은지 확인
                    .findAny(); //하나라도 있으면 찾기

    }

    @Override
    public List<Member> findAll() {
        return new ArrayList<>(store.values()); //member 반환
    }

    public void clearStore(){
        store.clear();
    }
}
