<template>
  <div class="window-border">
    <button v-on:click="close()" class="close">X</button>
    <div class="wip-content">
    </div>
  </div>
</template>

<script>

export default {
  name: "ReportWindow",
  props: {},
  data() {
    return {
      message: "",
    };
  },
  methods: {
    close(){
      this.$emit("close");
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.window-border {
  margin: auto;
  height: 70%;
  width: 58%;
  position: absolute;
  top: 12%;
  bottom: 18%;
  padding: 5px;
  left: 20%;
  right: 20%;
  overflow: visible;
  border-radius: 6px;
  border: 4px solid #ffa000;
  background-color: #ffffff;	
  z-index: 1000;
}
.close{
  opacity: 1;
  height: 40px;
  width: 40px;
  position: absolute;
  top: -4%;
  padding: 0;
  right: -4%;
  border-radius: 20px;
  color: #fff;
  border: 4px solid #e28f00;
  background-color: #ffa000;	
  z-index: 2;
}
.wip-content{
  position: absolute;
  width: 98%;
  height: 98%;
  background-size: contain;
  background-image: url("../assets/backgrounds/report.png");
  z-index: 1;
	background-repeat: no-repeat;
}
</style>