"use strict"
//? Two Sum
// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

//* First attempt - too slow and long
// let twoSum = function (nums, targetNum) {
//   let result = []
//   let foundTwoSum = false
//   while (foundTwoSum === false) {
//     for(let i = 0; i < nums.length; i++) {
//       for (let j = 0; j < nums.length; j++) {
//         if (nums[j] === nums[i]) {
//           continue
//         } 
//         else if (nums[i] + nums[j] === targetNum) {
//           foundTwoSum = true
//           result.push(nums.indexOf(nums[i]), nums.indexOf(nums[j]))
//           return console.log(result)
//           // return console.log(nums.indexOf(nums[i]), nums.indexOf(nums[j]))
//         }
//       }
//     }
//   }
// }

//* Second Attempt
// const twoSum = function (nums, target) {
//   for (let i = 0; i < nums.length; i++) {
//     for (let j = i + 1; j < nums.length; j++) {
//       if (nums[i] + nums[j] === target) {
//         return console.log([i, j])
//       }
//     }
//   }
// }

// // let nums = [5, 17, 77, 50] 
// // let target = 55
// let nums = [2, 7, 11, 15, 9] 
// let target = 9
// twoSum(nums, target)

//? Palindrome Checker
// const isPalindrome = function (s) {
//   s = s.replace(/[`~!@#$%^&*()_|+\-=?;:'",.<>\{\}\[\]\\\/]/gi, "").split(" ").join("").toLowerCase()
//   let rs = s.split("").reverse().join("")
//   s === rs ? console.log(true) : console.log(false)
// }

// let str = "A man, a plan, a canal: Panama"
// isPalindrome(str)