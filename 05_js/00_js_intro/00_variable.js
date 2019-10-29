// let (변수 )

let x = 1

if (x === 1) {
  let x = 2

  console.log(x)
}

console.log(x)

// const (상수) 

// const 선언 시에 초기값 미선언시 오류 발생 
// const MY_FAV

const MY_FAV = 7

console.log('my favourite number is:' +
  MY_FAV)

// MY_FAV = 20  재할당 안 됌
// const MY_FAV = 20 선언 안 됌
// let MY_FAV = 20 식별자 자체를 선언했기 떄문에 안됌 (var 도 안됌)

if (MY_FAV === 7) {
  // 블록 유효 범위로 지정된 MY_FAV 이라는 변수를 만듦으로 괜찮다.
  // 즉 전역이 아닌 범위 안이므로 이름 공간에서 충돌이 나지 않는다.
  // 단 const 는 재선언이 불가능하기 떄문에 let 으로 설정.
  let MY_FAV = 20

  console.log('my favourite number is:' + MY_FAV)
}

console.log(MY_FAV)


// var (변수)
function varTest() {
  var x = 1
  if (true) {
    var x = 2
    console.log(x) // 2 , 상위 블록과 다른 변수
  }
  console.log(x) // 2
}

varTest()


// let 
function letTest() {
  let x = 1
  if (true) {
    let x = 2
    console.log(x) // 2 , 상위 블록과 다른 변수
  }
  console.log(x) // 1
}

letTest()

// let 과 var

var a = 1
var b = 2

if (a === 1) {
  var a = 11
  let b = 22

  console.log(a) // 11
  console.log(b) // 22 

}

console.log(a) // 11
console.log(b) // 2

// 식별자 작성 스타일
// 1. 카멜 케이스(camelCase) - 객체, 변수, 함수 (=lower-camel-case)
let dog
let variableName

// 배열인 경우 복수형
const dogs = []

// 정규 표현식은 'r' 로 시작
const rDecs = /.*/

// 함수
function getPropertyName() {
  return 1
}

// boolean 을 반환하는 변수 - 'is' 로 시작
let isAvaiable = false

// 2. 파스칼 케이스 (PascalCase) - 클래스, 생성자  (=upper-camel-case)

class User {
  constructor(options) {
    this.name = option.name
  }
}

// 3. 대문자 스네이크 케이스 (SNAKE_CASE) - 상수 
// 이 표현은 변수와 변수의 속성이 변하지 않는다는 것을 프로그래머에게 알려준다.
const API_KEY = 'avcdsearsr'