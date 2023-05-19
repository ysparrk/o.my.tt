<template>
  <div>
    <p>선호하는 영화를 선택하세요</p>
    <SelectMovieItem 
    v-for="select in selects"
    :key="select.id"
    :select="select"/>

  </div>
</template>

<script>
import SelectMovieItem from '@/components/Recommend/SelectMovieItem'

export default {
  name: 'SelectMovie',
  components: {
    SelectMovieItem,
  },
  computed: {
    selects() {
      return this.$store.state.selects
    }
  }
}
</script>

<style>

</style>