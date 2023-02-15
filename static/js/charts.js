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
                        label: 'All Tasks Completed',
                        data: data,
                        backgroundColor: '#FC9BAE',
                        borderColor: '#FC9BAE',
                        borderWidth: 2

                    }],
                },
                options: {
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Frequency of Task',
                                borderColor: '#FC9BAE',
                                borderWidth: 2
                            },
                        },
                    y: {
                        title: {
                            display: true,
                            text: 'Number of Tasks Completed',
                            borderColor: '#FC9BAE',
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


// CODE REVIEW 2 2/3/23


// CHART DATA W/IN LAST MONTH - IN PROGRESS
document.getElementById('month_chart').addEventListener('click', (evt) => {
    evt.preventDefault();
    fetch('/get_date_range.json')
        .then((response) => response.json())
        .then((responseJson) => {
            const data = responseJson.data.map(tasks => ({
                x: tasks.freq,
                y: tasks.num,
                }));
            new Chart(document.querySelector('#bar-chart-month'), {
                type: 'bar',
                data: {
                    datasets: [{
                        label: 'Tasks Completed in Last 30 Days',
                        data: data,
                        backgroundColor: '#88D6FA',
                        borderColor: '#88D6FA',
                        borderWidth: 2

                    }],
                },
                options: {
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Frequency of Task',
                                borderColor: '#88D6FA',
                                borderWidth: 2
                            },
                        },
                    y: {
                        title: {
                            display: true,
                            text: 'Number of Tasks Completed',
                            borderColor: '#88D6FA',
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

// CHART FOR ALL HOUSEHOLD TASKS
document.getElementById('house_chart').addEventListener('click', (evt) => {
    evt.preventDefault();
    fetch('/house_tasks_complete.json')
        .then((response) => response.json())
        .then((responseJson) => {
            // make an array of responseJson key, values
            const user_data = Object.entries(responseJson['house'])
            // get list of colors for bar colors
            const background_dict = responseJson['bar_colors']

            let taskArr = [];
            for(const [user_name, user_tasks] of user_data){
                const data = user_tasks.map((tasks) => ({
                    x: tasks[0],
                    y: tasks[1],
                }));

                let dict = {}
                dict[user_name] = data
                taskArr.push(dict);
            }
            let dataArr = [];
            
            for(let i=0; i<taskArr.length; i++){
                // get name from taskArr keys
                let name = Object.keys(taskArr[i])[0]
                // get task freq type, total values and assign to data
                let data = taskArr[i][name]
                let color = background_dict['colors'][i]
                dataArr.push({
                    label: name,
                    data: data,
                    backgroundColor: color,
                    borderColor: color
                })
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
