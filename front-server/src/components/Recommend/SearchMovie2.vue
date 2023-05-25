<template>
  <div>

    <input class="m-3" type="text" v-model="searchQuery"
    @input="performSearch" placeholder="그 영화 뭐였지?" />

    <div v-if="selects.length === 0 && searchQuery !== ''">
      <img :src="require(`@/assets/empty.png`)" style="height:200px;">
    </div>

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
      // this.searchQuery = ''
    },
    searchToggle() {
      const container = this.$el.querySelector('.search-wrapper')
      if (!container.classList.contains('active')) {
        container.classList.add('active')
      } else {
        container.classList.remove('active')
        container.querySelector('.search-input').value = ''
      }
    }
  }
}
</script>

<style scoped>
body {
   background: #262433;
}
.main {
  background: rgba(255, 255, 255, 0.4);
  position: absolute;
  top: 20%;
  left: 30%;
  width: 40%;
  text-align: center;
  padding: 5px;
  border-radius: 3rem;
  box-shadow: 0px 0px 8px -5px #000000;
  padding-top: 3%;
  padding-bottom: 5%;
  font-family: "Poppins", sans-serif;
}
h1 {
  cursor: default;
  user-select: none;
}
input {
  font-family: 'NanumSquareNeo-Variable';
  border-radius: 3rem;
  border: none;
  padding: 10px;
  text-align: center;
  outline: none;
  margin: 10px;
  width: 400px;
  box-sizing: border-box;
  font-weight: 400;
}
input:hover {
  box-shadow: 0px 0px 8px -5px #000000;
}
input:active {
  box-shadow: 0px 0px 8px -5px #000000;
}
</style>