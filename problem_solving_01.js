"use strict"
//TODO: Problem Solving - Part 1
//? Reverse a string
//look for reverse method

//for loop backwards then add letters to str
// let reverseWord = function (word) {
//   let result = ""
//   for (let i = word.length - 1; i >= 0; i--) {
//     result += word[i]
//   }
//   return result
// }

// let str = "Hello"
// console.log(reverseWord(str))

//? Capitalize first letter in a word
//* create a function that takes input of a string and only uppercases the first word: hello world > Hello World
// function uppercaseFirstLetterInWord (sentence) {
//   sentence = sentence.split(" ") 
//   // output - ["firstWrd", "secondWrd", etc.]
//    for (let i = 0; i < sentence.length; i++) {
//      sentence[i] = sentence[i][0].toUpperCase() + sentence[i].substr(1) 
//      // output - Hello = H + ello
//    }
//    // join the array into a str and seperate w/space
//    sentence = sentence.join(" ")
//   return sentence
//  }

// const mySentence = "congratulations you have completed this challenge"
// console.log(uppercaseFirstLetterInWord(mySentence))

// //? Compress a string of characters
// //* For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"
// function getStringCompressed (str) {
//   let compressedStr = ""
//   let strArray = str.split("")
//   let count = 1
//   let currentLetter;
//   for (let i = 0; i < strArray.length; i++) {
//     currentLetter = strArray[i]
//     while (i < strArray.length && strArray[i] === strArray[i + 1]) {
//       count++
//       i++
//     }
//     if (count === 1) {
//       compressedStr += currentLetter
//     } else {
//       compressedStr += count + currentLetter
//       count = 1
//     }
//   } 
//   return compressedStr
// }

// let str = "aaabbbbbccccaacccbbbaaabbbaaa"
// console.log(getStringCompressed(str))

//? BONUS - Palindrome
// A word, phrase, or sequence that reads the same backward as forward
// words: "edivider", "deified", "civic", "radar", "level", "rotor", "kayak", "reviver", "racecar", "madam", and "refer".
// sentences: "Do geese see God" , "Was it a car or a cat I saw", "Step on no pets"

//Method 1 - create function for reverse str then check 
// let reverseWord = function (word) {
//   let result = ""
//   for (let i = word.length - 1; i >= 0; i--) {
//     result += word[i]
//   }
//   return result
// }

// const isPalindrome1 = function (word) {
//   word = word.split(' ').join('').toLowerCase()
//   let reversedWord = reverseWord(word)
//   if (word === reversedWord) {
//     return true
//   } else {
//     return false
//   }
// }

//Method 2 - reverse str using reverse w/o function
// const isPalindrome2 = function (word) {
//   word = word.split(' ').join('').toLowerCase()
//   let reversedWord = word.split(' ').reverse().join('')
//   if (word === reversedWord) {
//     return true
//   } else {
//    return false
//   }
// }

//Results
// let word = "Was it a car or a cat I saw"
// console.log(isPalindrome1(word))
// console.log(isPalindrome2(word))