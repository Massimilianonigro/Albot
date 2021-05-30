
<template>
  <div class="image-container">
    <div class="pH-scale">
    </div>
    <div class="bin item"></div>
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

.item{
	position: absolute;
	background-repeat: no-repeat;
	background-size: contain;
}
.bin{
  background-image: url("../assets/backgrounds/bin.png");
  width: 20%;
  height: 20%;
  bottom: 0;
  left: 15%;
  display: inline;
}
.table-item{
	bottom: 0;
	height: 42%;
	width:  100%;
	z-index: 1;
	background-position-x: center;
	background-position-y: bottom;
	background-image: url("../assets/backgrounds/TableTopView.png");
}

.pH-scale{
  height: 100%;
  width:  15%;
  z-index: 1;
  background-position-x: center;
  background-position-y: center;
  background-repeat: no-repeat;
  background-size: contain;
  background-image: url("../assets/backgrounds/pHScale.png");
  list-style-type: none;
}
</style>