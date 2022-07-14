import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";
import Config from "../../envConfig";
import qs from "qs";
import jwtDecode from "jwt-decode";



Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    status: '',
    token: localStorage.getItem('token') || '',
    user: localStorage.getItem('user') || {},
    data: {},
    deals: localStorage.getItem('deals') || [],
  },
  mutations: {
    auth_request(state) {
      state.status = 'loading'
    },
    auth_success(state, token, user) {
      state.status = 'success'
      state.token = token
      state.user = user
    },
    auth_error(state) {
      state.status = 'error'
    },
    deals_loaded (state, deals) {
      state.deals = deals
    },
    clear_deals (state) {
      state.deals = []
    },
    logout(state) {
      state.status = ''
      state.token = ''
      state.user = {}
      state.data = {}
      state.deals = []

    },
  },
  actions: {
    async login({commit}, user) {
      commit('auth_request')
      await axios({
        url: `http://${Config.Config.VUE_APP_HOST}:${Config.Config.VUE_APP_PORT}/user/sign-in/`, data: qs.stringify(user), method: 'POST', headers: {
          'content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        }
      })
        .then(resp => {
          const token = resp.data.access_token
          user = jwtDecode(token).user
          localStorage.setItem('token', token)
          localStorage.setItem("user", user)
          axios.defaults.headers.common['Authorization'] = token
          commit('auth_success', token, user)
        })
        .catch(err => {
          commit('auth_error')
          localStorage.removeItem('token')
          localStorage.removeItem('user')
          console.log(err)
        })
    },
    async register({commit}, user) {
      commit('auth_request')
      await axios({
        url: `http://${Config.Config.VUE_APP_HOST}:${Config.Config.VUE_APP_PORT}/user/sign-up/`, data: user, method: 'POST', headers: {
          'content-type': 'application/json;charset=utf-8'
        }
      })
        .then(resp => {
          console.log(resp)
          const token = resp.data.access_token
          localStorage.setItem('token', token)
          user = jwtDecode(token).user
          axios.defaults.headers.common['Authorization'] = token
          commit('auth_success', token, user)
        })
        .catch(err => {
          commit('auth_error', err)
          localStorage.removeItem('token')
          localStorage.removeItem('user')
          console.log(err)
        })
    },
    logout({commit}) {
      return new Promise((resolve, reject) => {
        commit('logout')
        localStorage.removeItem('token')
        localStorage.removeItem('user')
        delete axios.defaults.headers.common['Authorization']
        resolve()
      })
    },
    async getDeals({commit}) {
      commit('clear_deals')
      await axios({
        url: `http://${Config.Config.VUE_APP_HOST}:${Config.Config.VUE_APP_PORT}/request/getOpenDeals`, method: 'GET'
      })
        .then(resp => {
          const deals = JSON.stringify(resp.data)
          localStorage.setItem('deals', deals)
          commit('deals_loaded', deals)
        })
        .catch(err => {
          localStorage.removeItem('deals')
          console.log(err)
        })
    },
  },
  getters: {
    isLoggedIn: state => !!state.token,
    authStatus: state => state.status,
    getUser: state => state.user,
    getDeals: state => JSON.parse(state.deals),
    isAdmin: state => {
      try {
        return JSON.parse(state.user)["is_superuser"] === true
      }
      catch (err) {
        console.log(err)
        return false
        }
      }
  }
})
