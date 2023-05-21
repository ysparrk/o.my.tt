<template>
  <div>
    <button v-for="ott in otts" :key="ott.id" @click="buttonClick(ott.initial)">{{ ott.name }}</button>

    <MovieListItem v-for="movie in pagedMovies" :key="movie.id" :movie="movie" />

    <div class="pagination">
      <button v-for="pageNumber in totalPages" :key="pageNumber" @click="goToPage(pageNumber)">
        {{ pageNumber }}
      </button>
    </div>

  </div>
</template>

<script>
import MovieListItem from '@/components/MovieList/MovieListItem'

import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'OttListButton',
  components: {
    MovieListItem,
  },
  computed: {
    otts() {
      return this.$store.state.otts
    },
    pagedMovies() {
      // 현재 페이지에 해당하는 데이터만 반환
      const startIndex = (this.currentPage - 1) * 20;
      const endIndex = startIndex + 20;
      return this.movies.slice(startIndex, endIndex);
    },
  },
  data() {
    return {
      movies: [],
      totalPages: 0,
      currentPage: 1,
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

        this.movies = res.data

        // totalPages 계산
        this.totalPages = Math.ceil(this.movies.length / 20);

        // currentPage 초기화
        this.currentPage = 1;
      })
      .catch((err) => {
        console.log(err)
      })
    },
    goToPage(pageNumber) {
      this.currentPage = pageNumber;
    },
  }
}
</script>

<style>

</style>
