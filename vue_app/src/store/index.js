import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        blockPhase: false
    },
    mutations: {
        setBlockPhase(state, newValue){
            state.blockPhase = newValue;
        },
        // eslint-disable-next-line no-unused-vars
        prova(state, val){
            console.log("Sono in index.js,", val);
        }
    },
    actions:{
        setBlockPhase(context, newValue){
            context.commit('setBlockPhase', newValue)
            console.log("ok")
        }
    }
})