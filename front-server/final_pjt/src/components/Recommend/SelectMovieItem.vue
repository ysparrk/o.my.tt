<template>
  <div>
    <hr>
    <h5>tmdb_id : {{ select.tmdb_id }}</h5>
    
  </div>
</template>

<script>
export default {
  name: 'SelectMovieItem',
  props: {
    select: Object
  }

}
</script>

<style>

</style>