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



// js for sidebar

const body = document.querySelector('body'),
        sidebar = body.querySelector('nav'),
        toggle = body.querySelector(".toggle"),
        searchBtn = body.querySelector(".search-box"),
        modeSwitch = body.querySelector(".toggle-switch"),
        modeText = body.querySelector(".mode-text");
    toggle.addEventListener("click", () => {
        sidebar.classList.toggle("close");
    })
    searchBtn.addEventListener("click", () => {
        sidebar.classList.remove("close");
    })
    modeSwitch.addEventListener("click", () => {
        body.classList.toggle("dark");

        if (body.classList.contains("dark")) {
            modeText.innerText = "Light mode";
        } else {
            modeText.innerText = "Dark mode";

        }
    });


// end of js for sidebar





// js for toast progressbar


// end of js of proggress bar