
<template>
  <div class="image-container">
	<div class="background item">
		<div class="shelf item"></div>
		<div class="pan1 item low-opacity"></div>
		<div class="pan2 item low-opacity"></div>
		<div class="blender item low-opacity"></div>
		<div class="table-item item"></div>
	</div>
  </div>
</template>

<script>
export default {
  name: 'PickerBackground',
  props: {},
};
</script>

<style scoped>
.low-opacity{
	opacity: 0.5;
}
.table-item{
	bottom: 0;
	height: 38%;
	width:  100%;
	z-index: 1;
	background-position-x: center;
	background-position-y: bottom;
	background-image: url("../assets/backgrounds/Table-a.png");
}
</style>