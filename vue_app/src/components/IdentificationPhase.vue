<template>
  <div>
    <div class="background" v-bind:style="getBackgroundPosition()">
      <div class="albot"></div>
      <div class="element-selected" v-if="pouredSrc !== '' && showPoured"
           v-bind:style="{ backgroundImage: 'url(' + this.pouredSrc + ')'}"
           key="pouredSrc"></div>

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
               v-bind:style="getPouringStyle()"
               width="188" height="170" viewBox="0 0 188 170" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path opacity="0.3" d="M56.1398 69.58C55.7959 69.1601 55.4882 68.7118 55.2199 68.24C53.4499 65.42 51.7 64.98 50.6 65.7C46.03 68.7 41.5999 67.3 45.4699 72.57C70.6499 106.84 111.94 128.88 134.52 124.26C138.86 123.37 141.52 122.52 143.63 119.86C144.91 118.26 149.57 117.44 146.79 115.67C146.71 115.67 138.34 116.03 136.28 115.94C106.52 114.75 74.2598 89.09 56.1398 69.58Z" fill="#A4BEC4"/>
            <path opacity="0.3" d="M43.4601 83.39C43.1386 82.982 42.8697 82.5351 42.66 82.06C42.3234 81.394 41.8144 80.8306 41.1859 80.4285C40.5574 80.0263 39.8327 79.8002 39.087 79.7736C38.3414 79.7471 37.6021 79.9211 36.9466 80.2775C36.2911 80.6339 35.7433 81.1597 35.3602 81.7999C28.1602 92.7999 22.1302 96.95 25.8102 101.96C49.6902 134.45 95.6801 154.96 139.95 122.46C147.35 117.01 166.77 95.26 172.56 88.88C173.16 88.129 173.47 87.1872 173.432 86.2267C173.394 85.2662 173.012 84.3514 172.356 83.6496C171.699 82.9479 170.811 82.5061 169.855 82.4052C168.899 82.3042 167.939 82.5508 167.15 83.0999L166.84 83.32C122.58 115.85 76.3501 122.36 43.4601 83.39Z" fill="#A4BEC4"/>
            <path d="M175.18 6.00023C163 -10.6798 116 10.0002 78 37.9302C40 65.8602 6.21996 104.5 18.45 121.13C40.04 150.51 84.08 156.13 123.45 137.05L159 110.92C189 79.0502 196.77 35.3302 175.18 6.00023ZM137.69 119.2C98.03 148.35 47.4299 147.11 24.8899 116.44C19.0099 108.44 38.17 77.1802 82.73 44.4402C127.29 11.7002 162.86 2.75023 168.73 10.7502C191.27 41.3502 177.34 90.0003 137.69 119.15V119.2Z" fill="#A4BEC4"/>
            <path d="M169.09 46.8402C169.09 46.7802 169.09 46.7301 169.09 46.6701H169.03C163.73 35.5901 127.17 42.0502 87.36 61.0902C47.55 80.1302 19.5898 104.55 24.8898 115.62H24.82L24.9699 115.73C26.1599 118.07 28.78 119.62 32.58 120.4C54.24 131.57 85.24 131.31 114.31 117.4C143.38 103.49 163.05 79.5202 167.94 55.6402C169.73 52.2602 170.17 49.2502 169.09 46.8402Z" fill="currentColor"/>
            <g opacity="0.4">
              <path opacity="0.4" d="M154.11 61.1997C153.873 61.3127 153.61 61.3613 153.347 61.3405C153.085 61.3198 152.833 61.2305 152.616 61.0816C152.399 60.9327 152.226 60.7294 152.112 60.4922C151.999 60.2549 151.95 59.9919 151.97 59.7297C152.137 58.604 151.968 57.4541 151.484 56.4241C151 55.3941 150.223 54.5299 149.25 53.9397C141.15 48.7597 117.57 54.0297 96.6699 65.6897C96.3258 65.8683 95.9262 65.9076 95.5539 65.7997C95.1816 65.6917 94.8651 65.4446 94.6699 65.1097C94.4862 64.7666 94.4443 64.3653 94.5527 63.9916C94.6611 63.6179 94.9112 63.3013 95.2499 63.1097C117.74 50.5597 141.67 45.5497 150.91 51.4597C152.338 52.3417 153.483 53.6155 154.208 55.1295C154.933 56.6435 155.208 58.334 155 59.9997C154.968 60.2598 154.87 60.5071 154.714 60.7175C154.558 60.9279 154.35 61.0941 154.11 61.1997Z" fill="white"/>
            </g>
            <g opacity="0.4">
              <path opacity="0.4" d="M146.36 64.9098C146.171 64.9937 145.967 65.0412 145.76 65.0498C145.564 65.0565 145.368 65.0242 145.184 64.9548C145 64.8854 144.831 64.7803 144.688 64.6455C144.545 64.5107 144.43 64.3489 144.35 64.1694C144.269 63.99 144.225 63.7963 144.22 63.5998C144.249 62.7634 144.049 61.9351 143.639 61.2051C143.23 60.475 142.629 59.8713 141.9 59.4598C136.3 56.1598 121.09 59.5598 105.77 67.5298C105.417 67.7142 105.006 67.7508 104.626 67.6317C104.246 67.5126 103.93 67.2476 103.745 66.8948C103.561 66.5421 103.524 66.1305 103.643 65.7508C103.762 65.371 104.027 65.0541 104.38 64.8698C118.29 57.6298 135.75 52.3698 143.38 56.8698C144.546 57.5394 145.513 58.5074 146.181 59.6744C146.848 60.8414 147.193 62.1653 147.18 63.5098C147.188 63.7966 147.116 64.0799 146.971 64.3274C146.826 64.575 146.614 64.7768 146.36 64.9098Z" fill="white"/>
            </g>
            <path opacity="0.4" d="M32.5901 120.46C54.2501 131.63 85.2501 131.37 114.32 117.46C143.39 103.55 163.06 79.5802 167.95 55.7002C161.51 68.2102 137.64 86.3602 106.56 101.23C75.4801 116.1 46.3701 123.29 32.5901 120.46Z" fill="white"/>
            <path opacity="0.3" d="M67.4999 114.65C67.2782 114.416 67.1109 114.136 67.0099 113.83C66.1399 112.07 64.34 112.39 62.81 113.46C56.46 117.9 44.0899 121.32 47.2999 123.39C76.1399 142.04 107.14 145.39 132.86 129.39C138.57 125.83 138.57 125.83 142.05 122.64C144.13 120.73 146.2 120.53 143.78 120.09C143.71 120.09 139.94 121.41 139.88 121.44C105.73 134.85 80.1199 124.5 67.4999 114.65Z" fill="#B4CFD3"/>
            <path d="M115.78 89.35C77.7799 117.27 30.78 137.96 18.59 121.35C6.39999 104.74 40.1498 66.0701 78.1398 38.1501C116.13 10.2301 163.14 -10.4599 175.33 6.15006C187.52 22.7601 153.77 61.43 115.78 89.35ZM82.8798 44.5801C38.3198 77.3301 19.1599 108.58 25.0399 116.58C30.9199 124.58 66.4799 115.64 111.04 82.8901C155.6 50.1401 174.76 18.8901 168.88 10.8901C163 2.89005 127.44 11.8301 82.8798 44.5801Z" fill="#B4CFD3"/>
            <path d="M32.4099 132.61C32.6016 131.81 32.8765 131.033 33.23 130.29C33.6233 129.494 34.0641 128.723 34.55 127.98C42.92 115.16 65.55 108.12 65.55 108.12L33.25 99.6201C33.25 99.6201 27.2499 117.36 16.1799 124.99C15.2312 125.66 14.2277 126.249 13.1799 126.75C11.9813 127.364 10.9358 128.239 10.1201 129.31C4.12012 136.72 1.55997 155.79 0.469971 169.86C17.22 168.77 31.53 166.4 42.47 163.38C36.6 154 30.3199 141.19 32.4099 132.61Z" fill="currentColor"/>
          </svg>

        <div
            class="solution-bowl"
            v-if="!isPouring"
        ></div>
        <svg
            class="solution-liquid"
            v-if="!isPouring"
            v-bind:style="{
              color: getLiquidColor()
              }"
            width="161" height="63" viewBox="0 0 161 63" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M160.71 22.5799C160.74 22.5299 160.77 22.4799 160.8 22.4299H160.73C160.73 10.1499 124.96 0.199951 80.84 0.199951C36.72 0.199951 0.950073 10.1499 0.950073 22.4299H0.880005C0.910005 22.4799 0.939971 22.5299 0.969971 22.5799C1.02997 25.2099 2.73007 27.7399 5.82007 30.0799C20.5401 49.5099 48.62 62.6499 80.85 62.6499C113.08 62.6499 141.16 49.5099 155.88 30.0799C158.94 27.7399 160.64 25.2199 160.71 22.5799Z" fill="currentColor"/>

          ></svg>
        <div
            class="solution-overlay"
            v-if="!isPouring"
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
      isFirstPour: true,

      pouredSrc: "",
      showPoured: false,

      pouring: -1,
      pourColor: "#70319D",


      showCompliment: false,
      showTryAgain: false,
      showInfo: false,
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
    ...mapState(["substances", "blockPhase", "guessed", "showNextPhase", "isChatless", "guessingIndex"])
  },
  methods: {
    ...mapActions(["setBlockPhase", "setGuessingIndex"]),
    getLiquidColor(){
      if(this.guessingIndex !== -1){
        console.log("Setting custom liquid color");
        let stringified = JSON.stringify(require("../resources/colors.json"));
        let colors = JSON.parse(stringified);
        return (colors.colors[Math.round(this.pouredPh)].color);
      }
      if (this.guessingIndex === -1){
        return "#70319D";
      }
    },
    getBackgroundPosition(){
      if (!this.isChatless){
        return { margin: "auto auto auto 20%"};
      }
      return { margin: "auto auto auto 25%"};
    },
    getPouringStyle(){
      if (this.isChatless){
        return {
          color: this.pourColor,
          left: "150% !important"
        };
      }
      return {
        color: this.pourColor,
        left: "-15% !important"
      };
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

      //if we are not pouring for the first time, it means we have to throw away the content of the bowl
      if (!this.isFirstPour){

        this.throwLiquid();

        //pour and change color of bowl
        setTimeout(() => {
          this.pouredPh = 7;
        }, 1000);

        setTimeout(() => {
          this.pouredPh = data.ph;
          this.pouredIndex = index;
        }, 1500);

        setTimeout(() => {
          this.pouredIndex = -1;
        }, 3000);
      }
        //if we are selecting a new element to be guessed
        if ((this.guessingIndex === -1 || this.guessingIndex === -2 )&& !this.guessed[index]){
          this.setGuessingIndex(index);

          //show the element on screen
          this.pouredSrc = data.src;
          this.showPoured = true;

          //pour and change color of solution
          if (this.isFirstPour){
            this.pouredPh = data.ph;
            this.pouredIndex = index;

            setTimeout(() => {
              this.pouredIndex = -1;
            }, 500);
          }

          this.$emit("selectedElement",data.id);
          this.isFirstPour = false;
        }
    },
    throwLiquid(){
      this.isPouring = true;
      setTimeout(() => {this.isPouring = false; }, 1000);
      this.pourColor = this.getLiquidColor(this.pouredPh);
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
  z-index: 2;
  background-position-y: bottom;
  background-position-x: center;
  background-repeat: no-repeat;
  background-size: contain;
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

.element-selected {
  position: absolute;
  top: 10%;
  right: 15%;
  height: 30%;
  width: 15%;
  display: block;
  background-color: transparent;
  background-position-y: center;
  background-position-x: center;
  background-repeat: no-repeat;
  background-size: contain;
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