var loadFile = function (event) {
  var image = document.getElementById("output");
  image.src = URL.createObjectURL(event.target.files[0]);
  let t1 = document.getElementById("text");
  // let hidden = element.getAttribute("hidden");
  t1.removeAttribute("hidden");
};
