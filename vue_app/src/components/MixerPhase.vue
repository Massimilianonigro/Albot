<template>
  <div>
    <div class="background">
      <div class="item-container" >
        <div v-for="(data, index) in items" v-bind:key="index">
          <button 
            class="kitchen-item"
            v-on:click="selectItem(index, data.ph)"
            v-bind:class="getHighlight(index)"
            v-bind:style="getItemStyle(data,index)"
          ></button>
          <div class="solution-bowl"
            v-if="!poured[index]"
            v-bind:style="{
              left: (index * 22 - 3 )+ '%',
              bottom: '-20%',
              height: '35%',
              width: '15%',
            }">
            </div>
            <div 
              v-if="poured[index]"
              :style="getPhBowl(data.ph, index)"
              class="solution-style"
            >
            </div>
        </div>
      </div>
      <!--div class="solution-ph-meter">
        <h3 class="solution-ph-meter-label"> {{selectedPh}} </h3>
      </div-->
      <button class="back-btn ui-btn" 
        v-on:click="backButton">
      </button>
      
      <button class="setting-btn ui-btn" 
        v-on:click="settingButton">
      </button>
      
      <button class="home-btn ui-btn" 
        v-on:click="settingButton">
      </button>
    </div>
    <button :style="{ width: '100px' }" class="btn btn-primary corner-4" 
      v-on:click="practiceButton">
      Practice!
    </button>
  </div>
</template>

<script>
export default {
  name: "MixerPhase",
  props: {
    items: {
      type: Array,
      required: true,
    }
  },
  data(){
    return {
      selected: undefined,
      selectedPh: "Select",
      poured: [false, false, false, false, false]
    }
  },
  methods:{
    selectItem(index, ph){
      if(this.selected == index){
        this.selected = undefined;
        this.selectedPh = "Select";
      }
      else{
        this.selected = index;
        this.selectedPh = ph+"";
      }
      if(!this.poured[index])
        this.poured[index] = true;
    },
    getHighlight(index){
      if(this.selected == index)
        return 'highlight';
      return 'nothighlight';
    },
    getItemStyle(data, index){
      let styleItem
      if (this.selected == index){
        styleItem = {
          backgroundImage: 'url(' + data.src + ')',
          left: ((index * 22) - 6)+ '%',
          width: data.size.w,
          zIndex: 20,
        }
      }
      else{
        styleItem = {
          backgroundImage: 'url(' + data.src + ')',
          left: (index * 22 )+ '%',
          width: data.size.w,
        }
      }
      return styleItem
    },
    getPhBowl(ph, index){
      let urlImg = require("../assets/solutions/Solution"+ Math.round(ph) +".png");
      let styleItem = {
        left: (index * 22 - 3)+ '%',
        bottom: '-20%',
        height: '35%',
        width: '15%',
        'background-image': 'url('+ urlImg +')',
      }
      return styleItem;
    },
    pourItem(index){
      this.poured[index] = true;
    },
    backButton(){
      while(this.items.length > 0) {
        this.items.pop();
      }
      this.$emit("backPress");
    },
    practiceButton(){
      this.$emit("practicePress");
    },
    settingButton(){
        this.$alert("Not implemented");
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.item-container {
  margin: auto;
  position: absolute;
  z-index: 1000;
  bottom: 28%;
  left: 0%;
  right: 0;
  width: 65%;
  height: 25%;
}

.nothighlight{
  top: 0%;
  height: 80%;
}
.kitchen-item:hover.nothighlight{
	opacity: 0.8;
	border-radius: 0;
  border: 0;
	border-style: none;
  border-color: transparent;
	background-color: #ffffff70;
	border-radius: 5px;
}
.highlight {
	color: #ffffff;
	border-radius: 5px;
	border: none;
	background-color: transparent;
	transform: rotate(115deg);
  top: 34%;
  height: 80%;
}
.kitchen-item:hover.highlight{
	opacity: 0.8;
	border-radius: 0;
	border: 0;
	border-style: none;
	border-color: transparent;
}

.solution-bowl{
  position: absolute;
	z-index: 2;
	background-position-y: bottom;
	background-position-x: center;
	background-repeat: no-repeat;
	background-size: contain;
	background-image: url("../assets/solutions/Solutionbowl.png");
}
.solution-style{
  position: absolute;
	z-index: 2;
	background-position-y: bottom;
	background-position-x: center;
	background-repeat: no-repeat;
	background-size: contain;
}
.solution-ph-meter{
  position: absolute;
	z-index: 2;
  left: 0%;
  right: 0%;
  bottom: 2%;
  width: 50%;
  height: 12%;
  margin: auto;
	background-position-y: bottom;
	background-position-x: center;
	background-repeat: no-repeat;
	background-size: contain;
	background-image: url("../assets/uibuttons/PHIndicator.png");
}
.solution-ph-meter-label{
  color: white;
	z-index: 3;
  margin: 11.5% auto auto auto;
  left: 0%;
  right: 0%;
  bottom: 0%;
  width: 15%;
  height: 50%;
  font-weight: 100;
}
ul {
  list-style-type: none;
  padding: 0;
  columns: 5;
  -webkit-columns: 5;
  -moz-columns: 5;
}
a {
  color: #42b983;
}
</style>
