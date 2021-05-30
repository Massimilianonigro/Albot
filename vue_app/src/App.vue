<!--Main screen should only contain start button that leads to tutorial-->
<template>
  <div id="app" :style="{ height: '100%' }">
    <div v-if="this.gamePhase.phase === 'introduction' ">
      <MainScreen
        v-on:startIntro="startIntroduction"
        v-on:startPractice="startPractice"
        v-on:sendMessage="sendMessage"
        v-on:submitName="submitName"
      />
    </div>
    <div v-else>
      <Chat
        ref="chatRef"
        :style="{ zIndex: '20' }"
        v-on:sendMessage="sendMessage"
        v-on:addPoints="addPractisePoints"
        v-on:nextClicked="handleNextClick"
        v-on:nextPracticeClicked="handleNextPracticeClick"
        v-on:tryAgainClicked="handleTryAgainClick"
        v-on:continueClicked="handleContinueClick"
        v-on:showTryAgain="displayTryAgain"
      />
      <GameScreen
        ref="gameRef"
        :style="{ overflow: 'visible' }"
        v-bind:user_name="user_name"
        v-on:goHome="resetHome"
        v-on:goBack="sendBackClick"
        v-on:practicePress="handlePracticePress"
        v-on:introClick="sendIntroductoryJSON"
        v-on:practClick="sendPracticeJSON"
        v-on:sendNextInChat="displayNextButton"
        v-on:sendPracNextInChat="displayNextPracticeButton"
        v-on:sendItemMessage="sendItemClick"
        v-on:sendResetMessage="sendResetClick"
        v-on:selectItem="handleSelectItem"
        v-on:sendContinueMessage="handleContinueClick"
        v-on:sendTryAgainMessage="handleTryAgainClick"
        v-on:sendInfoMessage="handleInfoClick"
        v-on:selectionComplete="selectionComplete"
        v-on:pHIdentificationPhase="pHIdentificationPhase"
        v-on:PHGuess="sendPHGuess"
      />
    </div>
  </div>
</template>

<script>
// const io = require('socket.io-client')
import MainScreen from "./components/MainScreen.vue";
import GameScreen from "./components/GameScreen.vue";
import Chat from "./components/Chat.vue";
import { mapActions, mapState } from "vuex";
export default {
  name: "App",
  components: {
    MainScreen,
    GameScreen,
    Chat,
  },
  data() {
    return {
      message: "",
      user_name: "",
      chatLink: undefined,
      complete: false,
    };
  },
  computed: {
    ...mapState(["gamePhase"])
  },
  methods: {
    ...mapActions(["setBlockPhase", "setSubstances", "setShowNextPhase","setGuessed", "setGamePhase"]),
    resetHome() {
      //only for testing purposes, to be performed by backend
      this.setGamePhase("introduction");
      this.sendHomeClick();
    },
    pHIdentificationPhase() {
      //only for testing purposes, to be performed by backend
      this.setGamePhase("practice-pH");
    },
    sendPHGuess(index){
      let message = '{"content":"' + index + '", "type":"guessed"}';
      this.sendMessage(message);
    },
    startIntroduction() {
      this.sendIntroductoryJSON();
      //only for testing purposes, to be removed
      this.setGamePhase("tutorial-selection");
    },
    startPractice() {
      this.sendPracticeJSON();
      this.pHIdentificationPhase();
    },
    sendMessage: function (message) {
      console.log("Sending:" + message);
      this.connection.send(message);
    },
    displayNextButton() {
      this.$refs.chatRef.printNextButton();
    },
    displayNextPracticeButton() {
      this.$refs.chatRef.printNextPracticeButton();
    },
    handleNextClick() {
      this.$refs.gameRef.nextClicked();
      this.sendItemClick("next");
    },
    sendBackClick() {
      this.sendItemClick("back");
    },
    sendHomeClick() {
      this.sendItemClick("home");
    },
    handlePracticePress() {
      this.sendItemClick("next");
    },
    handleNextPracticeClick() {
      this.$refs.gameRef.nextPracticeClicked();
      this.sendItemClick("next");
    },
    handleTryAgainClick() {
      this.sendItemClick("tryAgain");
    },
    handleInfoClick() {
      this.sendItemClick("moreinfo");
    },
    handleContinueClick() {
      this.sendItemClick("continue");
    },
    displayTryAgain() {
      this.$refs.gameRef.displayTryAgain();
    },
    addPractisePoints() {
      console.log("Adding Points");
      this.$refs.gameRef.addPoints();
    },
    sendIntroductoryJSON() {
      this.sendItemClick("introduction");
    },
    sendPracticeJSON() {
      this.sendItemClick("practice");
    },
    sendResetClick() {
      this.sendItemClick("reset");
    },
    sendItemClick(id) {
      let message = '{"content":"' + id + '", "type":"click"}';
      this.sendMessage(message);
    },
    handleSelectItem(id) {
      this.sendItemClick(id);
    },
    selectionComplete() {
      let message = '{"content":"", "type":"selection_complete"}';
      this.sendMessage(message);
    },
    submitName(name) {
      this.user_name = name;
    },
  },
  created: function () {
    let _this = this;
    console.log("Starting connection to Server...");
    this.connection = new WebSocket("ws://636d86d4792a.ngrok.io");

    let self = this;
    this.connection.onmessage = function (event) {
      let messages = JSON.parse(event.data);
      messages.messages.forEach((message) => {
        console.log("Examining message with ui_effect: " + message.ui_effect);
        switch(message.ui_effect){
          case "hidden":
            this.user_name = message.text;
            return;
          case "unlock":
            _this.setBlockPhase(false);
            return;
          case "show_next_phase":
            _this.setShowNextPhase(true);
            self.$refs.chatRef.receiveMessage(message);
            return;
          case "guessed_ph":
            _this.setGuessed(message.text);
            _this.complete = _this.guessed.every((v) => v === true);
            if (_this.complete){
              _this.selectionComplete();
            }
            return;
          default:
            self.$refs.chatRef.receiveMessage(message);
        }
      });
      if (messages.change_phase !== "") {
        this.setGamePhase(messages.change_phase);
      }
    };

    this.connection.onopen = function (event) {
      console.log(event);
      console.log("Successfully connected to the websocket");
    };
  },
};
</script>

<style>
#app {
  font-family: "Berlin Sans FB", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #828e99;
}
</style>
