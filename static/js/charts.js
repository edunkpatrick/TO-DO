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


// CODE REVIEW 2 2/3/23


// CHART DATA TO MAKE SPECIFIC RANGE - IN PROGRESS
document.getElementById('date_range').addEventListener('submit', (evt) => {
    evt.preventDefault();
    console.log('button worked');
    fetch('/get_date_range.json')
        .then((response) => response.json())
        .then((responseJson) => {
            const data = responseJson.data.map(tasks => ({
                x: tasks.freq,
                y: tasks.num,
                }));
            Chart.destroy();
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

// CHART FOR ALL HOUSEHOLD TASKS
document.getElementById('house_chart').addEventListener('click', (evt) => {
    evt.preventDefault();
    fetch('/house_tasks_complete.json')
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
