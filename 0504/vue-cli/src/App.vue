<template>
  <div id="app">
    <header>
      <h1>버튼 박스 제작</h1>
    </header>
    <section>
      <h2>예약 페이지</h2>
      <h3>시간 선택</h3>
      <div class="time-table">
        <span v-for="(time, idx) in times" :key="idx"
          class="time" :class="{selected: isSelected(time)}"
          @click="selectTime(time)"
        >
          {{ time }}
        </span>
      </div>
      <div class="divider"></div>
      <div class="select-talbe">
        선택시간: 
        <span v-for="(time, idx) in selectTimes" :key="idx">
          {{time}}
        </span>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {      
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
        "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      selectTimes: [],
    }
  },
  methods: {
    isSelected(time) {
      return this.selectTimes.includes(time)
    },
    selectTime(time) {      
      const idx = this.selectTimes.indexOf(time)
      if(idx < 0){
        if(this.selectTimes.length === 5) {
          alert('그만...많이묵었다..')
          return
        }
        this.selectTimes.push(time)
      }else{
        this.selectTimes.splice(idx, 1)
      }
    }
  }
}
</script>

<style>
/* #0F4C81, #658dc63d, #84898C, #424242 */
* {
  font-family: 'Noto Sans KR', sans-serif;
}
header {
  text-align: center;
}
section {
  display: flex;
  flex-direction: column;
  align-items: center;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px;
}
.divider {
  border-bottom: 1px solid #0F4C81;
  width: 80%;
}
.time-table {
  width: 560px;
  display: flex;
  flex-wrap: wrap;
}
.time {
  width: 80px;
  margin-bottom: 10px;
  text-align: center;
}
.time:hover {
  cursor: pointer;
  background-color: #658dc63d;
}
.selected {
  background-color: #658dc63d;
}
</style>
