<template>
  <div>
    <input type="text" v-model="searchQuery" @input="performSearch1" placeholder="검색어를 입력하세요" />
    <!-- <button @click="performSearch">검색</button> -->
    <div v-if="movies.length === 0 && searchQuery !== ''">검색결과가 없습니다</div>

    <div v-else>
      <MovieListItem v-for="(movie, idx) in movies" :key="idx" :movie="movie"/>
    </div>

  </div>
</template>

<script>
// import axios from 'axios'
import MovieListItem from '@/components/MovieList/MovieListItem'

// const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'SearchMovie',
  components: {
    MovieListItem,
  },
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
    }
  },
}
</script>

<style>

.ripple-btn {
  width: 100px;
  height: 50px;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  position: relative;
  padding: 1em 1.5em;
  color: #fff;
  font-size: 1.15rem;
  border-radius: 100vmax;
  background-color: transparent;
  border: 2px solid #fff;
  text-transform: uppercase;
  overflow: hidden;
  cursor: pointer;
}
</style>