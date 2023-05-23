<template>
  <div>

    <h3 class="m-3">당신을 위한 OTT를 찾아보세요</h3> 
    <SelectMovie />
    
  </div>
</template>

<script>
import SelectMovie from '@/components/Recommend/SelectMovie'

export default {
  name: 'RecommendView',
  components: {
    SelectMovie,
  },
  created() {
    this.getSelect()
  },
  methods: {
    getSelect() {
      this.$store.dispatch('getSelect')
    }
  }
}
</script>

<style>

</style>