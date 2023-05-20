<template>
  <div>
    <div v-if="movie">
    <img :src="'https://image.tmdb.org/t/p/w300' + movie.backdrop_path">
    <h2>{{ movie.title }}</h2>
    <p>{{ movie.overview }}</p>
    <button @click="userLikes(movie.id)">좋아요</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieDetail',
  props: [
    'movie',
  ],
  data() {
    return {
      likes: false,
    }
  },
  methods: {
    userLikes() {
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
        url: `${API_URL}/movies/likes/`,
        data: { likes },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
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