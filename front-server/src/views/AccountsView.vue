<template>
  <div>
    <div class="text">{{ username }}님의 마이페이지</div>
    <MyPage />
    <div class="m-5"></div>
  </div>
</template>

<script>
import MyPage from '@/components/Accounts/MyPage'

export default {
  name: 'AccountsView',
  components: {
    MyPage
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    username() {
      return this.$store.state.username
    }
  },
  created() {
    this.checkLogin()
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

<style scoped>
.text {
  font-size: 50px;
  font-family: NanumSquareNeo-Variable;
  color: white;
  margin-top: 50px;
}
</style>