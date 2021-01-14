
<template>
  <div class="image-container">
	<div class="background item">
		<div class="table-item item"></div>
	</div>
  </div>
</template>

<script>
export default {
  name: 'PracticeBackground',
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
	height: 42%;
	width:  100%;
	z-index: 1;
	background-position-x: center;
	background-image: url("../assets/backgrounds/TabletopView.png");
}
.ImageContainer{
	border: 0;
	height: 100%;
	width: 80%;
}
</style>