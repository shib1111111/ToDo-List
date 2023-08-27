function deleteTask(taskId) {
            if (confirm("Are you sure you want to delete this task?")) {
                fetch(`/tasks/delete/${taskId}`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    }
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        alert("Task deleted successfully!");
                        window.location.reload(); // Refresh the page to update the task list
                    } else {
                        alert("Failed to delete the task.");
                    }
                })
                .catch(error => {
                    console.error("Error:", error);
                });
            }
        }


function openUpdatePopup(taskId, currentTitle, currentDescription) {
        var newTitle = prompt("Enter new title:", currentTitle);
        var newDescription = prompt("Enter new description:", currentDescription);
        
        if (newTitle !== null && newDescription !== null) {
            var data = {
                title: newTitle,
                description: newDescription
            };

            fetch(`/tasks/update/${taskId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert("Task updated successfully!");
                    window.location.reload(); // Refresh the page to update the task list
                } else {
                    alert("Failed to update the task.");
                }
            })
            .catch(error => {
                console.error("Error:", error);
            });
        }
    }
