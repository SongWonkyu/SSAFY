// 함수 선언식
function add(num1, num2){
  return num1+num2
}
console.log(add(1, 5))

// 함수 표현식
const add2 = function(num1, num2){
  return num1+num2
}
console.log(add2(1, 2))

// Spread syntax ( 전개 구문 )
// 배열과의 사용 ( 배열 복사 )
const abc = ['a', 'b', 'c']

const de = [...abc, 'd', 'e']

console.log(de)

// 함수와의 사용 ( Rest parameters )
// - 정해지지 않은 수의 매개 변수를 배열로 받을 수 있음
const restArgs = function(arg1, arg2, ...restArgs){
  return [arg1, arg2, restArgs]
}
restArgs(1, 2, 3, 4, 5)


// 함수 선언식으로 정의한 함수는 호이스팅이 발생한다.
sum(2, 7) // 9
function sum (num1, num2){
	return num1 + num2
}

// 화살표 함수
const arrow1 = function(name){
  return `hello, ${name}`
}

// 1. function 키워드 삭제
const arrow2 = (name) => {
  return `hello, ${name}`
}

/* 2. 인자가 1개일 경우에만 () 생략 가능. . .한데 명확성과 일관성을 위해 항상 인자 주위에는 
괄호('()')를 포함하는 것을 권장*/
const arrow3 = name => {
  return `hello, ${name}`
}

// 3. 함수 바디가 return을 포함한 표현식 1개일 경우에 {} & return 삭제 가능
const arrow4 = name => `hello, ${name}`