<template>
  <div class="background">
    <div class="ItemShelf">
      <div style="margin:5px; z-index:1000" >
        <button
          v-for="(data, index) in items" 
          v-bind:key="index"
          class="kitchen-item"
          v-on:click="handleClickedItem(data)"
          v-bind:class="{
            highlight: data.selected,
            nothighlight: !data.selected,
            unclickable: getUnclickable(data.ph, data.selected),
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
    
    <button class="setting-btn ui-btn" 
      v-on:click="settingButton">
    </button>
    <SettingsWindow v-on:close="settingButton" v-if="settings"/>
    
    <button class="home-btn ui-btn" 
      v-on:click="homeButton">
    </button>
  </div>
</template>

<script>
import SettingsWindow from "./SettingsWindow.vue";
export default {
  components: {
    SettingsWindow,
  },
  name: "PickerPhase",
  props: {
    items: {
      type: Array,
      required: true,
    }
  },
  data() {
    return {
      part: "acid",
      selection: 0,
      settings: false,
    };
  },
  methods:{
    mixItems(){
      let selItems = []
      let nonSelItems = []
      this.items.forEach(element => {
        if( element.selected == true){
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
      else{
        selItems.forEach(element => {
          this.$emit("sendItemMessage", element.id)
        });
        this.$emit("nextPress", selItems, nonSelItems);
      }
    },
    changePart(){
      if (this.part == "acid" && this.selection == 2){
      this.$emit("sendNextInChat");
      }
      else if(this.part == "basic"  && this.selection == 4){
      this.$emit("sendNextInChat");
      }
      else if(this.part == "water"  && this.selection == 5){
      this.$emit("sendNextInChat");
      }
    },
    updatePart(){
      if (this.part == "acid" && this.selection == 2){
        this.part = "basic";
      }
      else if(this.part == "basic"  && this.selection == 4){
        this.part = "water";
      }
      else if(this.part == "water"  && this.selection == 5){
        this.mixItems()
      }
    },
    getUnclickable(ph, selected){
      if(selected && this.part != "acid" && ph < 7) {
        return true;
      }
      else if( selected && this.part != "basic" && ph > 7){
        return true;
      }
      return false;
    },
    getDisabled(data){
      if (data.selected){
        return false;
      }
      else if (this.part == "acid" && data.ph != 7){
        return data.ph > 7;
      }
      else if(this.part == "basic" && data.ph != 7){
        return data.ph < 7;
      }
      else if(this.part == "water" && data.ph == 7){
        return false;
      }
      return true;
    },
    handleClickedItem(data){
      data.selected = !data.selected
      if (data.selected) {
        this.selection += 1;
      }
      else{
        this.selection -= 1;
      }
      this.changePart();
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
