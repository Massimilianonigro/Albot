<template>
  <div>
    <div class="background">
      <div class="ItemShelf">
        <div style="margin:5px; z-index:1000" >
          <button
            v-for="(data, index) in items" 
            v-bind:key="index"
            class="kitchen-item"
            v-on:click="data.selected = !data.selected"
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
          ></button>
        </div>
      </div>
    </div>
    <button :style="{ width: '100px' }" class="btn btn-primary corner-4" 
      v-on:click="mixItems">
      Next
    </button>
  </div>
</template>

<script>
export default {
  name: "PickerPhase",
  props: {
    items: {
      type: Array,
      required: true,
    }
  },
  methods:{
    mixItems(){
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
      if (selItems.length > 5) {
        
        this.$alert("Too many items selected. (Max. 5)");
        console.error("Too many items selected");
      }
      else if (selItems.length <= 0){
        this.$alert("No items selected");
        console.error("No item selected");
      }
      else{
        this.$emit("nextPress", selItems);
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.ItemShelf {
  margin: 2% auto;
  left: 0;
  right: 0;
  height: 48%;
  width: 77%;
  z-index: 4;
  position: absolute;
  top: 0;
}
a {
  color: #42b983;
}
</style>
