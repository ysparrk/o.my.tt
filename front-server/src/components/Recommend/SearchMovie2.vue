<template>
  <div>
    <input type="text" v-model="searchQuery" placeholder="검색어를 입력하세요" />
    <button @click="performSearch">검색</button>

    <div v-if="selects.length === 0">텅</div>
    

  </div>
</template>

<script>
export default {
  name: 'SearchMovie2',

  data() {
    return {
      searchQuery: '',
      is_search: false,
    }
  },
  computed: {
    selects() {
      return this.$store.state.selects
    },
  },
  methods: {
    performSearch() {
      this.$store.dispatch('performSearch', this.searchQuery)
      this.searchQuery = ''
    }
  },
}
</script>
