const scrollContainer = document.querySelector(".all-users");

scrollContainer.addEventListener("wheel", (evt) => {
  evt.preventDefault();
  scrollContainer.scrollLeft += evt.deltaY;
});

console.log("this is working");
