<template>
  <div class="image-container">
    <div class="pH-scale"
         v-if="this.isShowScale"
    >
      <div v-if="this.isShowItems">
      <div class="kitchen-item"
           v-for="(data, index) in substances"
           v-bind:key="index"
           v-bind:style="{
				backgroundImage: 'url(' + data.src + ')',
				left: data.scale_placement.x,
				bottom: data.scale_placement.y,
				height: data.scale_placement.h,
				width: data.scale_placement.w,
				}">
      </div>
      </div>
    </div>
    <div class="background item">
		<div class="shelf item"></div>
		<div class="ItemShelf"></div>
		<div class="table-item item"></div>
		<div class="blender item low-opacity"></div>
		<div class="pan1 item low-opacity"></div>
		<div class="pan2 item low-opacity"></div>
	</div>
  </div>
</template>

<script>
import {mapState} from "vuex";
export default {
  name: 'MixerBackground',
  props: {
    items: {
      type: Array,
      required: false,
    },
  },
  data(){
    return{
      isShowScale: true,
      isShowItems: true,
      isShowItem: [false, false, false]
    };
  },
  computed:{
    ...mapState(["substances"])
  }
};
</script>

<style scoped>
.kitchen-item, .low-opacity{
	opacity: 0.7;
}

.kitchen-item:hover {
	opacity: 0.7;
	border: none;
}
.item{
	position: absolute;
	background-repeat: no-repeat;
	background-size: contain;
}
.table-item{
	bottom: 0;
	height: 36%;
	width:  100%;
	z-index: 1;
	background-position-x: center;
	background-position-y: bottom;
	background-image: url("../assets/backgrounds/TableTopView.png");
}

.pH-scale{
  height: 100%;
  width:  15%;
  z-index: 1;
  padding: 0.7vw;
  background-position-x: center;
  background-position-y: center;
  background-repeat: no-repeat;
  background-size: contain;
  background-image: url("../assets/backgrounds/pHScale.png");
}
</style>