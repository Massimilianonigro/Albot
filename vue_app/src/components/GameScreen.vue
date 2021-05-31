<template>
  <div id="GameUI">
    <!--Tutorial Selection phase: !isMixer, isSelection, isTutorial-->
    <div class="GameUI" v-if="!gamePhase.isMixer && gamePhase.isSelection && gamePhase.isTutorial">
      <PickerBackground />
      <PickerPhase
        ref="picker"
        v-on:sendItemMessage="selectItem"
        v-on:sendNextInChat="displayNextButton"
        v-on:homePress="homeScreen"
        v-on:nextPress="mixItems"
        v-on:selectionComplete="selectionComplete"
      />
    </div>
    <!--Tutorial Mixer phase: isMixer, !isSelection, isTutorial-->
    <div class="GameUI" v-if="gamePhase.isMixer && !gamePhase.isSelection && gamePhase.isTutorial">
      <MixerBackground
        v-bind:isRerender="isRerender"
      >
      </MixerBackground>
      <MixerPhase
        v-on:homePress="homeScreen"
        v-on:backPress="prevScreen"
        v-on:practicePress="practicePress"
        v-on:selectItem="selectItem"
        v-on:selectionComplete="selectionComplete"
        v-on:nextPhasePress="pHIdentificationPhase"
        v-bind:items="selItems"
      />
    </div>
    <!--pH identifier phase: isMixer, isSelection, !isTutorial-->
    <div class="GameUI" v-if="gamePhase.isMixer && gamePhase.isSelection && !gamePhase.isTutorial">
      <IdentificationBackground v-on:PHGuess="sendPHGuess"/>
      <IdentificationPhase
          ref="game"
          v-on:selectedElement="sendItemMessage"
          v-on:resetPress="sendResetMessage"
          v-on:homePress="homeScreen"
          v-on:backPress="prevScreen"
          v-on:continuePress="continueClick"
          v-on:tryAgainPress="tryAgainClick"
          v-on:nextPhasePress="practicePress"
          v-on:infoPress="infoClick"
      />
    </div>
    <!--Practice Selection phase: !isMixer, isSelection, !isTutorial-->
    <div class="GameUI" v-if="!gamePhase.isMixer && gamePhase.isSelection && !gamePhase.isTutorial">
      <PickerBackground />
      <PickerPracticePhase
        ref="pracpicker"
        v-on:sendNextInPracticeChat="displayNextPracticeButton"
        v-on:sendItemMessage="selectItem"
        v-on:nextPress="nextScreen"
        v-on:homePress="homeScreen"
      />
    </div>
    <!--Practice Mixer phase: isMixer, !isSelection, !isTutorial-->
    <div
      class="GameUI"
      v-if="gamePhase.isMixer && !gamePhase.isSelection && !gamePhase.isTutorial">
      <PracticeBackground />
      <PracticePhase
        ref="game"
        v-on:selectedPractItem="sendItemMessage"
        v-on:resetPress="sendResetMessage"
        v-on:homePress="homeScreen"
        v-on:backPress="prevScreen"
        v-on:continuePress="continueClick"
        v-on:tryAgainPress="tryAgainClick"
        v-on:infoPress="infoClick"
      />
    </div>
  </div>
</template>

<script>
import PickerBackground from "./PickerBackground.vue";
import MixerBackground from "./MixerBackground.vue";
import PracticeBackground from "./PracticeBackground.vue";
import PickerPhase from "./PickerPhase.vue";
import MixerPhase from "./MixerPhase.vue";
import PickerPracticePhase from "./PickerPracticePhase.vue";
import PracticePhase from "./PracticePhase.vue";
import IdentificationPhase from "./IdentificationPhase.vue";
import {mapState, mapActions} from "vuex";
import IdentificationBackground from "./IdentificationBackground";

export default {
  name: "GameScreen",
  created() {
    this.setSubstances(this.gamePhase.phase);
  },
  components: {
    IdentificationBackground,
    PickerBackground,
    MixerBackground,
    PracticeBackground,
    PickerPhase,
    MixerPhase,
    PickerPracticePhase,
    PracticePhase,
    IdentificationPhase,
  },
  data() {
    return {
      selItems: [],
      nonSelItems: [],
      selItem: undefined,
      isRerender: 0,
    };
  },
  computed: {
    ...mapState(["blockPhase", "substances", "gamePhase"])
  },
  methods: {
    ...mapActions(["setSubstances", "setGamePhase"]),
    mixItems(selectedItems, nonSelectedItems) {
      this.selItems = [];
      this.nonSelItems = [];
      selectedItems.forEach((element) => {
        console.log(element);
        this.selItems.push(element);
      });
      nonSelectedItems.forEach((element) => {
        this.nonSelItems.push(element);
      });

      //only for testing purposes, to be removed
      this.setGamePhase("tutorial-mix");
    },
    practiceMix(selectedItems) {
      this.selItems = [];
      selectedItems.forEach((element) => {
        this.selItems.push(element);
      });
      this.setGamePhase("practice-mix");
    },
    pourItem(selectedItem) {
      console.log(selectedItem);
      this.selItem = selectedItem;
    },
    sendPHGuess(index) {
      this.$emit("PHGuess", index);
    },
    displayNextButton() {
      this.$emit("sendNextInChat");
    },
    displayNextPracticeButton() {
      this.$emit("sendPracNextInChat");
    },
    sendItemMessage(id) {
      this.$emit("sendItemMessage", id);
    },
    sendResetMessage() {
      this.$emit("sendResetMessage");
    },
    continueClick() {
      this.$emit("sendContinueMessage");
    },
    tryAgainClick() {
      this.$emit("sendTryAgainMessage");
    },
    infoClick() {
      this.$emit("sendInfoMessage");
    },
    //never used
    nextClicked() {
      if (this.gameStatus === 1) this.$refs.picker.updatePart();
    },
    practicePress() {
      this.$emit("practicePress");
    },
    selectItem(index) {
      this.$emit("selectItem", index);
      this.isRerender += 1;
    },
    addPoints() {
      this.$refs.game.addPoints();
    },
    displayTryAgain() {
      this.$refs.game.showTryAgainWindow();
    },
    nextScreen() {
      //TODO: add emit
      //this.selItems = [];
      this.nonSelItems = [];
      this.$emit("");
    },
    prevScreen() {
      let stringified = JSON.stringify(require("../resources/phases.json"));
      let phases = JSON.parse(stringified);
      phases.phases.forEach(phase => {
        if (phase.name === this.gamePhase.phase){
          this.setGamePhase(phase.prev_phase);
          this.setSubstances(phase.prev_phase);
        }
      })
      this.selItems = [];
      this.nonSelItems = [];
      this.$emit("goBack");
    },
    homeScreen() {
      this.$emit("goHome");
    },
    pHIdentificationPhase() {
      //only for testing purposes, to be removed
      this.setGamePhase("practice-pH");
      this.$emit("pHIdentificationPhase");
      this.setSubstances(this.gamePhase.phase);
    },
    selectionComplete() {
      this.$emit("selectionComplete");
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.GameUI {
  height: 100%;
  width: 80%;
  position: fixed;
  z-index: 1;
  top: 0;
  bottom: 0;
  overflow-x: hidden;
  left: 0;
}
</style>
