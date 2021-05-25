<template>
  <div>
    <div class="background">
      <div class="albot"></div>

      <div
          v-if="showCompliment"
          v-on:click="continueButton"
          class="congrats" >
      </div>

      <div
          v-if="showTryAgain"
          class="wrong">
        <button
            v-on:click="tryAgainButton"
            class="try-again-btn">
        </button>
        <button
            v-on:click="moreInfoButton"
            class="info-btn">
        </button>
        <button
            v-on:click="continueFailButton"
            class="continue-btn">
        </button>
      </div>

      <div class="item-container">
        <div v-for="(data, index) in substances" v-bind:key="index">
          <button
              class="kitchen-item"
              v-bind:class="{highlight: index === pouredIndex, nothighlight: index !== pouredIndex}"
              v-on:click="selectItem(data, index)"
              v-bind:style= "getItemStyle(data, index)"
          ></button>
        </div>
        <div v-for="(data, index) in substances" v-bind:key="index"
             v-bind:class="{'highlight-guessed': guessed[index]}"
             v-bind:style= "getCheckStyle(data, index)">
        </div>
        <div
            :style="getPhBowl()"
            class="solution-style"
        >
        </div>

      </div>
      <button class="back-btn ui-btn"
              v-on:click="backButton()">
      </button>

      <button class="home-btn ui-btn"
              v-on:click="homeButton()">
      </button>

      <button class="reset-btn" v-if="showReset"
              v-on:click="resetButton()">
      </button>
    </div>
  </div>
</template>

<script>
import {mapState, mapActions} from "vuex";

export default {
  components: {
  },
  name: "IdentificationPhase",
  data() {
    return {
      score: 0,
      pouredPh: -1,
      pouredIndex: -1,
      pouring: -1,
      showCompliment: false,
      showTryAgain: false,
      showInfo: false,
      showReset: false,
      settingsArray: [
        {x: "30%", y: "0%"},
        {x: "60%", y: "0%"},
        {x: "38%", y: "42%"},
        {x: "50%", y: "42%"},
        {x: "15%", y: "0%"},
        {x: "74%", y: "0%"},
        {x: "22%", y: "42%"},
        {x: "65%", y: "43%"},
        {x: "0%", y: "0%"},
        {x: "90%", y: "0%"},
        {x: "08%", y: "42%"},
        {x: "82%", y: "45%"},
      ]
    };
  },
  computed: {
    ...mapState(["substances", "blockPhase", "guessed"])
  },
  methods: {
    ...mapActions(["setBlockPhase"]),
    getXbyIndex(index) {
      if ( this.pouredIndex === index ){
        return "40%";
      }
      return this.settingsArray[index].x;
    },
    getYbyIndex(index) {
      if ( this.pouredIndex === index ){
        return "10%";
      }
      return this.settingsArray[index].y;
    },
    getItemStyle(data, index) {
      return {
        backgroundImage: "url(" + data.src + ")",
        left: this.getXbyIndex(index),
        bottom: this.getYbyIndex(index),
        height: data.prsize.h,
        width: data.prsize.w
      };
    },
    getCheckStyle(data, index){
      return{
        left: this.getXbyIndex(index),
        bottom: this.getYbyIndex(index),
        height: data.prsize.h,
        width: data.prsize.w
      }
    },
    selectItem(data, index){
      //if blockPhase is false, we are selecting a new element to be guessed
      if (!this.blockPhase){
        this.$emit("selectedElement",data.id);
        this.setBlockPhase(true); //TODO: testing flag
        this.showReset = true;
      }
      //in any case, whenever an element is clicked, we pour it and change the bowl
      this.pouredPh = data.ph;
      this.pouredIndex = index;
    },
    addPoints(){
      this.showCompliment = true;
      this.score += 10;
      setTimeout(() => this.showCompliment = false, 2800);
    },
    getPhBowl(){
      let urlImg;
      if (this.pouredPh  === -1){
        urlImg = require("../assets/solutions/Solutionbowl.png");
      }
      else{
        urlImg = require("../assets/solutions/Solution"+ Math.round(this.pouredPh) +".png");
      }
      let styleItem = {
        'background-image': 'url('+ urlImg +')',
      }
      return styleItem;
    },
    showTryAgainWindow(){
      this.showTryAgain = true;
      this.showInfo = true;
    },
    backButton(){
      while(this.items.length > 0) {
        this.items.pop();
      }
      this.$emit("backPress");
    },
    continueButton(){
      this.showCompliment = false;
      this.$emit("continuePress");
    },
    continueFailButton(){
      this.showTryAgain = false;
      this.$emit("continuePress");
    },
    tryAgainButton(){
      this.showTryAgain = false;
      this.$emit("tryAgainPress");
    },
    moreInfoButton(){
      if(this.showInfo)
        this.$emit("infoPress");
      this.showInfo = false;
    },
    settingButton(){
      this.settings = !this.settings;
    },
    homeButton() {
      this.$emit("homePress");
    },
    resetButton(){
      this.showReset = false;
      this.pouredPh = -1;
      this.pouredIndex = -1;
      this.$emit("resetPress");
    }
  },
};

</script>

<style scoped>

.albot {
  position: absolute;
  top: 10%;
  right: 25%;
  height: 40%;
  width: 40%;
  background-repeat: no-repeat;
  background-size: contain;
  background-position-x: center;
  background-position-y: center;
  background-image: url("../assets/backgrounds/Bot.png");
}
.solution {
  position: absolute;
  bottom: 0;
  height: 40%;
  width: 14%;
  right: 43%;
  z-index: 2;
  background-position-y: bottom;
  background-position-x: center;
  background-repeat: no-repeat;
  background-size: contain;
  background-image: url("../assets/solutions/Solutionbowl.png");
}

.solution-style{
  pointer-events: none;
  position: absolute;
  bottom: 0;
  height: 40%;
  width: 14%;
  right: 43%;
  z-index: 2;
  background-position-y: bottom;
  background-position-x: center;
  background-repeat: no-repeat;
  background-size: contain;
}

.item-container {
  margin: auto;
  position: absolute;
  z-index: 50;
  bottom: 22%;
  left: 0;
  right: 0;
  width: 88%;
  height: 30%;
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
.reset-btn{
  position: absolute;
  height: 14%;
  width: 30%;
  bottom: 9%;
  left: 35%;
  background-repeat: no-repeat;
  background-size: contain;
  background-color: transparent;
  background-position: center;
  border: 0px;
  border-radius: 40px;
  z-index: 1000;
  background-image: url("../assets/uibuttons/ResetButton.png");
}

.reset-btn:active{
  opacity: 0.7;
}

.reset-btn:focus{
  outline: none;
}

.highlight {
  border-radius: 5px;
  border: none;
  background-color: transparent;
  transform: rotate(115deg);
  z-index: 100;
}

.highlight-guessed {
  position: absolute;
  opacity: 0.8;
  border-radius: 5px;
  border: none;
  background-image: url("../assets/icons/check.png");
  background-size: contain;
  background-repeat: no-repeat;
  background-position-x: 70%;
  background-position-y: 10%;
}

.spotlight-selected {
  border-radius: 5px;
  border: none;
  background-color: transparent;
  transform: rotate(115deg);
  z-index: 100;
}

.ui-btn{
  position: absolute;
  height: 8%;
  width: 19%;
  background-repeat: no-repeat;
  background-size: contain;
  background-color: transparent;
  background-position: center;
  border: none;
  z-index: 1000;
}

.home-btn {
  top: 3%;
  left: 3%;
}

.back-btn {
  top: 10%;
  left: 3%;
}

.congrats{
  position: absolute;
  z-index: 2;
  left: 20%;
  top: 24%;
  width: 57%;
  height: 30%;
  margin: auto;
  color: white;
  background-position-y: center;
  background-position-x: center;
  background-repeat: no-repeat;
  background-size: contain;
  background-image: url("../assets/uibuttons/WellDone.png");
}

.wrong{
  overflow: visible;
  position: absolute;
  z-index: 2;
  left: 20%;
  top: 12%;
  width: 57%;
  height: 30%;
  margin: auto;
  color: white;
  background-position-y: center;
  background-position-x: center;
  background-repeat: no-repeat;
  background-size: contain;
  background-image: url("../assets/uibuttons/Wrong.png");
}

.try-again-btn{
  position: absolute;
  z-index: 4;
  left: -10%;
  top: 70%;
  width: 57%;
  height: 30%;
  margin: auto;
  border: none;
  background-color: transparent;
  background-position-y: center;
  background-position-x: center;
  background-repeat: no-repeat;
  background-size: contain;
  background-image: url("../assets/uibuttons/TryAgain.png");
  outline: none;
}

.info-btn{
  position: absolute;
  z-index: 4;
  right: -10%;
  top: 70%;
  width: 57%;
  height: 30%;
  margin: auto;
  border: none;
  background-color: transparent;
  background-position-y: center;
  background-position-x: center;
  background-repeat: no-repeat;
  background-size: contain;
  background-image: url("../assets/uibuttons/Info.png");
  outline: none;
}

.continue-btn{
  position: absolute;
  z-index: 4;
  left: 20%;
  top: 95%;
  width: 57%;
  height: 30%;
  margin: auto;
  border: none;
  background-color: transparent;
  background-position-y: center;
  background-position-x: center;
  background-repeat: no-repeat;
  background-size: contain;
  background-image: url("../assets/uibuttons/ContinueFail.png");
  outline: none;
}

.continue-btn:active,
.info-btn:active,
.try-again-btn:active{
  opacity: 0.7;
}

.continue-btn:focus,
.info-btn:focus,
.try-again-btn:focus{
  outline: none;
}
</style>