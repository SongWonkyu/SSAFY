<template>
  <div id="app">
    <header>
      <h1>버튼 박스 제작</h1>
    </header>

    <section>
      <h2>예약 페이지</h2>
      <h3>시간 선택</h3>

      <div class="time-table">
        <span class="time" 
        v-for="(time, index) in times" :key="`time-${index}`"
        :class="{selected: isSelected(time)}"
        @click="selectTime(time)"
        >
        {{ time }}
        </span>
      </div>

      <div class="divider"></div>

      <div class="select-table">
        선택 시간 : 
        <span
        v-for="(time, index) in selectTimes" :key="`select-${index}`">
          {{ time }}
        </span>
      </div>

    </section>


  </div>
</template>

<script>
export default {
  name: "App",
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
    isSelected(time){
      // time이 selectTimes에 있는지 확인해서 있다면 true를 반환
      return this.selectTimes.includes(time)
    },
    selectTime(time){
      // indexOf() 메서드는 배열에서 지정된 요소를 찾아 해당 인덱스를 반환한다. 배열에서 지정된 요소를 찾지 못하면 -1을 반환한다.

      // 선택된 시간이 이미 예약된 시간 목록에 있는지 확인한다.
      const index = this.selectTimes.indexOf(time)
      // 선택된 시간이 없으면(새로 선택하는 경우)
      // if(index<0)이 왜 선택된 시간이 없으면. . 이냐면 앞서 index를 정의할때 indexOf메서드를 썼기 때문이다. indexOf()는 배열에 지정된 요소를 찾지 못하면 -1을 반환한다.
      if(index<0){
        // 예약 가능한 시간은 최대 5개까지이다.
        if(this.selectTimes.length === 5){
          alert('예약은 5개가 최대입니다.')
          // 여기서의 return은 뭘 반환하는 것이 아닌 함수 실행 중지를 의미한다.
          return
        }
        this.selectTimes.push(time)
        // 선택된 시간이 이미 예약된 시간 목록에 있는 경우
      }else{
        this.selectTimes.splice(index, 1)
      }
    }
  },
};
</script>

<style>
header {
  margin-top: 100px;
  text-align: center;
}
section {
  display: flex;
  flex-direction: column;
  align-items: center;
  box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px;
  width: 600px;
  margin: 0 auto;
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
.time-table {
  width: 560px;
  display: flex;
  flex-wrap: wrap;
}

.divider {
  border-bottom: 1px solid #0F4C81;
  width: 80%;
}
</style>
