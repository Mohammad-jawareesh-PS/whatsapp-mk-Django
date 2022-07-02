function payments() {
  let by_now_button = document.querySelectorAll(".by_now"),
    card_payment_box = document.querySelector(".card_payment_box"),
    close_payment_box = document.querySelector(".close-box"),
    this_price_box = document.querySelector("#this_price"),
    price_input = document.querySelector('input[name="price"]');

  for (let index = 0; index < by_now_button.length; index++) {
    by_now_button[index].addEventListener("click", function () {
      card_payment_box.classList.remove("none");
      this_price_box.textContent = this.getAttribute("price");
      price_input.value = this.getAttribute("price").replace('$','');
      console.log(price_input.value);

      close_payment_box.addEventListener('click', function () {
        card_payment_box.classList.add("none");
      })
    });
  }
}
payments();
