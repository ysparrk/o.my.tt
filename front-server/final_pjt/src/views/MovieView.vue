<template>
  <div>
  <p>{{ username }} 입니다</p>
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
  computed: {
    username() {
      return this.$store.state.username
    }
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