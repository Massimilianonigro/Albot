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
  name: 'TableBackground',
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
	background-image: url("../assets/backgrounds/TabletopView.png");
}
.shelf{
	top: 1%;
	height: 45%;
	width:  100%;
	z-index: 1;
	background-position: center;
	background-image: url("../assets/backgrounds/Shelve.png");
}
.blender{
	top: 26.5%;
	height: 18%;
	width:  100%;
	z-index: 2;
	background-position-y: bottom;
	background-position-x: 22%;
	background-image: url("../assets/backgrounds/Blender.png");
}
.basket{
	top: 36.5%;
	height: 8%;
	width:  100%;
	z-index: 2;
	background-position-y: bottom;
	background-position-x: 72%;
	background-image: url("../assets/backgrounds/Basket.png");
}
.pan1{
	top: 5%;
	left: 0;
	height: 11.8%;
	width:  100%;
	z-index: 2;
	background-position-y: bottom;
	background-position-x: 65%;
	background-image: url("../assets/backgrounds/Pan1.png");
}
.pan2{
	top: 5%;
	left: 0;
	height: 11.8%;
	width:  100%;
	z-index: 2;
	background-position-y: bottom;
	background-position-x: 80%;
	background-image: url("../assets/backgrounds/Pan2.png");
}
.tap{
	bottom: 25%;
	height: 12%;
	width:  740px;
	z-index: 2;
	background-position-x: 12%;
	background-image: url("../assets/backgrounds/Tap.png");
}
.ImageContainer{
	border: 0;
	height: 100%;
	width: 80%;
}
</style>