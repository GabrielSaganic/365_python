document.getElementById("commit_button").addEventListener("click", function () {
    const text = aceEditor.getValue();

    fetch("http://127.0.0.1:8000/task-of-day/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({code: text}),
    })
    .then(response => {
        if (response.status === 201) {
          window.location.href = "http://127.0.0.1:8000/solution-list/";
        }
      })
    .catch(error => {
        console.error("An error occurred:", error);
    });
});
