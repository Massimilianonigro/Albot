<template>
  <div class="main-bg">
    <div class="background">
      <SettingsWindow v-on:close="settingsButton()" v-if="settings" />
      <ReportWindow v-on:close="reportButton()" v-if="report" />
      <button
        v-on:click="reportButton()"
        v-if="!start"
        class="report icon"
      ></button>
      <button
        v-on:click="settingsButton()"
        v-if="!start"
        class="settings icon"
      ></button>
      <div v-if="!start" class="magic-colors-sign icon"></div>
      <div v-if="!start" class="bot-tittle icon"></div>

      <button
        class="start-btn"
        type="button"
        v-on:click="clickOnStart"
        v-if="!start"
      ></button>
    </div>
    <div
      class="background"
      :style="{ 'z-index': '20' }"
      v-if="start"
      v-on:click="clickPart"
    >
      <button class="report icon"></button>
      <button class="settings icon"></button>
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
              class="bubble"
            >
              <div class="textbar">
                <div class="text input-group">
                  <input
                    type="text"
                    class="berlin-font"
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
                class="bubble-btn fade-in berlin-font"
                :style="{ left: '8%' }"
            >
              Tutorial
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
              class="bubble-btn fade-in berlin-font"
              :style="{ left: '8%' }"
            >
              Tutorial
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
import SettingsWindow from "./SettingsWindow.vue";
import ReportWindow from "./ReportWindow.vue";

export default {
  components: {
    SettingsWindow,
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
    },
    requestName() {
      this.$emit("requestName");
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
.magic-colors-sign {
  top: 35%;
  left: 30%;
  height: 7%;
  width: 40%;
  z-index: 1;
  background-position-x: center;
  background-image: url("../assets/backgrounds/MagicColors.png");
}
.bot-tittle {
  top: 10%;
  right: 18%;
  height: 30%;
  width: 18%;
  z-index: 1;
  background-position-x: center;
  background-image: url("../assets/backgrounds/BotTittle.png");
}
.icon {
  position: absolute;
  background-repeat: no-repeat;
  background-size: contain;
}
.report {
  top: 2%;
  left: 0;
  height: 8%;
  width: 20%;
  z-index: 21;
  border: none;
  background-position-x: center;
  background-image: url("../assets/uibuttons/ReportButton.png");
}
.settings {
  top: 11%;
  left: 0;
  height: 8%;
  width: 20%;
  z-index: 21;
  border: none;
  background-position-x: center;
  background-image: url("../assets/uibuttons/HomeSetting.png");
}
.settings:focus,
.report:focus,
.start-btn:focus,
.bubble-btn:focus {
  outline: none;
}
.settings:active,
.report:active,
.start-btn:active,
.bubble-btn:active {
  opacity: 0.7;
}
.bot-bg {
  position: absolute;
  background-color: #ffffffb0;
  z-index: 5;
  height: 100%;
  width: 100%;
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
}

.bubble {
  position: static;
  text-align: left;
  color: #CA7900;
  line-height: 1.4em;
  font-size: 2.5vh;
  right: 22%;
  width: auto;
  max-width: 50%;
  margin: 1% auto;
  border: 4px solid #CA7900;
  border-radius: 30px;
  padding: 10px 20px;
  background-color: #fff;
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
  border-color: #CA7900 #CA7900 transparent transparent;
}
.speech:after {
  right: 28px;
  bottom: -30px;
  border: 16px solid;
  border-color: #ffffff #ffffff transparent transparent;
}

.bubble-btn {
  position: static;
  text-align: center;
  line-height: 1.4em;
  font-size: 2.5vh;
  top: 70%;
  width: 30%;
  margin: 40px auto;
  color: #fff;
  border: 8px double #fff;
  border-radius: 30px;
  padding: 10px;
  background-color: #CA7900;
  z-index: 21;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
