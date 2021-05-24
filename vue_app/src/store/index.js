import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        blockPhase: false,
        substances: [],
        showNextPhase: false,
        showOnPHScale: [false, false, false, false]
    },
    mutations: {
        setShowOnPHScale(state, element){
          state.showOnPHScale[element] = true;
        },
        setBlockPhase(state, newValue) {
            state.blockPhase = newValue;
        },
        setSubstances(state, gamePhase) {
            var stringified = JSON.stringify(require("../resources/phases.json"));
            let phases = JSON.parse(stringified);
            stringified = JSON.stringify(require("../resources/substances.json"));
            let substances = JSON.parse(stringified);
            phases.phases.forEach((phase) => {
                if (phase.name === gamePhase) {
                    state.substances = [];
                    phase.substances.forEach((substance) => {
                        let substance_element = {};
                        substance_element.item = substances.ingredients[substance - 1].name;
                        substance_element.id = substances.ingredients[substance - 1].id;
                        substance_element.selected = false;
                        substance_element.src = require("../assets/items/" +
                            substances.ingredients[substance - 1].asset);
                        substance_element.size = substances.ingredients[substance - 1].size;
                        substance_element.prsize =
                            substances.ingredients[substance - 1].prsize;
                        substance_element.ph = substances.ingredients[substance - 1].ph;
                        substance_element.scale_placement =
                            substances.ingredients[substance - 1].scale_placement;

                        state.substances.push(substance_element);
                    });
                }
            });
        },
        removeSubstance(state, substance){
          state.substances.remove(substance);
        },
        setShowNextPhase(state, show){
            state.showNextPhase = show;
        }
    },
    actions:{
        setBlockPhase(context, newValue){
            context.commit('setBlockPhase', newValue);
        },
        setSubstances(context, phase){
            context.commit('setSubstances', phase);
        },
        setShowNextPhase(context, show){
            context.commit('setShowNextPhase', show);
        },
        removeSubstance(context, substance){
            context.commit('removeSubstance', substance);
        },
        setShowOnPHScale(context, element){
            context.commit('setShowOnPHScale', element);
        }
    }
})