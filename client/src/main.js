import Vue from 'vue';
import App from './App';
import router from './router';
import Router from 'vue-router'
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
Vue.config.productionTip = false;

Vue.use(BootstrapVue)


new Vue({
  el: '#App',
  router,
  components: { App },
  template: '<App/>'
})


const routerPush = Router.prototype.push
Router.prototype.push = function push(location){
  return routerPush.call(this, location).catch(error => error)
}
