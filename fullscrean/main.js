// main.js
new Pageable("#container");

document.addEventListener("DOMContentLoaded", function () {
  var transitionVideo = document.getElementById("transition-video2");
  var transitionSection = document.querySelector(".transition-video2");
  var nextPage = document.getElementById("page-2");

  // 페이지 로드 시에 트랜지션 영상을 숨깁니다
  transitionSection.style.display = "none";

  // 스크롤 이벤트를 감지하여 트랜지션 섹션을 보여줍니다
  window.addEventListener("scroll", function () {
    // Get the position of the transition section relative to the viewport
    var transitionSectionPosition = transitionSection.getBoundingClientRect();

    // Calculate the threshold position for showing the transition section
    var threshold = window.innerHeight * 0.8;

    // Show the transition section if it enters the viewport
    if (transitionSectionPosition.top < threshold) {
      transitionSection.style.display = "block";
      transitionVideo.play();
    }
  });

  // 영상이 종료되면 페이지 2를 보여줍니다
  transitionVideo.addEventListener("ended", function () {
    transitionSection.style.display = "none";
    nextPage.style.display = "block";
  });
});
