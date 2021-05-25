<template>
  <div class="background">
    <div class="ItemShelf">
      <div style="margin:5px; z-index:1000" >
        <button
          v-for="(data, index) in substances"
          v-bind:key="index"
          class="kitchen-item"
          v-on:click="handleClickedItem(data)"
          v-bind:class="{
            highlight: data.selected,
            nothighlight: !data.selected,
            unclickable: getUnclickable(data.selected),
          }"
          v-bind:style="{
            backgroundImage: 'url(' + data.src + ')',
            left: data.size.x,
            bottom: data.size.y,
            height: data.size.h,
            width: data.size.w,
          }"
          v-bind:disabled="getDisabled(data)"
        >
          <div v-if="data.selected" class="selected-icon"></div>
        </button>
      </div>
    </div>

    <button class="home-btn ui-btn" 
      v-on:click="homeButton">
    </button>
  </div>
</template>

<script>
import {mapState} from "vuex";

export default {
  components: {
  },
  name: "PickerPhase",
  props: {
    items: {
      type: Array,
      required: false,
    }
  },
  data() {
    return {
      selection: 0,
      settings: false,
    };
  },
  computed: {
    ...mapState(["substances"])
  },
  methods:{
    mixItems(){
      let selItems = []
      let nonSelItems = []
      this.substances.forEach(element => {
        if( element.selected === true){
          let tempItem = { 
            item: element.item,
            size: element.size,
            src: element.src,
            id: element.id,
            ph: element.ph
          };
          selItems.push(tempItem);
        }
        else{
          nonSelItems.push(element);
        }
      });
      if (selItems.length > 5) {
        this.$alert("Too many items selected. (Max. 5)");
        console.error("Too many items selected");
      }
      else if (selItems.length <= 0){
        this.$alert("No items selected");
        console.error("No item selected");
      }
      else {
        selItems.forEach(element => {
          this.$emit("sendItemMessage", element.id)
        });
        this.$emit("nextPress", selItems, nonSelItems);
      }
    },
    endSelection(){
      if (this.selection === 3){
        this.$emit("selectionComplete");
        this.mixItems();
      }
    },
    getUnclickable(selected){
      if(selected) {
        return true;
      }
      return false;
    },
    getDisabled(data){
      if (data.selected){
        return false;
      }
    },
    handleClickedItem(data){
      if (!data.selected){
        data.selected = !data.selected;
        this.selection += 1;
      }
      this.endSelection();
    },
    settingButton(){
      this.settings = !this.settings;
    },
    homeButton() {
      this.$emit("homePress");
    },
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.selected-icon{
  pointer-events: none;
  top:-10%;
  left:-10%;
  height: 4vh;
  width: 4vh;
	position: absolute;
  z-index: 500;
  background-image: url('../assets/icons/SelectedIcon.png');
	background-size: contain;
	background-repeat: no-repeat;
	background-position: center;
}
a {
  color: #42b983;
}
</style>
