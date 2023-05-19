<template>
  <div class="home">
    <homeHeader />
    <video class="background-video" autoplay muted loop>
      <source src="@/assets/homeBackgroundVideo.mp4" type="video/mp4" />
    </video>
  </div>
</template>

<script>
// @ is an alias to /src

export default {};
</script>
<style>
.home {
  background-color: rgba(255, 255, 255, 100); /* 흰색에 0.5의 투명도 설정 */
}

.background-video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -1;
}
</style>
