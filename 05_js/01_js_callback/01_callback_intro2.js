function doSomething(subject, callback) {
  console.log(`이제 ${subject} 과목평가 준비를 시작해볼까?`)
  callback()
}

doSomething('django', function () {
  console.log('며칠 안남았는데..')
})