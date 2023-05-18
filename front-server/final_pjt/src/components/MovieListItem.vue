<template>
  <div>
    <h5>{{ movie.id }}</h5>
    <p>{{ movie.tmdb_id }}</p>
    <p>{{ movie.ott_lst }}</p>
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