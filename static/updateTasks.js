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
                const toRemoveLabel = document.getElementById('taskid');
                toRemoveLabel.remove();
                const toRemoveBox = document.getElementById('task');
                toRemoveBox.remove();
                const toRemoveDelete = document.getElementById('delete');
                toRemoveDelete.remove();
                const toRemoveComplete = document.getElementById('complete');
                toRemoveComplete.remove();
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
            console.log(status);
    });
};

