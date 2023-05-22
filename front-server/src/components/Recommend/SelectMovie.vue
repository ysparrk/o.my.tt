<template>
  <div>
    <p>선호하는 영화를 선택하세요</p>
    <button @click="sendIds">제출하기</button>

    <div v-if="finalRecommend">
      <h2>추천하는 Ott는 : {{ finalRecommend.name }}</h2>
      
      <a v-bind:href="finalRecommend.signup">가입하기</a>
    </div>

    <button @click="getSelect">랜덤</button>

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
    }
  }
}
</script>

<style>

</style>