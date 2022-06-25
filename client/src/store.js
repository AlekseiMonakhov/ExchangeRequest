import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import qs from "qs"

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    status: '',
    token: localStorage.getItem('token') || '',
    user : {}
  },
  mutations: {
    auth_request(state){
      state.status = 'loading'
    },
    auth_success(state, token, user){
      state.status = 'success'
      state.token = token
      state.user = user
    },
    auth_error(state){
      state.status = 'error'
    },
    logout(state){
      state.status = ''
      state.token = ''

    },
  },
  actions: {
    async login({commit}, user){
        commit('auth_request')
        console.log(user)
        await axios({url: 'http://localhost:5000/user/sign-in/', data: qs.stringify(user), method: 'POST', headers: {
            'content-type': 'application/x-www-form-urlencoded;charset=utf-8'
          } })
          .then(resp => {
            const token = resp.data.access_token
            localStorage.setItem('token', token)
            axios.defaults.headers.common['Authorization'] = token
            commit('auth_success', token)

          })
          .catch(err => {
            commit('auth_error')
            localStorage.removeItem('token')
            console.log(err)
          })
    },
    async register({commit}, user){
        commit('auth_request')
        await axios({url: 'http://localhost:5000/user/sign-up/', data: qs.stringify(user), method: 'POST', headers: {
            'content-type': 'application/json;charset=utf-8'
          }  })
          .then(resp => {
            const token = resp.data.access_token
            localStorage.setItem('token', token)
            axios.defaults.headers.common['Authorization'] = token
            commit('auth_success', token)
          })
          .catch(err => {
            commit('auth_error', err)
            localStorage.removeItem('token')
            console.log(err)
          })
    },
    logout({commit}){
      return new Promise((resolve, reject) => {
        commit('logout')
        localStorage.removeItem('token')
        delete axios.defaults.headers.common['Authorization']
        resolve()
      })
    }
  },
    getters : {
      isLoggedIn: state => !!state.token,
      authStatus: state => state.status,
      isAdmin: state => state.user['is_superuser']
    }
})
