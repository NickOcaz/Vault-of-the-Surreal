
// ...existing code...
document.addEventListener('DOMContentLoaded', function() {
    var deleteModal = document.getElementById('deleteModal');
    if (deleteModal) {
        deleteModal.addEventListener('show.bs.modal', function (event) {
            var button = event.relatedTarget;
            var commentId = button.getAttribute('data-comment-id');
            var confirmDeleteButton = deleteModal.querySelector('#confirmDeleteButton');
            confirmDeleteButton.href = confirmDeleteButton.href.replace('0', commentId);
        });
    }