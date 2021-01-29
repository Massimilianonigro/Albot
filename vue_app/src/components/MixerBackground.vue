<template>
  <div class="image-container">
	<div class="background item">
		<div class="shelf item"></div>
		<div class="table-item item"></div>
		<div class="blender item"></div>
		<div class="basket item"></div>
		<div class="pan1 item"></div>
		<div class="pan2 item"></div>
	</div>
  </div>
</template>

<script>
export default {
  name: 'MixerBackground',
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
	height: 36%;
	width:  100%;
	z-index: 1;
	background-position-x: center;
	background-image: url("../assets/backgrounds/TableTopView.png");
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
	top: 39.5%;
	height: 10%;
	width:  100%;
	z-index: 2;
	background-position-y: bottom;
	background-position-x: 76%;
	background-image: url("../assets/backgrounds/Basket.png");
}
.pan1{
	top: 6.8%;
	left: 0%;
	height: 11.8%;
	width:  100%;
	z-index: 2;
	background-position-y: bottom;
	background-position-x: 67%;
	background-image: url("../assets/backgrounds/Pan1.png");
}
.pan2{
	top: 6.8%;
	left: 0;
	height: 11.8%;
	width:  100%;
	z-index: 2;
	background-position-y: bottom;
	background-position-x: 80%;
	background-image: url("../assets/backgrounds/Pan2.png");
}
.ImageContainer{
	border: 0;
	height: 100%;
	width: 80%;
}
</style>