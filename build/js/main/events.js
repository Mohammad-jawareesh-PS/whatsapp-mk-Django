function dashboard_events() {
  let menu_controle = document.querySelector("#menu_controle"),
    sidebar = document.querySelector(".dashboard > .left"),
    logo = document.querySelector(".dashboard > .right .header .logo"),
    full = document.querySelector(".dashboard > .right .header .full"),
    content = document.querySelector(".dashboard > .right");

  menu_controle.addEventListener("click", function () {
    if (document.body.clientWidth >= 850) {
      if (sidebar.classList.contains("hide_sidebar")) {
        sidebar.classList.remove("hide_sidebar");
        logo.style.display = "none";
        content.classList.remove("full_width");
      } else {
        sidebar.classList.add("hide_sidebar");
        logo.style.display = "flex";
        content.classList.add("full_width");
      }
    } else {
      if (sidebar.classList.contains("show_sidebar")) {
        sidebar.classList.remove("show_sidebar");
        logo.style.display = "flex";
        if (document.body.clientWidth <= 640) {
          full.classList.remove("rtl");
        }
      } else {
        sidebar.classList.add("show_sidebar");
        logo.style.display = "none";
        if (document.body.clientWidth <= 640) {
          full.classList.add("rtl");
        }
      }
    }
  });
}
dashboard_events();
