document.addEventListener('DOMContentLoaded', function() {
    // Get modal elements
    const loginModal = document.getElementById('loginModal');
    const signupModal = document.getElementById('signupModal');
    const loginBtn = document.getElementById('loginBtn');
    const signupBtn = document.getElementById('signupBtn');
    const closeBtns = document.getElementsByClassName('close');
    const logoutBtn = document.createElement('a');
    logoutBtn.href = '#';
    logoutBtn.textContent = 'Logout';
    logoutBtn.id = 'logoutBtn';

    // Check if user is logged in
    function checkLoginStatus() {
        const user = JSON.parse(localStorage.getItem('currentUser'));
        if (user) {
            loginBtn.style.display = 'none';
            signupBtn.style.display = 'none';
            if (!document.getElementById('logoutBtn')) {
                loginBtn.parentElement.insertAdjacentElement('afterend', 
                    Object.assign(document.createElement('li'), {
                        innerHTML: logoutBtn.outerHTML
                    })
                );
            }
        } else {
            loginBtn.style.display = '';
            signupBtn.style.display = '';
            const logoutBtnElement = document.getElementById('logoutBtn');
            if (logoutBtnElement) {
                logoutBtnElement.parentElement.remove();
            }
        }
    }

    // Open modals
    loginBtn.onclick = () => loginModal.style.display = "block";
    signupBtn.onclick = () => signupModal.style.display = "block";

    // Close modals
    Array.from(closeBtns).forEach(btn => {
        btn.onclick = function() {
            loginModal.style.display = "none";
            signupModal.style.display = "none";
        }
    });

    // Close when clicking outside
    window.onclick = function(event) {
        if (event.target == loginModal || event.target == signupModal) {
            loginModal.style.display = "none";
            signupModal.style.display = "none";
        }
    }

    // Handle form submissions
    document.getElementById('loginForm').onsubmit = function(e) {
        e.preventDefault();
        const email = document.getElementById('loginEmail').value;
        const password = document.getElementById('loginPassword').value;
        
        // Get users from localStorage
        const users = JSON.parse(localStorage.getItem('users')) || [];
        const user = users.find(u => u.email === email && u.password === password);
        
        if (user) {
            localStorage.setItem('currentUser', JSON.stringify(user));
            loginModal.style.display = "none";
            alert('Successfully logged in!');
            checkLoginStatus();
        } else {
            alert('Invalid email or password!');
        }
    }

    document.getElementById('signupForm').onsubmit = function(e) {
        e.preventDefault();
        const name = document.getElementById('signupName').value;
        const email = document.getElementById('signupEmail').value;
        const password = document.getElementById('signupPassword').value;
        const confirmPassword = document.getElementById('confirmPassword').value;

        if (password !== confirmPassword) {
            alert('Passwords do not match!');
            return;
        }

        // Get existing users
        const users = JSON.parse(localStorage.getItem('users')) || [];
        
        // Check if email already exists
        if (users.some(user => user.email === email)) {
            alert('Email already registered!');
            return;
        }

        // Add new user
        const newUser = {
            name,
            email,
            password,
            progress: {} // Add progress tracking object
        };
        
        users.push(newUser);
        localStorage.setItem('users', JSON.stringify(users));
        localStorage.setItem('currentUser', JSON.stringify(newUser));
        
        signupModal.style.display = "none";
        alert('Successfully registered!');
        checkLoginStatus();
    }

    // Handle logout
    document.addEventListener('click', function(e) {
        if (e.target && e.target.id === 'logoutBtn') {
            localStorage.removeItem('currentUser');
            checkLoginStatus();
            alert('Successfully logged out!');
        }
    });

    // Check login status on page load
    checkLoginStatus();
}); 