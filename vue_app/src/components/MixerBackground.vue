<template>
  <div class="image-container">
	<div class="background item">
		<div class="shelf item"></div>
		<div class="ItemShelf">
			<div class="kitchen-item"
				v-for="(data, index) in items" 
				v-bind:key="index"
				v-bind:style="{
				backgroundImage: 'url(' + data.src + ')',
				left: data.size.x,
				bottom: data.size.y,
				height: data.size.h,
				width: data.size.w,
				}">
			</div>
		</div>
		<div class="table-item item"></div>
		<div class="blender item"></div>
		<div class="pan1 item"></div>
		<div class="pan2 item"></div>
	</div>
  </div>
</template>

<script>
export default {
  name: 'MixerBackground',
  props: {
    items: {
      type: Array,
      required: true,
    }
  },
};
</script>

<style scoped>
.kitchen-item {
	opacity: 0.7;
}

.kitchen-item:hover {
	opacity: 0.7;
	border: none;
}
.item{
	position: absolute;
	background-repeat: no-repeat;
	background-size: contain;
}
.table-item{
	bottom: 0;
	height: 36%;
	width:  100%;
	z-index: 1;
	background-position-x: center;
	background-position-y: bottom;
	background-image: url("../assets/backgrounds/TableTopView.png");
}
</style>