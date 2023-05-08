<template>
  <div id="app">
    <div class="container">
      <header class="text-center text-primary">
        <h1>SSAFY TUBE</h1>
      </header>
      <!-- video가 null인 경우 처리 -->
      <div v-if="video" class="ratio ratio-16x9">
        <iframe :src="videoUrl" frameborder="0"></iframe>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',

  data() {
    return {
      video: null,
    }
  },

  computed: {
    videoUrl() {
      return `https://www.youtube.com/embed/${this.video.id.videoId}`
    }
  },

  created(){
    axios({
      url: YOUTUBE_URL,
      params: {
        key: API_KEY,
        part: 'snippet',
        q: '젤다',
        type: 'video'
      }
    })
      .then(res => {
        console.log(res)
        this.video = res.data.items[0]
      })
      .catch(err => {
        console.log(err)
      })
  }
}
</script>

<style>
* {
  font-family: 'Noto Sans KR', sans-serif;
}
</style>
