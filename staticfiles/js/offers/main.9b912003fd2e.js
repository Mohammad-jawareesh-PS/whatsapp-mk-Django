function payments(){let e=document.querySelectorAll(".by_now"),t=document.querySelector(".card_payment_box"),n=document.querySelector(".close-box"),c=document.querySelector("#this_price"),o=document.querySelector('input[name="price"]');for(let r=0;r<e.length;r++)e[r].addEventListener("click",(function(){t.classList.remove("none"),c.textContent=this.getAttribute("price"),o.value=this.getAttribute("price").replace("$",""),console.log(o.value),n.addEventListener("click",(function(){t.classList.add("none")}))}))}payments(),document.getElementById("offers").classList.add("this-page");
//# sourceMappingURL=../../maps/js/offers/main.js.29ffd8a3c63c.map