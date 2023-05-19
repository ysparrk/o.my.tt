<template>
  <div>
    <p>ott 추천 해드립니다</p>
    <p>아래의 내용에 따라 움직여주세요</p>
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