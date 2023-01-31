'use strict';

// DELETE SELECTED TASK
// deleteButton selects button and gives popup but checkbox irrelevant
function deleteButton() {
    const toDel = document.getElementById('task').value;
    const answer = confirm(`are you sure you want to delete ${toDel}`);
    if (answer) {
        const queryString = new URLSearchParams({ task: toDel }).toString();
        const url = `/delete_task?${queryString}`;
        fetch(url)
            .then((response) => response.text())
            .then((delete_task) => {
                // use dom manipulation to remove task from page
                // const toRemove = document.querySelector(status);
                // console.log(`this is status${status}`)
                // toRemove.remove();
                toDel.remove();
                // const toRemove = document.getElementById('task');
                // toRemove.remove(delete_task);
                console.log('worked and didnt reload');
            });
    }
    else {
        console.log('that didnt work');
    }
    }

// const button = document.querySelector('#delete_checkbox');
// button.addEventListener('submit', () => {
//     const task = document.querySelector('#task').value;
//     const url = `/delete_task?${task}`;

//     fetch(url)
//     })
//         .then((response) => response.text())
//         .then((task) => {
//             document.querySelector('#task').innerHTML = task;
//         });


// function deleteTask() {
//     let answer = confirm("Are you sure you want to delete this task?");
//     if (answer)
//         {
//             ("#delete_checkbox").remove();
//             //   then update the list with server/crud
//         }

// }

// MARKS COMPLETE

// completeTask = document.querySelector('#mark_complete');
// function handleTask() {
//     completeTask.innerH
// }
