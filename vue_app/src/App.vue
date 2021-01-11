<template>
  <div id="app" :style="{ 'height': '100%'}">
    <div v-if="mainStatus==0">
      <MainScreen v-on:startIntro="startIntroduction" v-on:startPractice="startPractice"/>
    </div>
    <div v-if="mainStatus==1">
      <GameScreen/>
      <Chat/>
    </div>
    <div v-if="mainStatus==3">
      <GameScreen/>
      <Chat/>
    </div>
  </div>
</template>

<!-- 
  import HelloWorld from './components/HelloWorld.vue'
-->
<script>
  import MainScreen from './components/MainScreen.vue'
  import GameScreen from './components/GameScreen.vue'
  import Chat from './components/Chat.vue'
  

export default {
  name: 'App',
  components: {
    MainScreen,
    GameScreen,
    Chat
  },
  data() {
    return {
      mainStatus: 0
    }
  },
  methods: {
    startIntroduction(){
      this.mainStatus = 1
    },
    startPractice(){
      this.mainStatus = 2
    }
  }

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
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
