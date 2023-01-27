'use strict';

new Chart(document.querySelector('#bar-chart'), {
  type: 'bar',
  data: {
    labels: ['Please', 'Help', 'Me'],
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
