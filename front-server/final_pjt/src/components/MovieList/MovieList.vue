<template>
  <div class="movie-list">
    <h3>Movie List</h3>
    <!-- <MovieListItem
    v-for="movie in movies"
    :key="movie.id"
    :movie="movie"
    /> -->
    <MovieListItem />

  </div>
</template>

<script>
import MovieListItem from '@/components/MovieList/MovieListItem'

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  computed: {
    movies() {
      return this.$store.state.movies
    }
  },
  props: {
    movie: Object
  },
}
</script>

<style>
.movie-list {
  text-align: start;
}
</style>