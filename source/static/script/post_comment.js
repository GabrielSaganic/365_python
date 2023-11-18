function postComment(solution_id) {
    const comment = document.getElementById("comment-text").value;

    fetch("http://127.0.0.1:8000/comment-list/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(
            {
                comment: comment,
                solution_id: solution_id,
            }
        ),
    })
    .then(response => response.json())
    .then(data => {
        var newCommentDiv = document.createElement("div");
        newCommentDiv.innerHTML = `
            <p class="gray-small-text">${data.user} - ${data.time}</p>
            <p class="comment-text">${comment}</p>
        `;
        var commentsContainer = document.getElementById("comment_box");
        commentsContainer.insertBefore(newCommentDiv, commentsContainer.firstChild);
    })
};
