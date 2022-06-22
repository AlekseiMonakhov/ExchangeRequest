import Vue from 'vue'
import store from "../store"
import Router from 'vue-router'
import Request from "../components/request";
import RequestsList from "../components/requestsList";
import AdminPanel from "../components/adminPanel";
import DealChat from "../components/chat";
import ChatAdminView from "../components/chatAdminView";
import Login from "../components/login";
import Register from "../components/register";
import Secure from "../components/secure";

Vue.use(Router)

let router = new Router({
  mode: "history",

  routes: [
    {
      path: '/',
      component: Request,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/requestsList',
      component: RequestsList,
      meta: {
        requiresAuth: true
      }
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
    {
      path: '/secure',
      name: 'secure',
      component: Secure,
      meta: {
        requiresAuth: true
      }
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
