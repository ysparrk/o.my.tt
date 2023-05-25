<template>
  <div class="container select_main" ref="container">

    <div v-if="finalRecommend">
      <h2>추천하는 OTT는 {{ finalRecommend.name }}</h2>
      <a v-bind:href="finalRecommend.signup">가입하기</a>
    </div>

    <div style="margin-bottom:10px">
    <button class="custom-btn btn-css" @click="getSelect"><div class="dot"></div>RANDOM</button>
    <button class="custom-btn btn-css" @click="sendIds"><span>제출하기</span></button>
    </div>
    <SearchMovie2 />
    <SelectMovieItem 
    v-for="select in selects"
    :key="select.id"
    :select="select"
    />

  </div>
</template>

<script>
import SearchMovie2 from '@/components/Recommend/SearchMovie2'
import SelectMovieItem from '@/components/Recommend/SelectMovieItem'

export default {
  name: 'SelectMovie',
  components: {
    SelectMovieItem,
    SearchMovie2,
  },
  computed: {
    selects() {
      return this.$store.state.selects
    },
    selectedId() {
      return this.$store.state.selectedId
    },
    finalRecommend() {
      return this.$store.state.finalRecommend
    }
  },
  methods: {
    getSelect() {
      this.$store.dispatch('getSelect')
    },
    sendIds() {
      this.$store.dispatch('sendIds', this.selectedId)
    },
  }
}
</script>

<style scoped>
button {
  margin: 20px;
}
.custom-btn {
  width: 130px;
  height: 40px;
  color: #fff;
  border-radius: 5px;
  padding: 10px 25px;
  font-family: 'Lato', sans-serif;
  font-weight: 500;
  background: transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  display: inline-block;
  box-shadow: inset 2px 2px 2px 0px rgba(255,255,255,.5),
  7px 7px 20px 0px rgba(0,0,0,.1),
  4px 4px 5px 0px rgba(0,0,0,.1);
  outline: none;
}
/* 11 */
.btn-css {
  border: none;
  background: rgb(251,33,117);
  background: linear-gradient(0deg, rgba(251,33,117,1) 0%, rgba(234,76,137,1) 100%);
  color: #fff;
  overflow: hidden;
}
.btn-css:hover {
  text-decoration: none;
  color: #fff;
}
.btn-css:before {
  position: absolute;
  content: '';
  display: inline-block;
  top: -180px;
  left: 0;
  width: 30px;
  height: 100%;
  background-color: #fff;
  animation: shiny-btn 3s ease-in-out infinite;
}
.btn-css:hover{
  opacity: .7;
}
.btn-css:active{
  box-shadow: 4px 4px 6px 0 rgba(255,255,255,.3),
  -4px -4px 6px 0 rgba(116, 125, 136, .2), 
  inset -4px -4px 6px 0 rgba(255,255,255,.2),
  inset 4px 4px 6px 0 rgba(0, 0, 0, .2);
}

.select_main {
  font-family: 'NanumSquareNeo-Variable';
  color: white;
}
/* @keyframes shiny-btn {
  0% { -webkit-transform: scale(0) rotate(45deg); opacity: 0; }
  80% { -webkit-transform: scale(0) rotate(45deg); opacity: 0.5; }
  81% { -webkit-transform: scale(4) rotate(45deg); opacity: 1; }
  100% { -webkit-transform: scale(50) rotate(45deg); opacity: 0; }
} */
</style>
