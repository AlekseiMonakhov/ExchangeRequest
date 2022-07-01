import Vue from 'vue'
import store from "../store/store"
import Router from 'vue-router'
import Request from "../components/request";
import RequestsList from "../components/requestsList";
import AdminPanel from "../components/adminPanel";
import DealChat from "../components/chat";
import ChatAdminView from "../components/chatAdminView";
import Login from "../components/login";
import Register from "../components/register";

Vue.use(Router)

let router = new Router({
  mode: "history",

  routes: [
    {
      path: '/',
      component: Request,
    },
    {
      path: '/requestsList',
      component: RequestsList,
    },
    {
      path: '/adminPanel',
      component: AdminPanel,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/chat',
      component: DealChat,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/chatAdminView',
      component: ChatAdminView,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    ],
});

router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isLoggedIn) {
      next()
      return
    }
    next('/login')
  } else {
    next()
  }
})

export default router
