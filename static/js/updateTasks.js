'use strict';


// DELETES CHECKED TASKS
document.getElementById('delete_tasks').addEventListener('click', (evt) => {
    evt.preventDefault();
    for (const cb of document.querySelectorAll('.form-check-input')){
        if (cb.checked === true){
            const toMark = cb.value;
            const queryString = new URLSearchParams({ task: toMark }).toString();
            const url = `/delete_task?${queryString}`;
            fetch(url)
                .then((response) => response.text())
                .then((status) => {
                    console.log(status);
                    const toDelete = document.getElementById(`${status}div`);
                    toDelete.remove();
                })
        }
    }});


// MARKS ALL CHECKED TASKS COMPLETE
document.getElementById('mark_complete').addEventListener('click', (evt) => {
    evt.preventDefault();
    for (const cb of document.querySelectorAll('.form-check-input')){
        if (cb.checked === true){
            const toMark = cb.value;
            const queryString = new URLSearchParams({ task: toMark }).toString();
            const url = `/complete_task?${queryString}`;
            fetch(url)
                .then((response) => response.text())
                .then((status) => {
                    console.log(status);
                    const selectItem = document.getElementById(`${status}div`);
                                        // insertAdjacentHTML placeholder to change style to crossout once CSS made
                    selectItem.insertAdjacentHTML('afterbegin', '<s>complete</s>');
                })
        }
    }});


// GET DATA TO MAKE CHART OF ALL TASKS

document.getElementById('chart').addEventListener('click', (evt) => {
    evt.preventDefault();
    fetch('/tasks_complete.json')
        .then((response) => response.json())
        .then((responseJson) => {
            const data = responseJson.data.map(tasks => ({
                x: tasks.freq,
                y: tasks.num,
                }));

            new Chart(document.querySelector('#bar-chart'), {
                type: 'bar',
                data: {
                    datasets: [{
                        label: 'All Tasks',
                        data: data,
                        backgroundColor: '#ff1493',
                        borderColor: '#ff1493',
                        borderWidth: 2

                    }],
                },
                options: {
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Frequency of Task',
                                borderColor: '#ff1493',
                                borderWidth: 2
                            },
                        },
                    y: {
                        title: {
                            display: true,
                            text: 'Number of Tasks Completed',
                            borderColor: '#ff1493',
                            borderWidth: 2
                        },
                        min: 0,
                        ticks: {
                            stepSize: 1
                        }
                    }},
                    },
                });
            });
        });

// CHART DATA TO MAKE SPECIFIC RANGE - IN PROGRESS
document.getElementById('date_range').addEventListener('submit', (evt) => {
    evt.preventDefault();
    fetch('/get_date_range.json')
        .then((response) => response.json())
        .then((responseJson) => {
            const data = responseJson.data.map(tasks => ({
                x: tasks.freq,
                y: tasks.num,
                }));

            new Chart(document.querySelector('#bar-chart'), {
                type: 'bar',
                data: {
                    datasets: [{
                        label: 'All Tasks',
                        data: data,
                        backgroundColor: '#ff1493',
                        borderColor: '#ff1493',
                        borderWidth: 2

                    }],
                },
                options: {
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Frequency of Task',
                                borderColor: '#ff1493',
                                borderWidth: 2
                            },
                        },
                    y: {
                        title: {
                            display: true,
                            text: 'Number of Tasks Completed',
                            borderColor: '#ff1493',
                            borderWidth: 2
                        },
                        min: 0,
                        ticks: {
                            stepSize: 1
                        }
                    }},
                    },
                });
            });
        });
// LOGS OUT USER

document.querySelector('#log_out').addEventListener('click', (evt) => {
    evt.preventDefault();
    const log_out_url = '/sign_out';
    fetch(log_out_url);
})


// EVENT LISTENER TO POPULATE TASKS FOR USER - CAN WORK ON WHEN CSS IMPLEMENTED

// document.getElementById('show_tasks').addEventListener('click', (evt) => {
//     evt.preventDefault();
//     document.getElementById('user_tasks').hidden = false;
// });


// FORMER AJAX FUNCTIONS, REMOVE WHEN MVP COMPLETE

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

// MARK COMPLETE
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