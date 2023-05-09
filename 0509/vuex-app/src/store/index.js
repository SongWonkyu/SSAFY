import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message: 'message in state'
  },
  getters: {
    messageLength(state){
      return state.message.length
    },
    doubleLength(state, getters){
      return getters.messageLength * 2
    }
  },
  mutations: {
    CHANGE_MESSAGE(state, message){
      //console.log(state)
      //console.log(message)
      state.message = message
    }
  },
  actions: {
    // action의 두 번째 인자는 payload라고 하는데, 데이터를 실어나른다
    changeMessage(context, message){
      context.commit('CHANGE_MESSAGE', message)
    }
  },
  modules: {
  }
})
