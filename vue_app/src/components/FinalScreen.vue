<template>
  <div class="main-bg">
    <div class="icon final-message"></div>
    <div class="blackboard">
      <div class="background">
        <div v-if="!start" class="bot-title icon"></div>
      </div>
    </div>
    <div class="background"
         :style="{ 'z-index': '20' }"
         v-if="start"
         v-on:click="clickPart">
      <div class="bot-welcome"></div>
    </div>
  </div>
</template>

<script>

export default {
  name: "FinalScreen",
  data() {
    return {
      current: 1,
      start: false,
      part2: false,
      part3: false,
      report: false,
      settings: false,
      message: "",
      visibilityIntro: "block",
      visibilityButtons: "none",
      alreadyNamed: false,
    };
  },
  methods: {
    clickOnStart() {
      this.start = true;
    },
    clickPart() {
      if (this.start === true) {
        this.current += 1;
        if (this.current === 2) {
          this.part2 = true;
        } else if (this.current === 3) {
          this.part3 = true;
        }
      }
    },
    clickOnIntro() {
      this.$emit("startIntro");
    },
    clickOnPractice() {
      this.$emit("startPractice");
    },
    reportButton() {
      this.report = !this.report;
    },
    settingsButton() {
      this.settings = !this.settings;
    },
    submitName() {
      this.user_name = this.message;
      let jsonMessage = '{"type":"name", "content":"' + this.user_name + '"}';
      this.$emit("sendMessage", jsonMessage);
      this.message = "";
      this.visibilityIntro = "none";
      this.visibilityButtons = "block";
      this.$emit("submitName", this.user_name);
    },
  },
};
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
a {
  color: #42b983;
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
  background-image: url("../assets/backgrounds/WhiteBG.png");
}
.background {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  margin: auto;
  width: 100vw;
  height: 75vw;
  max-width: 133.3vh;
  max-height: 100vh;
  background-image: url("../assets/backgrounds/Welcome.png");
  background-position-x: center;
  background-position-y: bottom;
  background-size: contain;
  background-repeat: no-repeat;
  z-index: 200 !important;
  overflow: visible;
}
.blackboard{
  background-image: url("../assets/backgrounds/blackboard.png");
  background-position-x: center;
  background-position-y: top;
  background-repeat: no-repeat;
  background-size: contain;
  width: 100%;
  height: 80%;
  z-index: 30 !important;
}

.bot-title {
  top: 0;
  right: 0;
  height: 40%;
  width: 30%;
  z-index: 1;
  background-position-x: center;
  background-image: url("../assets/backgrounds/BotTitle.png");
}
.icon {
  position: absolute;
  background-repeat: no-repeat;
  background-size: contain;
  background-color: transparent !important;
}

.bot-welcome {
  position: absolute;
  top: 18%;
  right: 0;
  height: 30%;
  width: 30%;
  background-repeat: no-repeat;
  background-size: contain;
  background-position-x: center;
  background-position-y: center;
  background-image: url("../assets/backgrounds/Bot.png");
}

.final-message{
  position: absolute;
  top: 5%;
  left: 15%;
  height: 50%;
  width: 50%;
  background-repeat: no-repeat;
  background-size: contain;
  background-position-x: center;
  background-position-y: center;
  background-image: url("../assets/backgrounds/final-message.png");
}

</style>