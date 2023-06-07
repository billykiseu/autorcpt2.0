//Copyright-Kiseu2023

//Mousemove
const heroContainers = document.querySelectorAll("[class^='herosubcontainer']");
heroContainers.forEach((container) => {
  const overlay = container.querySelector(".herooverlay");
  const backgroundImage = container.querySelector("[class^='heroimagetarget']");

  overlay.addEventListener("mousemove", (e) => {
    const rect = overlay.getBoundingClientRect();
    const offsetX = e.clientX - rect.left;
    const offsetY = e.clientY - rect.top;

    backgroundImage.style.setProperty("--mouse-x", -offsetX / 23 + "px");
    backgroundImage.style.setProperty("--mouse-y", -offsetY / 23 + "px");
  });
});

//Heroscroll
const heronext = document.getElementById("heronext");
const heroprev = document.getElementById("heroprev");
const herotarget = document.getElementById("herosupercontainer");

heronext.addEventListener("click", () => {
    herotarget.scrollBy(300, 0);
  });
heroprev.addEventListener("click", () => {
    herotarget.scrollBy(-300, 0);
  });

//Auto-scroll-hero
var autoScroll = setInterval(function () {
  herotarget.scrollBy(200, 0);
}, 10000);

//Auto-scroll-hero
var autoScroll = setInterval(function () {
  herotarget.scrollTo({ left: 0, behavior: 'smooth' });
}, 20000);


