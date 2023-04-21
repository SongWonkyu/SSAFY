const myObj = {
  numbers: [1],
  myFunc() {
    console.log(this) // myObj
    this.numbers.forEach(function (num)
{
      console.log(num) 
      console.log(this)
    })
  }
}