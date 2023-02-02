'use strict';
// sample chart
new Chart(document.querySelector('#bar-chart'), {
  type: 'bar',
  data: {
    labels: ['What', 'Am', 'I Doing'],
    datasets: [
      {
        label: 'Today',
        data: [10, 36, 27],
      },
      {
        label: 'Yesterday',
        data: [5, 0, 7],
      },
    ],
  },
});

