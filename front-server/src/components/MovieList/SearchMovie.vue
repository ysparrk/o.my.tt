<template>
  <div>
    <input type="text" v-model="searchQuery" @input="performSearch1" placeholder="검색어를 입력하세요" />

    <div v-if="movies.length === 0">텅</div>

    <!-- <div v-else>
      <MovieListItem v-for="movie in movies" :key="movie.id" :movie="movie"/>
    </div> -->
  </div>
</template>

<script>
// import axios from 'axios'
// import MovieListItem from '@/components/MovieList/MovieListItem'

// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'SearchMovie',
  data() {
    return {
      searchQuery: '',
      // movies: [],
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
  },
  methods: {
    performSearch1() {
      this.$store.dispatch('performSearch1', this.searchQuery)
      // this.searchQuery = ''
    }
  },
  // methods: {
  //   performSearch() {
  //     const query = encodeURIComponent(this.searchQuery)
  //     axios.get(`${API_URL}/movies/search/${query}/`)
  //       .then((res) => {
  //         this.movies = res.data
  //       })
  //       .catch((err) => {
  //         console.log(err)
  //       })
  //   },
  // },
}
</script>
