<template>
  <div>
    <div class="background"
         v-bind:style="{margin: 'auto', left: '-10%'}">
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
            }"
            v-bind:style="{
              backgroundImage: 'url(' + data.src + ')',
              left: data.size.x,
              bottom: data.size.y,
              height: data.size.h,
              width: data.size.w,
            }"
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
  </div>
</template>

<script>
import SettingsWindow from "./SettingsWindow.vue";
import {mapState} from "vuex";

export default {
  components: {
    SettingsWindow,
  },
  name: "PickerPractisePhase",
  props: {
    items: {
      type: Array,
      required: false,
    }
  },
  data() {
    return {
      selection: 0,
      selItems: [],
      settings: false,
    };
  },
  computed: {
    ...mapState(["substances"])
  },
  methods:{
    nextClick(){
      this.selItems = []
      
      this.substances.forEach(element => {
        if( element.selected === true){
          let tempItem = { 
            item: element.item,
            id: element.id,
            src: element.src,
            prsize: element.prsize,
            ph: element.ph,
          };
          this.selItems.push(tempItem);
        }
      });
      if (this.selection <= 1){
        this.$alert("Select more items!");
      }
      else{
        this.selItems.forEach(element => {
          this.$emit("sendItemMessage", element.id)
        });
        this.$emit("nextPress", this.selItems);
      }
    },
    handleClickedItem(data){
      data.selected = !data.selected
      if (data.selected) {
        this.selection += 1;
      }
      else{
        this.selection -= 1;
      }
      if (this.selection === 2){
        this.$emit("sendNextInPracticeChat");
      }
    },
    settingButton(){
      this.settings = !this.settings
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
