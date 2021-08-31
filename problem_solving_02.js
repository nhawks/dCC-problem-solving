"use strict"
//?  Happy Number - Determine if a number is a happy or sad number
// A happy number is a number defined by the following process: starting with any positive integer,
//replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1. 
//An example of a happy number is 19

// const numbersToArray = number => Array.from(String(number), Number)

// const isHappyNumber = function (number) {
//   let arr = numbersToArray(number)
//   let sum = 0
//   let previousNumbers = []
//   while (sum !== 1) {
//     for (let i = 0; i < arr.length; i++) {
//       sum += arr[i] ** 2
//     }
//     if (sum === 1) {
//       console.log(`${number}: Is a Happy Number`)
//       break
//     } else if (previousNumbers.includes(sum)) {
//       console.log(`${number}: Is not a Happy Number`)
//       break
//     } else {
//       arr = []
//       arr = numbersToArray(sum)
//       previousNumbers.push(sum)
//       sum = 0
//     }
//   }
//   return sum === 1 ? true : false
// }

// let number = 2
// console.log(isHappyNumber(number))

//? Prime Numbers - print out numbers 1 - 100 that are prime
// for (let i = 2; i <= 100; i++) {
//   let isPrime = true
//   for (let x = 2; x <= i - 1; x++) {
//     if (i % x === 0) {
//       isPrime = false
//     } 
//   }
//   if (isPrime === true) 
//   {
//       console.log(i)
//   }
// }

//? Fibonacci Sequence - write a method that prints the sequence starting from 1
// let arr = []

// for (let i = 0; i < 50; i++) {
//   if (i === 0 || i === 1) {
//     arr.push(1)
//   } else {
//     arr.push(arr[i - 1] + arr[i - 2])
//   }
// }
// console.log(arr) // Output:  1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...