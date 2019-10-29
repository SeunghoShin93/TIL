console.log(a) // undefined
var a = 10
console.log(a)

// JS 가 이해한 코드 
// 선언이 hoist 됌
var a
console.log(a) // undefined
a = 10
console.log(a)


// let 은 안된다. ReferenceError
// console.log(b)
// let b = 10
// console.log(b)


// // 마찬가지로 아래와 같은 과정을 거친다.
// let b // 선언 + TDZ
// console.log(b)
// b = 10 // 할당 불가 (초기화 안 됌)
// console.log(b)

// ReferenceError: Cannot access 'b' before initialization
// 왜 

if (x !== 1) {
  console.log(y) // undefined
  var y = 3
  if (y === 3) {
    var x = 1
  }
  console.log(y) // 3
}

if (x === 1) {
  console.log(y) // 3
}

// JS 가 이해한 코드 
var x
var y

if (x !== 1) {
  console.log(y) // undefined
  var y = 3
  if (y === 3) {
    var x = 1
  }
  console.log(y) // 3
}

if (x === 1) {
  console.log(y) // 3
}