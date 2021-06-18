
<template>
  <div class="image-container">
	<div class="background item" v-bind:style="{margin: 'auto', left: '-10%'}">
		<div class="shelf item" v-bind:style="{left: '0'}"></div>
		<div class="pan1 item low-opacity"></div>
		<div class="pan2 item low-opacity"></div>
		<div class="blender item low-opacity"></div>
		<div class="table-item item" v-if="!isChatless"></div>
    <div class="table-item-chatless item" v-if="isChatless"></div>
  </div>
  </div>
</template>

<script>
import {mapState} from "vuex";

export default {
  name: 'PickerBackground',
  props: {},
  computed: {
    ...mapState(["isChatless"]),
  },
};
</script>

<style scoped>
.low-opacity{
	opacity: 0.5;
}
.table-item{
	bottom: 0;
	height: 38%;
	width:  100%;
	z-index: 1;
	background-position-x: center;
	background-position-y: bottom;
  left: 0;
  background-image: url('../assets/backgrounds/Table-a.png');
}
.table-item-chatless{
  bottom: 0;
  height: 38%;
  width:  100%;
  z-index: 1;
  background-position-x: center;
  background-position-y: bottom;
  left: 0;
  background-image: url('../assets/backgrounds/Table-a-Chatless.png');
}
</style>