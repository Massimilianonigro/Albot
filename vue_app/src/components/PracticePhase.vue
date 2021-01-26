<template>
  <div>
    <div class="background">
      <div class="solution-ph-meter">
        <h2 class="solution-ph-meter-label">8</h2>
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
    </div>
    <button
      :style="{ width: '100px' }"
      class="btn btn-primary corner-1"
      v-on:click="homeButton"
    >
      Home
    </button>
  </div>
</template>

<script>
export default {
  name: "PracticePhase",
  props: {
    items: {
      type: Array,
      required: true,
    },
  },
  methods: {
    homeButton() {
      this.$emit("homePress");
    },
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
  left: 20%;
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
  color: gray;
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
  left: 35%;
  top: 10%;
  width: 30%;
  height: 20%;
  margin: auto;
	background-position-y: bottom;
	background-position-x: center;
	background-repeat: no-repeat;
	background-size: contain;
	background-image: url("../assets/uibuttons/PHIndicator.png");
}
.solution-ph-meter-label{
  color: gray;
	z-index: 3;
  margin: 37.5% auto auto auto;
  left: 0%;
  right: 0%;
  bottom: 0%;
  width: 15%;
  height: 50%;
  font-weight: 100;
}
.item-container {
  margin: auto;
  position: absolute;
  z-index: 1000;
  bottom: 26%;
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
</style>
