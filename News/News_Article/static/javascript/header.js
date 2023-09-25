$(document).ready(function() {
    // Default: Load latest articles on page load
    loadArticles('latest');
  
    // Button click events
    $('#latestBtn').click(function() {
      loadArticles('latest');
    });
  
    $('#updatedBtn').click(function() {
      loadArticles('updated');
    });
  
    $('#newBtn').click(function() {
      loadArticles('new');
    });
  });
  
  function loadArticles(type) {
    // Make an AJAX request to your Django view to get the articles based on the type
    $.ajax({
      type: 'GET',
      url: '/get_articles/',  // Replace with your Django view URL
      data: { type: type },
      success: function(data) {
        $('#articleContainer').html(data);
      }
    });
  }
  


  const hamburgerIcon = document.getElementById('hamburger-icon');
  const dropdownContent = document.querySelector('.dropdown-content');
  
  hamburgerIcon.addEventListener('click', () => {
      dropdownContent.style.display = dropdownContent.style.display === 'none' ? 'block' : 'none';
  });
  



  document.getElementById("registration-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the default form submission
    
    // Gather user input
    var username = document.getElementById("username").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    
    // Perform any necessary validation here
    
    // After validation, redirect to the login page
    window.location.href = "login.html"; // Replace "login.html" with your actual login page URL
});


const urlParams = new URLSearchParams(window.location.search);
        const dataFromlatestpost = urlParams.get('data');
        document.getElementById('data').textContent = dataFromlatestpost;
    

        const form = document.getElementById('data-form');
        form.addEventListener('submit', function(event) {
            event.preventDefault();
            const data = form.elements.data.value;
            window.location.href = `latest.html?data=${encodeURIComponent(data)}`;
        });