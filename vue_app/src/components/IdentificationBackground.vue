
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
    <div class="background item">
      <div class="table-item item"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'IdentificationBackground',
  props: {},
  methods: {
    sendPHGuess(index){
      this.$emit("PHGuess", index - 1);
    }
  }
};
</script>

<style scoped>

.item{
  position: absolute;
  background-repeat: no-repeat;
  background-size: contain;
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
.ImageContainer{
  border: 0;
  height: 100%;
  width: 80%;
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