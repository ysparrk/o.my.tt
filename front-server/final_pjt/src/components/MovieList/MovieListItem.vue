<template>
  <div>
    <router-link :to="{
      name: 'MovieDetail',
      params: { id: movie.id }}">
      <img :src="'https://image.tmdb.org/t/p/w300' + movie.poster_path">
    </router-link>
    <hr>
  </div>
</template>

<script>

export default {
  name: 'MovieListItem',
  props: {
    movie: Object
  },
}
</script>

<style>

</style>