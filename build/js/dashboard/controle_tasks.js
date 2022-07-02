function controle_tasks() {
  let delet = document.querySelectorAll(".delete"),
    start = document.querySelectorAll(".start"),
    send = document.querySelector("#go_tasks_manage"),
    input = document.querySelector("input[name='start']"),
    task_id = document.querySelectorAll("span#task_id"),
    url = document.querySelector(".go_to_message_engine");

  for (let index = 0; index < task_id.length; index++) {
    delet[index].addEventListener("click", function () {
      input.value = `delet,${task_id[index].getAttribute("data")}`;
      send.click();
    });
    if (start[index].getAttribute("statu") == "off") {
      start[index].style.backgroundColor = "#04b07d66";
    } else {
      start[index].addEventListener("click", function () {
        input.value = `start,${task_id[index].getAttribute("data")}`;
        send.click();
        url.href = this.getAttribute("url");
        url.click();
        // window.open("http://127.0.0.1:8000/dashboard/message_engine");
      });
    }
  }
}
controle_tasks();
