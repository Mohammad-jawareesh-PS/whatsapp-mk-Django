function tasks_status() {
  let main = document.querySelectorAll(".status");

  for (let index = 0; index < main.length; index++) {
    if (main[index].classList.contains("task_available")) {
      main[index].textContent = "متاحة";
    } else if (main[index].classList.contains("task_unavailable")) {
      main[index].textContent = "غير متاحة";
    }
  }
}

tasks_status();
