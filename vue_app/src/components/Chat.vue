<template>
  <div class="chat-bg-container">
    <div class="chat">
      <div class="chat-title robo-font" :style="{ height: '15px' }"></div >
      <!--input type="text" v-model="fontSize" :style="{ height: '25px', width:'19%', marginLeft:'10%' }" class="chat-tittle robo-font corner berlin-font" name="text" /-->
      <div
        class="message-box"
        :style="{ width: '98%', height: '70%', bottom: '100%'}"
      >
        <vuescroll ref="vs" :style="{ 'text-align': 'left' }" :ops="ops">
          <div
            v-bind:class="getClass(data)"
            class="message"
            :style="getMessageStyle(data.type)" 
            v-for="(data, index) in messages"
            v-bind:key="index"
          >
            <audio id="audio" src="../resources/new_message_received.wav" autoplay></audio>
            <div v-bind:class="getBoxClass(data)">
              <span>
                {{ data.message }}
              </span>
              <img 
                class="img-chat"
                alt="chat background"
                v-if="data.type === 'image'"
                :src="data.src"
              />
            </div>
            
            <button
              v-if="data.type === 'button'"
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
              placeholder="Type a message"
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
      messages: [],
      audioNotification: new Audio(require('../resources/new_message_received.wav')),
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
      if (functionType === "next" || functionType === "nextPractice") {
        styleItem = styleItem + "btn-chat";
      } else {
        styleItem = styleItem + "btn-chat";
      }
      return styleItem;
    },
    getMessageStyle(type){
      if(type === "text")
        return {'font-size': this.fontSize+'vh'}
      if(type === "button")
        return {'font-size': this.fontSize+'vh', 'padding-top':'2px', 'padding-bottom':'0px', 'margin-bottom':'-10px'}
    },
    handleClick(functionType) {
      if (functionType === "next") {
        this.$emit("nextClicked");
      } 
      else if (functionType === "nextPractice") {
        this.$emit("nextPracticeClicked");
      } 
      else if (functionType === "tryAgain") {
        this.$emit("tryAgainClicked");
      } 
      else if (functionType === "continue") {
        this.$emit("continueClicked");
      }
    },
    sendMessage() {
      let jsonMessage = '{"type":"text", "content":"' + this.message + ' "}';
      this.messages.push({ message: this.message, bot: false, type: "text" });
      this.$emit("sendMessage", jsonMessage);
      this.message = "";
    },
    receiveMessage(message_received) {
      console.log(message_received);
      let toPush = { message: message_received.text, bot: true, type: "text" }
      switch (message_received.ui_effect) {
        case "tryagain":
          toPush = { message: message_received.text, bot: true, type: "button", src: require("../assets/uibuttons/TryAgainButton.png"), func: "tryAgain" };
            this.$emit("showTryAgain");
            break;
          case "continue":
            toPush = { message: message_received.text, bot: true, type: "button", src: require("../assets/uibuttons/ContinueButton.png"), func: "continue", };
            this.$emit("addPoints");
            break;
          case "next":
            toPush = { message: message_received.text, bot: true, type: "button", src: require("../assets/uibuttons/NextButton.png"), func: "next", };
            this.$emit("nextClicked");
            break;
          default:
            if(message_received.ui_effect.includes("display")){
              toPush = { message: "", bot: true, type: "image", src:this.getImageById(message_received.text.split("_")[1]) };
            }
            break;
        }
        this.messages.push(toPush);
    },
    getImageById(id){
      switch (id){
        case("1"):
          return require("../assets/molecules/BakingSoda.png")
        case("2"):
          return require("../assets/molecules/EggWhite.png")
        case("3"):
          return require("../assets/molecules/Vinegar.png")
        case("4"):
          return require("../assets/molecules/Bleach.png")
        case("5"):
          return require("../assets/molecules/OvenCleaner.png")
        case("6"):
          return require("../assets/molecules/Soap.png")
        case("7"):
          return require("../assets/molecules/Cola.png")
        case("8"):
          return require("../assets/molecules/LemonJuice.png")
        case("9"):
          return require("../assets/molecules/Milk.png")
        case("10"):
          return require("../assets/molecules/PureWater.png")
        case("11"):
          return require("../assets/molecules/SparklingWater.png")
        default:
          return require("../assets/molecules/PureWater.png")
      }
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
    printContinueButton() {
      this.messages.push({ message: "Congrats, you won 10 points. Click to continue",
        bot: true,
        type: "button",
        src: require("../assets/uibuttons/ContinueButton.png"),
        func: "continue",
      });
    },
    printTryAgainButton() {
      this.messages.push({ message: "Do you want to give it another shot?",
        bot: true,
        type: "button",
        src: require("../assets/uibuttons/TryAgainButton.png"),
        func: "tryAgain",
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
.chat {
  margin: auto;
  display: flex;
  flex-direction: column;
  height: 90%;
  width: 95%;
  position: relative;
  z-index: 1;
  top: 2.5%;
  padding-top: 0.3vw;
  padding-bottom: 0.3vw;
  overflow-x: hidden;
  right: 1%;
  border-radius: 40px;
  border: 4px solid #ffa000;
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
  padding-top: 0.3vw;
  overflow-x: hidden;
  right: 0;
  border: 0 none;
  background: transparent;
}

.chat-title .textbar {
  flex: none;
}

.textbar {
  flex: none;
  bottom: 0;
  width: 100%;
  background-color: transparent;
  display: table;
  padding: 0.6vw;
}

.textbar .text {
  display: table-cell;
  width: 100%;
}

.message {
  text-align: left;
  background-repeat: no-repeat;
  display: block;
  margin-top: 0.2vw;
  padding-top: 0.2vw;
  margin-bottom: 0.2vw;
  padding-bottom: 0.6vw;
}

.user-message {
  padding-left: 2.5vw;
  padding-right: 2.25vw;
  background-image: url("../assets/icons/userchaticon.png");
  background-position-x: 95%;
  background-position-y: 15%;
  background-size: 1.5vw;
}

.user-message-box {
  color: #ffa000;
  border: 2px solid #ffa000;
  border-radius: 20px;
  padding: 0.3vw 0.6vw 0.3vw 0.6vw;
  width: 100%;
}

.bot-message {
  padding-left: 2.5vw;
  padding-right: 2.25vw;
  background-position-x: left;
  background-position-y: 15%;
  background-image: url("../assets/icons/botchaticon.png");
  background-size: 2vw;
}

.bot-message-box {
  color: #fff;
  background-color: #ffa000;
  border: 2px solid #ffa000;
  border-radius: 20px;
  padding: 0.3vw 0.6vw 0.3vw 0.6vw;
  width: 100%;
}

.message-box {
  flex: auto;
  margin-right: 1%;
  margin-left: 1%;
}

.form-style {
  margin: 0.3vw;
}

/*This division is ugly, we will get rid of it*/
.division {
  border-bottom: solid 5px #ffa000;
  border-radius: 1px;
  width: 90%;
  margin: 0 auto;
}

.btn-chat {
  position: relative;
  padding-bottom: 0.8vw;
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
  border: 3px solid #ffa000 !important;
  height: 40px;
  width: 90%;
  bottom: 100px !important;
  left: 5%;
  right: 5%;
  margin: 0.1vw;
  padding: 0.1vw;
  box-sizing: border-box;
}
</style>