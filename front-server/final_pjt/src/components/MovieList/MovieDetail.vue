<template>
  <div>
    <div v-if="movie">
    <img :src="'https://image.tmdb.org/t/p/w300' + movie.backdrop_path">
    <h2>{{ movie.title }}</h2>
    <p>{{ movie.overview }}</p>
    <button @click="userLikes(movie.id)">좋아요</button>
    <p>{{ movie.likes_count }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetail',
  data() {
    return {
      likes: false,
      movie: null,
    }
  },
  mounted() {
    this.getDetails()
  },
  methods: {
    getDetails() {
      const movieId = this.$route.params.id
      axios({
        method: 'get',
        url: `${API_URL}/movies/detail/${movieId}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        console.log('detail 요청함')
        console.log(res)
        this.movie = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    // 좋아요 누르기
    userLikes(movieId) {
      const likes = this.likes
      if (!likes) {
        this.likes = true
        console.log(likes)
      } else {
        this.likes = false
        console.log(likes)
      }
      axios({
        method: 'post',
        url: `${API_URL}/movies/${movieId}/likes/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        console.log('response!!')
        console.log(res)
        this.movie.likes_count = res.data.likes_count
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