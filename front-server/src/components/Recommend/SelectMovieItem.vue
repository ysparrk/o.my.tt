<template>
  <div>
    <hr>
    <img :src="'https://image.tmdb.org/t/p/w300' + select.poster_path" @click="saveSelect(select.id)">

  </div>
</template>

<script>

export default {
  name: 'SelectMovieItem',
  props: {
    select: Object
  },

  methods: {
    saveSelect() {
      const selectId = this.select.id
      this.$store.dispatch('saveSelect', selectId)
    }
  },
  computed: {
    selectedId() {
      return this.$store.state.selectedId
    }
  }
}
</script>

<style>

</style>