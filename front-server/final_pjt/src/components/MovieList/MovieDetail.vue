<template>
  <div>
    <div v-if="movie">
    <img :src="'https://image.tmdb.org/t/p/w300' + movie.backdrop_path">
    <h2>{{ movie.title }}</h2>
    <p>{{ movie.overview }}</p>
    <button>좋아요</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieDetail',
  props: [
    'movie',
  ]
}
</script>

<style>

</style>