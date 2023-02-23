'use strict';

// document.addEventListener("DOMContentLoaded", function(){
//     const btn = document.getElementById("flushButton");
//     const element = document.getElementById("flush-collapseOne");

//     // Create a collapse instance, toggles the collapse element on invocation
//     const myCollapse = new bootstrap.Collapse(element);

//     btn.addEventListener("click", function(){
//         myCollapse.toggle();
//     });
// });

// const btn = document.getElementById("flushButton");
const btn1 = document.querySelector("#flushButton1")
const element1 = document.getElementById("flush-collapseOne")

btn1.addEventListener("click", function () {
    const myCollapse = new bootstrap.Collapse(element1);
    myCollapse.toggle();
});
const btn2 = document.querySelector("#flushButton2")
const element2 = document.getElementById("flush-collapseTwo")
btn2.addEventListener("click", function () {
    const myCollapse = new bootstrap.Collapse(element2);
    myCollapse.toggle();
});


// const alertList = document.querySelectorAll('.alert')

// const collapsible_buttons = document.getElementsByClassName("accordion-button collapsed");
//         let i;

//         for (i=0; i < coll.length; i++) {
//             collapsible_buttons[i].addEventListener("click", function() {
//                 this.classList.toggle("active");
//                 let content = this.nextElementSibling;
//                 if (content.style.display === "block")  {
//                     content.style.display = "none";
//                 }  else    {
//                     content.style.display="block";
//                 }
//             });
//         }

// $('.collapse').collapse()

// $(document).ready(function(){
//   $("#demo").on("hide.bs.collapse", function(){
//     $(".btn").html('<span class="glyphicon glyphicon-collapse-down"></span> Open');
//   });
//   $("#demo").on("show.bs.collapse", function(){
//     $(".btn").html('<span class="glyphicon glyphicon-collapse-up"></span> Close');
//   });
// });