<template>
  <div>
    <p>ott 버튼이 생길 예정</p>
    <button v-for = "ott in otts" 
    :key="ott.id"
    @click="buttonClick(ott.initial)">{{ ott.name }}</button>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'OttListButton',
  computed: {
    otts() {
      return this.$store.state.otts
    }
  },
  mounted() {
    this.$store.dispatch('getOtts')
  },
  methods: {
    buttonClick(ott_initial) {
      console.log(ott_initial)
      const name = ott_initial
      axios({
        method: 'get',
        url: `${API_URL}/movies/tmdb/${name}`,
      })
      .then((res) => {
        console.log('response!!')
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>