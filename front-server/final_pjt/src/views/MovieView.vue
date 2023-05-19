<template>
  <div>
  <h1>오늘 영화 어때요?</h1>
  <OttListButton />
  <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList/MovieList.vue'
import OttListButton from '@/components/MovieList/OttListButton.vue'

export default {
  name: 'MovieView',
  components: {
    MovieList,
    OttListButton,
  },
  update() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    }
  }
}
</script>

<style>

</style>