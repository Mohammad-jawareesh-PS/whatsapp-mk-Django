function logout() {
  let logout_input = document.querySelector("input[name='logout']"),
    send = document.querySelector("#go_tasks_manage"),
    logout_bt = document.querySelector("#logout_bt");

  logout_bt.addEventListener("click", function () {
    logout_input.value = "True";
    send.click();
  });
}
logout();
