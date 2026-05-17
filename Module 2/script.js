

// Why DOM matters ? 
// JavaScript cannot touch your HTML file directly. It is just a text file sitting on a server.
// What JS can touch is the DOM - the live map the browser built. When JavaScript changes the DOM, the browser immediately updates what is on screen."

// getElementById
// querySelector
// let, var, const

// Variables in Javascript
// JavaScript is a loosely typed language.



// Declaration 
// const a = "Masai"
// console.log(a)

// // ReDeclaration 
// let a = 100
// console.log(a)

// Assignment
// a = true
// console.log(a)

// const btn1 = document.getElementById('btn-1')
// console.log(btn1)

// btn1.addEventListener('click', function() {
//     console.log("Button 1 clicked.")
// })

// const btn2 = document.getElementById('btn-2')
// console.log(btn2)

// btn2.addEventListener('click', function() {
//     console.log("Button 2 clicked.")
// })

// const btn3 = document.getElementById('btn-3')
// console.log(btn3)

// btn3.addEventListener('click', function() {
//     console.log("Button 3 clicked.")
// })

// Task - When the user clicks on Button-1, then display "Hello World" on the Webpage in a div element.

//getElementById - Function used to select element by ID.
// const btn1 = document.getElementById('btn-1')

// btn1.addEventListener('click', function() {
//     //Add an element inside the DOM
//     const newDiv = document.createElement("div")

//     newDiv.innerText = "Hello World!"

//     //querySelector() - Function used to select element by id # / class . / name
//     const body = document.querySelector("body")

//     body.appendChild(newDiv)
// })

// // Task - When the user clicks on Button-2, then display "Hello World" on the Webpage in a h1 element
// const btn2 = document.getElementById('btn-2')

// btn2.addEventListener('click', function() {
//     //Add an element inside the DOM
//     const newH1 = document.createElement("h1")

//     newH1.innerText = "Hello World!"

//     //querySelector() - Function used to select element by id # / class . / name
//     const body = document.querySelector("body")

//     body.appendChild(newH1)
// })

// // Task - When the user clicks on Button-3, then display "Hello World" on the Webpage in a p element
// const btn3 = document.getElementById('btn-3')

// btn3.addEventListener('click', function() {
//     //Add an element inside the DOM
//     const newP = document.createElement("p")

//     newP.innerText = "Hello World!"

//     //querySelector() - Function used to select element by id # / class . / name
//     const body = document.querySelector("body")

//     body.appendChild(newP)
// })

// // Task -  When the user clicks on Add Butter Button, then add a new Item "Butter" in the List.
// const addButterBtn = document.getElementById('add-butter')

// addButterBtn.addEventListener('click', function() {
//     const newListItem = document.createElement("li")

//     newListItem.innerText = "Butter"

//     newListItem.className = "item"

//     const ul = document.querySelector("ul")

//     ul.appendChild(newListItem)
// })

// Select all the list items from the unordered list. 
// const listItem = document.querySelector(".item")
// console.log(listItem)
// console.log(listItem.parentElement)


// const ul = document.getElementById("item-list")
// console.log(ul.parentElement) -> The element directly above
// console.log(ul.children) -> All direct children
// console.log(ul.firstElementChild) -> The first child element
// console.log(ul.nextElementSibling) -> The next element at the same level

//QuerySelector - returns only the first matching element, If there are more than one elements with the class .item, it 
// will just return the fist list item matching with the class.

// const allListItems = document.querySelectorAll(".item")
// console.log(allListItems)


// const items = document.getElementById("item-list")
// console.log(items)
// console.log(items.children[3])