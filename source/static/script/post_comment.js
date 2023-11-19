function postComment(solution_id) {
    var comment_textarea = document.getElementById("comment-text");
    const comment = comment_textarea.value

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
        comment_textarea.value = ""
        var commentsContainer = document.getElementById("comment_box");
        commentsContainer.insertBefore(newCommentDiv, commentsContainer.firstChild);
    })
};
