<template>
  <div>
    <div class="background">
      <div class="solution-ph-meter">
        <h2 class="solution-ph-meter-label">06</h2>
      </div>
      <div class="scoreboard">
        <h3 class="scoreboard-label">8 Points</h3>
      </div>
      <div class="item-container">
        <div v-for="(data, index) in items" v-bind:key="index">
          <button
            class="kitchen-item"
            v-on:click="data.selected = !data.selected"
            v-bind:class="{
              highlight: data.selected,
              nothighlight: !data.selected,
            }"
            v-bind:style="{
              backgroundImage: 'url(' + data.src + ')',
              left: data.prsize.x,
              bottom: data.prsize.y,
              height: data.prsize.h,
              width: data.prsize.w,
            }"
          ></button>
        </div>
        <div class="solution"></div>
        
      </div>
      <button class="back-btn ui-btn" 
        v-on:click="backButton()">
      </button>
      
      <button class="setting-btn ui-btn" 
        v-on:click="settingButton()">
      </button>
      <SettingsWindow v-on:close="settingButton()" v-if="settings"/>
      
      <button class="home-btn ui-btn" 
        v-on:click="homeButton()">
      </button>
        
      <button class="reset-btn" 
        v-on:click="resetButton()">
      </button>
    </div>
  </div>
</template>

<script>
import SettingsWindow from "./SettingsWindow.vue";
export default {
  components: {
    SettingsWindow,
  },
  name: "PracticePhase",
  props: {
    items: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      settings: false,
    };
  },
  methods: {
    backButton(){
      while(this.items.length > 0) {
        this.items.pop();
      }
      this.$emit("backPress");
    },
    settingButton(){
      this.settings = !this.settings;
    },
    homeButton() {
      this.$emit("homePress");
    },
    resetButton(){
      this.$alert("A unexpected problem occured");
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.solution {
  position: absolute;
  bottom: 0;
  height: 40%;
  width: 14%;
  right: 43%;
  z-index: 2;
  background-position-y: bottom;
  background-position-x: center;
  background-repeat: no-repeat;
  background-size: contain;
  background-image: url("../assets/solutions/Solutionbowl.png");
}
.scoreboard{
  position: absolute;
	z-index: 2;
  left: 30%;
  top: 0%;
  width: 30%;
  height: 14%;
  margin: auto;
	background-position-y: center;
	background-position-x: center;
	background-repeat: no-repeat;
	background-size: contain;
	background-image: url("../assets/uibuttons/Scoreboard.png");
}
.scoreboard-label{
  position: absolute;
  color: #ffffff;
	z-index: 3;
  margin: auto auto auto auto;
  left: 16%;
  right: 0%;
  top: 28%;
  width: 80%;
  height: 40%;
  font-weight: 100;
}
.solution-ph-meter{
  position: absolute;
	z-index: 2;
  left: 30%;
  top: 20%;
  width: 40%;
  height: 20%;
  margin: auto;
	background-position-y: center;
	background-position-x: center;
	background-repeat: no-repeat;
  background-size: contain;
	background-image: url("../assets/uibuttons/PHMeterAcid.png");
}
.solution-ph-meter-label{
  color: gray;
	z-index: 3;
  margin: 14.5% auto auto auto;
  top: 0%;
  left: 0%;
  right: 0%;
  bottom: 0%;
  width: 15%;
  height: 50%;
  font-size: 4vh;
  font-weight: 100;
}
.item-container {
  margin: auto;
  position: absolute;
  z-index: 50;
  bottom: 22%;
  left: 0%;
  right: 0;
  width: 88%;
  height: 30%;
}
ul {
  list-style-type: none;
  padding: 0;
  columns: 5;
  -webkit-columns: 5;
  -moz-columns: 5;
}
a {
  color: #42b983;
}
.reset-btn{
	position: absolute;
	height: 14%;
	width: 30%;
	bottom: 9%;
	left: 35%;
	background-repeat: no-repeat;
	background-size: contain;
	background-color: transparent;
	background-position: center;
  border: 0px;
  border-radius: 40px;
	z-index: 1000;
	background-size: contain;
  background-image: url("../assets/uibuttons/ResetButton.png");
}

.ui-btn{
	position: absolute;
	height: 8%;
	width: 19%;
	background-repeat: no-repeat;
	background-size: contain;
	background-color: transparent;
	background-position: center;
	border: none;
	z-index: 1000;
}

.setting-btn {
	top: 3%;
	left: 3%;
}

.home-btn {
	top: 10%;
	left: 3%;
}

.back-btn {
	top: 17%;
	left: 3%;
}
</style>
