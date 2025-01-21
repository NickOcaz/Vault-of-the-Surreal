document.addEventListener("DOMContentLoaded", function() {
  const editButtons = document.getElementsByClassName("btn-edit");
  const commentText = document.getElementById("id_body");
  const commentForm = document.getElementById("commentForm");
  const submitButton = document.getElementById("submitButton");

  for (let button of editButtons) {
      button.addEventListener("click", (e) => {
          e.preventDefault();  // Prevent default behavior
          let commentId = e.target.getAttribute("comment_id");
          let commentContent = document.getElementById(`comment${commentId}`).innerText;
          commentText.value = commentContent;
          submitButton.innerText = "Update";
          commentForm.setAttribute("action", `edit_comment/${commentId}`);
      });
  }

  commentForm.addEventListener("submit", function(e) {
      e.preventDefault();  // Prevent default form submission

      const formData = new FormData(commentForm);
      const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

      fetch(commentForm.action, {
          method: 'POST',
          headers: {
              'X-CSRFToken': csrfToken
          },
          body: formData
      })
      .then(response => response.json())
      .then(data => {
          if (data.success) {
              if (data.is_update) {
                  const commentElement = document.getElementById(`comment${data.comment_id}`);
                  commentElement.innerText = data.comment_body;
                  submitButton.innerText = "Submit Comment";
              } else {
                  const newComment = document.createElement("div");
                  newComment.className = "p-2 comments";
                  newComment.id = `comment${data.comment_id}`;
                  newComment.innerHTML = `
                      <p class="font-weight-bold">
                          ${data.comment_author}
                          <span class="font-weight-normal">
                              ${data.comment_created_on}
                          </span> wrote:
                      </p>
                      <div id="comment${data.comment_id}">
                          ${data.comment_body}
                      </div>
                      <a href="#" class="btn btn-edit" comment_id="${data.comment_id}">Edit</a>
                      <a href="#" class="btn btn-delete" comment_id="${data.comment_id}">Delete</a>
                  `;
                  document.querySelector(".card-body").appendChild(newComment);
                  addEditDeleteListeners(newComment);
              }
              commentForm.reset();
          } else {
              console.error('Failed to update comment');
          }
      })
      .catch(error => console.error('Error:', error));
  });

  function addEditDeleteListeners(commentElement) {
      const editButton = commentElement.querySelector(".btn-edit");
      const deleteButton = commentElement.querySelector(".btn-delete");

      editButton.addEventListener("click", (e) => {
          e.preventDefault();
          let commentId = e.target.getAttribute("comment_id");
          let commentContent = document.getElementById(`comment${commentId}`).innerText;
          commentText.value = commentContent;
          submitButton.innerText = "Update";
          commentForm.setAttribute("action", `edit_comment/${commentId}`);
      });

      deleteButton.addEventListener("click", (e) => {
          e.preventDefault();
          let commentIdToDelete = e.target.getAttribute("comment_id");
          fetch(`delete_comment/${commentIdToDelete}`, {
              method: 'POST',
              headers: {
                  'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
              }
          }).then(response => {
              if (response.ok) {
                  document.getElementById(`comment${commentIdToDelete}`).remove();
              } else {
                  console.error('Failed to delete comment');
              }
          });
      });
  }
});