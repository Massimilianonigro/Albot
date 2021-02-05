<template>
  <div id="app" :style="{ height: '100%' }">
    <div v-if="mainStatus == 0">
      <MainScreen
        v-on:startIntro="startIntroduction"
        v-on:startPractice="startPractice"
      />
    </div>
    <div v-else>
      <Chat ref="chatRef" 
      :style="{zIndex:'20'}"
      v-on:sendMessage="sendMessage"
      v-on:nextClicked="handleNextClick"
      v-on:nextPracticeClicked="handleNextPracticeClick"/>
      <GameScreen ref="gameRef"
      :style="{overflow:'visible'}"
      v-bind:gameType="mainStatus" 
      v-on:goHome="resetHome" 
      v-on:practicePress="handlePracticePress"
      v-on:introClick="sendIntroductoryJSON"
      v-on:practClick="sendPracticeJSON"
      v-on:sendNextInChat="displayNextButton"
      v-on:sendPracNextInChat="displayNextPracticeButton"
      v-on:sendItemMessage="sendItemClick"
      v-on:sendResetMessage="sendResetClick"
      v-on:selectItem="handleSelectItem"
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
    return {
      message: "",
      mainStatus: 0,
      chatLink: undefined,
    };
  },
  methods: {
    resetHome() {
      this.mainStatus = 0;
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
      this.sendMessage('{"highlighted":"next", "text":""}')
    },
    handlePracticePress(){
      this.sendMessage('{"highlighted":"next", "text":""}')
    },
    handleNextPracticeClick(){
      this.$refs.gameRef.nextPracticeClicked();
      this.sendMessage('{"highlighted":"next", "text":""}')
    },
    sendIntroductoryJSON(){
      let message = '{"highlighted":"introduction", "text":""}'
      this.sendMessage(message);
    },
    sendPracticeJSON(){
      let message = '{"highlighted":"practice", "text":""}'
      this.sendMessage(message);
    },
    sendItemClick(id){
      let message = '{"highlighted":"'+ id +'", "text":""}'
      this.sendMessage(message);
    },
    sendResetClick(){
      let message = '{"highlighted":"reset", "text":""}'
      this.sendMessage(message);
    },
    handleSelectItem(id){
      let message = '{"highlighted":"'+ id +'", "text":""}'
      this.sendMessage(message); 
    }
  },
  created: function () {
    console.log("Starting connection to Server...");
    this.connection = new WebSocket("ws://localhost:2345");

    let self = this
    this.connection.onmessage = function (event) {
      console.log("Event Log:");
      console.log(event);
      console.log("Data Log:");
      console.log(event.data)
      let messages = JSON.parse(event.data)
      console.log(messages)
      self.$refs.chatRef.receiveMessage(messages)
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
  font-family: 'Berlin Sans FB';
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

<!-- Python Viewport Calculator
def viewportRatio(x, y):
  print("width: ",100,"vw;", sep="")
  print("height: ",y*100/x,"vw;", sep="")
  print("max-width: ",x / y * 100,"vh;", sep="")
  print("max-height: ",100,"vh;", sep="")


viewportRatio(4615, 3463)
-->
