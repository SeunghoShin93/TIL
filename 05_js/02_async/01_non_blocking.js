const nothing = () => {
  console.log('sleeping....')
}

function sleep_3s() {
  setTimeout(() => console.log('wake up'), 3000)
}

// console.log('start of sleeping') // 1출력
// sleep_3s()
// console.log('end of program')

function first() {
  console.log('first')
}

function second() {
  console.log('second')
}

function third() {
  console.log('third')
}

// first()
// setTimeout(second, 1000)
// third()

// console.log('Hi')

// setTimeout(function ssafy() {
//   console.log('ssafy')
// }, 1)

// console.log('bye')


function printHello() {
  console.log('hello from baz')
}

function baz() {
  setTimeout(printHello, 3000)
}

function bar() {
  baz()
}

function foo() {
  bar()
}

foo()