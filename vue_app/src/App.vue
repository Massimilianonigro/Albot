<!--Main screen should only contain start button that leads to tutorial-->
<template>
  <div id="app" :style="{ height: '100%' }">
    <div v-if="mainStatus === 0">
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
        v-on:submitName="submitName"
        v-on:requestName="requestName"
      />
      <GameScreen
        ref="gameRef"
        :style="{ overflow: 'visible' }"
        v-bind:gameType="mainStatus"
        v-bind:gamePhase="gamePhase"
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
      />
    </div>
  </div>
</template>

<script>
// const io = require('socket.io-client')
import MainScreen from "./components/MainScreen.vue";
import GameScreen from "./components/GameScreen.vue";
import Chat from "./components/Chat.vue";
import { mapActions } from "vuex";

export default {
  name: "App",
  components: {
    MainScreen,
    GameScreen,
    Chat,
  },
  data() {
    //mainStatus to be deleted
    return {
      message: "",
      mainStatus: 0, // 0 -> Main Screen, 1 -> Picker Tutorial, 2-> Mixer Tutorial, 3-> Picker Practice 4-> Mixer Practice
      gamePhase: {
        phase: "introduction",
        isSelection: false,
        isMixer: false,
        isTutorial: false,
      },
      user_name: "",
      chatLink: undefined,
      selectable_items: [],
      blockPhase: false, //blocks any action from the user
    };
  },
  methods: {
    ...mapActions(["setBlockPhase", "setSubstances"]),
    resetHome() {
      this.mainStatus = 0;
      this.sendHomeClick();
      this.requestName();
    },
    pHIdentificationPhase() {
      //only for testing purposes, to be removed
      this.gamePhase.phase = "practice-pH";
      this.gamePhase.isSelection = false;
      this.gamePhase.isMixer = true;
      this.gamePhase.isTutorial = false;

      this.fetchItems();
      console.log(this.selectable_items);
    },
    startIntroduction() {
      this.sendIntroductoryJSON();
      this.mainStatus = 1;
    },
    startPractice() {
      this.sendPracticeJSON();
      this.mainStatus = 3;
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
    requestName() {
      let message = '{"content":"", "type":"name_request"}';
      this.sendMessage(message);
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
    handleChangePhase(next_phase) {
      let phases = JSON.parse("../resources/phases.json");
      phases.forEach((phase) => {
        if (phase.name === next_phase) {
          this.gamePhase.phase = phase.name;
          this.gamePhase.isMixer = phase.isMixer;
          this.gamePhase.isSelection = phase.isSelection;
          this.gamePhase.isTutorial = phase.isTutorial;
          //TODO: check if needed as it is already done in GameScreen upon creation
          this.fetchItems();
        }
      });
    },
    fetchItems() {
      var stringified = JSON.stringify(require("./resources/phases.json"));
      let phases = JSON.parse(stringified);
      stringified = JSON.stringify(require("./resources/substances.json"));
      let substances = JSON.parse(stringified);
      phases.phases.forEach((phase) => {
        if (phase.name === this.gamePhase.phase) {
          phase.substances.forEach((substance) => {
            let substance_element = {};
            substance_element.item = substances.ingredients[substance - 1].name;
            substance_element.id = substances.ingredients[substance - 1].id;
            substance_element.selected = false;
            substance_element.src = require("./assets/items/" +
              substances.ingredients[substance - 1].asset);
            substance_element.size = substances.ingredients[substance - 1].size;
            substance_element.prsize =
              substances.ingredients[substance - 1].prsize;
            substance_element.ph = substances.ingredients[substance - 1].ph;

            this.selectable_items.push(substance_element);
          });
        }
      });
    },
    submitName(name) {
      this.user_name = name;
    },
  },
  created: function () {
    var _this = this;
    console.log("Starting connection to Server...");
    this.connection = new WebSocket("ws://9cb606a67d5e.ngrok.io");

    let self = this;
    this.connection.onmessage = function (event) {
      let messages = JSON.parse(event.data);
      messages.messages.forEach((message) => {
        console.log("Examing message with ui_effect: " + message.ui_effect);
        if (message.ui_effect === "hidden") {
          this.user_name = message.text;
        } else if (message.ui_effect === "unlock") {
          _this.setBlockPhase(false);
        } else {
          self.$refs.chatRef.receiveMessage(message);
        }
      });
      if (messages.change_phase !== "") {
        this.handleChangePhase(messages.change_phase);
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
.button-exe {
  position: absolute;
  z-index: 100;
  top: 105%;
}
</style>
