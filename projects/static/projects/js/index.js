const scrollContainer = document.querySelector(".all-users");

if (scrollContainer) {
  scrollContainer.addEventListener("wheel", (evt) => {
    evt.preventDefault();
    scrollContainer.scrollLeft += evt.deltaY;
  });
}
