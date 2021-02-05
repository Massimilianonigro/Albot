<template>
  <div class="chat-bg-container">
    <div class="chat">
      <!--div class="chat-tittle robo-font" :style="{ height: '35px' }"></div -->
      <input type="text" v-model="fontSize" :style="{ height: '35px', width:'19%', marginLeft:'10%' }" class="chat-tittle robo-font corner berlin-font" name="text" />
      <div
        class="message-box"
        :style="{ width: '98%', height: '70%', bottom: '40px' }"
      >
        <vuescroll ref="vs" :style="{ 'text-align': 'left' }" :ops="ops">
          <div
            v-bind:class="getClass(data)"
            class="message"
            :style="{fontSize: fontSize+'vh'}"
            v-for="(data, index) in messages"
            v-bind:key="index"
          >
            <div v-bind:class="getBoxClass(data)">
              <span>
                {{ data.message }}
              </span>
              <img 
                class="img-chat"
                v-if="data.type == 'image'"
                :src="data.src"
              />
            </div>
            
            <button
              v-if="data.type == 'button'"
              :class="getButtonClass(data.func)"
              v-on:click="handleClick(data.func)"
              :style="{ backgroundImage: 'url(' + data.src + ')' }"
              
            ></button>
          </div>
        </vuescroll>
      </div>

      <div class="division"></div>

      <form @submit.prevent="sendMessage" autocomplete="off" class="form-style">
        <div class="textbar">
          <div class="text input-group">
            <input
              type="text"
              class="corner berlin-font"
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
      fontSize: 2.0,
      message: "",
      messages: [
        {
          message: "Hi I'm Albot, what is your name?",
          bot: true,
          type: "text",
        },
        {
          message: "To continue you have to select at least 2 items",
          bot: true,
          type: "text",
        },
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
    getClass(data) {
      let styleItem = "";
      if (data.bot) {
        styleItem = styleItem + "bot-message";
      } else {
        styleItem = styleItem + "user-message";
      }
      return styleItem;
    },
    getBoxClass(data) {
      let styleItem = "";
      if (data.bot) {
        styleItem = styleItem + "bot-message-box";
      } else {
        styleItem = styleItem + "user-message-box";
      }
      return styleItem;
    },
    getButtonClass(functionType) {
      let styleItem = "";
      if (functionType == "next" || functionType == "nextPractice") {
        styleItem = styleItem + "btn-chat";
      } else {
        styleItem = styleItem + "btn-chat";
      }
      return styleItem;
    },
    handleClick(functionType) {
      if (functionType == "next") {
        this.$emit("nextClicked");
      } else if (functionType == "nextPractice") {
        this.$emit("nextPracticeClicked");
      }
    },
    sendMessage() {
      var result = true;
      if (result) {
        let jsonMessage = '{"highlighted":"", "text":"' + this.message + ' "}';

        this.messages.push({ message: this.message, bot: false, type: "text" });
        this.$emit("sendMessage", jsonMessage);
        this.message = "";
      } else {
        console.log("Too Short message");
      }
    },
    receiveMessage(messages) {
      messages.forEach(message => {
        this.messages.push({ message: message, bot: true, type: "text" });
      });
    },
    printNextButton() {
      this.messages.push({
        message: "Click on next button to continue!",
        bot: true,
        type: "button",
        src: require("../assets/uibuttons/NextButton.png"),
        func: "next",
      });
    },
    printNextPracticeButton() {
      this.messages.push({ message: "Click on next button to continue!",
        bot: true,
        type: "button",
        src: require("../assets/uibuttons/NextButton.png"),
        func: "nextPractice",
      });
    },
  },
  updated() {
    this.$refs["vs"].scrollTo({ y: "100%" }, 500);
  },
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
  width: 23%;
  position: fixed;
  z-index: 1;
  top: 2.5%;
  padding-top: 5px;
  overflow-x: hidden;
  right: 1%;
  border: 4px solid;
  border-radius: 60px;
  border-color: #ffa000;
  background-color: #fff;
  background-image: url("../assets/backgrounds/WhiteBG.png");
}

.chat-bg-container {
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
  padding-bottom: 8px;
}

.user-message {
  padding-left: 2vw;
  padding-right: 3.6vw;
  background-image: url("../assets/icons/userchaticon.png");
  background-position-x: 0.5vw;
  background-position-y: 15%;
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
  padding-left: 2.5vw;
  padding-right: 2.25vw;
  margin-right: 10px;
  background-position-x: right;
  background-position-y: 15%;
  background-image: url("../assets/icons/botchaticon.png");
  background-size: 2vw;
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

.division {
  border-bottom: solid 5px #ffa000;
  border-radius: 1px;
  width: 90%;
  margin: 0 auto;
}

.btn-chat {
  position: relative;
  top: -8px;
  height: 45px;
  left: 20%;
  width: 60%;
  border: none;
  background-color: transparent;
  background-position: center;
  background-size: contain;
  background-repeat: no-repeat;
}
.btn-chat:focus {
  outline: none;
}
.btn-chat:active {
  opacity: 0.8;
}
.img-chat{
  max-width:100%;
}

.corner {
  background-color: transparent !important;
  color: #ffa000 !important;
  border-radius: 10px !important;
  border: solid 3px !important;
  border-color: #ffa000 !important;
  height: 40px;
  width: 90%;
  bottom: 100px !important;
  left: 5%;
  right: 5%;
  margin: 2px;
  padding: 2px;
  box-sizing: border-box;
}
</style>