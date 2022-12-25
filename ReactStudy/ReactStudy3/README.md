### 라우팅이란
+ 사용자가 요청한 URL에 따라 해당 URL에 맞는 페이지를 보여주는 것
+ 리액트 라우터(React Router) 라이브러리 사용
### SPA vs MPA
+ SPA(Single Page Application)는 한 개(Single)의 Page로 구성된 Application이다.
+ MPA(Multiple Page Application)는 여러 개(Single)의 Page로 구성된 Application이다.
+ MPA는 새로운 페이지를 요청할 때마다 정적 리소스가 다운로드된다. 매번 전체 페이지가 다시 렌더링 된다.  
  반면 SPA는 웹 에플리케이션에 필요한 모든 정적 리소스를 최초 한 번에 다운로드한다.  
  그 이후 새로운 페이지 요청이 있을 때, 페이지 갱신에 필요한 데이터만 전달 받아서 페이지를 갱신한다.  
+ 그래서 SPA를 CSR(Client Side Rendering) 방식으로 렌더링한다고 말한다.  
  그래서 MPA를 SSR(Server Side Rendering) 방식으로 렌더링한다고 말한다.  
### 리액트는 SPA (Single Page Application) 방식
+ 기존 웹 페이지 처럼(MPA 방식) 여러개의 페이지를 사용, 새로운 페이지를 로드하는 방식이 아니다.
+ 새로운 페이지를 로드하지 않고 하나의 페이지 안에서 필요한 데이터만 가져오는 형태를 가진다.
### 리액트 라우터
+ 사용자가 입력한 주소를 감지하는 역할을 하며, 여러 환경에서 동작할 수 있도록 여러 종유의 라우터 컴포넌트를 제공
+ 여러 페이지로 구성된 프로젝트 제작 가능
+ 손쉽게 싱글 페이지 애플리케이션 제작 가능
### 싱글 페이지 애플리케이션
 기술적으로는 한 페이지만 존재하는 것이지만, 사용자가 경험하기에는 여러 페이지가 존재하는 것 처럼 느낄 수 있음
### Query String
```js run
/users?id=123 # Fetch a user who has id of 123 
```
+ ? 뒤에 id란 변수에 값을 담아 백엔드에 전달하는 방식  
+ searchParams 는 .get() 을 통해서 전달 받은 Query String 을 꺼내서 쓸 수 있는 용도로 사용  
+ setSearchParams 는 searchParams 를 변경 시키는 기능
### Path Variable
```js run
/users/123 # Fetch a user who has id 123
```
+ 경로의 변수를 사용
+ URL에 변수를 담아서 전달하는 방법
+ useParams 사용
### Page Moving
```js run
const navigate = useNavigate();
navigate('/home');
```
+ 페이지를 이동 시킬 수 있는 기능
+ useNavigate 라는 훅은 페이지를 이동 시킬 수 있는 기능을 하는 함수를 하나 반환을 하는데,  
  함수의 이름을 navigate 라고 받고 navigate 의 인자로 경로를 작성을 하면  
  호출을 해서 경로를 옮길 수 있다.
+ Link 태그를 클릭 안했을 경우에도 의도적으로 페이지를 바꿀 수 있다.