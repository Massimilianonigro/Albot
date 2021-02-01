<template>
  <div class="chat-bg-container">
    <div class="chat">
      <div class="chat-tittle robo-font" :style="{ height: '35px' }"></div>

      <div class="message-box" :style="{ width: '98%', height: '70%', bottom: '40px' }">
        <vuescroll ref="vs" :style="{ 'text-align': 'left' }" :ops="ops">
          <div
            v-bind:class="{ 'user-message': !data.bot, 'bot-message': data.bot }"
            class="child-element message"
            v-for="(data, index) in messages"
            v-bind:key="index"
          >
            <div v-bind:class="{ 'user-message-box': !data.bot, 'bot-message-box': data.bot }">
              <span>
                {{ data.message }} 
              </span>
            </div>
          </div>
        </vuescroll>
      </div>

      <div class="division"></div>
      
      <form @submit.prevent="sendMessage" autocomplete="off" class="form-style">
        <div class="textbar">
          <div class="text input-group">
            <input
              type="text"
              class="corner"
              placeholder="Write your message here..."
              v-model="message"
              name="message"
            />
          </div>
        </div>
      </form>
      <div :style="{ height: '10px' }"></div>
    </div>
  </div>
</template>

<script>
import vuescroll from "vuescroll";

export default {
  components: {
    vuescroll,
  },
  name: "Chat",
  props: {},
  data() {
    return {
      message: "",
      messages: [
        { message: "Hi I'm Albot, what is your name?", bot: true },
      ],
      ops: {
        rail: {
          background: "#01a99a",
          opacity: 0,
          size: "6px",
          specifyBorderRadius: false,
          gutterOfEnds: null,
          gutterOfSide: "2px",
          keepShow: false,
        },
        bar: {
          background: "#ffa000",
          keepShow: false,
          size: "10px",
          minSize: 0.2,
        },
        scrollButton: {
          enable: false,
          background: "#cecece",
        },
        vuescroll: {
          wheelScrollDuration: 100,
          wheelDirectionReverse: false,
          locking: true,
          checkShifKey: true,
        },
        scrollPanel: {
          initialScrollY: "100%",
        },
      },
    };
  },
  methods: {
    sendMessage() {
      var result = true;
      if (result) {
        this.messages.push({ message: this.message, bot: false });
        this.$emit("sendMessage", this.message);
        this.message = "";
        
      } else {
        console.log("Too Short message");
      }
    },
    receiveMessage(message) {
        this.messages.push({ message: message, bot: true });
    },
  },
  updated(){
    this.$refs["vs"].scrollTo(
        {
          y: "100%",
        },
        500
      );
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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

.chat {
  margin: auto;
  display: flex;
  flex-direction: column;
  height: 95%;
  width: 20%;
  position: fixed;
  z-index: 1;
  top: 2.5%;
  padding-top: 5px;
  overflow-x: hidden;
  right: 1%;
  border: 4px solid;
  border-radius: 60px;
  border-color: #ffa000;
}

.chat-bg-container {
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 22%;
  position: fixed;
  z-index: 1;
  top: 0;
  padding-top: 5px;
  overflow-x: hidden;
  right: 0;
  border: 0px none;
  background: transparent;
}

.chat-tittle .textbar {
  flex: none;
}

.textbar {
  flex: none;
  bottom: 0;
  width: 100%;
  background-color: transparent;
  display: table;
  padding: 7px;
}

.textbar .text {
  display: table-cell;
  width: 100%;
}

.message {
  text-align: left;
  background-repeat: no-repeat;
  display: block;
  margin-top: 2px;
  padding-top: 2px;
  margin-bottom: 2px;
  padding-bottom: 2px;
}

.user-message {
  padding-left: 32px;
  padding-right: 26px;
  background-image: url("../assets/icons/userchaticon.png");
  background-position: 4px;
  background-size: 18px 24px;
}

.user-message-box {
  color: #ffa000;
  border: 2px solid #ffa000;
  border-radius: 20px;
  padding: 4px 8px 4px 8px;
  width: 100%;
}

.bot-message {
  padding-left: 20px;
  padding-right: 30px;
  margin-right: 10px;
  background-position: right;
  background-image: url("../assets/icons/botchaticon.png");
  background-size: 24px 24px;
}

.bot-message-box {
  color: #fff;
  background-color: #ffa000;
  border: 2px solid #ffa000;
  border-radius: 20px;
  padding: 4px 8px 4px 8px;
  width: 100%;
}

.message-box {
  flex: auto;
  margin-right: 1%;
  margin-left: 1%;
}

.form-style {
  margin-top: 4px;
  margin-right: 4px;
  margin-bottom: 4px;
}

.division{
  border-bottom: solid 5px #ffa000;
  border-radius: 1px;
  width: 90%;
  margin:  0 auto;
}

.corner {
  background-color: transparent !important;
  color: #ffa000 !important;
  border-radius: 10px !important;
  border: solid 3px !important;
  border-color: #ffa000 !important;
  height: 40px;
  width: 90% !important;
  bottom: 100px !important;
  left: 5%;
  right: 5%;
  margin: 2px;
  padding: 2px;
  box-sizing: border-box;
}
</style>