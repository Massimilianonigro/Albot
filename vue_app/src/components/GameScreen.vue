<template>
  <div id="GameUI">
    <div class="GameUI" v-if="gameStatus == 1">
      <PickerBackground />
      <PickerPhase 
        v-bind:items="items" 
        v-on:homePress="homeScreen"
        v-on:nextPress="mixItems" 
      />
    </div>
    <div class="GameUI" v-if="gameStatus == 2">
      <MixerBackground />
      <MixerPhase
        v-bind:items="selItems"
        v-on:homePress="homeScreen"
        v-on:backPress="prevScreen"
        v-on:practicePress="nextScreen"
      />
    </div>
    <div class="GameUI" v-if="gameStatus == 3">
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
import PracticePhase from "./PracticePhase.vue";

export default {
  name: "GameScreen",
  components: {
    PickerBackground,
    MixerBackground,
    PracticeBackground,
    PickerPhase,
    MixerPhase,
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
          selected: false,
          src: require("../assets/items/BakingSoda.png"),
          size: { x: "27%", y: "53.5%", w: "12%", h: "28%" },
          prsize: { x: "0%", y: "0%", w: "10%", h: "40%" },
          ph: 8,
        },
        {
          item: "Egg White",
          selected: false,
          src: require("../assets/items/EggWhite.png"),
          size: { x: "40%", y: "53.5%", w: "9%", h: "35%" },
          prsize: { x: "8%", y: "42%", w: "7%", h: "50%" },
          ph: 9.2,
        },
        {
          item: "Vinegar",
          selected: false,
          src: require("../assets/items/Vinegar.png"),
          size: { x: "51%", y: "53.5%", w: "9%", h: "44%" },
          prsize: { x: "22%", y: "42%", w: "7%", h: "60%" },
          ph: 3,
        },
        {
          item: "Bleach",
          selected: false,
          src: require("../assets/items/Bleach.png"),
          size: { x: "62%", y: "67%", w: "12%", h: "28%" },
          prsize: { x: "60%", y: "0%", w: "10%", h: "42%" },
          ph: 12,
        },
        {
          item: "Oven Cleaner",
          selected: false,
          src: require("../assets/items/OvenCleaner.png"),
          size: { x: "75%", y: "67%", w: "9%", h: "28%" },
          prsize: { x: "90%", y: "0%", w: "8%", h: "48%" },
          ph: 13,
        },
        {
          item: "Soap",
          selected: false,
          src: require("../assets/items/Soap.png"),
          size: { x: "85%", y: "67%", w: "12%", h: "28%" },
          prsize: { x: "74%", y: "0%", w: "12%", h: "48%" },
          ph: 1,
        },
        {
          item: "Cola",
          selected: false,
          src: require("../assets/items/Cola.png"),
          size: { x: "63%", y: "36%", w: "9%", h: "22%" },
          prsize: { x: "38%", y: "42%", w: "7%", h: "32%" },
          ph: 3,
        },
        {
          item: "Lemon Juice",
          selected: false,
          src: require("../assets/items/LemonJuice.png"),
          size: { x: "63%", y: "2%", w: "9%", h: "28%" },
          prsize: { x: "65%", y: "43%", w: "7%", h: "45%" },
          ph: 2,
        },
        {
          item: "Milk",
          selected: false,
          src: require("../assets/items/Milk.png"),
          size: { x: "30%", y: "2%", w: "9%", h: "38%" },
          prsize: { x: "50%", y: "42%", w: "8%", h: "55%" },
          ph: 6,
        },
        {
          item: "Pure Water",
          selected: false,
          src: require("../assets/items/PureWater.png"),
          size: { x: "40%", y: "2%", w: "9%", h: "34%" },
          prsize: { x: "15%", y: "0%", w: "7%", h: "56%" },
          ph: 7,
        },
        {
          item: "Sparkling Water",
          selected: false,
          src: require("../assets/items/SparklingWater.png"),
          size: { x: "50%", y: "2%", w: "9%", h: "34%" },
          prsize: { x: "30%", y: "0%", w: "7%", h: "56%" },
          ph: 6,
        },
      ],
      selItems: [],
      selItem: undefined,
    };
  },
  methods: {
    mixItems(selectedItems) {
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
    nextScreen() {
      this.gameStatus += 1;
    },
    prevScreen() {
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
