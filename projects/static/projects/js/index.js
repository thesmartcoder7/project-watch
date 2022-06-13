const scrollContainer = document.querySelector(".all-users");

scrollContainer.addEventListener("wheel", (evt) => {
  evt.preventDefault();
  scrollContainer.scrollLeft += evt.deltaY;
});

document.querySelector(".current-year").textContent = new Date().getFullYear();
