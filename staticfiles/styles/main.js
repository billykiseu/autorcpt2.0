//Copyright-Kiseu2023

//Preloader
var loader = document.getElementById("preloader");
window.addEventListener("load", function () {
  loader.style.display = "none";
  logodesktop.style.display = "block";
});

//Scroll-to-top
mybutton = document.getElementById("up");
window.onscroll = function () {
  scrollFunction();
};
function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0;
}
//Hover effects
const handleOnMouseMove = e =>{
  const {currentTarget: target} =e;

  const rect = target.getBoundingClientRect(),
          x = e.clientX - rect.left,
          y = e.clientY - rect.top; 
  
  target.style.setProperty("--mouse-x", `${x}px`)
  target.style.setProperty("--mouse-y", `${y}px`);
}
//menubox
for(const card of document.querySelectorAll(".menusuperbox")){
card.onmousemove = e => handleOnMouseMove(e);
}
//footer hover
for(const card of document.querySelectorAll(".footer-subcontainer2")){
card.onmousemove = e => handleOnMouseMove(e);
}


//Search-toggle-full
const icon1 = document.getElementById("search-icon-full");
const search = document.getElementById("search-full");
const cancel = document.getElementById("close-full");
const menusuperbox1 = document.getElementById("menusuperbox1");
const menusuperbox2 = document.getElementById("menusuperbox2");
const menusuperbox3 = document.getElementById("menusuperbox3");
const menusuperbox4 = document.getElementById("menusuperbox4");

icon1.addEventListener("click", () => {
search.classList.toggle("active");
icon1.classList.toggle("active");
menusuperbox1.classList.toggle("hide");
menusuperbox2.classList.toggle("hide");
menusuperbox3.classList.toggle("hide");
menusuperbox4.classList.toggle("hide");
});
cancel.addEventListener("click", () => {
search.classList.toggle("active");
icon1.classList.toggle("active");
menusuperbox1.classList.toggle("hide");
menusuperbox2.classList.toggle("hide");
menusuperbox3.classList.toggle("hide");
menusuperbox4.classList.toggle("hide");
});

//Menu-toggle
const menutoggle = document.getElementById("mobile-toggle");
const menuclose = document.getElementById("mobile-close");
const navmobile = document.getElementById("mobilebox");

menutoggle.addEventListener("click", () => {
navmobile.classList.toggle("hide");
});
menuclose.addEventListener("click", () => {
navmobile.classList.toggle("hide");
});

//Navbar Stuff
let lastScroll = 0;
let isScrolling = false;

const target = document.getElementById("navcontainer");

function debounce(func, wait) {
let timeout;
return function executedFunction() {
  const context = this;
  const args = arguments;

  clearTimeout(timeout);

  timeout = setTimeout(() => {
    func.apply(context, args);
  }, wait);
};
}

function handleScroll() {
if (isScrolling) {
  return;
}

isScrolling = true;

const currentScroll = window.pageYOffset;

const menusperbox1 = document.getElementById("menusuperbox1");
const menusperbox2 = document.getElementById("menusuperbox2");
const menusperbox3 = document.getElementById("menusuperbox3");
const menusperbox4 = document.getElementById("menusuperbox4");
const menutoggle = document.getElementById("menutoggleicon");
const menutoggle2 = document.getElementById("mobile-toggle");
const contactbtn = document.getElementById("contactbtn");
const logo = document.getElementById("logo");
const searchicon = document.getElementById("search-icon-full");
const closesearch = document.getElementById("close-full");
const gosearch = document.getElementById("go-icon");

if (currentScroll < 50) {
  target.style.backgroundColor = "transparent";
  menusperbox1.style.filter = "invert(0)";
  menusperbox2.style.filter = "invert(0)";
  menusperbox3.style.filter = "invert(0)";
  menusperbox4.style.filter = "invert(0)";
  menutoggle.style.filter = "invert(100)";
  contactbtn.style.filter = "invert(0)";
  logo.style.filter = "invert(100)";
  searchicon.style.filter = "invert(100)";
  closesearch.style.filter = "invert(100)";
  gosearch.style.filter = "invert(100)";
} else if (currentScroll > 50) {
  target.style.backgroundColor = "var(--white)";
  menusperbox1.style.filter = "invert(100)";
  menusperbox2.style.filter = "invert(100)";
  menusperbox3.style.filter = "invert(100)";
  menusperbox4.style.filter = "invert(100)";
  menutoggle.style.filter = "invert(0)";
  contactbtn.style.filter = "invert(100)";
  logo.style.filter = "invert(0)";
  searchicon.style.filter = "invert(0)";
  closesearch.style.filter = "invert(0)";
  gosearch.style.filter = "invert(0)";
} else if (currentScroll > lastScroll && !target.classList.contains("hide")) {
  target.classList.remove("show");
  target.classList.add("hide");
  menutoggle2.classList.remove("show");
  menutoggle2.classList.add("hide");
  logo.classList.remove("show");
  logo.classList.add("hide");
}
if (currentScroll < lastScroll && !target.classList.contains("show")) {
  target.classList.remove("hide");
  target.classList.add("show");
  menutoggle2.classList.remove("hide");
  menutoggle2.classList.add("show");
  logo.classList.remove("hide");
  logo.classList.add("show");
} else if (currentScroll > lastScroll && target.classList.contains("show")) {
  target.classList.remove("show");
  target.classList.add("hide");
  menutoggle2.classList.remove("show");
  menutoggle2.classList.add("hide");
  logo.classList.remove("show");
  logo.classList.add("hide");
}

lastScroll = currentScroll;

setTimeout(() => {
  isScrolling = false;
}, 200);
}

// Debounced event listener
window.addEventListener("scroll", debounce(handleScroll, 100));


//Contact-scroll
const contactbtn = document.getElementById("contactbtn");
const contactscrollmobi = document.getElementById("contactbtnmobi");
const footerloc = document.getElementById("contactloc");

contactbtn.addEventListener("click", () => {
  footerloc.scrollIntoView();
});
contactscrollmobi.addEventListener("click", () => {
  footerloc.scrollIntoView();
});


//notifications
const closeButtons = document.querySelectorAll(".messageclose");
closeButtons.forEach((closeButton) => {
  closeButton.addEventListener("click", () => {
    const message = closeButton.closest(".messages");
    message.classList.add("hide");
  });
});