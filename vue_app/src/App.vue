<!--Main screen should only contain start button that leads to tutorial-->
<template>
  <div id="app" :style="{ height: '100%' }">
    <div v-if="this.gamePhase.phase === 'introduction'">
      <MainScreen
        v-on:startIntro="startIntroduction"
        v-on:startPractice="startPractice"
        v-on:sendMessage="sendMessage"
        v-on:submitName="submitName"
      />
    </div>
    <div v-if="(this.gamePhase.phase !== 'introduction')">
      <div v-bind:style="displayChat()">
      <Chat
        ref="chatRef"
        :style="{ zIndex: '20' }"
        v-on:sendMessage="sendMessage"
        v-on:addPoints="addPractisePoints"
        v-on:nextClicked="handleNextClick"
        v-on:nextPracticeClicked="selectionComplete"
        v-on:tryAgainClicked="handleTryAgainClick"
        v-on:continueClicked="handleContinueClick"
        v-on:showTryAgain="displayTryAgain"
      />
      </div>
      <GameScreen
        ref="gameRef"
        :style="{ overflow: 'visible' }"
        v-bind:user_name="user_name"
        v-on:goHome="resetHome"
        v-on:goBack="sendBackClick"
        v-on:practicePress="selectionComplete"
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
      <div class="chatlessInstructions" v-if="isChatless && !showNextPhase">
        <h2 class="instruction">
          {{this.currentInstruction}}
        </h2>
        <button class="next-phase-button" v-on:click="nextStateTripetto" v-bind:disabled="!isNextActive"></button>
      </div>
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
      to_show_index: 0,
      currentInstruction: "Colors in your kitchen, press \"Next\" to play.",
      currentInstructionId: 0,
      instructions: "",
      isNextActive: true,
    };
  },
  computed: {
    ...mapState(["gamePhase", "isChatless", "showNextPhase"]),
  },
  methods: {
    ...mapActions([
      "setBlockPhase",
      "setSubstances",
      "setShowNextPhase",
      "setGuessed",
      "setGamePhase",
      "setShowPHScale",
      "setCanSelectSubstances",
        "setShowOnPHScale",
        "setThumbRotation",
        "setIsThumbVisible",
        "setIsScaleClickable"
    ]),
    displayChat(){
      if (this.isChatless){
        return {"display": "none"};
      }
      return {"display": "block"};
    },
    nextStateTripetto(){
      if (this.instructions.instructions[this.currentInstructionId].effect !== ""){
        console.log("sending click tripetto");
        let message = '{"content":"", "type":"click_tripetto"}';
        this.sendMessage(message);
      }
      if(this.instructions.instructions[this.currentInstructionId].effect_2 !== ""){
        console.log("sending click tripetto 2");
        let message = '{"content":"", "type":"click_tripetto_2"}';
        this.sendMessage(message);
      }
      this.currentInstructionId++;
      this.currentInstruction = this.instructions.instructions[this.currentInstructionId].instruction;
      console.log("moving to instruction " + this.currentInstructionId + "with effect" + this.instructions.instructions[this.currentInstructionId].effect);
    },
    resetHome() {
      //only for testing purposes, to be performed by backend
      this.setGamePhase("introduction");
      this.sendHomeClick();
    },
    pHIdentificationPhase() {
      //only for testing purposes, to be performed by backend
      this.setGamePhase("practice-pH");
      this.sendMessage('{"content":"next", "type":"click"}');
    },
    sendPHGuess(index) {
      let message = '{"content":"' + index + '", "type":"guessed"}';
      this.sendMessage(message);
    },
    startIntroduction() {
      this.sendItemClick("introduction");
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
      let message;
      if (this.isChatless){
        message = '{"content":"", "type":"selection_complete"}';
      } else {
        message = '{"content":"", "type":"selection_complete_2"}';
      }
      this.sendMessage(message);
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
      let message;
      if (this.isChatless){
        message = '{"content":"", "type":"selection_complete"}';
      } else {
        message = '{"content":"", "type":"selection_complete_2"}';
      }
      this.sendMessage(message);
    },
    submitName(name) {
      this.user_name = name;
    },
  },
  created: function () {
    var stringified = JSON.stringify(require("./resources/instructions.json"));
    this.instructions = JSON.parse(stringified);
    let _this = this;
    console.log("Starting connection to Server...");
    this.connection = new WebSocket("ws://9d91c87fbef8.ngrok.io");

    let self = this;
    this.connection.onmessage = function (event) {
      let messages = JSON.parse(event.data);
      messages.messages.forEach((message) => {
        console.log("Examining message with ui_effect: " + message.ui_effect);
        switch (message.ui_effect) {
          case "hidden":
            this.user_name = message.text;
            return;
          case "unlock":
            _this.setBlockPhase(false);
            self.$refs.chatRef.receiveMessage(message);
            return;
          case "show_next_phase":
            _this.setShowNextPhase(true);
            self.$refs.chatRef.receiveMessage(message);
            return;
          case "guessed_ph":
            _this.setGuessed(message.text);
            _this.complete = _this.guessed.every((v) => v === true);
            if (_this.complete) {
              _this.selectionComplete();
            }
            return;
          case "show_universal":
            _this.setShowPHScale(0);
            _this.$refs.gameRef.isRerender += 1;
            self.$refs.chatRef.receiveMessage(message);
            return;
          case "show_cabbage":
            _this.setShowPHScale(1);
            _this.$refs.gameRef.isRerender += 1;
            self.$refs.chatRef.receiveMessage(message);
            return;
          case "show_element":
            _this.setShowOnPHScale(_this.to_show_index);
            _this.to_show_index++;
            _this.$refs.gameRef.isRerender += 1;
            self.$refs.chatRef.receiveMessage(message);
            return;
          case "select_from_shelves":
            _this.setCanSelectSubstances(true);
            self.$refs.chatRef.receiveMessage(message);
            return;
          case "correct":
            _this.setThumbRotation(true);
            _this.setIsThumbVisible(true);
            self.$refs.chatRef.receiveMessage(message);
            return;
          case "wrong":
            _this.setThumbRotation(false);
            _this.setIsThumbVisible(true);
            self.$refs.chatRef.receiveMessage(message);
            return;
          case "unlock_next":
            _this.isNextActive = true;
            self.$refs.chatRef.receiveMessage(message);
            return;
          case "lock_next":
            _this.isNextActive = false;
            self.$refs.chatRef.receiveMessage(message);
            return;
          case "unlock_scale":
            console.log("----------------------Unlocking scale");
            _this.setIsScaleClickable(true);
            self.$refs.chatRef.receiveMessage(message);
            return;
          case "lock_scale":
            console.log("----------------------Locking scale");
            _this.setIsScaleClickable(false);
            self.$refs.chatRef.receiveMessage(message);
            return;
          default:
            self.$refs.chatRef.receiveMessage(message);
        }
      });
      if (messages.change_phase !== "") {
        _this.setGamePhase(messages.change_phase);
        _this.setSubstances(messages.change_phase);
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

.sc-hHEiqL {
  height: 95vh !important;
  width: 40% !important;
  left: 60% !important;
}

.chatlessInstructions {
  bottom: 1%;
  height: 15%;
  width: 70%;
  left: 15%;
  border-radius: 15px;
  border: 4px solid #ca7900;
  background-color: #fff;
  display: block;
  position: absolute;
}

.next-phase-button {
  position: absolute;
  height: 80%;
  width: 20%;
  top: 10%;
  left: 78%;
  background-repeat: no-repeat;
  background-size: contain;
  background-color: transparent;
  background-position: center;
  border: 0;
  z-index: 1000;
  background-image: url("./assets/uibuttons/NextPhaseButton.png");
  outline: none;
}

.next-phase-button:disabled{
  opacity: 0.3;
}

.instruction{
  font-size: x-large;
  text-align: center !important;
  margin-left: 1%;
  width: 75%;
}

</style>
