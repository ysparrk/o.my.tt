<template>
  <div class="container" ref="container">

    <button type="button" variant="primary" class="m-2 btn btnEvent" v-for="(ott, idx) in otts" :key="idx" @click="buttonClick(ott.initial)">
      <img :src="require(`@/assets/${ott.initial}.png`)" style="width:70px; height:70px">
    </button>

    <p>
    <SearchMovie />
    <p>

    <!--영화 정보-->
    <div style="margin:auto;">
    <div v-for="(movie, idx) in movies" :key="'m'+idx">
      <MovieListItem :movie="movie" />
    </div>
    </div>

    <infinite-loading @infinite="infiniteHandler"></infinite-loading>
  
  </div>
</template>

<script>
// import OttListButton from '@/components/MovieList/OttListButton'
import MovieListItem from '@/components/MovieList/MovieListItem'
import SearchMovie from '@/components/MovieList/SearchMovie'
import InfiniteLoading from 'vue-infinite-loading'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieList',
  components: {
    SearchMovie,
    MovieListItem,
    // OttListButton,
    InfiniteLoading,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  computed: {
    otts() {
      return this.$store.state.otts
    },
    movies() {
      return this.$store.state.movies
    },
    visibleMovies() {
      return this.movies.slice(0, this.currentPage * 10)
    },
  },
  data() {
    return {
      // movies: [],
      totalPages: 0,
      currentPage: 1,
    }
  },
  // watch: {
  //   movies() {
  //     return this.$store.state.movies
  //   }
  // },
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

<style scoped>
.container {
  display: inline;
  /* max-height: 700px; */
  /* overflow-y: scroll; */
}
.btn {
  border: none;
}
.btn:focus {
	border: none;
	outline: none;
}
</style>
