<template>
  <div>
    <div class="background">
      <div 
        v-if="pouredPh !== -1" 
        class="solution-ph-meter" 
        :class="{
          acid: pouredPh < 7,
          basic: pouredPh >= 7,
        }">
        <h2 class="solution-ph-meter-label"> {{pouredPh}}</h2>
      </div>
      <div class="scoreboard">
        <h3 class="scoreboard-label"> {{score}} Points</h3>
      </div>

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
            v-on:click="selectItem(data, index)"
            v-bind:class="{
              highlight: index === pouredIndex,
              notHighlight: index !== pouredIndex,
            }"
            v-bind:style="{
              backgroundImage: 'url(' + data.src + ')',
              left: getXbyIndex(index),
              bottom:  getYbyIndex(index),
              height: data.prsize.h,
              width: data.prsize.w,
            }"
          ></button>
        </div>
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
import {mapState} from "vuex";
export default {
  components: {
  },
  name: "PracticePhase",
  data() {
    return {
      settings: false,
      score: 0,
      pouredPh: -1,
      pouredIndex: -1,      
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
        {x: "00%", y: "0%"},
        {x: "90%", y: "0%"},
        {x: "08%", y: "42%"},
        {x: "82%", y: "45%"},
      ]
    };
  },
  computed: {
    ...mapState(["substances"])
  },
  methods: {
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
        return "40%"
      }
      return this.settingsArray[index].x
    },
    getYbyIndex(index) {
      if ( this.pouredIndex === index ){
        return "10%"
      }
      return this.settingsArray[index].y
    },
    selectItem(data, index){
      this.showReset = true;
      if (this.pouredIndex !== index){
        this.pouredPh = data.ph;
        this.pouredIndex = index;
        console.log("Emitting from Phase");
        this.$emit("selectedPractItem",data.id);
      }
      else{
        this.pouredPh = -1;
        this.pouredIndex = -1;
      }
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
    backButton(){
      while(this.substances.length > 0) {
        this.substances.pop();
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

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.scoreboard{
  position: absolute;
	z-index: 2;
  left: 30%;
  top: 0;
  width: 30%;
  height: 14%;
  margin: auto;
	background-position-y: center;
	background-position-x: center;
	background-repeat: no-repeat;
	background-size: contain;
	background-image: url("../assets/uibuttons/Scoreboard.png");
}
.scoreboard-label{
  position: absolute;
  color: #ffffff;
	z-index: 3;
  margin: auto auto auto auto;
  left: 16%;
  right: 0;
  top: 28%;
  width: 80%;
  height: 40%;
  font-weight: 100;
}
.solution-ph-meter{
  position: absolute;
	z-index: 2;
  left: 30%;
  top: 20%;
  width: 40%;
  height: 20%;
  margin: auto;
	background-position-y: center;
	background-position-x: center;
	background-repeat: no-repeat;
  background-size: contain;
}
.acid{
	background-image: url("../assets/uibuttons/PHMeterAcid.png");

}
.basic{
	background-image: url("../assets/uibuttons/PHMeterBasic.png");
}
.solution-ph-meter-label{
  color: gray;
	z-index: 3;
  margin: 14.5% auto auto auto;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 15%;
  height: 50%;
  font-size: 4vh;
  font-weight: 100;
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
