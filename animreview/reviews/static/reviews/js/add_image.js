const preview = document.getElementById("preview");
const fileInput = document.getElementById('file-input');

document.querySelector("input[type='file']").addEventListener("change", function (event) {
  if (this.files[0]) {
    let fr = new FileReader();

    fr.addEventListener("load", function () {
      let image = document.createElement('img');
      image.classList.add('preview-item');
      image.src = fr.result;
      preview.append(image);
      fileInput.style.display = 'none';
    }, false);

    fr.readAsDataURL(this.files[0]);
  }
});