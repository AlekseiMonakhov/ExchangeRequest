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
import deals from "../components/deals";

Vue.use(Router)

let router = new Router({
  mode: "history",

  routes: [
    {
      path: '/',
      name: 'Создать заявку',
      component: Request,
    },
    {
      path: '/requestsList',
      name: 'Заявки',
      component: RequestsList,
    },
    {
      path: '/myDeals',
      name: 'Мои сделки',
      component: deals,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/adminPanel',
      name: 'Админпанель',
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
      name: 'Логин',
      component: Login
    },
    {
      path: '/register',
      name: 'Регистрация',
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
