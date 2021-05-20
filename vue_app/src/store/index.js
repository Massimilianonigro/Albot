import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        blockPhase: false
    },
    mutations: {
        setBlockPhase(state, newValue) {
            state.blockPhase = newValue;
        }
    },
    actions:{
        setBlockPhase(context, newValue){
            context.commit('setBlockPhase', newValue)
            console.log("ok")
        }
    }
})