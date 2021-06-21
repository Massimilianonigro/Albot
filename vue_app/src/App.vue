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
    <div v-if="this.gamePhase.phase !== 'introduction'">
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
      <div class="chatlessInstructions" v-if="isChatless">
        <h2 class="instruction"  v-bind:style=getInstructionsWidth()>
          {{this.currentInstruction}}
        </h2>
        <button class="next-phase-button" v-on:click="nextStateTripetto" v-bind:disabled="!isNextActive" v-if="!showNextPhase"></button>
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
      complete: 0,
      to_show_index: 0,
      currentInstruction: "Colors in your kitchen, press \"Next\" to play.",
      currentInstructionId: 0,
      instructions: "",
      isNextActive: true,
    };
  },
  computed: {
    ...mapState(["gamePhase", "isChatless", "showNextPhase", "showFinalScreen"]),
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
        "setIsScaleClickable",
        "setGuessingIndex",
        "setShowFinalScreen"
    ]),
    displayChat(){
      if (this.isChatless || this.showFinalScreen){
        return {"display": "none"};
      }
      return {"display": "block"};
    },
    getInstructionsWidth(){
      if (this.showNextPhase){
        return {width: "95%"};
      }
      return { width: "75%"};
    },
    nextStateTripetto(){
      if (this.instructions.instructions[this.currentInstructionId].effect !== ""){
        let message = '{"content":"", "type":"click_tripetto"}';
        this.sendMessage(message);
      }
      if(this.instructions.instructions[this.currentInstructionId].effect_2 !== ""){
        let message = '{"content":"", "type":"click_tripetto_2"}';
        this.sendMessage(message);
      }
      this.currentInstructionId++;
      this.currentInstruction = this.instructions.instructions[this.currentInstructionId].instruction;
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
      this.currentInstructionId = 17;
      this.currentInstruction = this.instructions.instructions[this.currentInstructionId].instruction;
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
    this.connection = new WebSocket("ws://16bc602d9483.ngrok.io");

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
            _this.setGuessingIndex(-2);
            _this.complete++;
            if (_this.complete === 3) {
              _this.setShowFinalScreen(true);
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
            _this.setIsScaleClickable(true);
            self.$refs.chatRef.receiveMessage(message);
            return;
          case "lock_scale":
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
  width: 65%;
  left: 20%;
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
}

</style>
