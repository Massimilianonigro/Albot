<template>
  <div id="GameUI">
    <div class="GameUI" v-if="gameStatus == 1">
      <ShelfBackground />
      <Phase1 
        v-bind:items="items" 
        v-on:nextPress="mixItems" 
      />
    </div>
    <div class="GameUI" v-if="gameStatus == 2">
      <TableBackground />
      <Phase2
        v-bind:items="selItems"
        v-on:nextPress="pourItem"
        v-on:backPress="prevScreen"
      />
    </div>
    <div class="GameUI" v-if="gameStatus == 3">
      <SolutionBackground />
      <Phase3 
        v-bind:item="selItem" 
        v-on:backPress="prevScreen" 
      />
    </div>
  </div>
</template>

<script>
import ShelfBackground from "./ShelfBackground.vue";
import TableBackground from "./TableBackground.vue";
import SolutionBackground from "./SolutionBackground.vue";
import Phase1 from "./Phase1.vue";
import Phase2 from "./Phase2.vue";
import Phase3 from "./Phase3.vue";

export default {
  name: "GameScreen",
  components: {
    ShelfBackground,
    TableBackground,
    SolutionBackground,
    Phase1,
    Phase2,
    Phase3,
  },
  props: {},
  data() {
    return {
      gameStatus: 1,
      items: [
        {
          item: "Baking Soda",
          selected: false,
          src: require("../assets/items/BakingSoda.png"),
          size: { x: "27%", y: "53.5%", w: "12%", h: "28%" },
          ph: 8,
        },
        {
          item: "Egg White",
          selected: false,
          src: require("../assets/items/EggWhite.png"),
          size: { x: "40%", y: "53.5%", w: "9%", h: "35%" },
          ph: 9.2,
        },
        {
          item: "Vinegar",
          selected: false,
          src: require("../assets/items/Vinegar.png"),
          size: { x: "51%", y: "53.5%", w: "9%", h: "44%" },
          ph: 3,
        },
        {
          item: "Bleach",
          selected: false,
          src: require("../assets/items/Bleach.png"),
          size: { x: "62%", y: "67%", w: "12%", h: "28%" },
          ph: 12,
        },
        {
          item: "Oven Cleaner",
          selected: false,
          src: require("../assets/items/OvenCleaner.png"),
          size: { x: "75%", y: "67%", w: "9%", h: "28%" },
          ph: 13,
        },
        {
          item: "Soap",
          selected: false,
          src: require("../assets/items/Soap.png"),
          size: { x: "85%", y: "67%", w: "12%", h: "28%" },
          ph: 1,
        },
        {
          item: "Cola",
          selected: false,
          src: require("../assets/items/Cola.png"),
          size: { x: "63%", y: "36%", w: "9%", h: "22%" },
          ph: 3,
        },
        {
          item: "Lemon Juice",
          selected: false,
          src: require("../assets/items/LemonJuice.png"),
          size: { x: "63%", y: "2%", w: "9%", h: "28%" },
          ph: 2,
        },
        {
          item: "Milk",
          selected: false,
          src: require("../assets/items/Milk.png"),
          size: { x: "30%", y: "2%", w: "9%", h: "38%" },
          ph: 6,
        },
        {
          item: "Pure Water",
          selected: false,
          src: require("../assets/items/PureWater.png"),
          size: { x: "40%", y: "2%", w: "9%", h: "34%" },
          ph: 7,
        },
        {
          item: "Sparkling Water",
          selected: false,
          src: require("../assets/items/SparklingWater.png"),
          size: { x: "50%", y: "2%", w: "9%", h: "34%" },
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
