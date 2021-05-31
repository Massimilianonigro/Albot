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
              v-bind:class="{highlight: index === pouredIndex, notHighlight: index !== pouredIndex}"
              v-on:click="selectItem(data, index)"
              v-bind:style= "getItemStyle(data, index)"
          ></button>
        </div>
        <button v-for="(data, index) in substances" v-bind:key="index"
             v-bind:class="{'highlight-guessed': guessed[index], 'highlight-not-guessed': !guessed[index], highlight: index === pouredIndex, notHighlight: index !== pouredIndex}"
             v-bind:style= "getCheckStyle(data, index)"
                v-on:click="selectItem(data, index)">
        </button>
        <svg class="pouring-solution" v-if="isPouring"
             v-bind:style="{color: getLiquidColor()}"
        xmlns="http://www.w3.org/2000/svg"
             viewBox="0 0 187.02 169.86"><defs><style>.cls-1,.cls-2{fill:#a4bec4;}.cls-1,.cls-8{opacity:0.3;}.cls-3{fill:none;}.cls-4{fill:currentColor;}.cls-5,.cls-7{opacity:0.4;}.cls-6,.cls-7{fill:#fff;}.cls-8,.cls-9{fill:#b4cfd3;}</style>
        </defs><g id="图层_2" data-name="图层 2"><g id="图层_1-2" data-name="图层 1"><path class="cls-1" d="M55.69,69.58a8.4,8.4,0,0,1-.91-1.35C53,65.42,51.25,65,50.15,65.69c-4.57,3-9,1.6-5.13,6.88,25.18,34.27,66.48,56.31,89,51.69,4.34-.89,7-1.74,9.11-4.4,1.28-1.6,5.94-2.42,3.16-4.19-.08,0-8.45.35-10.51.27C106.07,114.75,73.81,89.09,55.69,69.58Z"/>
          <path class="cls-1" d="M43,83.39a5.83,5.83,0,0,1-.79-1.34,4.18,4.18,0,0,0-7.31-.26C27.71,92.82,21.68,97,25.36,102c23.88,32.49,69.87,53,114.14,20.49,7.4-5.44,26.82-27.19,32.62-33.58a4,4,0,0,0-5.42-5.77l-.3.22C122.13,115.85,75.9,122.36,43,83.39Z"/>
          <path class="cls-2" d="M174.73,6c-12.22-16.64-59.19,4.06-97.18,32S5.78,104.5,18,121.13c21.59,29.38,65.64,35,105,15.92l35.56-26.13C188.55,79,196.32,35.32,174.73,6Zm-37.49,113.2C97.58,148.3,47,147.06,24.45,116.39c-5.88-8,13.28-39.27,57.84-72s80.12-41.7,86-33.7C190.82,41.35,176.89,90,137.24,119.15Z"/>
          <path class="cls-3" d="M82.29,44.38c-44.56,32.74-63.72,64-57.84,72C47,147.06,97.58,148.3,137.24,119.15s53.58-77.8,31-108.47C162.41,2.68,126.85,11.63,82.29,44.38Z"/><path class="cls-4" d="M168.64,46.84c0-.06,0-.12,0-.18l-.06,0c-5.3-11.08-41.86-4.62-81.67,14.42s-67.77,43.46-62.47,54.53l-.07,0,.15.1c1.19,2.35,3.81,3.9,7.61,4.68,21.66,11.17,52.66,10.9,81.73-3S162.61,79.58,167.5,55.7C169.28,52.26,169.72,49.24,168.64,46.84Z"/>
          <g class="cls-5">
            <path class="cls-6" d="M153.66,61.2a1.5,1.5,0,0,1-2.14-1.47,5.78,5.78,0,0,0-2.72-5.79c-8.1-5.18-31.68.09-52.58,11.74a1.5,1.5,0,1,1-1.46-2.62c22.49-12.55,46.42-17.55,55.66-11.65A8.79,8.79,0,0,1,154.51,60,1.51,1.51,0,0,1,153.66,61.2Z"/></g>
          <g class="cls-5">
            <path class="cls-6" d="M145.91,64.9a1.48,1.48,0,0,1-.6.15,1.5,1.5,0,0,1-1.54-1.46,4.58,4.58,0,0,0-2.31-4.13c-5.61-3.3-20.81.1-36.14,8.06a1.5,1.5,0,1,1-1.38-2.66c13.9-7.23,31.36-12.5,39-8a7.58,7.58,0,0,1,3.79,6.64A1.49,1.49,0,0,1,145.91,64.9Z"/></g>
          <path class="cls-7" d="M32.14,120.46c21.66,11.17,52.66,10.9,81.73-3S162.61,79.58,167.5,55.7c-6.44,12.51-30.31,30.65-61.39,45.52S45.92,123.29,32.14,120.46Z"/>
          <path class="cls-8" d="M67.05,114.64a2.07,2.07,0,0,1-.49-.81c-.87-1.76-2.67-1.44-4.2-.37-6.35,4.44-18.72,7.86-15.51,9.93,28.84,18.65,59.84,22,85.56,6,5.71-3.56,5.71-3.56,9.19-6.75,2.08-1.92,4.15-2.11,1.73-2.55-.07,0-3.84,1.32-3.9,1.35C105.28,134.85,79.68,124.49,67.05,114.64Z"/>
          <path class="cls-9" d="M115.33,89.34c-38,27.92-85,48.62-97.18,32S39.7,66.05,77.69,38.13s85-48.62,97.19-32S153.32,61.42,115.33,89.34ZM82.43,44.58c-44.56,32.74-63.72,64-57.84,72s41.44-1,86-33.69,63.72-64,57.84-72S127,11.83,82.43,44.58Z"/>
          <path class="cls-4" d="M32,132.6a12,12,0,0,1,.82-2.32,22.09,22.09,0,0,1,1.33-2.3c8.36-12.82,31-19.86,31-19.86l-32.3-8.5s-6,17.73-17.07,25.37a22.63,22.63,0,0,1-3,1.76,9,9,0,0,0-3.06,2.55c-6,7.42-8.56,26.48-9.65,40.56,16.75-1.1,31.06-3.46,42-6.48C36.15,154,29.87,141.18,32,132.6Z"/></g></g>
        </svg>>
        <div
            class="solution-bowl"
        ></div>
        <svg
            class="solution-liquid"
            v-bind:style="{
              color: getLiquidColor()
              }"
            width="161" height="63" viewBox="0 0 161 63" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M160.71 22.5799C160.74 22.5299 160.77 22.4799 160.8 22.4299H160.73C160.73 10.1499 124.96 0.199951 80.84 0.199951C36.72 0.199951 0.950073 10.1499 0.950073 22.4299H0.880005C0.910005 22.4799 0.939971 22.5299 0.969971 22.5799C1.02997 25.2099 2.73007 27.7399 5.82007 30.0799C20.5401 49.5099 48.62 62.6499 80.85 62.6499C113.08 62.6499 141.16 49.5099 155.88 30.0799C158.94 27.7399 160.64 25.2199 160.71 22.5799Z" fill="currentColor"/>

          ></svg>
        <div
            class="solution-overlay"
        ></div>

      </div>
      <div class="white-block" v-if="complete">
        <div class="gj-banner">
          <h2>Good Job!</h2>
        </div>
        <button class="next-phase-btn" v-on:click="nextPhaseButton"></button>
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
      complete: true,
      isPouring: false,
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
    ...mapState(["substances", "blockPhase", "guessed", "showNextPhase"])
  },
  methods: {
    ...mapActions(["setBlockPhase"]),
    getLiquidColor(){
      if(this.pouredIndex !== -1){
        let stringified = JSON.stringify(require("../resources/colors.json"));
        let colors = JSON.parse(stringified);
        return (colors.colors[Math.round(this.pouredPh)].color);
      }
      return "#70319D";
    },
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
      this.complete = this.guessed.every((v) => v === true);
      return{
        left: this.getXbyIndex(index),
        bottom: this.getYbyIndex(index),
        height: data.prsize.h,
        width: data.prsize.w,
      }
    },
    selectItem(data, index){
      //if blockPhase is false, we are selecting a new element to be guessed
      if (!this.blockPhase && !this.guessed[index]){
        this.$emit("selectedElement",data.id);
        this.setBlockPhase(true); //TODO: testing flag
        this.showReset = true;
      }
      if (this.pouredIndex !== -1 ){
        this.isPouring = true;
        this.throwLiquid();
      }
      //in any case, whenever an element is clicked, we pour it and change the bowl
      this.pouredPh = data.ph;
      this.pouredIndex = index;
    },
    throwLiquid(){
      setTimeout(() => {  this.isPouring = false; }, 1000);
    },
    addPoints(){
      this.showCompliment = true;
      this.score += 10;
      setTimeout(() => this.showCompliment = false, 2800);
    },
    showTryAgainWindow(){
      this.showTryAgain = true;
      this.showInfo = true;
    },
    nextPhaseButton() {
      this.$emit("nextPhasePress");
    },
    backButton(){
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
.white-block {
  position: absolute;
  background-color: #ffffffb0;
  z-index: 105;
  height: 100%;
  width: 100%;
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
.pouring-solution{
  position: absolute;
  bottom: -21%;
  height: 40%;
  width: 14%;
  left: -15%;
  z-index: 2;
  background-position-y: bottom;
  background-position-x: center;
  background-repeat: no-repeat;
  background-size: contain;
  background-image: url("../assets/solutions/pouring.png");
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
  border: 0;
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

.highlight-not-guessed {
  position: absolute;
  border: none transparent;
  background-color: transparent;
}

.highlight-guessed {
  position: absolute;
  opacity: 0.8;
  border: none transparent;
  background-image: url("../assets/icons/check.png");
  background-size: contain;
  background-repeat: no-repeat;
  background-position-x: 70%;
  background-position-y: 10%;
  background-color: transparent;
}

.highlight-guessed:focus{
  outline: none;
}

.highlight-not-guessed:focus{
  outline: none;
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
  background-image: url("../assets/uibuttons/NextButton.png");
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