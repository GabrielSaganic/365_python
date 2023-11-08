document.querySelectorAll('.like-button').forEach(button => {
    button.addEventListener('click', function() {
        const solutionId = this.getAttribute('data-solution-id');

        // Create an object to send as JSON data
        const requestData = {
            solution_id: solutionId,
        };

        fetch('http://127.0.0.1:8000/solution-list/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(requestData), // Send the solutionId in the request body
        })
        .then(response => response.json())
        .then(data => {
            if (data.output) {

                const outputDiv = document.getElementById("reaction_" + solutionId);
                outputDiv.textContent = data.output;
            } else if (data.error) {
                console.error("Error:", data.error);
            }
        })
        .catch(error => {
            console.error('An error occurred:', error);
        });
    });
});
