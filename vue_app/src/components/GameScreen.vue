<template>
  <div id="GameUI">
    <div class="GameUI" v-if="gameStatus == 1">
      <PickerBackground />
      <PickerPhase 
        ref="picker"
        v-bind:items="items" 
        v-on:sendNextInChat="displayNextButton"
        v-on:homePress="homeScreen"
        v-on:nextPress="mixItems" 
      />
    </div>
    <div class="GameUI" v-if="gameStatus == 2">
      <MixerBackground 
        v-bind:items="nonSelItems"/>
        
      <MixerPhase
        v-bind:items="selItems"
        v-bind:nsitems="nonSelItems"
        v-on:homePress="homeScreen"
        v-on:backPress="prevScreen"
        v-on:practicePress="nextScreen"
      />
    </div>
    <div class="GameUI" v-if="gameStatus == 3">
      <PickerBackground/>
      <PickerPracticePhase 
        ref="pracpicker"
        v-bind:items="items" 
        v-on:sendNextInPracticeChat="displayNextPracticeButton"
        v-on:nextPress="practiceMix"
        v-on:homePress="homeScreen"
      />
    </div>
    <div class="GameUI" v-if="gameStatus == 4">
      <PracticeBackground />
      <PracticePhase 
        v-bind:items="items" 
        v-on:homePress="homeScreen"
        v-on:backPress="prevScreen" 
      />
    </div>
  </div>
</template>

<script>
import PickerBackground from "./PickerBackground.vue";
import MixerBackground from "./MixerBackground.vue";
import PracticeBackground from "./PracticeBackground.vue";
import PickerPhase from "./PickerPhase.vue";
import MixerPhase from "./MixerPhase.vue";
import PickerPracticePhase from "./PickerPracticePhase.vue";
import PracticePhase from "./PracticePhase.vue";

export default {
  name: "GameScreen",
  components: {
    PickerBackground,
    MixerBackground,
    PracticeBackground,
    PickerPhase,
    MixerPhase,
    PickerPracticePhase,
    PracticePhase,
  },
  props: {
    gameType: {
      type: Number,
      required: true,
      },
  },
  data() {
    return {
      gameStatus: this.gameType,
      items: [
        {
          item: "Baking Soda",
          id: 1,
          selected: false,
          src: require("../assets/items/BakingSoda.png"),
          size: { x: "68%", y: "2%", w: "10%", h: "24%" },
          prsize: { x: "0%", y: "0%", w: "10%", h: "40%" },
          ph: 8,
        },
        {
          item: "Egg White",
          id: 2,
          selected: false,
          src: require("../assets/items/EggWhite.png"),
          size: { x: "84%", y: "2%", w: "9%", h: "30%" },
          prsize: { x: "8%", y: "42%", w: "7%", h: "50%" },
          ph: 9.2,
        },
        {
          item: "Vinegar",
          id: 3,
          selected: false,
          src: require("../assets/items/Vinegar.png"),
          size: { x: "53%", y: "2%", w: "7%", h: "34%" },
          prsize: { x: "22%", y: "42%", w: "7%", h: "60%" },
          ph: 3,
        },
        {
          item: "Bleach",
          id: 4,
          selected: false,
          src: require("../assets/items/Bleach.png"),
          size: { x: "85%", y: "36%", w: "10%", h: "24%" },
          prsize: { x: "60%", y: "0%", w: "10%", h: "42%" },
          ph: 12,
        },
        {
          item: "Oven Cleaner",
          id: 5,
          selected: false,
          src: require("../assets/items/OvenCleaner.png"),
          size: { x: "63%", y: "36%", w: "8.5%", h: "26%" },
          prsize: { x: "90%", y: "0%", w: "8%", h: "48%" },
          ph: 13,
        },
        {
          item: "Soap",
          id: 6,
          selected: false,
          src: require("../assets/items/Soap.png"),
          size: { x: "73%", y: "36%", w: "10%", h: "24%" },
          prsize: { x: "74%", y: "0%", w: "12%", h: "48%" },
          ph: 1,
        },
        {
          item: "Cola",
          id: 7,
          selected: false,
          src: require("../assets/items/Cola.png"),
          size: { x: "35%", y: "2%", w: "8%", h: "23%" },
          prsize: { x: "38%", y: "42%", w: "7%", h: "32%" },
          ph: 3,
        },
        {
          item: "Lemon Juice",
          id: 8,
          selected: false,
          src: require("../assets/items/LemonJuice.png"),
          size: { x: "27%", y: "2%", w: "8%", h: "30%" },
          prsize: { x: "65%", y: "43%", w: "7%", h: "45%" },
          ph: 2,
        },
        {
          item: "Milk",
          id: 9,
          selected: false,
          src: require("../assets/items/Milk.png"),
          size: { x: "43.5%", y: "2%", w: "8%", h: "33%" },
          prsize: { x: "50%", y: "42%", w: "8%", h: "55%" },
          ph: 6,
        },
        {
          item: "Pure Water",
          id: 10,
          selected: false,
          src: require("../assets/items/PureWater.png"),
          size: { x: "51%", y: "53%", w: "7%", h: "38%" },
          prsize: { x: "15%", y: "0%", w: "7%", h: "56%" },
          ph: 7,
        },
        {
          item: "Sparkling Water",
          id: 11,
          selected: false,
          src: require("../assets/items/SparklingWater.png"),
          size: {  x: "30%", y: "53%", w: "7%", h: "38%" },
          prsize: { x: "30%", y: "0%", w: "7%", h: "56%" },
          ph: 6,
        },
        {
          item: "Sparkling Water",
          id: 11,
          selected: false,
          src: require("../assets/items/SparklingWater.png"),
          size: {  x: "40.5%", y: "53%", w: "7%", h: "38%" },
          prsize: { x: "30%", y: "0%", w: "7%", h: "56%" },
          ph: 6,
        },
      ],
      selItems: [],
      nonSelItems: [],
      selItem: undefined,
    };
  },
  methods: {
    mixItems(selectedItems, nonSelectedItems) {
      this.selItems = [];
      this.nonSelItems = [];
      selectedItems.forEach((element) => {
        this.selItems.push(element);
      });
      nonSelectedItems.forEach((element) => {
        this.nonSelItems.push(element);
      });
      this.gameStatus += 1;
    },
    practiceMix(selectedItems) {
      this.selItems = [];
      selectedItems.forEach((element) => {
        this.selItems.push(element);
      });
      this.gameStatus += 1;
    },
    pourItem(selectedItem) {
      console.log(selectedItem);
      this.selItem = selectedItem;
      this.gameStatus += 1;
    },
    displayNextButton(){
      this.$emit("sendNextInChat");
    },
    displayNextPracticeButton(){
      this.$emit("sendPracNextInChat");
    },
    nextClicked(){
      if(this.gameStatus == 1)
        this.$refs.picker.updatePart()
    },
    nextPracticeClicked(){
      if(this.gameStatus == 3)
        this.$refs.pracpicker.nextClick()
    },
    nextScreen() {
      if(this.gameStatus == 2){ // Reset on Practise picking
        this.items.forEach(element => element.selected = false);
      }
      this.gameStatus += 1;
    },
    prevScreen() {
      this.items.forEach(element => element.selected = false);
      this.gameStatus -= 1;
    },
    homeScreen() {
      this.$emit("goHome");
    }
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.GameUI {
  height: 100%;
  width: 80%;
  position: fixed;
  z-index: 1;
  top: 0;
  bottom: 0;
  overflow-x: hidden;
  left: 0;
}
</style>
