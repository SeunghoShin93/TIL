const numbers = [1, 2, 3, 4, ]

// 인덱스로 접근가능

console.log(numbers[0])
console.log(numbers[-1]) // undefined : 정확한 양의 정수 index 만 가능
console.log(numbers.length) // count

// 원본 조작 reverse()
console.log(numbers.reverse())
console.log(numbers)

console.log(numbers.reverse())
console.log(numbers)

// push  
console.log(numbers.push('a')) // 5 push 의 리턴 값은 array 의 length
console.log(numbers)

// pop
console.log(numbers.pop()) // a, 배열 마지막 요소 제거
console.log(numbers)

// unshift - 배열의 가장 앞에 요소를 추가하고 return 은 배열의 길이
console.log(numbers.unshift('a'))
console.log(numbers)

// shift - 배열의 가장 앞 요소 제거 후 return 
console.log(numbers.shift())
console.log(numbers)

// include - 포함인지 여부 확인 후 bool 값 return 
console.log(numbers.includes(1))
console.log(numbers.includes(0))

// push - 뒤에 append
console.log(numbers.push('a', 'a'))
console.log(numbers)
//indexOf 찾기
console.log(numbers.indexOf('a')) // 4  
console.log(numbers.indexOf('b')) //-1 , 찾고자 하는 요소가 없으면

// join - 배열의 요소를 join 함수의 인자를 기준으로 이어서 문자열로 return
console.log(numbers.join()) // 배열을 문자열로 
console.log(numbers.join('')) //  
console.log(numbers.join('-')) //  1-2-3-4-a-a

console.log(numbers)