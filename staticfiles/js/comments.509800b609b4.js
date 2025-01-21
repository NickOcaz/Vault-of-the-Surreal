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
              const commentElement = document.getElementById(`comment${data.comment_id}`);
              commentElement.innerText = data.comment_body;
              submitButton.innerText = "Submit Comment";
              commentForm.reset();
          } else {
              console.error('Failed to update comment');
          }
      })
      .catch(error => console.error('Error:', error));
  });
});