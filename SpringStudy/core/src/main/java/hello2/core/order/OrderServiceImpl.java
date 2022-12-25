package hello2.core.order;

import hello2.core.annotation.MainDiscountPolicy;
import hello2.core.discount.DiscountPolicy;
import hello2.core.discount.FixDiscountPolicy;
import hello2.core.discount.RateDiscountPolicy;
import hello2.core.member.Member;
import hello2.core.member.MemberRepository;
import hello2.core.member.MemoryMemberRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;
//롬복 라이브러리가 제공하는 @RequiredArgsConstructor 기능을 사용하면 final이 붙은 필드를 모아서
//생성자를 자동으로 만들어준다. (다음 코드에는 보이지 않지만 실제 호출 가능하다.)
@Component
//@RequiredArgsConstructor//롬복 생성자 자동 생성
public class OrderServiceImpl implements OrderService {

    // private final DiscountPolicy discountPolicy=new FixDiscountPolicy();
    // private final DiscountPolicy discountPolicy=new RateDiscountPolicy();

    private  final MemberRepository memberRepository;
    private final DiscountPolicy discountPolicy;//final:값이 할당 되어야 함//인터페이스에만 의존 DIP
    //이 문제를 해결하려면 누군가가 클라이언트인 OrderServiceImpl 에 DiscountPolicy 의 구현 객체를
    //대신 생성하고 주입해주어야 한다.
    //생성자 주입
    //생성자 호출시점에 딱 1번만 호출되는 것이 보장된다.
    //불변, 필수 의존관계에 사용
    //생성자가 딱 1개만 있으면 @Autowired를 생략해도 자동 주입 된다.
    /*
    @Autowired
    public void setMemberRepository(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }
    @Autowired
    public void setDiscountPolicy(DiscountPolicy discountPolicy) {
        this.discountPolicy = discountPolicy;
    }
    */
    //수정자 주입(setter 주입)
    //setter라 불리는 필드의 값을 변경하는 수정자 메서드를 통해서 의존관계를 주입하는 방법이다.
    //선택, 변경 가능성이 있는 의존관계에 사용
    //자바빈 프로퍼티 규약의 수정자 메서드 방식을 사용하는 방법이다.


    @Autowired
    public OrderServiceImpl(MemberRepository memberRepository, @MainDiscountPolicy DiscountPolicy discountPolicy) {
        this.memberRepository = memberRepository;
        this.discountPolicy = discountPolicy;
    }

    @Override
    public Order createOrder(Long memberId, String itemName, int itemPrice) {
        Member member=memberRepository.findById(memberId);
        int discountPrice= discountPolicy.discount(member, itemPrice);
        return new Order(memberId, itemName, itemPrice, discountPrice);

    }
    //테스트 용도
    public MemberRepository getMemberRepository() {
        return memberRepository;
    }
}
