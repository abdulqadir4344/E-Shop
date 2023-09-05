let lastScrollTop = 0;

window.addEventListener("scroll", () => {
    const currentScrollTop = window.pageYOffset;

    if (currentScrollTop > lastScrollTop) {
        // Scrolling down
        document.querySelector(".navbar").classList.add("navbar-hide");
    } else {
        // Scrolling up
        document.querySelector(".navbar").classList.remove("navbar-hide");
    }

    lastScrollTop = currentScrollTop;
});
