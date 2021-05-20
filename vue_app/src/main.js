import Vue from 'vue'
import App from './App.vue'
import 'jquery'
import 'popper.js'
import 'bootstrap'
import './assets/app.css'
import './assets/items.css'
import './assets/backgrounds.css'
import vuescroll from 'vuescroll';
import VueSimpleAlert from "vue-simple-alert";
import store from './store';


Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  store,
}).$mount('#app')

// You can set VueScroll global config here.
Vue.use(vuescroll)
// You can set Simple Alert global config here.
Vue.use(VueSimpleAlert);