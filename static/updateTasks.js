'use strict';

// DELETE SELECTED TASK
function deleteButton() {
    const toDel = document.getElementById('task').value;
    const answer = confirm(`are you sure you want to delete ${toDel}`);
    if (answer) {
        const queryString = new URLSearchParams({ task: toDel }).toString();
        const url = `/delete_task?${queryString}`;
        fetch(url)
            .then((response) => response.text())
            .then((status) => {
                const toRemoveTask = document.getElementById('eachtask');
                console.log(toRemoveTask);
                toRemoveTask.remove();
                // const toRemoveLabel = document.getElementById('taskid');
                // toRemoveLabel.remove();
                // const toRemoveBox = document.getElementById('task');
                // toRemoveBox.remove();
                // const toRemoveDelete = document.getElementById('delete');
                // toRemoveDelete.remove();
                // const toRemoveComplete = document.getElementById('complete');
                // toRemoveComplete.remove();
                alert(`${status} has successfully been removed`);
            });
    }
    else {
        console.log('that didnt work');
    }
    }

// MARKS TASK COMPLETE

function completeButton() {
    const toComplete = document.getElementById('task').value;
    const queryString = new URLSearchParams({ task: toComplete }).toString();
    const url = `/complete_task?${queryString}`;
    fetch(url)
        .then((response) => response.text())
        .then((status) => {
            // insertAdjacentHTML placeholder to change style to crossout once CSS made
            const selectItem = document.getElementById(`${status}div`);
            console.log(selectItem);
            console.log(status);
    });
};

// CLEAR COMPLETED TASKS FROM CHECKLIST

function clearButton() {
    const toClear = document.getElementById('task').value;
    const queryString = new URLSearchParams({ task: toClear }).toString();
    const url = `/clear_task?${queryString}`;
    fetch(url)
        .then((response) => response.text())
        .then((status) => {
            const toClearLabel = document.getElementById('`${status}div`');
            toClearLabel.remove();
            alert(`${status} has successfully been cleared`);
        })
}