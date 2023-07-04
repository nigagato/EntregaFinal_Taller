const btn = document.querySelector('.btn.btn-light.btn-lg.ms-auto');

btn.addEventListener('click', function() {
  document.querySelector('.bg-modal').style.display = "flex";
});

document.querySelector('.close').addEventListener("click", function() {
	document.querySelector('.bg-modal').style.display = "none";
});