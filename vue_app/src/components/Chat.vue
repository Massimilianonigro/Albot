<template>
  <div class="chat">
    <div class="chat-tittle robo-font" :style="{ 'height': '6%'}"><h2>Chat with Albot</h2></div>
    
    <div class="message-box" :style="{ 'height': '70%', 'bottom': '40px'}">
      <vuescroll :style="{'text-align':'left'}" :ops="ops"> 
        <div v-bind:class="{'user-message': !data.bot, 'bot-message': data.bot}" class="child-element message" 
        v-for="(data, index) in messages" v-bind:key="index"> 
          <span>{{data.message}} </span>
        </div> 
      </vuescroll>
    </div>
    
    <form @submit.prevent="sendMessage" autocomplete="off" class="formy">
      <div class="textbar">
        <div class="text input-group mb-3"> <input type="text" class="form-control albot-text" placeholder="Write your message here..." v-model="message" name="message"/> </div>
        <input class="btn  corner-chat" type="button" value="Send" v-on:click="sendMessage"/>
      </div>
    </form>
  </div>
</template>

<script>
import vuescroll from 'vuescroll';

export default {
  components: {
      vuescroll
    },   
  name: 'Chat',
  props: {},
  data() {
    return {
      message: "",
      messages: [
        {message: "Hi, I'm over here now", bot: true},
        {message: "I'm an Artificial Intelligence(AI) powered bot", bot: true},
        {message: "If you want to ask me something, just type it down here.", bot: true}
      ],
      ops: {
        rail: {
          background: '#01a99a',
          opacity: 0,
          size: '6px',
          specifyBorderRadius: false,
          gutterOfEnds: null,
          gutterOfSide: '2px',
          keepShow: false
        },
        bar: {
          background: '#a06000',
          keepShow: true,
          size: '10px',
          minSize: 0.2,
        },
        scrollButton: {
          enable: false,
          background: '#cecece'
        },
        vuescroll: {
          wheelScrollDuration: 100,
          wheelDirectionReverse: false,
          locking: true,
          checkShifKey: true
        },
        scrollPanel: {
          initialScrollY: "100%"
        }
      },
    };
  },
  methods:{
    sendMessage(){
      var result = true
        if (result) {
          this.messages.push({message: this.message, bot: false})
          this.message = '';
        } else {
          console.log('Too Short message');
        }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.chat{
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 20%;
  position: fixed;
  z-index: 1;
  top: 0;
  padding-top: 5px;
  overflow-x: hidden;
  right: 0;
  border-left: 4px solid;
  border-color: #ffffff;
}
.chat-tittle .textbar{
  flex: none;
}
.textbar{
  flex: none;
  bottom: 0;
  width: 100%;
  background-color: #ff9900;
  display: table;
  padding: 7px;
}
.textbar .text{
    display: table-cell;
    width: 100%;
}
.textbar .text > input {
    width: 100%;
    margin: 2px;
    padding: 2px;
    box-sizing: border-box;
}
.user-message{
  text-align: left;
  padding-left: 32px;
  padding-right: 26px;

  background-image: url("../assets/icons/userchaticon.png");
  background-position: 4px;
  background-size: 18px 24px;
}
.bot-message{
  text-align: left;
  padding-left: 40px;
  padding-right: 24px;
  margin-right: 10px;
  background-position: right;
  width: wrap;
  background-color: #ffe5be;

  background-image: url("../assets/icons/botchaticon.png");
  background-size: 24px 24px;
}
.message{
  background-repeat: no-repeat;
  display: block;
  margin-top: 2px;
  padding-top: 2px;
  margin-bottom: 2px;
  padding-bottom: 2px;
}
.message-box{
  flex: auto;
}
.formy{
  margin-top:4px;
  margin-right:4px;
  margin-bottom:4px;
}
h3 {
  margin: 40px 0 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.corner-chat {
  background-color: #ffae35 !important;
  border-color: #ffffff !important;
  color: #ffffff !important;
  border-bottom-right-radius: 10px !important;
  border-top-right-radius: 10px !important;
  border-width: 0px;
}
.albot-text{
  border-bottom-left-radius: 10px !important;
  border-top-left-radius: 10px !important;
  height: 40px;
}
</style>