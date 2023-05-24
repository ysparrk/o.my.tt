<template>
  <div>

    <h3 class="m-3">당신을 위한 OTT를 찾아보세요</h3> 
    <SelectMovie />
    
  </div>
</template>

<script>
import SelectMovie from '@/components/Recommend/SelectMovie'

export default {
  name: 'RecommendView',
  components: {
    SelectMovie,
  },
  computed: {
    isLogin(){
      return this.$store.getters.isLogin // 로그인 여부 -> true 또는 false
    }
  },
  created() {
    this.checkLogin()
    this.getSelect()
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
    getSelect() {
      this.$store.dispatch('getSelect')
    }
  }
}
</script>

<style>

</style>