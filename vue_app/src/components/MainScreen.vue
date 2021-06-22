<template>
  <div class="main-bg">
    <div class="blackboard">
      <div class="background">
      <ReportWindow v-on:close="reportButton()" v-if="report" />
      <button
        v-on:click="reportButton()"
        v-if="!start"
        class="report icon"
      ></button>
      <div v-if="!start" class="magic-colors-sign icon"></div>
      <div v-if="!start" class="bot-title icon"></div>

      <button
        class="start-btn"
        type="button"
        v-on:click="clickOnStart"
        v-if="!start"
      ></button>
        </div>
    </div>
      <div class="background"
           :style="{ 'z-index': '20' }"
           v-if="start"
           v-on:click="clickPart">
      <button class="report icon"></button>
      <div class="bot-welcome"></div>
      <transition name="fade">
        <ul class="chat-welcome" v-bind:style="{ display: visibilityIntro }"  v-if="this.user_name === ''">
          <li>
            <p class="bubble berlin-font">Hi! I'm Albot.</p>
          </li>
          <li>
            <p class="bubble berlin-font">What's your name?</p>
          </li>
          <li>
            <form
              @submit.prevent="submitName"
              autocomplete="off"
              class="bubble form-box"
            >
              <div class="textbar">
                <div class="text input-group">
                  <input
                    type="text"
                    class="berlin-font textarea"
                    placeholder="Type your name"
                    v-model="message"
                    name="message"
                    style="border: none transparent; outline: none"
                  />
                </div>
              </div>
            </form>
          </li>
        </ul>
      </transition>
      <transition name="fade">
        <ul class="chat-welcome" v-bind:style="{ display: visibilityIntro }" v-if="this.user_name !== ''">
          <li>
            <p class="bubble berlin-font">
              Welcome back, {{ this.user_name }}! Click to continue.
            </p>
          </li>
          <li>
            <button
                v-on:click="clickOnIntro"
                class="bubble-tutorial-btn fade-in berlin-font"
                :style="{ left: '8%' }"
            >Tutorial</button>
            <button
                v-on:click="clickOnPractice"
                class="bubble-btn fade-in berlin-font"
                :style="{ right: '8%' }"
            >
              Experiment
            </button>
          </li>
        </ul>
      </transition>
      <transition name="fade">
        <ul class="chat-welcome" v-bind:style="{ display: visibilityButtons }">
          <li>
            <p class="bubble berlin-font">
              Welcome {{ this.user_name }}! We will carry out this experiment
              together. Please choose a lesson to start:
            </p>
          </li>
          <li>
            <button
              v-on:click="clickOnIntro"
              class="bubble-tutorial-btn berlin-font fade-in"
              :style="{ left: '8%' }"
            >Tutorial
            </button>
            <button
              v-on:click="clickOnPractice"
              class="bubble-btn fade-in berlin-font"
              :style="{ right: '8%' }"
            >
              Experiment
            </button>
          </li>
        </ul>
      </transition>
    </div>
    </div>
</template>

<script>
import ReportWindow from "./ReportWindow.vue";

export default {
  components: {
    ReportWindow,
  },
  name: "MainScreen",
  data() {
    return {
      current: 1,
      start: false,
      part2: false,
      part3: false,
      report: false,
      settings: false,
      message: "",
      user_name:
        this.$root.$children[0].user_name === undefined
          ? ""
          : this.$root.$children[0].user_name,
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

      let chat = this.isChatless ? "chatless" : "chat";
      let codeMessage = '{"type":"user_code", "content":" ' + chat + ' "}';
      this.$emit("sendMessage", codeMessage);
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
  width: 24%;
  left: 38%;
  background-repeat: no-repeat;
  background-size: contain;
  background-color: transparent;
  background-position: top;
  background-image: url("../assets/uibuttons/StartButton.png");
  border: 0;
}

.start-btn:focus{
  outline: none;
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
.magic-colors-sign {
  top: 35%;
  left: 20%;
  height: 30%;
  width: 60%;
  background-position-x: center;
  background-image: url("../assets/backgrounds/MagicColors.png");
  background-size: contain;
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
.report {
  top: 2%;
  left: 0;
  height: 10%;
  width: 20%;
  z-index: 1000;
  border: none;
  background-position-x: center;
  background-size: contain;
  background-image: url("../assets/uibuttons/ReportButton.png");
  background-color: transparent !important;
}

.report:focus{
  outline: none;
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

.chat-welcome {
  list-style-type: none;
  padding-top: 10%;
  z-index: 1000;
}

.bubble {
  position: static;
  text-align: left;
  color: #F9A400;
  line-height: 1.4em;
  font-size: 2.5vh;
  right: 22%;
  width: auto;
  max-width: 50%;
  margin: 1% auto;
  border: 4px solid #F9A400;
  border-radius: 30px;
  padding: 10px 20px;
  background-color: #fff;
}

.textarea {
  color: #3E4349;
  width: 100% !important;
}

.bubble:before,
.bubble:after {
  content: "";
  position: absolute;
  width: 0;
  height: 0;
}
.speech:before {
  right: 24px;
  bottom: -40px;
  border: 20px solid;
  border-color: #F9A400 #F9A400 transparent transparent;
}
.speech:after {
  right: 28px;
  bottom: -30px;
  border: 16px solid;
  border-color: #ffffff #ffffff transparent transparent;
}

.bubble-btn {
  line-height: 5em;
  position: static;
  top: 70%;
  width: 20%;
  height: 100%;
  z-index: 2000 !important;
  color: transparent;
  background-image: url("../assets/uibuttons/Experiment.png");
  background-repeat: no-repeat;
  background-size: contain;
  background-position-x: center;
  background-position-y: center;
  background-color: transparent;
  border: none;
  margin: 1vw;
}

.bubble-btn:focus{
  outline: none;
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

.bubble-tutorial-btn:focus{
  outline: none;
}

</style>
