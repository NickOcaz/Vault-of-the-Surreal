
document.addEventListener('DOMContentLoaded', function () {
    // ...existing code...

    function showSuccessMessage(message) {
        const successMessageElement = document.createElement('div');
        successMessageElement.className = 'alert alert-success';
        successMessageElement.innerText = message;
        document.body.prepend(successMessageElement);
        setTimeout(() => {
            successMessageElement.remove();
        }, 3000);
    }

    // Example usage after login, logout, or registration
    document.getElementById('loginForm').addEventListener('submit', function (e) {
        e.preventDefault();
        // ...existing login logic...
        showSuccessMessage('Successfully logged in.');
    });

    document.getElementById('logoutButton').addEventListener('click', function (e) {
        e.preventDefault();
        // ...existing logout logic...
        showSuccessMessage('Successfully logged out.');
    });

    document.getElementById('registerForm').addEventListener('submit', function (e) {
        e.preventDefault();
        // ...existing registration logic...
        showSuccessMessage('Successfully registered.');
    });

    // ...existing code...
});