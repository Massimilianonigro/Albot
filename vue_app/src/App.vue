<template>
  <div id="app" :style="{ height: '100%' }">
    <div v-if="mainStatus == 0">
      <MainScreen
        v-on:startIntro="startIntroduction"
        v-on:startPractice="startPractice"
      />
    </div>
    <div v-else>
      <GameScreen v-bind:gameType="mainStatus" v-on:goHome="resetHome" />
      <Chat />
    </div>
    <button class="button-exe" v-on:click="sendMessage('message test')">Send Message</button>
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
      mainStatus: 0
    };
  },
  methods: {
    resetHome() {
      this.mainStatus = 0;
    },
    startIntroduction() {
      this.mainStatus = 1;
    },
    startPractice() {
      this.mainStatus = 3;
    },
    sendMessage: function(message) {
      console.log(this.connection);
      this.connection.send(message);
    }
  },
  created: function () {
    console.log("Starting connection to WebSocket Server");
    this.connection = new WebSocket("ws://localhost:2345");

    

    this.connection.onmessage = function (event) {
      console.log(event);
    };

    this.connection.onopen = function (event) {
      console.log(event);
      console.log("Successfully connected to the echo websocket server...");
    };
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
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
