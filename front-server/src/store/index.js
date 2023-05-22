import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'
// import { compileToFunctions } from 'vue-template-compiler'

const API_URL = 'http://127.0.0.1:8000'


Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    username: null,
    articles: [],
    movies: [],
    otts: null,
    selects: [],
    token: null,
    selectedId: [], // 선택된 movie.id
    finalRecommend: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
      console.log(this.movies)
      console.log("요청 받음")
    },
    GET_OTTS(state, otts) {
      state.otts = otts
      console.log(this.otts)
    },
    // recommend 관련
    GET_SELECT(state, selects) {
      state.selects = []  // 초기화 후 다시 저장
      state.selects = selects
      console.log(this.selects)
    },
    SAVE_SELECTED(state, selectId) {
      const index = state.selectedId.indexOf(selectId)
      console.log(index)
      if (index !== -1) {  // 이미 선택된 이미지
        state.selectedId.splice(index, 1)  
      } else {
        state.selectedId.push(selectId)
        console.log(this.selectedId)
      }

      console.log(this.selectedId)
    },
    FINAL_RECOMMEND(state, finalRecommend) {
      state.finalRecommend = finalRecommend
      state.selectedId = [] // 원래 선택된 배열 초기화
    },

    // login 관련
    SAVE_USERNAME(state, username) {
      state.username = username
      console.log(this.username)
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name : 'MovieView'}) // store/index.js $router 접근 불가 -> import를 해야함
    },
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/tmdb/initial/`,
      })
        .then((res) => {
          context.commit('GET_MOVIES', res.data)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    getOtts(context) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/ott/`,
      })
      .then((res) => {
        console.log(res)
        context.commit('GET_OTTS', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // recommend
    // 1) random 영화 가져오기
    getSelect(context) {
      axios({
        method: 'get',
        url: `${API_URL}/recommend/random/`,
      })
      .then((res) => {
        console.log(res)
        context.commit('GET_SELECT', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // 2) 선택한 영화 저장
    saveSelect(context, selectId) {
      console.log('함수 들어옴')
      console.log(selectId)
      context.commit('SAVE_SELECTED', selectId)
    },
    performSearch(context, searchQuery) {
      const query = encodeURIComponent(searchQuery)
      axios.get(`${API_URL}/movies/search/${query}/`)
        .then((res) => {
          context.commit('GET_SELECT', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    // 3) 선택한 영화 django로 보내기
    sendIds(context, selectedId) {
      const payload = selectedId
      axios({
        method: 'post',
        url: `${API_URL}/recommend/optimize_ott/`,
        data: {
          payload
        }
      })
      .then((res) => {
        console.log('response!!')
        console.log(res)
        context.commit('FINAL_RECOMMEND', res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // login 관련
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then((res) => {
          console.log(res)
          // context.commit('SIGN_UP', res.data.key)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    login(context, payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then((res) => {
        context.commit('SAVE_TOKEN', res.data.key)
        context.commit('SAVE_USERNAME', username)
        })
      .catch((err) => console.log(err))
    }
  },
  modules: {
  }
})
