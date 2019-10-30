// dict
const me = {
  name: 'ssafy', // key 가 한 단어 일때는 
  'phone number': '01012345678', // key 가 여러 단어일 떄 
  appleProducts: {
    ipad: '2018pro',
    iphone: '7',
    macbook: '2019pro',
  }
}

console.log(me.name)
console.log(me['name'])
console.log(me['phone number']) // key 가 여러 단어인 경우 반드시 대괄호로 접근

console.log(me.appleProducts)
console.log(me.appleProducts.ipad)

// Object Literal (객체 표현법)
// ES5
var books = ['Learning JS', 'Eloquent JS']

var comics = {
  'DC': ['Joker', 'Aquaman'],
  'Marvel': ['Captain Marvel', 'Avengers'],
}
var magazines = null

var bookShop = {
  books: books,
  comics: comics,
  magazines: magazines,
}

console.log(bookShop)
console.log(typeof bookShop)
console.log(bookShop.books[0])

// ES6+
// object 의 key 와 value 가 같다면, 마치 배열처럼 한 번만 작성 가능하다.
let bookShopTwo = {
  books,
  comics,
  magazines,
}

console.log(bookShopTwo)

//////////////

// JSON(JS Object Notation, JS 객체 표기법)

const jsonData = JSON.stringify({ // JSON -> String
  coffee: 'Americano',
  iceCream: 'Mint Choco'
})

console.log(jsonData) // {"coffee":"Americano","iceCream":"Mint Choco"}
console.log(typeof jsonData) // string

const parseData = JSON.parse(jsonData)
console.log(parseData)
console.log(typeof parseData)