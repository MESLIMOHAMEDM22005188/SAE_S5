document.addEventListener('DOMContentLoaded', function() {
    const passwordInput = document.getElementById('password');
    const strengthMessage = document.getElementById('strengthMessage');

    passwordInput.addEventListener('input', function() {
        const password = passwordInput.value;

        // Critères de vérification de la force du mot de passe
        const regexWeak = /^.{1,7}$/;
        const regexMedium = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$/;
        const regexStrong = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>]).{8,}$/;

        if (regexWeak.test(password)) {
            strengthMessage.textContent = 'Faible';
            strengthMessage.className = 'weak';
        } else if (regexMedium.test(password)) {
            strengthMessage.textContent = 'Moyen';
            strengthMessage.className = 'medium';
        } else if (regexStrong.test(password)) {
            strengthMessage.textContent = 'Fort';
            strengthMessage.className = 'strong';
        } else {
            strengthMessage.textContent = '';
            strengthMessage.className = '';
        }
    });
});
