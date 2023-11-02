let editor = document.querySelector("#editor");

const aceEditor = ace.edit(editor, {
    theme: "ace/theme/tomorrow_night_blue",
    mode: "ace/mode/python",
    // maxLines: 40,
    // minLines: 40,
    hasCssTransforms: true,
    value: "print(\"Hello world\")",
    fontSize: "18px",
});

document.getElementById("run_button").addEventListener("click", function () {
    const text = aceEditor.getValue();

    fetch("http://127.0.0.1:8000/run-code/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({code: text}),
    })
    .then(response => response.json())
    .then(data => {
        if (data.output) {
            // Update the content of the output <div>
            const outputDiv = document.getElementById("console_log");
            outputDiv.textContent = data.output;
        } else if (data.error) {
            console.error("Error:", data.error);
        }
    })
    .catch(error => {
        console.error("An error occurred:", error);
    });
});
