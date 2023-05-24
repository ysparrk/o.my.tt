<template>
  <div>
  <p>Hi, {{ username }}. Enjoy your Flight.</p>
  <MovieList />
  </div>
</template>

<script>
import MovieList from '@/components/MovieList/MovieList'

export default {
  name: 'MovieView',
  components: {
    MovieList,
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
@import url('https://cdn.jsdelivr.net/font-iropke-batang/1.2/font-iropke-batang.css');

@font-face {
    font-family: 'KBO-Dia-Gothic_bold';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-2@1.0/KBO-Dia-Gothic_bold.woff') format('woff');
    font-weight: 700;
    font-style: normal;
}
</style>