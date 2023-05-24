<template>
  <div>
    <div class="backdropcontainer"
    :style="{ backgroundImage: `linear-gradient( rgba(255, 255, 255, 0.4), rgba(0, 0, 0, 0.8) ), url(https://image.tmdb.org/t/p/original${movie.backdrop_path})`}">


      <div v-if="movie">
        <p class="title">{{ movie.title }}</p>


        <div class="card" style="width:700px; margin:auto;">
          <div v-if="movie.video_key" class="card-img-top">
            <iframe id="player" width="700px" height="360px"
            :src="`https://www.youtube.com/embed/${movie.video_key}`"
            frameborder="0">
            </iframe>
          </div>

          <div class="card-img-top" v-else>
            <img :src="'https://image.tmdb.org/t/p/original'+ movie.backdrop_path" style="width:640px; height:auto;">
          </div>

          <div class="card-body">
            <div class="card-text">{{ movie.overview }}</div>
          </div>
        </div>

        <div v-if="ott_lst" class="ott-btn" style="margin-bottom:20px;">
          <span v-for="(ott, idx) in ott_lst" :key="idx" style="margin:5px;">
            <img :src="require(`@/assets/${ott}.png`)" style="width:70px; height:70px;">
          </span>
        </div>

        <!-- <button @click="userLikes(movie.id)">
          {{ likes ? '좋아요' : '좋아요  취소' }}
        </button> -->

        <button type="button" class="like btn btnEvent" @click="userLikes(movie.id)">
          <img v-if="likes" :src="require('@/assets/heart_after.png')" style="width: 35px; height: 35px;">
          <img v-else :src="require('@/assets/heart_before.png')" style="width: 35px; height: 35px;">
        </button>
        
        <p>{{ movie.likes_count }}</p>
        <MovieCommentCreate :movie="movie" v-if="movie"/>
      </div>
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

<style scoped>
.backdropcontainer {
  background-repeat: no-repeat;
  background-position: center top;
}
@font-face {
  font-family: 'MBC1961M';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-01@1.0/MBC1961M.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'LINESeedKR-Bd';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_11-01@1.0/LINESeedKR-Bd.woff2') format('woff2');
  font-weight: 700;
  font-style: normal;
}
p.title {
  padding-top: 20px;
  font-family: MBC1961M;
  font-size: 50px;
  text-shadow: 10px;
}
.ott-btn img {
  border-radius: 10px;
}
.card {
  background: transparent;
}
@font-face {
  font-family: 'Arita-buri-SemiBold';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/Arita-buri-SemiBold.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'ChosunCentennial';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2206-02@1.0/ChosunCentennial.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}
/* @font-face {
  font-family: 'Dokrip';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_twelve@1.1/Dokrip.woff') format('woff');
  font-weight: normal;
  font-style: normal;
} */
.card {
  border: transparent;
}
.card-text {
  color: white;
  font-size: 20px;
  font-family: ChosunCentennial;
}
.like:focus{ 	
  border: none;
  outline: none;
}
.like:hover {
  transition: 0.2s ease-out;
  opacity : 0.8;
}
.like:not(:hover) {
  transition: 0.2s ease-out;
}
/* @keyframes jello-horizontal {
0% {
  -webkit-transform: scale3d(1, 1, 1);
          transform: scale3d(1, 1, 1);
}
30% {
  -webkit-transform: scale3d(1.25, 0.75, 1);
          transform: scale3d(1.25, 0.75, 1);
}
40% {
  -webkit-transform: scale3d(0.75, 1.25, 1);
          transform: scale3d(0.75, 1.25, 1);
}
50% {
  -webkit-transform: scale3d(1.15, 0.85, 1);
          transform: scale3d(1.15, 0.85, 1);
}
65% {
  -webkit-transform: scale3d(0.95, 1.05, 1);
          transform: scale3d(0.95, 1.05, 1);
}
75% {
  -webkit-transform: scale3d(1.05, 0.95, 1);
          transform: scale3d(1.05, 0.95, 1);
}
100% {
  -webkit-transform: scale3d(1, 1, 1);
          transform: scale3d(1, 1, 1);
}
} */
</style>
