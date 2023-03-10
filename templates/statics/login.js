const signInButton = document.querySelector('button');

signInButton.addEventListener('click', () => {
  const email = document.querySelector('input[type="email"]').value;
  const password = document.querySelector('input[type="password"]').value;
  
  // Here we can perform some logic to check if the email and password are correct
  // For example, we can send an API request to a backend server to authenticate the user
  
  // If the user is authenticated, we can redirect them to another page
  window.location.href = '/dashboard.html';
});
