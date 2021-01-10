<template>
  <div>
    <div class="background">
      <div class="item-container" >
        <div v-for="(data, index) in items" v-bind:key="index">
          <button 
            class="kitchen-item"
            v-on:click="selectItem(index, data.ph)"
            v-bind:class="getHighlight(index)"
            v-bind:style="{
              backgroundImage: 'url(' + data.src + ')',
              left: (index * 22 )+ '%',
              top: '0',
              height: '80%',
              width: data.size.w,
            }"
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
      <div class="solution-ph-meter">
        <h3 class="solution-ph-meter-label"> {{selectedPh}} </h3>
      </div>
    </div>
    <button :style="{ width: '100px' }" class="btn btn-primary corner-3" 
      v-on:click="backButton">
      Back
    </button>
    <button :style="{ width: '100px' }" class="btn btn-primary corner-4" 
      v-on:click="practiceButton">
      Practice!
    </button>
  </div>
</template>

<script>
export default {
  name: "Phase2",
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
    nextButton(){
      // TODO One itme must be selected
      if (this.selected == undefined){
        console.error("No item selected");
      }
      else{
        this.$emit("nextPress", this.items[this.selected]);
        /*
        var selItems = []
        this.items.forEach(element => {
          if( element.selected == true){
            let tempItem = { 
              item: element.item,
              size: element.size,
              src: element.src,
              ph: element.ph
            };
             selItems.push(tempItem);
          }
        });
        this.$emit("nextPress", selItems[0]);
        */
      }
    },
    practiceButton(){
      this.$alert("Not implemented yet.");
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.kitchen-item {
  position: absolute;
  z-index: inherit;
  background-size: contain;
  background-repeat: no-repeat;
  background-position-x: center;
  background-position-y: bottom;
}
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
  width: 100%;
  height: 12%;
	background-position-y: bottom;
	background-position-x: center;
	background-repeat: no-repeat;
	background-size: contain;
	background-image: url("../assets/uibuttons/PHIndicator.png");
}
.solution-ph-meter-label{
  color: white;
	z-index: 3;
  margin: 5.5% auto auto auto;
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
