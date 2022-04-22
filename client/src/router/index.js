import Vue from 'vue'
import Router from 'vue-router'
import Request from "../components/request";
import RequestsList from "../components/requestsList";
import AdminPanel from "../components/adminPanel";
import Chat from "../components/chat";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/createRequest',
      component: Request,
    },
    {
      path: '/requestsList',
      component: RequestsList,
    },
    {
      path: '/adminPanel',
      component: AdminPanel,
    },
    {
      path: '/chat',
      component: Chat,
    }
  ]
});
