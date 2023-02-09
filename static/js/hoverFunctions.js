'use strict';

// hover over trash user
const trashUser = document.getElementById("delete_user");

trashUser.addEventListener('mouseover', () => {
    document.getElementById('pop_delete_user').style.display = 'block';
});

trashUser.addEventListener('mouseout', () => {
    document.getElementById('pop_delete_user').style.display = 'none';
});

// hover over log out
const logout = document.getElementById("log_out");

logout.addEventListener('mouseover', () => {
    document.getElementById('pop_logout').style.display = 'block';
});

logout.addEventListener('mouseout', () => {
    document.getElementById('pop_logout').style.display = 'none';
});

// hover over mark task complete
const markCompleteButton = document.getElementById("mark_complete");

markCompleteButton.addEventListener('mouseover', () => {
    document.getElementById('pop_complete').style.display = 'block';
});

markCompleteButton.addEventListener('mouseout', () => {
    document.getElementById('pop_complete').style.display = 'none';
});

// hover over mark task complete
const markDeleteButton = document.getElementById("delete_tasks");

markDeleteButton.addEventListener('mouseover', () => {
    document.getElementById('pop_delete').style.display = 'block';
});

markDeleteButton.addEventListener('mouseout', () => {
    document.getElementById('pop_delete').style.display = 'none';
});

// hover over show chart
const chartButton = document.getElementById("chart");

chartButton.addEventListener('mouseover', () => {
    document.getElementById('pop_chart').style.display = 'block';
});

chartButton.addEventListener('mouseout', () => {
    document.getElementById('pop_chart').style.display = 'none';
});

// hover over household chart
const houseChartButton = document.getElementById("house_chart");

houseChartButton.addEventListener('mouseover', () => {
    document.getElementById('pop_house_chart').style.display = 'block';
});

houseChartButton.addEventListener('mouseout', () => {
    document.getElementById('pop_house_chart').style.display = 'none';
});