## 7주차

- 미디어쿼리 사용법

```dart run
width: MediaQuery.of(context).size.height * 0.5
```

- 상태: 화면에 나타나는 변수 중 지속적으로 변하는 데이터. 이벤트에 의해 변화.
- 이벤트: 상태의 변화를 발생시키는 동작
- enum(열거형)
  - 어떤 상수들의 집합. 여기에 선언해놓은 상수들은 어떤 자료형의 값을 사용하듯 가져다 쓸 수 있음.
  - 자료형 A를 선언하고 이 자료형이 가질 수 있는 값으로 a, b, c를 할당시켜 A 자료형에 대해 정의 가능.
  - enum은 코드의 직관성을 상승시킴.
- late: 초기값을 설정해야 하는 변수의 초기화를 나주에 하겠다는 키워드.
- initState(): 상태값 초기화. 위젯이 빌드되고 바로 실행되는, 초기 실행 메서드.
- Timer.periodic(Duration duration, Timer t) -> 단위 시간마다 코드를 실행. import dart: async; 필수. 외부 영역에서 데이터를 불러오는데 시간이 걸려 설정 하기도 함
- sprintf: 문자열 포맷팅
- Toast: 화면에 잠깐 나타났다가 사라지는 작은 메시지

## 9주차

- 프론트엔드 / 백엔드
- Html: 하이퍼텍스트 + 마크업 언어
- css: 종속 스타일 시트
- JavaScript: Html과 css를 통해 만들어진 웹페이지가 동작 하도록 만들어줌. 객체 기반 언어.
- php: 서버와 브라우저간의 다리.
- c++: c언어 발전된 버전.
- java: 객체 기반 프로그래밍 언어
- python: 빠르고 효율적
- providers 폴더: 데이터 관련 기능을 제공
- sharedPreference
  - 저장해야 하는 데이터의 양이 적거나 아주 간단한 경우 사용
  - 키-값 방식.
  - 기기 내 xml 파일을 통해 앱에 대한 간단한 데이터 저장
- iOS의 UserDefaults와 Flutter의 SharedPreferences의 차이
  - 언어와 플랫폼
  - 데이터 저장
  - 데이터 접근성
  - API 및 사용법
  - 타입 안정성
- SplashScreen
  - 앱을 처음 켰을 때 브랜드 로고가 나타나는 일종의 인트로 화면.
  - 로고를 보여주는 시간 동안 필요한 정보를 로드.
- 시간이 소요되는 기능 구현 시 비동기(async-await)로 구성.
  - 다음 수행해야 할 일은 .then()으로 선언.
  - 비동기 -> Future 타입 함수
- sqlite
  - 관계형 데이터베이스(RDBMS)
  - 경량화 된 데이터베이스 SW
  - Serverless
  - 독립실행형: 운영 체제나 외부 라이브러리의 지원이 최소한으로 필요
  - Zero-configuration: 서버리스 아키텍처 -> SQLite 설치 필요 X
  - 트랜잭션 처리: 모든 트랙잭션은 완전히 ACID 준수 Atomic, Consistent, Isolated, Durable. All or Nothing
- toMap(): Todo 데이터를 외부로 보내기 위한 양식을 맞춤
- fromMap(): 네트워크 호출을 통해 받아오는 데이터를 Todo 모델로 변환. 데이터의 양식은 Json.

```dart run
 Map<String, dynamic> toMap() {
    return {
      'id': id,
      'title': title,
      'description': description,
    };
  }

  Todo.fromMap(Map<dynamic, dynamic>? map) {
    id = map?['id'];
    title = map?['title'];
    description = map?['description'];
  }
```

- ListView.separated: List의 각 요소들 사이에 구분자를 넣어주는 기능. separatorBuilder 옵션에서 설정 가능.
- AlertDialog: 화면 전환 없이 다이얼로그 형태로 띄워 바로 입력 가능.(팝업). 확인/ 취소 버튼 존재.
  - TextField: 값 입력
- SimpleDialog: 확인 / 취소 버튼이 없는 Todo 내용만 표현하기 적합한 다이얼로그

## 10주차

- Firebase: 구글의 BaaS(Backend asa Service). 백엔드 구현을 알아서 해줌.
- Firestore: Firebase의 저장소, 데이터베이스 역할.
  - NoSQL 기반. 테이블 구조가 아닌 문서의 형태로 저장.
- NoSQL 장점
  - 비용 효율성
  - 유연성
  - 복제
  - 속도

## 11주차

- Firebase 프로젝트: 하나 이상의 Firebase 앱을 등록 가능. 최상위 항목.
- Firebase 식별자: 프로젝트 이름 / 프로젝트 번호 / 프로젝트 ID ...
- Firebase 최소 옵션: API 키 / 프로젝트 ID / 애플리케이션 ID
- 배포 파이프라인: 개발-테스트-시연-배포
- Firebase 보안 체크리스트
  - 악성 트래픽 방지
  - API 키 이해
  - 보안 규칙
  - 환경 관리
  - 라이브러리 관리
  - Cloud 함수의 안전성
- 설치 인증 토큰 != Firebase 인증 토큰
- 설치 인증 토큰: JWT 형식의 단기 Bearer 토큰. 기본 수명 1주일
  - Firebase 설치 ID
  - 연결된 프로젝트
  - 연결된 Firebase 애플리케이션 ID
  - 토큰의 만료일
- Google Clout BigQuery를 사용하여 세크먼트 데이터를 Firebase로 가져옴.
  BigQuery는 데이터를 로드하는 여러 방법 제공.

## 12주차
