
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
	background-image: url("../assets/backgrounds/TableTopView.png");
}
.ImageContainer{
	border: 0;
	height: 100%;
	width: 80%;
}
</style>