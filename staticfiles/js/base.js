
const hamburger= document.querySelector(".hamburger");
const navbar_nav= document.querySelector(".navbar-nav");

hamburger.addEventListener("click",() => {
    hamburger.classList.toggle("active")
    navbar_nav.classList.toggle("active")
})

document.querySelectorAll(".nav-link").forEach(n => n.addEventListener("click", () => {
    hamburger.classList.remove("active");
    navbar_nav.classList.remove("active");
}))

