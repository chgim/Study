# 리액트 개념정리
## 참고하기 좋은 사이트: https://react.vlpt.us/basic/07-useState.html
<strong>MVC</strong>(Model-View-Controller)  
<strong>MVVM</strong>(Model-View-View-Model)  
<strong>Model</strong>: 애플리케이션에서 사용하는 데이터를 관리하는 영역  
<strong>View</strong>: 사용자에게 보이는 부분  
<strong>Controller</strong>: 프로그램이 사용자에게 어떤 작업을 받으면 모델데이터를 조회, 수정, 변경된 사항을 View에 반영  
## 리액트
- 자바스크립트 라이브러리로써 사용자 인터페이스를 만들기 위해 사용된다.
- facebook에서 제공
- 오직 View만 신경 쓰는 라이브러리
## 리액트 사용 이유
- 컴포넌트 기반의 UI 라이브러리
- 선언형 프로그래밍
- Virtual DOM
## 컴포넌트
- 특정 부분이 어떻게 생길지 정하는 선언체
- 재사용이 가능한 API
- 컴포넌트 하나에서 해당 컴포넌트의 생김새와 작동방식을 정의
- 컴포넌트에서의 데이터 변화->새로운 요소로 갈아 끼운 것. 
- 리액트는 단반향으로만 데이터가 흐른다.
## 엘리먼트
- 컴포넌트의 구성요소
- React앱의 가장 작은 단위
## 렌더링
- 사용자 화면에 뷰를 보여주는 것.
- 어떤 프레임워크, 라이브러리를 사용하던지 초기 렌더링이 필요.
- 리액트에서는 이를 다루는 render 함수 존재. render(){…}
## Render 함수
- 컴포넌트가 어떻게 생겼는지 정의  
- Html 형식의 문자열 반환 x 뷰가 어떻게 생겼고 어떻게 작동하는지에 대한 정보를 지닌 객체 반환
- 컴포넌트 내부에는 또 다른 컴포넌트가 들어갈 수 있음
- Render 함수를 실행하면 내부의 컴포넌트들도 재귀적 렌더링
## DOM(Document Object Model)
- 객체로 문서 구조를 표현하는 방법. 트리 형태라서 특정 노드를 찾거나 수정, 제거, 원하는 곳에 삽입 가능.
## Virtual DOM
- DOM을 추상화한 가상의 객체(가상의 DOM)
- 브라우저에 실제로 보여지는 DOM 이 아니라 그냥 메모리에 가상으로 존재하는 DOM 으로서 그냥 JavaScript 객체.  
## JSX
- 리액트로 프로젝트를 개발시에 사용. 공식적 자바스크립트 문법은 아님.
- 자바스크립트 확장 문법
- DOM 요소 렌더링


### 문법
#### 컴포넌트에 여러 요소가 있다면 반드시 부모 요소 하나로 감싸야 한다.
#### 코드를 {}로 감싸 JSX 안에 자바스크립트 표현식 사용 가능
#### if문 대신 조건부 연산자
JSX 내부의 자바스크립트 표현식에서는 if문을 사용하지 않고 삼항연산자 사용
```js run
function App(){
    const name='리액트';
    return(
        <div>
        {name==='리액트'?(
            <h1>리액트입니다.</h1>
        ):(
            <h2>리액트가 아닙니다.</h2>
        )}
        </div>
        );
        }
```
#### AND 연산자(&&)를 사용한 조건부 렌더링
```js run
function App(){
    const name='리액트';
    return(
        <div>
        {name==='리액트'&&<h1>리액트입니다.</h1>}
        </div>
        );
        }
```
&&연산자로 조건부 렌더링을 할 수 있는 이유는 리액트에서 false를 렌더링 할 때에는 null과 마찬가지로 아무것도 나타나지 않기 때문.
예외적으로 falsy한 값인 0은 화면에 나타남.
#### undefined를 렌더링 하지 않기
함수에서 undefined만 반환하여 렌더링 x
```js run
function App(){
    const name=undefined;
    return name;
        }//오류
```
#### OR 연산자(||)
```js run
function App(){
    const name=undefined;
    return name||'값이 undefined입니다.';
        }
```
#### 인라인 스타일링
리액트에서 DOM 요소에 스타일을 적용할 때는 문자열 형태로 넣는 것이 아니라 객체 형태로 넣어준다.
background-color -> backgroundColor(카멜 표기법)
#### class 대신 className
일반 html에서 css 사용 시 <div class="ds"></div>와 같이 class라는 속성 설정.
JSX에서는 class가 아닌 className으로 설정
```js run
function App(){
    const name=리액트;
    return <div className="react">{name}</div>;
        }
```
## 함수형 컴포넌트와 클래스형 컴포넌트
함수형 컴포넌트
```js run
funciton App(){
    const name='리액트';
    return <div className="react">{name}</div>;
}
```
클래스형 컴포넌트
```js run
import React, {Component} from 'react';

class App extends Component{
    render(){
        const name='react';
        return <div className="react">{name}</div>;
    }
}
```
클래스형 컴포넌트는 {Component} import 필요  
render 함수 필요

## props와 state
<strong>React에서 구성 요소가 데이터를 받거나 처리하고 보내기 위해 사용됨.</strong>
### props
- 불변의 데이터
- 부모로부터 전달됨
- 변경 불가
### state(상태)
- 가변 데이터(동적)
- 구성요소에 의해 유지
- 변경 가능

<strong>State</strong>는 내부 (컴포넌트)에서 생성하고 활동하고, 데이터를 변경할 수 있음.
<strong>Props</strong>는 외부(부모 컴포넌트)에서 상속 받는 데이터이며, 데이터를 변경할 수 없음.

