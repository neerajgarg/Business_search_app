const slider = document.querySelector("#slider-input");
const selector = document.querySelector(".slider");
const progressBar = document.querySelector(".slider-range");
const track = document.querySelector(".slider-track");
let upperlimit = document.querySelector("#upperlimit");

const thumbSize = 12;

console.log(track.offsetWidth);
console.log(slider.offsetWidth);

upperlimit.innerText = slider.value;

let newVal = Number(
  ((slider.value - slider.min) * 100) / (slider.max - slider.min)
);

selector.style.left =
  this.value == 0 ? `0px` : `calc(${newVal}% + (${3 - newVal * 0.15}px))`;
progressBar.style.width =
  this.value == 0 ? `0px` : `calc(${newVal}% + (${3 - newVal * 0.15}px))`;

slider.oninput = function () {
  newVal = Number(((this.value - this.min) * 100) / (this.max - this.min));

  selector.style.left =
    this.value == 0 ? `0px` : `calc(${newVal}% + (${3 - newVal * 0.15}px))`;

  progressBar.style.width =
    this.value == 0 ? `0px` : `calc(${newVal}% + (${3 - newVal * 0.15}px))`;
  upperlimit.innerText = newVal;
};

$(window).scroll(function () {
  var scroll = $(window).scrollTop();

  //>=, not <=
  if (scroll >= 30) {
    $(".navbar").removeClass("is-transparent");
    $(".navbar").addClass("is-bg-light");
  } else {
    $(".navbar").addClass("is-transparent");
    $(".navbar").removeClass("is-bg-light");
  }
});

$(".navbar-toggler").click(function () {
  if ($(".navbar-collapse").hasClass("show")) {
    $(".navbar").addClass("is-transparent");
    $(".navbar").removeClass("is-bg-light");
  } else {
    $(".navbar").removeClass("is-transparent");
    $(".navbar").addClass("is-bg-light");
  }
});

$("#as-grid").click(function () {
  if ($(".result-list-card")) {
    $("#as-grid").addClass("active");
    $("#as-list").removeClass("active");

    $(".result-list-card").addClass("result-grid-card");
    $(".result-list-card").addClass("col-md-4");
    $(".result-list-card").addClass("my-2");
    $(".result-list-card").removeClass("px-0");
    $(".result-list-card").removeClass("result-list-card");
    $("#results").removeClass("col-md-10");
    $("#results").addClass("col-12");
    $(".color-codes").removeClass("d-md-block");
    $("#color-codes").removeClass("d-md-none");
  }
});

$("#as-list").click(function () {
  if ($(".result-grid-card")) {
    $("#as-list").addClass("active");
    $("#as-grid").removeClass("active");

    $(".result-grid-card").addClass("result-list-card");
    $(".result-grid-card").removeClass("col-md-4");
    $(".result-grid-card").removeClass("my-2");
    $(".result-grid-card").addClass("px-0");
    $(".result-grid-card").removeClass("result-grid-card");
    $("#results").addClass("col-md-10");
    $("#results").removeClass("col-12");
    $(".color-codes").addClass("d-md-block");
    $("#color-codes").addClass("d-md-none");
  }
});

let userType = "guest";

$("input[type=radio][name=isSubscribe]").change(function () {
  userType = this.value;
});

$(".show-more").click(function (e) {
  e.preventDefault();
  var id = e.target.id;
  var digit = id.split("-")[1];

  var isSubscribed = false;

  $(`#card-${digit} .flip-card-inner`).toggleClass("flip");

  $("input[type=radio][name=isSubscribe]").change(function () {
    userType = this.value;
  });

  if (userType == "subscribe") {
    $(`#card-${digit} .flip-card-back .result-info`).html(
      `<small>
        <span class="mdi mdi-email mr-2"> </span>
        rnehr@cobank.com
      </small>
      <small>
        <span class="mdi mdi-phone mr-2"> </span>
        (303)-740-6570
      </small>
      <small>
        <span class="mdi mdi-trending-up mr-2"> </span>
        $100M - $499M
      </small>
      <small>
        <span class="mdi mdi-star mr-2"> </span>
        Ransomeware Hostage Rescue Manual
      </small>
      <small>
        <span class="mdi mdi-label-variant mr-2"> </span>
        KnowBe4
      </small>`
    );
  } else {
    $(`#card-${digit} .flip-card-back .result-info`).html(
      `<div class="subscribe">
          <a href="" class="subs-btn">subscribe</a>
          <p class="is-light">This part is only available for members</p>
        </div>`
    );
  }
});
