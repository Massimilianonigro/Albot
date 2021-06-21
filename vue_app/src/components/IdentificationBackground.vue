
<template>
  <div class="image-container">
    <ul class="pH-scale">
      <li class="pH-element"
          v-for="pH_button in 15"
          v-bind:key="pH_button" v-on:click="sendPHGuess(pH_button)">
        <button class="pH-button">
        </button>
      </li>
    </ul>
    <div class="bin item" v-bind:style="getBinPosition()"></div>
    <div class="background item" v-bind:style="getBackgroundPosition()">
      <div class="table-item item"></div>
    </div>
  </div>
</template>

<script>
import {mapState, mapActions} from "vuex";
export default {
  name: 'IdentificationBackground',
  props: {},
  computed: {
    ...mapState(["isChatless", "isThumbVisible", "thumbRotation", "isScaleClickable"])
  },
  methods: {
    ...mapActions(["setIsThumbVisible"]),
    sendPHGuess(index){
      if (this.isScaleClickable){
        this.$emit("PHGuess", index - 1);
        setTimeout(() => {
          this.setIsThumbVisible(false);
        }, 5000);
      }
    },
    getBinPosition(){
      if (this.isChatless){
        return {left: "87%"};
      }
      return { left: "12%"};
    },
    getBackgroundPosition(){
      if (!this.isChatless){
        return { margin: "auto auto auto 20%"};
      }
      return { margin: "auto auto auto 25%"};
    },
  }
};
</script>

<style scoped>

.item{
  position: absolute;
  background-repeat: no-repeat;
  background-size: contain;
}
.bin{
  background-image: url("../assets/backgrounds/bin.png");
  width: 20%;
  height: 20%;
  bottom: 0;
  display: inline;
}
.table-item{
  bottom: 0;
  height: 42%;
  width:  100%;
  z-index: 1;
  background-position-x: center;
  background-position-y: bottom;
  background-image: url("../assets/backgrounds/TableTopView.png");
}
.pH-scale{
  height: 100%;
  width:  15%;
  z-index: 10;
  background-position-x: center;
  background-position-y: center;
  background-repeat: no-repeat;
  background-size: contain;
  background-image: url("../assets/backgrounds/pHScale.png");
  list-style-type: none;
}
.pH-element{
  width: 70%;
  height: 6.65%;
}

.pH-button{
  width: 78%;
  height: 100%;
  border-style: none;
  border-color: transparent;
  color: transparent;
  background-color: transparent;
}

.pH-button:focus{
  outline: #ffffff solid 4px;
}

</style>