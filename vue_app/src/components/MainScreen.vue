<template>
  <div class="main-bg">
    <div class="background">
      <div class="settings icon"></div>
      <div class="share icon"></div>
      <div class="report icon"></div>
    </div>
    <button
      :style="{ width: '140px' }"
      class="btn btn-primary main-btn"
      type="button"
      v-on:click="clickOnStart"
    >
      Start!
    </button>
    <div
      v-if="start" 
      class="bot-bg">
        <div class="bot-welcome"></div>
      <transition name="fade">
        <p class="bubble speech bubble-1"> Hi, I'm Albot, lets have some fun with chemistry</p>
      </transition>
      <transition name="fade">
        <p v-if="part2" class="bubble speech bubble-2"> 
          <button v-on:click="clickOnIntro" class="bubble-btn fade-in" :style="{'left': '8%'}"> Introduction </button>
          or 
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
      //this.$emit("startPractice");
      this.$alert("Not implemented yet.");
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
.main-btn {
  position: absolute;
  top: 48%;
  -ms-transform: translateX(-50%);
  transform: translateX(-50%);

  background-color: #ff9900 !important;
  border-color: #ffffff !important;
  border-width: 3px;
}
.main-bg {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
	width: 100%;
	height: 100%;
  background-color: #ff9100;
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
  background-image: url("../assets/backgrounds/StartPage.png");
  background-position: center;
  background-size: contain;
  background-repeat: no-repeat;
}
.icon{
	position: absolute;
	background-repeat: no-repeat;
	background-size: contain;
}
.settings{
	top: 8.5%;
  left: 4.5%;
	height: 5%;
	width:  5%;
	z-index: 1;
	background-position-x: center;
	background-image: url("../assets/icons/SettingIcon.png");
}
.share{
	top: 15%;
  left: 4.5%;
	height: 5%;
	width:  5%;
	z-index: 1;
	background-position-x: center;
	background-image: url("../assets/icons/ShareIcon.png");
}
.report{
	top: 22%;
  left: 4.5%;
	height: 5%;
	width:  5%;
	z-index: 1;
	background-position-x: center;
	background-image: url("../assets/icons/ReportIcon.png");
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
	text-align: center;
	line-height: 1.4em;
	font-family: sans-serif;
	font-size: large;
  right: 35%;
	width: 50%;
	margin: 40px auto;
	border: 4px solid #ff9100;
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
	border-color: #ff9100 #ff9100 transparent transparent;
}
.speech:after {
	right: 28px;
	bottom: -30px;
	border: 15px solid;
	border-color: #ffffff #ffffff transparent transparent;
}

.bubble-1{
  top: 10%;
}
.bubble-2{
  top: 28%;
  height: 12%;
}
.bubble-3{
  top: 48%;
  height: 15%;
}
.bubble-btn {
	position: absolute;
	text-align: center;
	line-height: 1.4em;
	font-family: sans-serif;
	font-size: large;
  top: -35%;
	width: 30%;
	margin: 40px auto;
  color: #ffaa00;
	border: 2px solid #ff9100;
	border-radius: 30px;
	padding: 10px;
	background-color: #fff;
}
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0
}

</style>
