<template>
  <div>
    <router-link :to="{
      name: 'MovieDetail',
      params: { id: movie.id }}">
      <img :src="getMoviePoster(movie)" alt="Movie Poster">
    </router-link>
    <p>{{ movie.title }}</p> <!-- 영화 제목 표시 -->
    <hr>
  </div>
</template>
<script>

export default {
  name: 'MovieListItem',
  props: {
    movie: Object
  },
  methods: {
    getMoviePoster(movie) {
      if (movie.poster_path) {
        return 'https://image.tmdb.org/t/p/w300' + movie.poster_path
      }
    }
  }
}
</script>

<style>

</style>
