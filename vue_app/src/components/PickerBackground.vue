
<template>
  <div class="image-container">
	<div class="background item">
		<div class="shelf item"></div>
		<div class="blender item"></div>
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
.background{
	position: absolute;
	top: 0; bottom: 0; left: 0; right: 0;
	margin: auto;
	z-index: 0;
	width: 100vw;
	height: 75vw;
	max-width: 133.3vh;
	max-height: 100vh;
	background-position: center;
	background-size: contain;
	/*background-image: url("../assets/backgrounds/OrangeBG.png");*/
}
.item{
	position: absolute;
	background-repeat: no-repeat;
	background-size: contain;
}
.table-item{
	bottom: 0;
	height: 38%;
	width:  100%;
	z-index: 1;
	background-position-x: center;
	background-image: url("../assets/backgrounds/Table-a.png");
}
.shelf{
	top: 1%;
	height: 50%;
	width:  100%;
	z-index: 0;
	background-position-x: center;
	background-image: url("../assets/backgrounds/Shelve.png");
}
.blender{
	top: 31.5%;
	height: 18%;
	width:  100%;
	z-index: 2;
	background-position-y: bottom;
	background-position-x: 20%;
	background-image: url("../assets/backgrounds/Blender.png");
}
.basket{
	bottom: 23%;
	left: 0;
	height: 8%;
	width:  100%;
	z-index: 2;
	background-position-y: bottom;
	background-position-x: 71%;
	background-image: url("../assets/backgrounds/Basket.png");
}
.cabbage{
	bottom: 23%;
	height: 8%;
	width:  100%;
	z-index: 2;
	background-position-x: 75%;
	background-image: url("../assets/items/Cabbage.png");
}
.tap{
	bottom: 25%;
	height: 12%;
	width:  100%;
	z-index: 2;
	background-position-x: 18%;
	background-image: url("../assets/backgrounds/Tap.png");
}
</style>