import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        blockPhase: true,
        isChatless: false,
        substances: [],
        showNextPhase: false,
        showOnPHScale: [false, false, false, false],
        thumbRotation: true,
        isThumbVisible: false,
        isScaleClickable: false,
        showFinalScreen: false,
        guessed: [false, false, false, false, false, false, false, false, false, false, false],
        guessingIndex: -1,
        isFirstPour: true,
        showPHScale: [false, false],
        canSelectSubstances: false,
        gamePhase: {
            phase: "introduction",
            isSelection: false,
            isMixer: false,
            isTutorial: false,
        },
    },
    mutations: {
        setCanSelectSubstances(state, value) {
            state.canSelectSubstances = value;
        },

        setShowFinalScreen(state, show) {
            state.showFinalScreen = show;
        },
        setThumbRotation(state, outcome) {
            state.thumbRotation = outcome;
        },
        setIsThumbVisible(state, visibility) {
            state.isThumbVisible = visibility;
        },
        setIsScaleClickable(state, clickable) {
            state.isScaleClickable = clickable;
        },
        setShowOnPHScale(state, element) {
            state.showOnPHScale[element] = true;
        },
        setShowPHScale(state, scale) {
            state.showPHScale[scale] = true;
        },
        setBlockPhase(state, newValue) {
            state.blockPhase = newValue;
        },
        setGuessingIndex(state, reset) {
            state.guessingIndex = reset;
        },
        setGamePhase(state, phase) {
            state.gamePhase.phase = phase;
            const stringified = JSON.stringify(require("../resources/phases.json"));
            let phases = JSON.parse(stringified);
            phases.phases.forEach((p) => {
                if (p.name === phase) {
                    state.gamePhase.isSelection = p.isSelection;
                    state.gamePhase.isMixer = p.isMixer;
                    state.gamePhase.isTutorial = p.isTutorial;
                }
            });
        },
        setGuessed(state, element) {
            console.log("guessed element " + element);
            state.guessed[parseInt(element) - 1] = true;
            console.log("it is now " + state.guessed[parseInt(element) - 1]);
        },
        setSubstances(state, gamePhase) {
            let stringified = JSON.stringify(require("../resources/phases.json"));
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
                        substance_element.circle_y_placement =
                            substances.ingredients[substance - 1].circle_y_placement;
                        state.substances.push(substance_element);
                    });
                }
            });
        },
        setShowNextPhase(state, show) {
            state.showNextPhase = show;
        }
    },
    actions: {
        setBlockPhase(context, newValue) {
            context.commit('setBlockPhase', newValue);
        },
        setSubstances(context, phase) {
            context.commit('setSubstances', phase);
        },
        setIsScaleClickable(context, clickable) {
            context.commit('setIsScaleClickable', clickable);
        },
        setShowNextPhase(context, show) {
            context.commit('setShowNextPhase', show);
        },
        setShowOnPHScale(context, element) {
            context.commit('setShowOnPHScale', element);
        },
        setGuessed(context, element) {
            context.commit('setGuessed', element);
        },
        setGamePhase(context, phase) {
            context.commit('setGamePhase', phase);
        },
        setShowPHScale(context, scale) {
            context.commit('setShowPHScale', scale);
        },
        setCanSelectSubstances(context, value) {
            context.commit('setCanSelectSubstances', value);
        },
        setThumbRotation(context, outcome) {
            context.commit('setThumbRotation', outcome);
        },
        setIsThumbVisible(context, visibility) {
            context.commit('setIsThumbVisible', visibility);
        },
        setGuessingIndex(context, reset) {
            context.commit('setGuessingIndex', reset);
        },
        setShowFinalScreen(context, show) {
            context.commit('setShowFinalScreen', show);
        }
    }
})
