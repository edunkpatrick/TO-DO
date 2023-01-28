// 'use strict';

// editButtons = document.querySelectorAll('.add_task');

// for (const button of editButtons) {
//   button.addEventListener('click', () => {
//     // first ask the user what they want the new rating to be
//     const newTask = prompt('What is this task');
//     // console.log('hi');
//     // const formInputs = {
//     //   add_task: newTask,
//     //   task_id: button.id,
// //   };

//     fetch('/add_task')
//         .then((response) => response.text())
//         .then((status) => {
//             document.querySelector('#task').innerHTML = status;
//             console.log('hola');
//         })
//     })}

//     // send a fetch request to the add_task route
//     fetch('/add_task', {
//     //   method: 'POST',
//     //   body: JSON.stringify(formInputs),
//     //   headers: {
//     //     'Content-Type': 'application/json',
//     //   },
//     }).then((response) => {
//       if (response.ok) {
//         // document.querySelector(`span.rating_num_${button.id}`).innerHTML = newTask;
//       } else {
//         alert('Failed to update task.');
//       }
//     });
//   });
// }

// deletes selected task

// deleteButtons = document.querySelectorAll('.delete_checkbox');

// for (const button of deleteButtons) {
//   button.addEventListener('click', () => {
//     if (document.getElementById('delete_checkbox').checked){
//           const answer = confirm('Are you sure you want to delete this task?');
//            if (answer)
//              {
//              $("#delete_checkbox").remove();
//              }
//            }
//         })};

function deleteTask() {
    let answer = confirm("Are you sure you want to delete this task?");
    if (answer)
        {
            ("#delete_checkbox").remove();
            //   then update the list with server/crud
        }

}
