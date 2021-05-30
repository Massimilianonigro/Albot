<template>
  <div class="image-container">
    <div class="scales-container">
      <div class="pH-scale-universal" :key = isRerender></div>
      <div class="pH-scale" :key = isRerender>
        <div v-for="(data, index) in substances"
             v-bind:key="index">
          <div v-show="showOnPHScale[index]"
               v-if="showOnPHScale[index]">
            <div
                class="kitchen-item"
                v-bind:style="{
				backgroundImage: 'url(' + data.src + ')',
				left: data.scale_placement.x,
				bottom: data.scale_placement.y,
				height: data.scale_placement.h,
				width: data.scale_placement.w,
				}">
            </div>
            <!--div class="item-arrow"
                 v-bind:style=getArrowStyle(data.scale_placement.y)
            >
            </div-->
          </div>
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
    isRerender: {
      type: Number,
      required: false,
    }
  },
  data(){
    return{
      scaleKey: 0
    };
  },
  computed:{
    ...mapState(["substances", "showOnPHScale"])
  },
  methods:{
    getShowElement(index){
      console.log(this.showOnPHScale[index]);
      return this.showOnPHScale[index];
    },
    forceRerender() {
      this.scaleKey += 1;
    },
    getArrowStyle(y){
      let y_position_elem = y.substring(0, y.length - 1);
      let y_position_arrow = parseInt(y_position_elem) + 2;

      return ({
        bottom: y_position_arrow + "%"
      })
    }
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
.item-arrow{
  left: 2%;
  position: absolute;
  background-image: url("../assets/icons/arrow.png");
  background-repeat: no-repeat;
  background-size: contain;
  height: 4%;
  width: 4%;
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
  display: inline;
  height: 100%;
  width: 25%;
  z-index: 1;
  padding: 0.7vw;
  margin-left: 1vw;
  background-position-x: 0;
  background-position-y: center;
  background-repeat: no-repeat;
  background-size: contain;
  position: relative;
  float: left;
  background-image: url("../assets/backgrounds/pHScale.png");
}

.pH-scale-universal{
  display: inline;
  height: 100%;
  width: 25%;
  z-index: 1;
  padding: 0.7vw;
  margin-left: 1vw;
  background-position-x: 0;
  background-position-y: center;
  background-repeat: no-repeat;
  background-size: contain;
  position: relative;
  float: left;
  background-image: url("../assets/backgrounds/pH-scale-universal.png");
}

.scales-container{
  height: 100%;
  width: 25%;
  margin: 0;
  padding: 0;
}

</style>