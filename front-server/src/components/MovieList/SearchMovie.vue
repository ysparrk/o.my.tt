<template>
  <div>
    <input class="search" type="text" v-model="searchQuery" @input="performSearch1" placeholder="검색어를 입력하세요" />
    <!-- <button @click="performSearch">검색</button> -->
    <div v-if="movies.length === 0 && searchQuery !== ''">검색결과가 없습니다</div>

    <!-- <div v-else>
      <MovieListItem v-for="(movie, idx) in movies" :key="idx" :movie="movie"/>
    </div> -->

  </div>
</template>

<script>
export default {
  name: 'SearchMovie',
  data() {
    return {
      searchQuery: '',
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
  },
  methods: {
    performSearch1() {
      this.$store.dispatch('performSearch1', this.searchQuery)
    }
  },
}
</script>

<style>

</style>
