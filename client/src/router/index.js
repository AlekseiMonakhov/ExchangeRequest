import Vue from 'vue'
import store from "../store/store"
import Router from 'vue-router'
import request from "../components/request";
import requestsList from "../components/requestsList";
import adminPanel from "../components/adminPanel";
import chat from "../components/chat";
import chatAdminView from "../components/chatAdminView";
import login from "../components/login";
import register from "../components/register";
import deals from "../components/deals";
import Error404 from "../components/404"

Vue.use(Router)

let router = new Router({
  mode: "history",

  routes: [
    {
      path: '/',
      name: 'Создать заявку',
      component: request,
    },
    {
      path: '/requestsList',
      name: 'Заявки',
      component: requestsList,
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
      component: adminPanel,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/chat',
      component: chat,
      name: 'chat',
      props: true,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/chatAdminView',
      component: chatAdminView,
      name: 'adminChat',
      props: true,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/login',
      name: 'Логин',
      component: login
    },
    {
      path: '/register',
      name: 'Регистрация',
      component: register
    },
    {
      path: '/*',
      name: '404',
      component: Error404
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
