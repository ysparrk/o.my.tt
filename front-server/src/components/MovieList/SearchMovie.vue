<template>
  <div>
    <input type="text" v-model="searchQuery" placeholder="검색어를 입력하세요" />
    <button @click="performSearch">검색</button>

    <div v-if="movies.length === 0">텅</div>

    <div v-else>
      <MovieListItem v-for="movie in movies" :key="movie.id" :movie="movie"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieListItem from '@/components/MovieList/MovieListItem'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'SearchMovie',
  components: {
    MovieListItem,
  },
  data() {
    return {
      searchQuery: '',
      movies: [],
    };
  },
  methods: {
    performSearch() {
      const query = encodeURIComponent(this.searchQuery)
      axios.get(`${API_URL}/movies/search/${query}/`)
        .then((res) => {
          this.movies = res.data
        })
        .catch((err) => {
          console.log(err)
        });
    },
  },
};
</script>
