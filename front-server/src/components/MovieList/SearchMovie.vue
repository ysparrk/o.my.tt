<template>
  <div>

    <input class="m-3" type="text" v-model="searchQuery"
    @input="performSearch1" placeholder="검색어를 입력하세요" />
    <div v-if="movies.length === 0 && searchQuery !== ''">
      검색결과가 없습니다
    </div>

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

<style scoped>
input {
  font-family: 'NanumSquareNeo-Variable';
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
