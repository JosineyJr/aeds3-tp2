document.addEventListener("DOMContentLoaded", function() {
  const submitButton = document.getElementById('submit-button');
  const fileInput = document.getElementById('file-input');

  submitButton.disabled = true;

  fileInput.addEventListener('change', function() {
      if (this.files.length > 0) {
          submitButton.disabled = false;
      } else {
          submitButton.disabled = true;
      }
  });
});