document.addEventListener('DOMContentLoaded', function () {
    const editButtons = document.getElementsByClassName("btn-edit");
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");
    const deleteModalElement = document.getElementById("deleteModal");
    const deleteModal = new bootstrap.Modal(deleteModalElement);
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("confirmDeleteButton");

    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("data-comment_id");
            let commentElement = document.getElementById(`comment${commentId}`);
            if (commentElement) {
                let commentContent = commentElement.innerText;
                commentText.value = commentContent;
                submitButton.innerText = "Update";
                commentForm.setAttribute("action", `edit_comment/${commentId}/`);
            } else {
                console.error(`Comment element with ID comment${commentId} not found.`);
            }
        });
    }

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("data-comment-id");
            deleteConfirm.href = `delete_comment/${commentId}`;
            deleteModal.show();
        });
    }
});

var deleteModal = document.getElementById('deleteModal');
deleteModal.addEventListener('show.bs.modal', function (event) {
    var button = event.relatedTarget;
    var commentId = button.getAttribute('data-comment-id');
    var confirmDeleteButton = deleteModal.querySelector('#confirmDeleteButton');
    confirmDeleteButton.href = "{% url 'comment_delete' slug=movie.slug comment_id=0 %}".replace('0', commentId);
});