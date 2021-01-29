<template>
  <div class="main-bg">
    <div class="background">
      <div class="report icon"></div>
      <div class="settings icon"></div>
      <div class="magic-colors-sign icon"></div>
      <div class="bot-tittle icon"></div>
      
      <button
        class="start-btn"
        type="button"
        v-on:click="clickOnStart"
      >
      </button>
    </div>
    <div
      v-if="start" 
      class="bot-bg">
        <div class="bot-welcome"></div>
      <transition name="fade">
        <p class="bubble speech bubble-1"> Hi -name-, I'm Albot.</p>
      </transition>
      <transition name="fade">
        <p v-if="part2" class="bubble speech bubble-2"> 
          <button v-on:click="clickOnIntro" class="bubble-btn fade-in" :style="{'left': '8%'}"> Introduction </button>
          We  will  execute  this  experiment  together.  Please  choose a lesson to start:
          <button v-on:click="clickOnPractice" class="bubble-btn fade-in" :style="{'right': '8%'}"> Practice </button>
        </p>
      </transition>
      <transition name="fade">
        <p v-if="part3" class="bubble speech bubble-3 fade-in"> If whis topic is new for you, you can click on Introduction, or if you already know it, you can practice!</p>
      </transition>
      
    </div>
  </div>
</template>

<script>
export default {
  name: "MainScreen",
  data(){
    return {
      time: 1500,
      start: false,
      part2: false,
      part3: false,
    }
  },
  methods: {
    clickOnStart(){
      this.start = true;
      setTimeout(() => this.part2 = true, this.time);
      setTimeout(() => this.part3 = true, this.time*2);
    },
    clickOutOfStart(){
      this.start = false;
    },
    clickOnIntro() {
      this.$emit("startIntro");
    },
    clickOnPractice() {
      this.$emit("startPractice");
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
a {
  color: #42b983;
}
.start-btn {
	position: absolute;
  top: 48%;
  height: 12%;
  width: 24% ;
  left: 38%;
	background-repeat: no-repeat;
	background-size: contain;
  background-color: transparent;
  background-position: top;
  background-image: url("../assets/uibuttons/StartButton.png");
  border: 0px;

}
.main-bg {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
	width: 100%;
	height: 100%;
  background-color: #ffffff;
	background-size: contain;
	background-image: url('../assets/backgrounds/WhiteBG.png');
}
.background{
	position: absolute;
	top: 0; bottom: 0; left: 0; right: 0;
	margin: auto;
	z-index: 0;
	width: 100vw;
	height: 75vw;
	max-width: 133.3vh;
	max-height: 100vh;
  background-image: url("../assets/backgrounds/Welcome.png");
  background-position-x: center;
  background-position-y: bottom;
  background-size: contain;
  background-repeat: no-repeat;
}
.magic-colors-sign{
	top: 35%;
  left: 30%;
	height: 7%;
	width:  40%;
	z-index: 1;
  background-position-x: center;
	background-image: url("../assets/backgrounds/MagicColors.png");
}
.bot-tittle{
	top: 10%;
  right: 18%;
	height: 30%;
	width:  18%;
	z-index: 1;
  background-position-x: center;
	background-image: url("../assets/backgrounds/BotTittle.png");
}
.icon{
	position: absolute;
	background-repeat: no-repeat;
	background-size: contain;
}
.settings{
	top: 18%;
  left: 4%;
	height: 8%;
	width:  20%;
	z-index: 1;
	background-position-x: center;
	background-image: url("../assets/uibuttons/SettingButton.png");
}
.report{
	top: 9%;
  left: 4%;
	height: 8%;
	width:  20%;
	z-index: 1;
	background-position-x: center;
	background-image: url("../assets/uibuttons/ReportButton.png");
}
.bot-bg{
  position: absolute;
  background-color: #ffffffb0;
  z-index: 5;
  height: 100%;
  width:  100%;
}
.bot-welcome{
  position: absolute;
  top: 30%;
  right: 15%;
  height: 30%;
  width:  30%;
	background-repeat: no-repeat;
	background-size: contain;
	background-position-x: center;
	background-position-y: center;
	background-image: url("../assets/backgrounds/Bot.png");
}

.bubble {
	position: absolute;
  text-align: left;
  color: #fbb13d;
	line-height: 1.4em;
	font-family: sans-serif;
	font-size: large;
  right: 35%;
	width: 50%;
	margin: 40px auto;
	border: 4px solid #fbb13d;
	border-radius: 30px;
	padding: 20px 30px;
	background-color: #fff;
}

.bubble:before,
.bubble:after {
	content: '';
	position: absolute;
	width: 0;
	height: 0;
}
.speech:before {
	right: 24px;
	bottom: -40px;
	border: 20px solid;
	border-color: #fbb13d #fbb13d transparent transparent;
}
.speech:after {
	right: 28px;
	bottom: -30px;
	border: 16px solid;
	border-color: #ffffff #ffffff transparent transparent;
}

.bubble-1{
  top: 8%;
  height: 9%;
}
.bubble-2{
  top: 24%;
  height: 9%;
}
.bubble-3{
  top: 46%;
  height: 15%;
}
.bubble-btn {
	position: absolute;
	text-align: center;
	line-height: 1.4em;
	font-family: sans-serif;
	font-size: large;
  top: 70%;
	width: 30%;
	margin: 40px auto;
  color: #fff;
	border: 8px double #fff;
	border-radius: 30px;
	padding: 10px;
	background-color: #fbb13d;
}
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0
}

</style>
