'use strict';

fetch('/tasks_per_week.json')
.then(response => response.json())
.then(responseJson => {
  let data = [];
  for(const dailyTotal of responseJson.data){
    data.push({x: dailyTotal.tasks, y: dailyTotal.frequency
  });
  new Chart(document.querySelector('#bar-chart'), {
  type: 'bar',
  data: {
    labels: ['Call', 'Me', 'Maybe', '?'],
    datasets: [
      {
        label: 'As Needed',
        data: [10, 36, 27],
      },
      {
        label: 'Daily',
        data: [5, 0, 7],
      },
      {
        label: 'Weekly',
        data: [5, 0, 7],
      },      {
        label: 'Monthly',
        data: [5, 0, 7],
      },]
    }})}});
