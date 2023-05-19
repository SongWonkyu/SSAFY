<template>
  <div id="app">
    <nav-bar></nav-bar>
    <router-view />

    <div class="mainText">
      <span ref="textContainer">{{ typedText }}</span>
    </div>
  </div>
</template>

<script>
/* eslint-disable no-constant-condition */

import NavBar from "./NavBar.vue";

export default {
  name: "App",
  components: {
    NavBar,
  },
  mounted() {
    this.runTypingAnimation();
  },
  methods: {
    async runTypingAnimation() {
      const texts = [
        "Every ego has different movie.",
        "모든 자아는 다른 영화를 가지고 있습니다.",
        "すべてのエゴは異なる映画を持っている.",
        "每个自我都有不同的电影.",
        "Cada ego tiene películas diferentes.",
      ];

      const typingSpeed = 90; // 타이핑 속도 (1자당 밀리초)
      const eraseSpeed = 100; // 지우기 속도 (1자당 밀리초)
      const typingDelay = 100; // 다음 텍스트까지의 딜레이 (밀리초)
      const eraseDelay = 2000; // 텍스트를 모두 지우고 다음 텍스트까지의 딜레이 (밀리초)

      let index = 0;
      while (true) {
        const text = texts[index];
        const textContainer = this.$refs.textContainer;

        if (!textContainer) break; // 참조가 제대로 되지 않으면 종료

        // 타이핑 효과
        for (let j = 0; j <= text.length; j++) {
          textContainer.textContent = text.substr(0, j);
          await this.sleep(typingSpeed);
        }

        // 지우기 대기 시간
        await this.sleep(eraseDelay);

        // 지우기 효과
        for (let j = text.length; j >= 0; j--) {
          textContainer.textContent = text.substr(0, j);
          await this.sleep(eraseSpeed);
        }

        // 다음 텍스트까지의 딜레이
        await this.sleep(typingDelay);

        index = (index + 1) % texts.length; // 다음 텍스트로 이동
      }
    },
    sleep(ms) {
      return new Promise((resolve) => setTimeout(resolve, ms));
    },
  },
};
/* eslint-enable no-constant-condition */
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.mainText {
  font-size: 60px;
  font-weight: bold;
  color: white;
}
</style>
