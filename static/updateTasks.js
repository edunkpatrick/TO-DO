'use strict';

// DELETE SELECTED TASK
// for (const button of document.querySelectorAll('.delete')) {
//     button.addEventListener('click', () => {
//     // get task by button.id
//         const toDel = button.id;
//         const answer = confirm(`are you sure you want to delete ${toDel}`);
//         if (answer) {
//             const queryString = new URLSearchParams({ task: toDel }).toString();
//             const url = `/delete_task?${queryString}`;
//             fetch(url)
//                 .then((response) => response.text())
//                 .then((status) => {
//                     console.log(status);
//                     const toDeleteLabel = document.getElementById(`${status}div`);
//                     toDeleteLabel.remove();
//                 });
//         }
//         else {
//             console.log('cancelled');
//         }
//     });
// };
// // DELETES CHECKED TASKS
// const button = document.querySelector('#delete_tasks');
// button.addEventListener('click', () => {
document.getElementById('delete_tasks').addEventListener('click', (evt) => {
    evt.preventDefault();
    for (const cb of document.querySelectorAll('.cb')){
        if (cb.checked === true){
            const toMark = cb.value;
            const queryString = new URLSearchParams({ task: toMark }).toString();
            const url = `/delete_task?${queryString}`;
            fetch(url)
                .then((response) => response.text())
                .then((status) => {
                    const toDelete = document.getElementById(`${status}div`);
                    toDelete.remove();
                })
        }
    }});

// MARKS TASK COMPLETE
// for (const button of document.querySelectorAll('.complete')) {
//     button.addEventListener('click', () => {
//     // get task by button.id
//         const toComp = button.id;
//         const queryString = new URLSearchParams({ task: toComp }).toString();
//         const url = `/complete_task?${queryString}`;
//         fetch(url)
//             .then((response) => response.text())
//             .then((status) => {
//                 // insertAdjacentHTML placeholder to change style to crossout once CSS made
//                 const selectItem = document.getElementById(`${status}div`);
//                 selectItem.insertAdjacentHTML('afterbegin', '<s>complete</s>');
//     });
// });
// };

// MARKS ALL CHECKED TASKS COMPLETE
document.getElementById('mark_complete').addEventListener('click', (evt) => {
    evt.preventDefault();
    for (const cb of document.querySelectorAll('.cb')){
        if (cb.checked === true){
            const toMark = cb.value;
            const queryString = new URLSearchParams({ task: toMark }).toString();
            const url = `/complete_task?${queryString}`;
            fetch(url)
                .then((response) => response.text())
                .then((status) => {
                    // insertAdjacentHTML placeholder to change style to crossout once CSS made
                    const selectItem = document.getElementById(`${status}div`);
                    selectItem.insertAdjacentHTML('afterbegin', '<s>complete</s>');
                })
        }
    }});
// for (const button of document.querySelectorAll('.complete')) {
//     button.addEventListener('click', () => {
//     // get task by button.id
//         const toComp = button.id;
//         const queryString = new URLSearchParams({ task: toComp }).toString();
//         const url = `/complete_task?${queryString}`;
//         fetch(url)
//             .then((response) => response.text())
//             .then((status) => {
//                 // insertAdjacentHTML placeholder to change style to crossout once CSS made
//                 const selectItem = document.getElementById(`${status}div`);
//                 selectItem.insertAdjacentHTML('afterbegin', '<s>complete</s>');
//     });
// });
// };

// CLEAR COMPLETED TASKS FROM CHECKLIST
// only clears one at a time, need to update so it clears all tasks marked complete


// document.querySelector('#remove_complete').addEventListener('click', (evt) => {
//     evt.preventDefault();
//     for(const cb of document.querySelectorAll('.cb')){
//         if (cb.checked === true){
//             console.log(cb.checked);
//             const toClear = cb.value;
//             const queryString = new URLSearchParams({ task: toClear }).toString();
//             const url = `/clear_task?${queryString}`;
//             fetch(url)
//                 .then((response) => response.text())
//                 .then((status) => {
//                     console.log(status);
//                     if (status){
//                         const toDeleteLabel = document.getElementById(`${status}div`);
//                         toDeleteLabel.remove();
//                     }})}
//         }
//         });


// function clearButton() {
//     const toClear = document.getElementById('taskinput').value;
//     const queryString = new URLSearchParams({ task: toClear }).toString();
//     const url = `/clear_task?${queryString}`;
//     fetch(url)
//         .then((response) => response.text())
//         .then((status) => {
//             const toClearLabel = document.getElementById(`${status}div`);
//             toClearLabel.remove();
//             alert(`${status} has successfully been cleared`);
//         })
// };

// GET DATA TO MAKE CHART

document.getElementById('chart').addEventListener('click', (evt) => {
    evt.preventDefault();
    fetch('/tasks_complete.json')
        .then((response) => response.json())
        .then((responseJson) => {
            const data = responseJson.data.map((tasks) => ({
                x: tasks.freq,
                y: tasks.num,
                }));

            new Chart(document.querySelector('#bar-chart'), {
                type: 'bar',
                data: {
                    datasets: [{
                        label: 'All Tasks',
                        data: data
                    }],
                },
                options: {
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Frequency of Task'
                            },
                        },
                    y: {
                        title: {
                            display: true,
                            text: 'Times Done'
                        },
                        min: 0,
                        suggestedMax: 15,
                        ticks: {
                            stepSize: 1
                        }
                    }},
                    },
                });
            });
        });
