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
// https://www.youtube.com/watch?v=Zr0a8dk43Zk
// https://www.youtube.com/watch?v=mw5i_QGDomw
// https://www.youtube.com/watch?v=VU5spDuIG2U
document.getElementById('house_chart').addEventListener('click', (evt) => {
    evt.preventDefault();
    fetch('/house_tasks_complete.json')
        .then((response) => response.json())
        .then((responseJson) => {
            // console.log(`this is responseJson ${responseJson}`);
            console.log(JSON.stringify(responseJson));
            // grab data from house key in JSON response
            const user_data = Object.entries(responseJson['house']);
            console.log(JSON.stringify(user_data));
            // get dict of colors from bar_colors from responseJson
            const background_dict = responseJson['bar_colors'];
            // console.log(`this is background_colors ${background_dict}`);

            const taskList = [];

            // loop through user data in house data (user_data)
            for(const [user_name, user_tasks] of user_data){
                console.log(`this is user_name ${user_name}`);
                console.log(`this is user_tasks ${user_tasks}`);
                const taskData = user_tasks.map((tasks) => ({
                    // x is frequency type
                    x: tasks[0],
                    // y is total occurences of freq type
                    y: tasks[1],
                }));
                // console.log(`this is taskData ${taskData}`);
                
                const dict = {}

                // dict with user_name as key, data as values
                dict[user_name] = taskData
                // console.log(`this is dict ${dict}`);
                // tuck dict inside taskList
                taskList.push(dict);
            }
            // console.log(`this is taskList ${taskList}`);
            const chartDataList = [];
            
            // python = start at 0 index, continue until len(list), 
            // add index +1 each loop
            for(let i = 0; i < taskList.length; i++){
                // get name from taskList keys
                const name = Object.keys(taskList[i])[0]
                console.log(name);
                // get task freq type, total values and assign to data
                // const data = Object.keys(user_data[i])[0]
                const data = taskList[i][name]
                console.log(data);
                // assign color by iteration
                const color = background_dict['colors'][i]
                // add name, data, and color to chartDataList for chart
                chartDataList.push({
                    label: name,
                    data: data,
                    backgroundColor: color,
                    borderColor: color
                })
                // console.log(`this is dataList ${chartDataList}`);
            }

            new Chart(document.querySelector('#house-chart'), {
                type: 'bar',
                data: {
                    datasets: chartDataList,
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
