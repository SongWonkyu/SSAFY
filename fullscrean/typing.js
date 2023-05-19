// 텍스트 컨테이너 요소 선택
var textContainer = document.getElementById("text-container");

// 타이핑 애니메이션 실행
function runTypingAnimation() {
  var texts = [
    "Every ego has different \nmovie",
    "모든 자아는 다른 영화를 \n가지고 있습니다",
    "すべてのエゴは異なる\n映画を持っている",
    "每个自我都有不同的电影",
    "Cada ego tiene películas\n diferentes",
  ];

  var currentTextIndex = 0;
  var currentText = texts[currentTextIndex];

  var typingSpeed = 90; // 타이핑 속도 (1자당 밀리초)
  var eraseSpeed = 100; // 지우기 속도 (1자당 밀리초)
  var showDuration = 2000; // 텍스트를 표시할 시간 (밀리초)

  var typingDelay = 100; // 다음 텍스트까지의 딜레이 (밀리초)
  var eraseDelay = 0; // 텍스트를 모두 지우고 다음 텍스트까지의 딜레이 (밀리초)

  var charIndex = 0;
  var isTyping = true;

  function type() {
    if (charIndex < currentText.length) {
      textContainer.textContent += currentText.charAt(charIndex);
      charIndex++;
      setTimeout(type, typingSpeed);
    } else {
      isTyping = false;
      setTimeout(erase, eraseDelay);
    }
  }

  function erase() {
    if (charIndex > 0) {
      textContainer.textContent = currentText.substring(0, charIndex - 1);
      charIndex--;
      setTimeout(erase, eraseSpeed);
    } else {
      isTyping = true;
      currentTextIndex++;
      if (currentTextIndex >= texts.length) {
        currentTextIndex = 0;
      }
      currentText = texts[currentTextIndex];
      setTimeout(type, typingDelay);
    }
  }

  type();
}

// 타이핑 애니메이션 실행 시작
runTypingAnimation();
