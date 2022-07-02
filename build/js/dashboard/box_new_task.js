function box_new_task() {
  let close_box = document.querySelectorAll(".close-box"),
    add_task_bt = document.querySelector(".add_task_bt");
  box = document.querySelector(".box_new_task");

  close_box[0].addEventListener("click", function () {
    box.classList.add("none");
  });
  close_box[1].addEventListener("click", function () {
    box.classList.add("none");
  });
  add_task_bt.addEventListener("click", function () {
    box.classList.remove("none");
  });
}
box_new_task();
