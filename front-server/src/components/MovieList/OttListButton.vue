<template>
  <div>
    <button v-for="ott in otts" :key="ott.id" @click="buttonClick(ott.initial)">{{ ott.name }}</button>
    <SearchMovie />
  <div class="container" ref="container">
  <button type="button" variant="primary" class="m-2 btn btnEvent" v-for="ott in otts" :key="ott.id" @click="buttonClick(ott.initial)">
    <img :src="require(`@/assets/${ott.initial}.png`)" style="width:50px; height:50px" alt="btnImages" class="btnImages">
  </button>

    <div v-for="movie in visibleMovies" :key="movie.id">
      <MovieListItem :movie="movie"/>
    </div>
  </div>
    <infinite-loading @infinite="infiniteHandler"></infinite-loading>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieList/MovieListItem'
import SearchMovie from '@/components/MovieList/SearchMovie'

import InfiniteLoading from 'vue-infinite-loading'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'OttListButton',
  components: {
    MovieListItem,
    SearchMovie,
    InfiniteLoading,
  },
  computed: {
    otts() {
      return this.$store.state.otts
    },
    visibleMovies() {
      return this.movies.slice(0, this.currentPage * 10)
    },
    movies() {
      return this.$store.state.movies
    },
  },
  data() {
    return {
      // movies: [],
      totalPages: 0,
      currentPage: 1,
    }
  },
  mounted() {
    this.$store.dispatch('getOtts')
    this.$refs.container.addEventListener('scroll', this.checkScroll)
  },
  beforeUnmount() {
    this.$refs.container.removeEventListener('scroll', this.checkScroll)
  },
  methods: {
    infiniteHandler($state) {
      const name = 'ott_initial'
      axios
        .get(`${API_URL}/movies/tmdb/${name}`, {
          params: {
            page: this.currentPage,
          },
        })
        .then(({ data }) => {
          if (data.length) {
            this.movies.push(...data)
            this.currentPage += 1
            $state.loaded()
          } else {
            $state.complete()
          }
        })
        .catch((err) => {
          console.log(err)
          $state.complete()
        })
    },
    buttonClick(input) {
      // const ott_initial = input
      this.$store.dispatch('buttonClick', input)
      this.totalPages = Math.ceil(this.movies.length / 10)
      this.currentPage = 1
    },
    // buttonClick(ott_initial) {
    //   const name = ott_initial
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/movies/tmdb/${name}`,
    //   })
    //     .then((res) => {
    //       this.movies = res.data
    //       this.totalPages = Math.ceil(this.movies.length / 10)
    //       this.currentPage = 1
    //     })
    //     .catch((err) => {
    //       console.log(err)
    //     })
    // },
    checkScroll() {
      const container = this.$refs.container
      if (container) {
        const scrollHeight = container.scrollHeight
        const scrollTop = container.scrollTop
        const clientHeight = container.clientHeight

        if (scrollTop + clientHeight >= scrollHeight) {
          this.loadMoreMovies()
        }
      }
    },
    loadMoreMovies() {
      const remainingMovies = this.movies.slice(this.visibleMovies.length, this.currentPage * 10)
      this.visibleMovies.push(...remainingMovies)
      this.currentPage++
    },
  },
}
</script>

<style>
.container {
  max-height: 700px;
  overflow-y: scroll;
}

.container::-webkit-scrollbar {
  width: 0.5em; /* 스크롤바 너비 */
}

.container::-webkit-scrollbar-track {
  background-color: #ffffff; /* 스크롤바 트랙 배경색 */
}

.container::-webkit-scrollbar-thumb {
  background-color: #ffffff; /* 스크롤바 색상 */
}

</style>
