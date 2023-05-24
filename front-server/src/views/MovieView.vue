<template>
  <div>
  <p>Hi, {{ username }}. Enjoy your Flight.</p>
  <MovieList />
  </div>
</template>

<script>
import MovieList from '@/components/MovieList/MovieList'

export default {
  name: 'MovieView',
  components: {
    MovieList,
  },
  computed: {
    username() {
      return this.$store.state.username
    },
    isLogin(){
      return this.$store.getters.isLogin // 로그인 여부 -> true 또는 false
    }
  },
  created() {
    this.checkLogin()
  },
  update() {
    this.getMovies()
  },
  methods: {
    checkLogin() {
      if(this.isLogin){
        console.log(11333333)
      }
      else{
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({name:'LogInView'})
      }
    },
    getMovies() {
      this.$store.dispatch('getMovies')
    }
  }
}
</script>

<style>
@import url('https://cdn.jsdelivr.net/font-iropke-batang/1.2/font-iropke-batang.css');

@font-face {
    font-family: 'KBO-Dia-Gothic_bold';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-2@1.0/KBO-Dia-Gothic_bold.woff') format('woff');
    font-weight: 700;
    font-style: normal;
}
</style>