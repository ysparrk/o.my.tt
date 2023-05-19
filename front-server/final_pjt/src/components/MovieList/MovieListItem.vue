<template>
  <div>
    <h5>{{ movie.id }}</h5>
    <p>{{ movie.tmdb_id }}</p>
    <p>{{ movie.ott_lst }}</p>
    <!-- <router-link :to="{
        name: 'DetailView',
        params: { id: movie.tmdb_id }}">
        [DETAIL]
    </router-link> -->
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