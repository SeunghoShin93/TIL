// 배열로 이루어진 숫자들을 모두 더하는 함수

const numberAddEach = numbers => {
  let sum = 0
  for (const number of numbers) {
    sum += number
  }
  return sum
}

// 배열로 이루어진 숫자들을 모두 빼는 함수
const numberSubEach = numbers => {
  let sub = 0
  for (const number of numbers) {
    sub -= number
  }
  return sub
}

// 배열로 이루어진 숫자들을 모두 곱하는 함수
const numberMulEach = numbers => {
  let mul = 0
  for (const number of numbers) {
    mul *= number
  }
  return mul
}

// 매번 함수를 새로 정의하나
// 공통점 : 숫자로 이루어진 배열의 요소들을 각각 [] 한다.
// [] 를 callback 함수에서 처리하는 일로 바꿔보기


// base func template
const numbersEach = (numbers, callback) => {
  let acc
  for (const number of numbers) {
    acc = callback(number, acc)
  }
  return acc
}

// 더한다
const addEach = (number, acc = 0) => {
  return acc + number
}

const subEach = (number, acc = 0) => {
  return acc - number
}

const mulEach = (number, acc = 1) => {
  return acc * number
}

const NUMBERS = [1, 2, 3, 4, 5, ]
console.log(numbersEach(NUMBERS, addEach))

// 다시 사용 안할 것같은데
// numbersEach 이후의 제어를 함수 정의 없이 매번 자유롭게 하려면
console.log(numbersEach(NUMBERS, (number, acc = 0) => acc + number))
console.log(numbersEach(NUMBERS, (number, acc = 0) => acc - number))
console.log(numbersEach(NUMBERS, (number, acc = 1) => acc * number))