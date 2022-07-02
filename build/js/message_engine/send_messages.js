function send_messages() {
  let received_numbers = document.querySelectorAll(".received_number");
  let reloader = document.querySelector(".reloader");
  let sending = document.querySelector(".sending");
  let sended = document.querySelector(".sended");
  let header_number = document.querySelector(".header_this_number");
  let stop = document.querySelector(".stop");
  let start = document.querySelector(".start");
  let mesages = document.querySelectorAll(".mesages_by_number");
  let full_background = document.querySelector(".full_element_back");
  let this_message = document.querySelector(".this_message");
  let this_time = document.querySelector(".this_time");

  const sleep = (milliseconds) => {
    return new Promise((resolve) => setTimeout(resolve, milliseconds));
  };

  const doSomething = async () => {
    for (let index = 0; index < received_numbers.length; index++) {
      header_number.textContent =
        received_numbers[index].getAttribute("number");

      this_message.classList.add("this_message_waite");
      this_time.textContent = "";

      for (let i = 0; i < mesages.length; i++) {
        if (
          mesages[i].getAttribute("number") ==
          received_numbers[index].getAttribute("number")
        ) {
          mesages[i].classList.remove("none");
        } else {
          mesages[i].classList.add("none");
        }
      }

      await sleep(5000);
      received_numbers[index].classList.add("phone-activate");
      this_message.classList.remove("this_message_waite");

      let today = new Date();
      this_time.textContent = today.getHours() + ":" + today.getMinutes();

      reloader.classList.add("none");
      sending.classList.add("none");
      sended.classList.remove("none");
      await sleep(2000);
      reloader.classList.remove("none");
      sending.classList.remove("none");
      sended.classList.add("none");
    }
    reloader.classList.add("none");
    sending.classList.add("none");
    sended.classList.remove("none");
    stop.classList.add("none");
    start.classList.remove("none");
    full_background.classList.remove("none");
  };

  doSomething();
}

send_messages();
