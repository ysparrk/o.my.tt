<template>
  <div>
    <div v-if="movie">
      <p class="title">{{ movie.title }}</p>
      
      <div v-if="ott_lst" class="ott-btn">
        <span v-for="(ott, idx) in ott_lst" :key="idx" style="margin:5px;">
          <img :src="require(`@/assets/${ott}.png`)" style="width:70px; height:70px;">
        </span>
      </div>

      <div v-if="movie.video_key">
        <iframe id="player" width="640" height="360"
        :src="`https://www.youtube.com/embed/${movie.video_key}`"
        frameborder="0">
        </iframe>
      </div>

      <div v-else>
        <img :src="'https://image.tmdb.org/t/p/w300'+ movie.backdrop_path" style="width:640px; height:auto;">
      </div>

      <p>{{ movie.overview }}</p>


      <button @click="userLikes(movie.id)">{{ likes ? '좋아요' : '좋아요  취소' }}</button>
      <p>{{ movie.likes_count }}</p>
      <MovieCommentCreate :movie="movie" v-if="movie"/>

    </div>
  </div>

</template>

<script>
import MovieCommentCreate from '@/components/MovieList/MovieCommentCreate'

const API_URL = 'http://127.0.0.1:8000'

import axios from 'axios'

export default {
  name: 'MovieDetail',
  components: {
    MovieCommentCreate
  },
  data() {
    return {
      movie: null,
      likes: null,
      ott_lst: [],
    }
  },
  computed: {
    movieProp() {
      return this.$route.params.movie || this.movie
    },
  },
  created() {
    this.likes = JSON.parse(localStorage.getItem('likes')) || false
    },
  mounted() {
    this.getDetails()
    this.getOfferOtt()
  },
  methods: {
    getOfferOtt() {
      const movieId = this.$route.params.id
      axios({
        method: 'get',
        url: `${API_URL}/movies/detail/${movieId}/ott/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.otts = res.data
        this.ott_lst = this.otts.ott_lst
        console.log(this.ott_lst)
      })
      .catch((err) => {
        console.log(err)
      })
    },
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
        console.log(res)
        this.movie = res.data
        this.movie.video_key = res.data.video_key
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getLikes(movieId) {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${movieId}/likes/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
        .then((res) => {
          console.log(res)
          this.movie.likes_count = res.data.likes_count
        })
        .catch((err) => {
          console.log(err)
        })
      })
    },
    // 좋아요 누르기
    userLikes(movieId) {
      this.likes = !this.likes
      localStorage.setItem('likes', JSON.stringify(this.likes))

      axios({
        method: 'post',
        url: `${API_URL}/movies/${movieId}/likes/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
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
@font-face {
    font-family: 'MBC1961M';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-01@1.0/MBC1961M.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}
p.title {
  margin-top: 30px;
  font-family: MBC1961M;
  font-size: 40px;
  text-shadow: 10px;
}
/* .ott-btn img {
} */
</style>
