<template>
  <div>
    <p>선호하는 영화를 선택하세요</p>
    <PreferMovieItem 
    v-for="prefer in prefers"
    :key="prefer.id"
    :prefer="prefer"/>

  </div>
</template>

<script>
import PreferMovieItem from '@/components/PreferMovieItem'

export default {
  name: 'PreferMovie',
  components: {
    PreferMovieItem,
  },
  computed: {
    prefers() {
      return this.$store.state.prefers
    }
  }
}
</script>

<style>

</style>