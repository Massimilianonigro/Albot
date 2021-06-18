<template>
  <div class="image-container">
    <div class="scales-container">
      <div
        class="pH-scale-universal"
        :key="isRerender"
        v-if="showPHScale[0]"
      ></div>
      <ul class="pH-scale nav" :key="isRerender" v-if="showPHScale[1]">
          <li
            class="buttons"
            v-for="pH_button in 15"
            v-bind:key="pH_button"
            v-on:click="sendPHGuess(pH_button)"
          >
            <button class="button-ph"></button>
          </li>
        <div v-for="(data, index) in substances" v-bind:key="index">
          <div v-show="showOnPHScale[index]" v-if="showOnPHScale[index]">
            <div
              class="kitchen-item"
              v-bind:style="{
                backgroundImage: 'url(' + data.src + ')',
                left: data.scale_placement.x,
                bottom: data.scale_placement.y,
                height: data.scale_placement.h,
                width: data.scale_placement.w,
                opacity: '1',
                zIndex: 100,
              }"
            ></div>
          </div>
        </div>
      </ul>
    </div>
    <div :key="isRerender">
      <div v-for="(data, index) in substances" v-bind:key="index">
        <div v-show="showOnPHScale[index]" v-if="showOnPHScale[index]">
          <div
            class="item-circle"
            v-bind:style="getCircleStyle(data)"
          ></div>
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
    <div class="thumbUp" v-if="thumbRotation" ></div>
    <div class="thumbDown" v-if="!thumbRotation" ></div>

  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "MixerBackground",
  props: {
    items: {
      type: Array,
      required: false,
    },
    isRerender: {
      type: Number,
      required: false,
    },
  },
  data() {
    return {
      scaleKey: 0,
    };
  },
  computed: {
    ...mapState(["substances", "showOnPHScale", "showPHScale", "thumbRotation"]),
  },
  methods: {
    sendPHGuess(index) {
      this.$emit("PHGuess", index - 1);
    },
    getThumbRotation(){
      const rotation = "rotate(" + this.thumbRotation + ")";
      return ({
        "transform": rotation
      });
    },
    getCircleStyle(data) {
      return {
        bottom: data.circle_y_placement,
        left: "2.5%",
        height: "7%",
        width: "20%",
        zIndex: "5",
      };
    },
  },
};
</script>

<style scoped>
.kitchen-item,
.low-opacity {
  opacity: 0.7;
}

.kitchen-item:hover {
  opacity: 0.7;
  border: none;
}
.item {
  position: absolute;
  background-repeat: no-repeat;
  background-size: contain;
}
.item-circle {
  position: absolute;
  background-image: url("../assets/icons/circle.png");
  background-repeat: no-repeat;
  background-size: contain;
}
.table-item {
  bottom: 0;
  height: 36%;
  width: 100%;
  z-index: 1;
  background-position-x: center;
  background-position-y: bottom;
  background-image: url("../assets/backgrounds/TableTopView.png");
}

.pH-scale {
  display: inline;
  height: 100%;
  width: 25%;
  z-index: 1;
  left:20%;
  background-position-x: 0;
  background-position-y: center;
  background-repeat: no-repeat;
  background-size: contain;
  position: relative;
  float: left;
  background-image: url("../assets/backgrounds/pHScale.png");
}

.pH-scale-universal {
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

.scales-container {
  height: 100%;
  width: 25%;
  margin: 0;
  padding: 0;
}

.nav {
  margin: 0;
  height: 100%;
  width: 50%;
  display: flex;
  flex-direction: column;
  flex-wrap: nowrap;
  cursor: pointer;
  /*list-style-type: none;*/
}

.nav:hover{
  cursor: pointer;

}

.buttons {
  width: 46%;
  height: 100%;
  border-style: none;
  border-color: transparent;
  color: transparent;
  background-color: transparent;
  display: flex;
  flex-grow: 1;
}
.buttons:focus{
  outline: #ffffff solid 4px;
}

/*optional*/
.nav li:last-child {
  border-right: none;
}

.button-ph {
  display: none;
}

.thumbUp{
  width: 20%;
  position: absolute;
  height: 30%;
  top: 10%;
  right: 30%;
  border-style: none;
  border-color: transparent;
  color: transparent;
  background-color: transparent;
  background-image: url("../assets/uibuttons/Thumb.png");
  background-position-x: center;
  background-position-y: center;
  background-size: contain;
  transform: rotate(0deg);
}

.thumbDown{
  width: 20%;
  position: absolute;
  height: 30%;
  top: 10%;
  right: 30%;
  border-style: none;
  border-color: transparent;
  color: transparent;
  background-color: transparent;
  background-image: url("../assets/uibuttons/Thumb.png");
  background-position-x: center;
  background-position-y: center;
  background-size: contain;
  transform: rotate(180deg);
}

.white-block {
  position: absolute;
  background-color: #ffffffb0;
  z-index: 105;
  height: 100%;
  width: 100%;
}
</style>