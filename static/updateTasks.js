'use strict';

// DELETE SELECTED TASK
for (const button of document.querySelectorAll('.delete')) {
    button.addEventListener('click', () => {
    // get task by button.id
        const toDel = button.id;
        const answer = confirm(`are you sure you want to delete ${toDel}`);
        if (answer) {
            const queryString = new URLSearchParams({ task: toDel }).toString();
            const url = `/delete_task?${queryString}`;
            fetch(url)
                .then((response) => response.text())
                .then((status) => {
                    console.log(status);
                    const toDeleteLabel = document.getElementById(`${status}div`);
                    toDeleteLabel.remove();
                });
        }
        else {
            console.log('cancelled');
        }
    });
};

// MARKS TASK COMPLETE
for (const button of document.querySelectorAll('.complete')) {
    button.addEventListener('click', () => {
    // get task by button.id
        const toComp = button.id;
        const queryString = new URLSearchParams({ task: toComp }).toString();
        const url = `/complete_task?${queryString}`;
        fetch(url)
            .then((response) => response.text())
            .then((status) => {
                // insertAdjacentHTML placeholder to change style to crossout once CSS made
                const selectItem = document.getElementById(`${status}div`);
                selectItem.insertAdjacentHTML('afterbegin', '<s>complete</s>');
    });
});
};

// CLEAR COMPLETED TASKS FROM CHECKLIST
// only clears one at a time, need to update so it clears all tasks marked complete
// function clearButton() {
//     const toClear = document.getElementById('taskinput').value;
//     const queryString = new URLSearchParams({ task: toClear }).toString();
//     const url = `/clear_task?${queryString}`;
//     fetch(url)
//         .then((response) => response.text())
//         .then((status) => {
//             const toClearLabel = document.getElementById(`${status}div`);
//             toClearLabel.remove();
//             alert(`${status} has successfully been cleared`);
//         })
// };