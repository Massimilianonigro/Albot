<!--Main screen should only contain start button that leads to tutorial-->
<template>
  <div id="app" :style="{ height: '100%' }">
    <div v-if="mainStatus === 0">
      <MainScreen
        v-on:startIntro="startIntroduction"
        v-on:startPractice="startPractice"
      />
    </div>
    <div v-else>
      <Chat 
        ref="chatRef" 
        :style="{zIndex:'20'}"
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
        :style="{overflow:'visible'}"
        v-bind:gameType="mainStatus"
        v-bind:selectable_items="selectable_items"
        v-bind:gamePhase="gamePhase"
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
      />
    </div>
   
  </div>
</template>

<script>
// const io = require('socket.io-client')
import MainScreen from "./components/MainScreen.vue";
import GameScreen from "./components/GameScreen.vue";
import Chat from "./components/Chat.vue";

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
      chatLink: undefined,
      selectable_items:[],
    };
  },
  methods: {
    resetHome() {
      this.mainStatus = 0;
      this.sendHomeClick();
    },
    startIntroduction() {
      this.sendIntroductoryJSON();
      this.mainStatus = 1;
    },
    startPractice() {
      this.sendPracticeJSON();
      this.mainStatus = 3;
    },
    sendMessage: function(message) {
      console.log("Sending:" + message)
      this.connection.send(message);
    },
    displayNextButton(){
      this.$refs.chatRef.printNextButton();
    },
    displayNextPracticeButton(){
      this.$refs.chatRef.printNextPracticeButton();
    },
    handleNextClick(){
      this.$refs.gameRef.nextClicked();
      this.sendItemClick("next");
    },
    sendBackClick(){
      this.sendItemClick("back");
    },
    sendHomeClick(){
      this.sendItemClick("home");
    },
    handlePracticePress(){
      this.sendItemClick("next");
    },
    handleNextPracticeClick(){
      this.$refs.gameRef.nextPracticeClicked();
      this.sendItemClick("next");
    },
    handleTryAgainClick(){
      this.sendItemClick("tryAgain");
    },
    handleInfoClick(){
      this.sendItemClick("moreinfo");
    },
    handleContinueClick(){
      this.sendItemClick("continue");
    },
    displayTryAgain(){
      this.$refs.gameRef.displayTryAgain()
    },
    addPractisePoints(){
          console.log("Adding Points")
      this.$refs.gameRef.addPoints()
    },
    sendIntroductoryJSON(){
      this.sendItemClick("introduction")
    },
    sendPracticeJSON(){
      this.sendItemClick("practice");
    },
    sendResetClick(){
      this.sendItemClick("reset");
    },
    sendItemClick(id){
      let message = '{"content":"'+ id +'", "type":"click"}';
      this.sendMessage(message);
    },
    handleSelectItem(id){
      this.sendItemClick(id);
    },
    handleChangePhase(next_phase){
      let phases = JSON.parse("../resources/phases.json");
      phases.forEach(phase => {
        if (phase.name === next_phase){
          this.gamePhase.phase = phase.name;
          this.gamePhase.isMixer = phase.isMixer;
          this.gamePhase.isSelection = phase.isSelection;
          this.gamePhase.isTutorial = phase.isTutorial;
          this.fetchItems();
          return;
        }
      })
    },
    fetchItems(){
      let phases = JSON.parse("../resources/phases.json");
      let substances = JSON.parse("../resources/substances.json");
      let substance_element;
      this.selectable_items = [];
      phases.forEach(phase => {
        if (phase.name === this.gamePhase){
          phase.ingredients.forEach(substance => {

            substance_element.item = substances[substance].name;
            substance_element.id = substances[substance].id;
            substance_element.selected = false;
            substance_element.src = require(substances[substance].asset);
            substance_element.size = substances[substance].size;
            substance_element.prsize = substances[substance].prsize;
            substance_element.ph = substances[substance].prsize;

            this.selectable_items.push(substance_element);
            console.log(substance_element);
          })
        }
      })
    }
  },
  created: function () {
    console.log("Starting connection to Server...");
    this.connection = new WebSocket("ws://localhost:2345");

    let self = this
    this.connection.onmessage = function (event) {
      let messages = JSON.parse(event.data)
      messages.messages.forEach(message => {
        self.$refs.chatRef.receiveMessage(message)
      });
      if (messages.change_phase !== ""){
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
  font-family: 'Berlin Sans FB',sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #828e99;
}
.button-exe{
  position: absolute;
  z-index: 100;
  top: 105%;
}
</style>
