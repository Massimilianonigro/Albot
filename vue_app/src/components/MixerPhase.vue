<template>
  <div>
    <div class="background">
      <div class="item-container">
        <div v-for="(data, index) in substances" v-bind:key="index">
          <button
            class="kitchen-item"
            v-on:click="selectItem(index, data.ph, data.id)"
            v-bind:class="getHighlight(index)"
            v-bind:style="getItemStyle(data, index)"
          ></button>
          <div
            class="solution-bowl"
            v-if="!poured[index]"
            v-bind:style="{
              left: index * 22 - 3 + '%',
              bottom: '-20%',
              height: '35%',
              width: '15%',
            }"
          ></div>
          <div
            v-if="poured[index]"
            :style="getPhBowl(data, index)"
            class="solution-style"
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
      poured: [false, false, false],
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
        this.setShowOnPHScale(3);
        this.setShowOnPHScale(index);
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
    getHighlight(index) {
      if (this.selected === index) return "highlight";
      return "nothighlight";
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
    getPhBowl(data, index) {
      console.log(data);
      let urlImg = require("../assets/solutions/Solution" +
        Math.round(data.ph) +
        ".png");
      let styleItem = {
        left: index * 22 - 3 + "%",
        bottom: "-20%",
        height: "35%",
        width: "15%",
        "background-image": "url(" + urlImg + ")",
      };
      return styleItem;
    },
    pourItem(index) {
      this.poured[index] = true;
    },
    practiceButton() {
      this.$emit("practicePress");
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

.nothighlight {
  top: 0%;
  height: 80%;
}
.kitchen-item:hover.nothighlight {
  opacity: 0.8;
  border-radius: 0;
  border: 0;
  border-style: none;
  border-color: transparent;
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
  border: 0;
  border-style: none;
  border-color: transparent;
}

.solution-bowl {
  position: absolute;
  z-index: 2;
  background-position-y: bottom;
  background-position-x: center;
  background-repeat: no-repeat;
  background-size: contain;
  background-image: url("../assets/solutions/Solutionbowl.png");
}
.solution-style {
  position: absolute;
  z-index: 2;
  background-position-y: bottom;
  background-position-x: center;
  background-repeat: no-repeat;
  background-size: contain;
}
.solution-ph-meter {
  position: absolute;
  z-index: 2;
  left: 0%;
  right: 0%;
  bottom: 2%;
  width: 50%;
  height: 12%;
  margin: auto;
  background-position-y: bottom;
  background-position-x: center;
  background-repeat: no-repeat;
  background-size: contain;
  background-image: url("../assets/uibuttons/PHIndicator.png");
}
.solution-ph-meter-label {
  color: white;
  z-index: 3;
  margin: 11.5% auto auto auto;
  left: 0%;
  right: 0%;
  bottom: 0%;
  width: 15%;
  height: 50%;
  font-weight: 100;
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
.practice-btn {
  position: absolute;
  height: 12%;
  width: 50%;
  top: 40%;
  left: 25%;
  background-repeat: no-repeat;
  background-size: contain;
  background-color: transparent;
  background-position: center;
  border: 0;
  z-index: 1000;
  background-image: url("../assets/uibuttons/PracticeButton.png");
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
  background-image: url("../assets/uibuttons/Tutorial.png");
}
.bubble-tutorial-btn {
  line-height: 5em;
  position: static;
  top: 70%;
  width: 20%;
  height: 100%;
  z-index: 2000 !important;
  color: transparent;
  background-image: url("../assets/uibuttons/Tutorial.png");
  background-repeat: no-repeat;
  background-size: contain;
  background-position-x: center;
  background-position-y: center;
  background-color: transparent;
  border: none;
  margin: 1vw;
}
.practice-btn:focus {
  outline: none;
}
.practice-btn:active {
  opacity: 0.7;
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
