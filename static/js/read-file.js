function readFile(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function (e) {
      document.getElementById('file-content').textContent = e.target.result;
    };
    reader.readAsText(input.files[0]);
  }
}