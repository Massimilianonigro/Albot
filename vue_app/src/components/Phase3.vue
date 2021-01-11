<template>
  <div>
    <div class="background">
      <div class="item-container">
        <div class="solution-text">
          <h1>Ph Level: {{item.ph}}, Acid</h1>
        </div>
        <div class="solution"></div>
      </div>
    </div>
    <button :style="{ width: '100px' }" class="btn btn-primary corner-3" 
      v-on:click="backButton">
      Back
    </button>
  </div>
</template>

<script>
export default {
  name: "Phase3",
  props: {
    item: {
      type: Object,
      required: true,
    }
  },
  methods:{
    backButton(){
      this.$emit("backPress");
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.solution{
	position: absolute;
	bottom: 0;
	height: 70%;
	width:  100%;
	z-index: 2;
	background-position-y: bottom;
	background-position-x: center;
	background-repeat: no-repeat;
	background-size: contain;
	background-image: url("../assets/solutions/Solutionbowl.png");
}
.solution-text{
	position: absolute;
  margin: auto;
	top: 0;
  right: 0;
  left: 0;
	height: 25%;
	width:  60%;
	z-index: 2;
  background-color: #ffffff6e;
  border-radius: 10px !important;
}
.highlight {
  color: #ffffff;
  background-color: #58a8eb;
}
.nothighlight {
  color: #000000;
  background-color: #ffffff00;
}
.kitchen-item {
  position: absolute;
  z-index: inherit;
  height: 100px;
  width: 100px;
  background-size: contain;
  background-repeat: no-repeat;
  background-position-x: center;
  background-position-y: bottom;
  border: 3px;
}
.item-container {
  margin: auto;
  position: absolute;
  z-index: 1000;
  bottom: 28%;
  left: 0%;
  right: 0;
  width: 65%;
  height: 25%;
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
