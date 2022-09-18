import Vue from 'vue';
import App from './App';
import router from './router';
import Router from 'vue-router'
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import store from './store/store'
import Axios from 'axios'
import Vuelidate from 'vuelidate'
import vuetify from '../src/plugins/vuetify'
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";

Vue.use(Toast, {
  transition: "Vue-Toastification__bounce",
  maxToasts: 20,
  newestOnTop: true
});

Vue.prototype.$MyToast = function(content, type) {
  this.$toast(content, {
    position: "top-right",
    type: type,
    timeout: 3048,
    closeOnClick: true,
    pauseOnFocusLoss: true,
    pauseOnHover: true,
    draggable: true,
    draggablePercent: 0.6,
    showCloseButtonOnHover: false,
    hideProgressBar: false,
    closeButton: "button",
    icon: true,
    rtl: false
  })
}

Vue.prototype.$http = Axios;
const token = localStorage.getItem('token')
if (token) {
  Vue.prototype.$http.defaults.headers.common['Authorization'] = token
}
Vue.config.productionTip = false;
Vue.use(BootstrapVue, Vuelidate)


new Vue({
  el: '#App',
  router,
  store,
  vuetify,
  components: { App },
  template: '<App/>'
})


const routerPush = Router.prototype.push
Router.prototype.push = function push(location){
  return routerPush.call(this, location).catch(error => error)
}
