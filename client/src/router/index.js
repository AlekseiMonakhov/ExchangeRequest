import Vue from 'vue'
import Router from 'vue-router'
import App from "../App";
import Request from "../components/request";
import RequestsList from "../components/requestsList";
import adminPanel from "../components/adminPanel";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'App',
      component: App
    },
    {
      path: '/createRequest',
      name: 'Request',
      component: Request
    },
    {
      path: '/requestsList',
      name: 'RequestList',
      component: RequestsList
    },
    {
      path: '/adminPanel',
      name: 'AdminPanel',
      component: adminPanel
    },
  ]
});
