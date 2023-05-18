<template>
  <div>
    <p>ott 추천 해드립니다</p>
    <p>아래의 내용에 따라 움직여주세요</p>
    <PreferMovie />
  </div>
</template>

<script>

import PreferMovie from '@/components/PreferMovie'

export default {
  name: 'RecommendView',
  components: {
    PreferMovie,
  },
  created() {
    this.getPrefer()
  },
  methods: {
    getPrefer() {
      this.$store.dispatch('getPrefer')
    }
  }
}
</script>

<style>

</style>