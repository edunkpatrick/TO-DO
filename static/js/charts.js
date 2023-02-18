// GET DATA TO MAKE CHART OF ALL TASKS
'use strict';

// document.getElementById('chart').addEventListener('click', (evt) => {
//     evt.preventDefault();
//     fetch('/tasks_complete.json')
//         .then((response) => response.json())
//         .then((responseJson) => {
//             const data = responseJson.data.map(tasks => ({
//                 x: tasks.freq,
//                 y: tasks.num,
//                 }));

//             new Chart(document.querySelector('#bar-chart'), {
//                 type: 'bar',
//                 data: {
//                     datasets: [{
//                         label: 'All Tasks Completed',
//                         data: data,
//                         backgroundColor: '#FC9BAE',
//                         borderColor: '#FC9BAE',
//                         borderWidth: 2

//                     }],
//                 },
//                 options: {
//                     scales: {
//                         x: {
//                             title: {
//                                 display: true,
//                                 text: 'Frequency of Task',
//                                 borderColor: '#FC9BAE',
//                                 borderWidth: 2
//                             },
//                         },
//                     y: {
//                         title: {
//                             display: true,
//                             text: 'Number of Tasks Completed',
//                             borderColor: '#FC9BAE',
//                             borderWidth: 2
//                         },
//                         min: 0,
//                         ticks: {
//                             stepSize: 1
//                         }
//                     }},
//                     },
//                 });
//             });
//         });


// CODE REVIEW 2 2/3/23


// CHART DATA W/IN LAST MONTH
// document.getElementById('month_chart').addEventListener('click', (evt) => {
//     evt.preventDefault();
//     fetch('/get_date_range.json')
//         .then((response) => response.json())
//         .then((responseJson) => {
//             const data = responseJson.data.map(tasks => ({
//                 x: tasks.freq,
//                 y: tasks.num,
//                 }));
//             new Chart(document.querySelector('#bar-chart-month'), {
//                 type: 'bar',
//                 data: {
//                     datasets: [{
//                         label: 'Tasks Completed in Last 30 Days',
//                         data: data,
//                         backgroundColor: '#88D6FA',
//                         borderColor: '#88D6FA',
//                         borderWidth: 2

//                     }],
//                 },
//                 options: {
//                     scales: {
//                         x: {
//                             title: {
//                                 display: true,
//                                 text: 'Frequency of Task',
//                                 borderColor: '#88D6FA',
//                                 borderWidth: 2
//                             },
//                         },
//                     y: {
//                         title: {
//                             display: true,
//                             text: 'Number of Tasks Completed',
//                             borderColor: '#88D6FA',
//                             borderWidth: 2
//                         },
//                         min: 0,
//                         ticks: {
//                             stepSize: 1
//                         }
//                     }},
//                     },
//                 });
//             });
//         });

// // CHART FOR ALL HOUSEHOLD TASKS
document.getElementById('house_chart').addEventListener('click', (evt) => {
    evt.preventDefault();
    fetch('/house_tasks_complete.json')
        .then((response) => response.json())
        .then((responseJson) => {
            console.log(`this is responseJson ${responseJson}`);
            // make an array of responseJson key, values
            const user_data = Object.entries(responseJson['house']);
            console.log(`this is user_data ${user_data}`);
            // get dict of colors from bar_colors from responseJson
            const background_dict = responseJson['bar_colors'];
            console.log(`this is background_colors ${background_dict}`);

            const taskArr = [];

            // loop through users
            for(const [user_name, user_tasks] of user_data){
                console.log(user_name);
                console.log(user_tasks);
                const data = user_tasks.map((tasks) => ({
                    // x is frequency type
                    x: tasks[0],
                    // y is total occurences of freq type
                    y: tasks[1],
                }));

                const dict = {}

                // dict with user_name as key, data as values
                dict[user_name] = data
                console.log(`this is dict ${dict}`);
                // add dict to taskArr
                taskArr.push(dict);
            }
            console.log(`this is taskArr ${taskArr}`);
            const dataArr = [];
            
            for(let i = 0; i < taskArr.length; i++){
                // get name from taskArr keys
                const name = Object.keys(user_data[i])[0]
                console.log(name);
                // const name = Object.keys(taskArr[i])[0]
                // get task freq type, total values and assign to data
                const data = Object.keys(user_data[1])[0]
                console.log(data);
                // const data = taskArr[i][name]
                // assign color by iteration
                const color = background_dict['colors'][i]
                // add name, data, and color to dataArr for chart
                dataArr.push({
                    label: name,
                    data: data,
                    backgroundColor: color,
                    borderColor: color
                })
                console.log(`this is dataArr ${dataArr}`);
            }

            new Chart(document.querySelector('#house-chart'), {
                type: 'bar',
                data: {
                    datasets: dataArr,
                },
                options: {
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Frequency of Task',
                                borderWidth: 2
                            },
                        },
                    y: {
                        title: {
                            display: true,
                            text: 'Number of Tasks Completed',
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
