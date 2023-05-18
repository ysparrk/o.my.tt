<template>
  <div>
    <h1>Movie Detail</h1>
    <p>글 번호 : {{ movie?.id }}</p>
    <p>TMDB ID : {{ movie?.tmdb_id }}</p>
    <p>OTT : {{ movie?.ott_lst }}</p>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailView',
  data() {
    return {
      movie: null
    }
  },
  created() {
    this.getMovieDetail()
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/tmdb/${this.$route.params.id}/`,
      })
      .then((res) => {
        console.log('2')
        console.log(res)
        this.movie = res.data
      })
      .catch(err => {
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>