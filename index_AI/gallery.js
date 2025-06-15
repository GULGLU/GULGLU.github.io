const modal = document.getElementById("modal");
const modalImg = document.getElementById("modal-img");
const closeBtn = document.getElementById("close");

document.querySelectorAll(".gallery img").forEach((img) => {
  img.addEventListener("click", () => {
    modal.style.display = "block";
    modalImg.src = img.src;
  });
});

closeBtn.onclick = () => {
  modal.style.display = "none";
};

window.onclick = (e) => {
  if (e.target == modal) {
    modal.style.display = "none";
  }
};
