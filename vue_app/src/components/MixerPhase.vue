<template>
  <div>
    <div class="background" >
      <div class="item-container">
        <div v-for="(data, index) in substances" v-bind:key="index">
          <button
            class="kitchen-item"
            v-on:click="selectItem(index, data.ph, data.id)"
            v-bind:class="getHighlight(index)"
            v-bind:style="getItemStyle(data, index)"
            v-bind:disabled="blockPhase"
          ></button>
          <div
            class="solution-bowl"
            v-bind:style="{
              left: index * 22 - 3 + '%',
              bottom: '-20%',
              height: '35%',
              width: '15%',
            }"
          ></div>
          <svg
              class="solution-liquid"
              v-bind:style="{
              left: index * 22 - 2 + '%',
              bottom: '-19%',
              height: '19%',
              width: '13%',
              color: getLiquidColor(index, data.ph),
              }"
              width="161" height="63" viewBox="0 0 161 63" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M160.71 22.5799C160.74 22.5299 160.77 22.4799 160.8 22.4299H160.73C160.73 10.1499 124.96 0.199951 80.84 0.199951C36.72 0.199951 0.950073 10.1499 0.950073 22.4299H0.880005C0.910005 22.4799 0.939971 22.5299 0.969971 22.5799C1.02997 25.2099 2.73007 27.7399 5.82007 30.0799C20.5401 49.5099 48.62 62.6499 80.85 62.6499C113.08 62.6499 141.16 49.5099 155.88 30.0799C158.94 27.7399 160.64 25.2199 160.71 22.5799Z" fill="currentColor"/>

          ></svg>
          <div
              class="solution-overlay"
              v-bind:style="{
              left: index * 22 - 3 + '%',
              bottom: '-20%',
              height: '35%',
              width: '15%',
            }"
          ></div>
        </div>
      </div>

      <div class="white-block" v-if="complete && showNextPhase">
      <!--div class="white-block" v-if="complete"//TODO: testing flag-->
        <div class="gj-banner">
          <h2>Good Job!</h2>
        </div>
        <button class="next-phase-btn" v-on:click="nextPhaseButton"></button>
      </div>

      <button class="back-btn ui-btn" v-on:click="backButton"></button>

      <button class="home-btn ui-btn" v-on:click="homeButton"></button>
    </div>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";

export default {
  created() {
    let phases = JSON.parse(
      JSON.stringify(require("../resources/phases.json"))
    );
    phases.phases.forEach((phase) => {
      if (phase === "tutorial-mix") {
        this.selectionOrder = phase.substances;
        this.nextSelected = this.selectionOrder[0];
      }
    });
  },
  components: {},
  name: "MixerPhase",
  props: {
    items: {
      type: Array,
      required: false,
    },
  },
  data() {
    return {
      selected: undefined,
      selectedPh: "Select",
      complete: false,
      poured: [false, false, false, false],
      selectionOrder: [],
      nextSelected: 0,
    };
  },
  computed: {
    ...mapState(["blockPhase", "substances", "showNextPhase"]),
  },
  methods: {
    ...mapActions(["setBlockPhase", "setShowOnPHScale"]),
    selectItem(index, ph, id) {
      if (index === this.nextSelected && !this.blockPhase) {
        this.$emit("selectItem", id);
        //this.setShowOnPHScale(index);
        if (this.selected === index) {
          this.selected = undefined;
          this.selectedPh = "Select";
        } else {
          this.selected = index;
          this.selectedPh = ph + "";
        }
        if (!this.poured[index]) this.poured[index] = true;

        this.complete = this.poured.every((v) => v === true);
        this.nextSelected += 1;
        this.$emit("selectionComplete");
        this.setBlockPhase(true); //TODO: testing flag
      }
    },
    getLiquidColor(index, pH){
      if (this.poured[index]){
        let stringified = JSON.stringify(require("../resources/colors.json"));
        let colors = JSON.parse(stringified);
        return (colors.colors[Math.round(pH)].color);
      }
      return "#70319D";
    },
    getHighlight(index) {
      if (this.selected === index) return "highlight";
      return "notHighlight";
    },
    getItemStyle(data, index) {
      let styleItem;
      if (this.selected === index) {
        styleItem = {
          backgroundImage: "url(" + data.src + ")",
          left: index * 22 - 6 + "%",
          width: data.size.w,
          zIndex: 20,
        };
      } else {
        styleItem = {
          backgroundImage: "url(" + data.src + ")",
          left: index * 22 + "%",
          width: data.size.w,
        };
      }
      return styleItem;
    },
    pourItem(index) {
      this.poured[index] = true;
    },
    nextPhaseButton() {
      this.$emit("nextPhasePress");
    },
    backButton() {
      while (this.items.length > 0) {
        this.items.pop();
      }
      this.$emit("backPress");
    },
    homeButton() {
      this.$emit("homePress");
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.item-container {
  margin: auto;
  position: absolute;
  z-index: 50;
  bottom: 28%;
  left: 0;
  right: 0;
  width: 82%;
  height: 25%;
}

.notHighlight {
  top: 0;
  height: 80%;
}
.kitchen-item:hover.notHighlight {
  opacity: 0.8;
  border: 0 none transparent;
  background-color: #ffffff70;
  border-radius: 5px;
}
.highlight {
  color: #ffffff;
  border-radius: 5px;
  border: none;
  background-color: transparent;
  transform: rotate(115deg);
  top: 34%;
  height: 80%;
}
.kitchen-item:hover.highlight {
  opacity: 0.8;
  border-radius: 0;
  border: 0 none transparent;
}

.solution-bowl {
  position: absolute;
  z-index: 2;
  background-position-y: bottom;
  background-position-x: center;
  background-repeat: no-repeat;
  background-size: contain;
  background-image: url("../assets/solutions/bowl.svg");
}
.solution-liquid {
  position: absolute;
  z-index: 3;
  background-position-y: bottom;
  background-position-x: center;
  background-repeat: no-repeat;
  background-size: contain;
}
.solution-overlay {
  position: absolute;
  z-index: 4;
  background-position-y: bottom;
  background-position-x: center;
  background-repeat: no-repeat;
  background-size: contain;
  background-image: url("../assets/solutions/overlay.svg");
}

ul {
  list-style-type: none;
  padding: 0;
  columns: 5;
  -webkit-columns: 5;
  -moz-columns: 5;
}
a {
  color: #42b983;
}
.next-phase-btn {
  position: absolute;
  height: 10%;
  width: 50%;
  top: 40%;
  left: 25%;
  background-repeat: no-repeat;
  background-size: contain;
  background-color: transparent;
  background-position: center;
  border: 0;
  z-index: 1000;
  background-image: url("../assets/uibuttons/NextPhaseButton.png");
}
.gj-banner {
  position: absolute;
  padding-top: 7%;
  height: 30%;
  width: 68%;
  top: 22%;
  left: 16%;
  background-repeat: no-repeat;
  background-size: contain;
  background-color: transparent;
  background-position: center;
  border: 0;
  z-index: 999;
  background-image: url("../assets/uibuttons/gj.png");
}
.gj-banner > h2 {
  color: white;
  text-align: center;
  font-size: xxx-large;
  padding: 1vw 1vw 4vw 1vw;
}
.white-block {
  position: absolute;
  background-color: #ffffffb0;
  z-index: 105;
  height: 100%;
  width: 100%;
}
</style>
