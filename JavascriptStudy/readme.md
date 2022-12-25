# JavaScript 개념 정리

## var, let, const 차이점

- var
  - 변수 재선언(중복 선언) 가능
  - let, const는 불가능

```js run
var name = "A";
var name = "B"; //o
```

- var, let
  - 값의 재할당 가능
  - const는 불가능

```js run
var a = 10;
var a = 20; //o

let b = 20;
let b = 30; //o
```

## 템플릿 리터럴

내장된 표현식을 허용하는 문자열 리터럴  
템플릿 리터럴은 표현식/문자열 삽입, 여러 줄 문자열, 문자열 형식화, 문자열 태깅 등 다양한 기능을 제공

### Syntax

```js run
`string text``string text line 1
 string text line 2``string text ${expression} string text`;
tag`string text ${expression} string text`;
```

템플릿 리터럴은 작은따옴표(')나 큰따옴표(") 대신 백틱(`)으로 감싸준다.

### 표현식

템플릿 리터럴에서는 아래와 같이 $와 중괄호{}를 사용하여 표현식을 표기할 수 있다.

```js run
let a = 20;
let b = 8;
let c = "자바스크립트";
let str = `저는 ${a + b}살이고 ${c}를 좋아합니다.`;
console.log(str); //저는 28살이고 자바스크립트를 좋아합니다.
```

## 비교 연산자

```js run
let compareA = 1 == "1";
console.log(compareA);
```

동등 연산자 ==를 사용하여 비교를 하면 값만 비교하기 때문에 자료형이 다르더라도 결과는 true가 나온다.

```js run
let compareA = 1 === "1";
console.log(compareA);
```

일치 연산자 ===를 사용하여 비교를 하면 값 뿐만 아니라 자료형의 동등 여부까지 검사하기 때문에 결과는 false가 나온다.

## nullish 병합 연산자 '??'

```js run
let a;
a = a ?? 10;
console.log(a);
```

값이 없다면 10을 대입하고 값이 있다면 그 값을 대입
a ?? b -> a가 null도 아니고 undefined도 아니면 a , 그 외의 경우에는 b

## 다중'?'

물음표 연산자?를 여러 개 연결하면 복수의 조건을 처리 가능

```js run
let age = prompt("나이를 입력해주세요.", 18);

let message =
  age < 3
    ? "아기야 안녕?"
    : age < 18
    ? "안녕!"
    : age < 100
    ? "환영합니다!"
    : "나이가 아주 많으시거나, 나이가 아닌 값을 입력 하셨군요!";

alert(message);
```

## 함수 표현식

기존 함수 선언

```js run
function sayHi() {
  alert("Hello");
}
```

함수 표현식

```js run
let sayHi = function () {
  alert("Hello");
};
```

### 끝에 세미콜론이 있는 이유

```js run
function sayHi() {
  // ...
}

let sayHi = function () {
  // ...
};
```

if { ... }, for { }, function f { } 같이 중괄호로 만든 코드 블록 끝엔 ;이 없어도 된다.  
함수 표현식은 let sayHi = ...;과 같은 구문 안에서 값의 역할을 한다. 코드 블록이 아니고 값처럼 취급되어 변수에 할당.  
모든 구문의 끝엔 세미 콜론 ;을 붙이는 게 좋다. 함수 표현식에 쓰인 세미 콜론은 함수 표현식 때문에 붙여진 게 아니라, 구문의 끝이기 때문에 붙여졌다.

## 호이스팅

함수 안에 있는 선언들을 모두 끌어올려서 해당 함수 유효 범위의 최상단에 선언하는 것을 말한다.

### 호이스팅이란

- 자바스크립트 함수는 실행되기 전에 함수 안에 필요한 변수값들을 모두 모아서 유효 범위의 최상단에 선언한다.
  - 자바스크립트 Parser가 함수 실행 전 해당 함수를 한 번 훑는다.
  - 함수 안에 존재하는 변수/함수선언에 대한 정보를 기억하고 있다가 실행시킨다.
  - 유효 범위: 함수 블록 {} 안에서 유효
- 즉, 함수 내에서 아래쪽에 존재하는 내용 중 필요한 값들을 끌어올리는 것이다.
  - 실제로 코드가 끌어올려지는 건 아니며, 자바스크립트 Parser 내부적으로 끌어올려서 처리하는 것이다.
  - 실제 메모리에서는 변화가 없다.

### 호이스팅의 대상

- var 변수 선언과 함수선언문에서만 호이스팅이 일어난다.
  - var 변수/함수의 선언만 위로 끌어 올려지며, 할당은 끌어 올려지지 않는다.
  - let/const 변수 선언과 함수표현식에서는 호이스팅이 발생하지 않는다.

```js run
console.log("hello");
var myname = "HEEE"; // var 변수
let myname2 = "HEEE2"; // let 변수
/** --- JS Parser 내부의 호이스팅(Hoisting)의 결과 - 위와 동일 --- */
var myname; // [Hoisting] "선언"
console.log("hello");
myname = "HEEE"; // "할당"
let myname2 = "HEEE2"; // [Hoisting] 발생 X
```

### 함수표현식에서의 호이스팅

함수 표현식의 선언이 호출보다 위에 있는 경우: 정상출력

```js run
/* 정상 */
function printName(firstname) {
  // 함수선언문
  var inner = function () {
    // 함수표현식
    return "inner value";
  };

  var result = inner(); // 함수 "호출"
  console.log("name is " + result);
}

printName(); // > "name is inner value"
```

함수 표현식의 선언이 호출보다 아래에 있는 경우: 에러

```js run
/* 오류 */
function printName(firstname) {
  // 함수선언문
  console.log(inner); // > "undefined": 선언은 되어 있지만 값이 할당되어있지 않은 경우
  var result = inner(); // ERROR!!
  console.log("name is " + result);

  var inner = function () {
    // 함수표현식
    return "inner value";
  };
}
printName(); // > TypeError: inner is not a function
```

## 화살표 함수

### 기존 코드

```js run
let func = function (arg1, arg2, ...argN) {
  return expression;
};
```

### 화살표 함수 적용

```js run
let func = (arg1, arg2, ...argN) => expression;
```

예시 1)

```js run
let sum = (a, b) => a + b;
alert(sum(1, 2)); // 3
```

예시 2)

```js run
let sayHi = () => alert("안녕하세요!");
sayHi();
```

예시 3)

```js run
let age = prompt("나이를 알려주세요.", 18);

let welcome = age < 18 ? () => alert("안녕") : () => alert("안녕하세요!");

welcome();
```

## 콜백 함수

```js run
*!*
function ask(question, yes, no) {
  if (confirm(question)) yes()
  else no();
}
*/!*

function showOk() {
  alert( "동의하셨습니다." );
}

function showCancel() {
  alert( "취소 버튼을 누르셨습니다." );
}

// 사용법: 함수 showOk와 showCancel가 ask 함수의 인수로 전달됨
ask("동의하십니까?", showOk, showCancel);
```

**함수 `ask`의 인수, `showOk`와 `showCancel`은 _콜백 함수_ 또는 *콜백*이라고 불린다.**

함수를 함수의 인수로 전달하고, 필요하다면 인수로 전달한 그 함수를 "나중에 호출(called back)"하는 것이 콜백 함수의 개념.
위 예시에선 사용자가 "yes"라고 대답한 경우 `showOk`가 콜백이 되고, "no"라고 대답한 경우 `showCancel`가 콜백이 된다.

## 객체

- 객체는 중괄호{...}를 이용해 만들 수 있다.
- 중괄호 안에는 ‘키(key): 값(value)’ 쌍으로 구성된 프로퍼티(property) 를 여러 개 넣을 수 있다.

```js run
let user = new Object(); // '객체 생성자' 문법
let user = {}; // '객체 리터럴' 문법
```

중괄호 {...}를 이용해 객체를 선언하는 것을 객체 리터럴(object literal)이라고 한다.

### 리터럴과 프로퍼티

중괄호 {...} 안에는 ‘키: 값’ 쌍으로 구성된 프로퍼티가 들어간다.

```js run
let user = {
  // 객체
  name: "John", // 키: "name",  값: "John"
  age: 30, // 키: "age", 값: 30
};
```

'콜론(:)'을 기준으로 왼쪽엔 키가, 오른쪽엔 값이 위치. 프로퍼티 키는 프로퍼티 ‘이름’ 혹은 '식별자’라고도 부름
객체 user에는 프로퍼티가 두 개 있음.

- 첫 번째 프로퍼티 – "name"(이름)과 "John"(값)
- 두 번째 프로퍼티 – "age"(이름)과 30(값)
  user.location="한국";
  user["gender"]="남성"; -->객체 추가 가능  
  프로퍼티를 삭제하고 싶을 때: delete obj.prop

```js run
const person = {
  name: "이정환",
  age: 25,
  say: function () {
    console.log(`안녕 나는 ${this["name"]}`);
  },
};

person["say"]();
```

객체 안에 메소드를 만들게 되면 메소드 안에서는 자신을 this로 부를 수 있음

```js run
const person={
 name:"이정환",
 age:25,
 say:function(){
  console.log(`안녕 나는 ${this["name"]}`);
 }
};

console.log(`name:${"name" in person}`};
```

해당 key를 가진 프로퍼티가 객체 내에 있는지 확인하고자 할 때: "key" in obj

```js run
let user = {
  name: "John",
  age: 30,
  isAdmin: true,
};

for (let key in user) {
  // 키
  alert(key); // name, age, isAdmin
  // 키에 해당하는 값
  alert(user[key]); // John, 30, true
}
```

프로퍼티를 나열할 때: for (let key in obj)

### 참조에 의한 객체 복사

객체와 원시 타입의 근본적인 차이 중 하나는 객체는 ‘참조에 의해(by reference)’ 저장되고 복사된다는 것이다.
객체가 할당된 변수를 복사할 땐 객체의 참조 값이 복사되고 객체는 복사되지 않는다.

```js run
let user = { name: "John" };
let admin = user;
admin.name = "Pete"; // 'admin' 참조 값에 의해 변경됨
alert(user.name); // 'Pete'가 출력됨. 'user' 참조 값을 이용해 변경사항을 확인함
```

### 메서드와 this

```js run
let user = {
  name: "John",
  age: 30,
  sayHi() {
    // 'this'는 '현재 객체'를 나타냅니다.
    alert(this.name);
  },
};
user.sayHi(); // John
```

메서드 내부에서 this 키워드를 사용하면 객체에 접근가능

### new 연산자와 생성자 함수

'new' 연산자와 생성자 함수를 사용하면 유사한 객체 여러 개를 쉽게 만들 수 있다.

#### 생성자 함수

- 함수 이름의 첫 글자는 대문자로 시작
- 반드시 'new' 연산자를 붙여 실행

```js run
function User(name) {
  this.name = name;
  this.isAdmin = false;
}

let user = new User("보라");

alert(user.name); // 보라
alert(user.isAdmin); // false
```

## 배열

```js run
let arr = new Array();
let arr = [];
```

위의 두 문법을 활용하여 배열 생성 가능

```js run
let fruits = ["사과", "오렌지", "자두"];

alert(fruits[0]); // 사과
alert(fruits[1]); // 오렌지
alert(fruits[2]); // 자두
```

배열 내 특정 요소를 얻고 싶다면 대괄호 안에 순서를 나타내는 숫자인 인덱스를 넣어주면 된다.

### pop, push와 shift, unshift

#### pop:배열 끝 요소를 제거하고, 제거한 요소를 반환

```js run
let fruits = ["사과", "오렌지", "배"];
alert(fruits.pop()); // 배열에서 "배"를 제거하고 제거된 요소를 얼럿창에 띄웁니다.
alert(fruits); // 사과,오렌지
```

#### push: 배열 끝에 요소를 추가

```js run
let fruits = ["사과", "오렌지"];
fruits.push("배");
alert(fruits); // 사과,오렌지,배
```

#### shift: 배열 앞 요소 제거, 제거한 요소 반환

```js run
let fruits = ["사과", "오렌지", "배"];
alert(fruits.shift()); // 배열에서 "사과"를 제거하고 제거된 요소를 얼럿창에 띄웁니다.
alert(fruits); // 오렌지,배
```

#### unshift: 배열 앞에 요소를 추가

```js run
let fruits = ["오렌지", "배"];
fruits.unshift("사과");
alert(fruits); // 사과,오렌지,배
```

## 반복문

```js run
let person = {
  name: "이정환",
  age: 25,
  tall: 175,
};

const personKeys = object.keys(person);

for (let i = 0; i < personKeys.length; i++) {
  const curKey = personKeys[i];
  const curValue = person[curKey];

  console.log(`${curKey} : ${curValue}`);
}
```

## 배열 내장함수

### for each

배열의 forEach 함수를 사용하면 for문을 대체할 수 있다.

```js run
const superheroes = ["아이언맨", "캡틴 아메리카", "토르", "닥터 스트레인지"];

for (let i = 0; i < superheroes.length; i++) {
  console.log(superheroes[i]);
}
```

기존

```js run
const superheroes = ["아이언맨", "캡틴 아메리카", "토르", "닥터 스트레인지"];

superheroes.forEach((hero) => {
  console.log(hero);
});
```

forEach문 사용

### map

map 은 배열 안의 각 원소를 변환 할 때 사용 되며, 이 과정에서 새로운 배열이 만들어진다.

```js run
const array = [1, 2, 3, 4, 5, 6, 7, 8];

const squared = [];

array.forEach((n) => {
  squared.push(n * n);
});

console.log(squared);
```

forEach문

```js run
const array = [1, 2, 3, 4, 5, 6, 7, 8];

const square = (n) => n * n;
const squared = array.map(square);
console.log(squared);
```

map 함수 적용

```js run
const arr = [1, 2, 3, 4];
const newArr = arr.map((elm) => {
  return elm * 2;
});

console.log(newArr);
```

map 예제 2

### includes

```js run
const arr = [1, 2, 3, 4];
let number = 2;
console.log(arr.includes(number));
```

includes 함수 사용 시 주어진 배열에서 전달받은 인자와 일치하는지 확인. 맞으면 true 틀리면 false.
값과 자료형 모두 비교

### index of

원하는 항목이 몇번째 원소인지 찾아주는 함수

```js run
const superheroes = ["아이언맨", "캡틴 아메리카", "토르", "닥터 스트레인지"];
const index = superheroes.indexOf("토르");
console.log(index);
```

이 경우 결과는 2가 나온다.

### findindex

배열 안에 있는 값이 객체이거나, 배열일 경우 사용

```js run
const arr = [
  { color: "red" },
  { color: "black" },
  { color: "blue" },
  { color: "green" },
];
let number = 3;
console.log(arr.findIndex((elm) => elm.color === "red"));
```

### filter

filter 함수는 배열에서 특정 조건을 만족하는 값들만 따로 추출하여 새로운 배열을 만든다.

```js run
const arr = [
  { num: 1, color: "red" },
  { num: 2, color: "black" },
  { num: 3, color: "blue" },
  { num: 4, color: "green" },
  { num: 6, color: "blue" },
];
console.log(arr.filter((elm) => elm.color === "blue"));
```

### slice

배열을 잘라낼 때 사용. 기존의 배열은 건들이지 않음.

```js run
const numbers = [10, 20, 30, 40];
const sliced = numbers.slice(0, 2); // 0부터 시작해서 2전까지

console.log(sliced); // [10, 20]
console.log(numbers); // [10, 20, 30, 40]
```

### concat

여러개의 배열을 하나의 배열로 합쳐준더.

```js run
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const concated = arr1.concat(arr2);

console.log(concated);
```

결과:

```js run
[1, 2, 3, 4, 5, 6];
```

### sort

원본 배열의 순서를 정렬

### join

배열 안의 값들을 문자열 형태로 합쳐준다.

```js run
const array = [1, 2, 3, 4, 5];
console.log(array.join()); // 1,2,3,4,5
console.log(array.join(" ")); // 1 2 3 4 5
console.log(array.join(", ")); // 1, 2, 3, 4, 5
```

## Truthy and Falsy

### Truthy

자바스크립트에서, truthy인 값(참 같은 값) Boolean(불리언) 문맥에서 true로 평가되는 값이다. falsy값으로 정의된 값이 아니면 모두 truthy값으로 평가된다.

### Falsy

falsy인 값(거짓 같은 값)은 Boolean 문맥에서 false로 평가되는 값이다.
ex) false, 0, "", null, undefined, NaN

#### case1

```js run
function print(person) {
  console.log(person.name);
}

const person = {
  name: "John",
};

print(); //print(person); 일시 John 출력 가능. 파라미터가 비어진 채로 실행됐다고 가정
```

#### case2

```js run
function print(person) {
  if (person === undefined) {
    console.log("person이 없네요");
    return;
  }
  console.log(person.name);
}

const person = null;
print(person);
```

두가지 case 모두 에러가 생성되게 된다.
person 이 undefined 이거나, null 인 상황을 대비하려면 아래와 같이 코드를 작성하면 간단하다.

```js run
function print(person) {
  if (!person) {
    console.log("person이 없네요");
    return;
  }
  console.log(person.name);
}

const person = null;
print(person);
```

undefined 와 null 은 Falsy 한 값이기 때문에 Falsy 한 값 앞에 느낌표를 붙여주면 true 로 전환된다.
False + !(NOT)=>True

## 삼항 연산자

조건 ? true일때 : false일때

#### case1

```js run
const array = [];
let text =
  array.length === 0 ? "배열이 비어있습니다" : "배열이 비어있지 않습니다.";

console.log(text);
```

#### case2 - 삼항 연산자의 중첩 사용

```js run
const condition1 = false;
const condition2 = false;

const value = condition1 ? "와우!" : condition2 ? "blabla" : "foo";

console.log(value);
```

#### case3 - 삼항 연산자의 Truthy 와 Falsy 응용

```js run
let a;
const result = a ? true : false;
console.log(result); //false
```

## 단락회로 평가

```js run
true && true; // true
true && false; // false
true || false; // true
false || true; // true
```

```js run
const dog = {
  name: "멍멍이",
};

function getName(animal) {
  return animal.name;
}

const name = getName(); //getName(dog); 일시 멍멍이 출력 가능. 파라미터에 객체가 주어지지 않았을 경우
console.log(name);
```

파라미터에 객체가 주어지지 않았을 경우 에러가 난다.

```js run
const dog = {
  name: "멍멍이",
};

function getName(animal) {
  if (animal) {
    return animal.name;
  }
  return undefined;
}

const name = getName();
console.log(name);
```

if 문을 통해 조건을 달아주면 animal 값이 주어지지 않아도, 에러가 발생하지 않게 된다.

```js run
const dog = {
  name: '멍멍이'
};

### 논리 연산자 && 로 코드 단축시키기
function getName(animal) {
  return animal && animal.name;
}

const name = getName();
console.log(name); // undefined
```

논리 연산자 &&를 사용하면 코드를 더 단축시킬 수 있다.
A && B 연산자를 사용하게 될 때에는 A 가 Truthy 한 값이라면, B 가 결과값. A 가 Falsy 한 값이라면 결과는 A.

### 논리 연산자 || 로 코드 단축시키기

|| 연산자는 만약 어떤 값이 Falsy 하다면 대체로 사용 할 값을 지정해줄 때 매우 유용하게 사용 할 수 있다.

```js run
const namelessDog = {
  name: "",
};

function getName(animal) {
  const name = animal && animal.name;
  if (!name) {
    return "이름이 없는 동물입니다";
  }
  return name;
}

const name = getName(namelessDog);
console.log(name); // 이름이 없는 동물입니다.
```

```js run
const namelessDog = {
  name: "",
};

function getName(animal) {
  const name = animal && animal.name;
  return name || "이름이 없는 동물입니다.";
}

const name = getName(namelessDog);
console.log(name); // 이름이 없는 동물입니다.
```

다음 두개의 코드는 같은 동작을 한다.  
A || B 는 만약 A 가 Truthy 할경우 결과는 A 가 된다. 반면, A 가 Falsy 하다면 결과는 B 가 된다.

## 조건문 업그레이드

### 특정 값이 여러 값중 하나인지 확인해야 할 때

```js run
function isKoreanFood(food) {
  if (food === "불고기" || food === "비빔밥" || food === "떡볶이") {
    return true;
  }
  return false;
}
const food1 = isKoreanFood("치킨"); //false
console.log(food1);
```

위의 경우 비교해야 할 값이 많아질 수록 코드는 길어진다.

```js run
function isKoreanFood(food) {
  if (["불고기", "비빔밥", "떡볶이"].includes(food)) {
    return true;
  }
  return false;
}
const food1 = isKoreanFood("치킨"); //false
console.log(food1);
```

배열의 includes 함수를 사용하여 간단히 해결 가능하다.

### 값에 따라 다른 결과물을 반환 해야 할 때

```js run
const getMeal = (mealType) => {
  if (mealType === "한식") return "불고기";
  if (mealType === "양식") return "파스타";
  if (mealType === "중식") return "멘보샤";
  if (mealType === "일식") return "스시";
  return "굵기";
};
console.log(getMeal("한식"));
```

이 경우에도 좀더 간단하게 표현할 수 있다.

```js run
const meal = {
  한식: "불고기",
  양식: "파스타",
  중식: "멘보샤",
  일식: "스시",
};
const getMeal = (mealType) => {
  return meal[mealType] || "굶기";
};

console.log(getMeal("한식")); //불고기
console.log(getMeal()); //굶기
```

## 비구조화 할당

```js run
let arr = ["one", "two", "three"];

let one = arr[0];
let two = arr[1];
let three = arr[2];

console.log(one, two, three); //one two three
```

변수에 각각 값을 할당->arr[] 반복코드 존재

#### case1

```js run
let arr = ["one", "two", "three"];

let [one, two, three] = arr;

console.log(one, two, three); //one two three
```

#### case2

```js run
let[one, two, three]==["one", "two", "three"];
console.log(one, two, three); //one two three
```

#### case3

```js run
let object = { one: "one", two: "two", three: "three", name: "jack" };
let { name, one, two, three } = object; //순서가 아닌 키 값을 기준으로 비구조화 할당 이루어짐
console.log(one, two, three, name); //one two three jack
```

비구조화 할당

## spread와 rest

### spread

spread 라는 단어가 가지고 있는 의미는 펼치다, 퍼뜨리다이다.
이 문법을 사용 시 객체 혹은 배열을 펼칠 수 있다.

#### 객체에서의 spread

```js run
const slime = {
  name: "슬라임",
};

const cuteSlime = {
  name: "슬라임",
  attribute: "cute",
};

const purpleCuteSlime = {
  name: "슬라임",
  attribute: "cute",
  color: "purple",
};

console.log(slime);
console.log(cuteSlime);
console.log(purpleCuteSlime);
```

위 코드에서는 slime이라는 객체를 선언 후 cuteSlime, purpleCuteSlime 객체를 차례로 선언하였고
기존에 선언한 slime 을 건들이지 않고 새로운 객체를 만들어서 slime 이 가지고 있는 값을 그대로 사용하였다.
위 코드에서의 핵심은, 기존의 것을 건들이지 않고, 새로운 객체를 만든다는 것인데, 이러한 상황에 사용 할 수 있는 유용한 문법이 spread 이다.

```js run
const slime = {
  name: "슬라임",
};

const cuteSlime = {
  ...slime,
  attribute: "cute",
};

const purpleCuteSlime = {
  ...cuteSlime,
  color: "purple",
};

console.log(slime);
console.log(cuteSlime);
console.log(purpleCuteSlime);
```

여기서 사용한 ... 문자가 바로 spread 연산자이다.

```js run
const animals = ["개", "고양이", "참새"];
const anotherAnimals = [...animals, "비둘기"];
console.log(animals);
console.log(anotherAnimals);
```

#### 배열에서의 spread

```js run
const numbers = [1, 2, 3, 4, 5];

const spreadNumbers = [...numbers, 1000, ...numbers];
console.log(spreadNumbers); // [1, 2, 3, 4, 5, 1000, 1, 2, 3, 4, 5]
```

spread 연산자 여러번 사용

```js run
const arr = ["a", "b", "c", "d"];
const arr1 = arr; // 이것을 복사라고 말하는 사람은 경계 대상 1호.
const arr2 = [...arr]; // 배열 복사. 새로운 배열의 생성하되 그 요소들을 arr을 펼쳐서 새로운 배열의 요소로써 채우는 것.
```

배열 복사

### rest

하나의 함수에서 여러 개의 인자를 받을 때, 앞 쪽에서 받은 인자를 제외한 나머지(rest) 인자들을 배열로 합쳐서 받을 수 있게 해준다.

#### 객체에서의 rest

```js run
const purpleCuteSlime = {
  name: "슬라임",
  attribute: "cute",
  color: "purple",
};

const { color, ...rest } = purpleCuteSlime;
console.log(color); //결과: purple
console.log(rest); //결과: object{name:"슬라임", attribute:"cute"}
```

rest 안에 name 값을 제외한 값이 들어있다.

#### 배열에서의 rest

```js run
const numbers = [0, 1, 2, 3, 4, 5, 6];

const [one, ...rest] = numbers;

console.log(one); //0
console.log(rest); //[1,2,3,4,5,6]
```

#### 함수 파라미터에서의 rest

```js run
function sum(...rest) {
  return rest.reduce((acc, current) => acc + current, 0);
}

const result = sum(1, 2, 3, 4, 5, 6);
console.log(result); // 21
```

@reduce는 주로 배열이 주어졌을때 배열안에 있는 모든 값들을 사용하여 연산할 때 사용함  
acc: 누적된 값 / current: 각 원소 / 맨 뒤에 0이 뜻하는건 초기 acc 값을 설정했다고 생각하면 된다.

## 동기 & 비동기

### 동기

JavaScript는 동기식 언어이다.
한 번에 하나의 작업을 수행한다.
이러한 동작을 단일 스레드(싱글 스레드), 동기(Synchronous)라고 부른다.

### 비동기

비동기는 어떠한 요청을 보내면 그 요청이 끝날 때까지 기다리는 것이 아니라,  
응답에 관계없이 바로 다음 동작이 실행되는 방식을 말한다.
비동기로 처리하는 방식은 효율성을 상승시켜 처리 속도를 높여준다.

#### 비동기 처리 예시 1

```js run
function hello() {
  console.log("hello");
  niceTo();
}
function niceTo() {
  setTimeout(() => {
    console.log("niceTo");
  }, 0);
  meetYou();
}
function meetYou() {
  console.log("meetYou");
}
hello();
// hello meetYou niceTo
```

setTimeout 메서드: 자바스크립트 내장 함수가 아닌, 브라우저에서 제공하는 웹 API이자 비동기 함수
hello() 함수가 호출되면 해당 함수는 콜스택에 쌓인다.  
이 함수가 niceTo()함수를 호출하므로 niceTo()도 콜스택에 쌓이지만 setTimeout의 콜백함수는 즉시 실행되지 않고,  
지정 대기 시간만큼 기다린 후 이벤트 발생시 큐로 이동하여 콜스택이 비어졌을때가 되서야 다시 콜스택으로 이동되어 실행된다.

#### 비동기 처리 예시 2

```js run
setTimeout(() => {
  console.log("1번");
}, 5000);
setTimeout(() => {
  console.log("2번");
}, 3000);
setTimeout(() => {
  console.log("3번");
}, 1000);
console.log("4번"); // 4번->(1초)->3번->(2초)->2번->(2초)->1번
```

1번 2번 3번 4번 순서대로 될 것 같지만,
setTimeout은 비동기 함수이기 때문에 완전히 다른 결과가 나오게 된다.
setTimeout이 만약 동기적으로 처리됐다면 5초뒤 1번이, 3초뒤 2번이, 1초뒤 호출되어 총 8초가 걸렸겠지만,
비동기적으로 처리됐기 때문에 전체 걸린 시간은 5초가 된 것이다.

## promise

## async & await

## API 호출하기
