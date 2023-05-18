<template>
  <div>
    <hr>
    <h5>tmdb_id : {{ prefer.tmdb_id }}</h5>
    
  </div>
</template>

<script>
export default {
  name: 'PreferMovieItem',
  props: {
    prefer: Object
  }

}
</script>

<style>

</style>