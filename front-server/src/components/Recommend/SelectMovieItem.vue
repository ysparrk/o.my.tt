<template>
  <div>
    <hr>
    <h5>{{ select.title }}</h5>
    <img :src="'https://image.tmdb.org/t/p/w300' + select.poster_path" @click="itemToList(select.id)">

  </div>
</template>

<script>

export default {
  name: 'SelectMovieItem',
  props: {
    select: Object
  },
  data() {
    return {
      selectedId: []
    }
  },
  methods: {
    itemToList: function() {
      console.log('함수 들어옴')
      console.log(this.select.id)
      this.$emit('item-to-list', this.select.id)
    }
  }
}
</script>

<style>

</style>