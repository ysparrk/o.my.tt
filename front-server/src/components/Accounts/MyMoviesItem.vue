<template>
  <div class="card">

    <router-link :to="{
      name: 'MovieDetail',
      params: { id: movie.id }}">
      <img :src="getMoviePoster(movie)" alt="Movie Poster">
    </router-link>
    <div class="title-box"></div>
    <!-- <div class="name">{{ movie.title }}</div> -->

  </div>
</template>

<script>
export default {
  name: 'MyMoviesItem',
  props: {
    movie: Object
  },
  methods: {
    getMoviePoster(movie) {
      if (movie.poster_path) {
        return 'https://image.tmdb.org/t/p/original' + movie.poster_path
      }
    }
  }
}
</script>

<style scoped>
.card {
  display: inline-block;
  margin-top: 30px;
  margin-bottom: 30px;
  margin-inline: -20px;
  /* margin: 20px; */
  background: linear-gradient(180deg, #212A3E 0%, #212A3E 100%);
  /* width: 13rem; */
  overflow: hidden;
  box-shadow: 15px 15px 25px black;
  cursor: pointer;
}
.card img {
  /* width: 13rem; */
  width: auto;
  height: 200px;
  overflow: hidden;
  object-fit: cover;
  transition: all 0.2s linear;
}
.card:hover {
  animation: slide-top 1s forwards;
}
.slide-top {
  -webkit-animation: slide-top 0.5s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
  animation: slide-top 0.5s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
}
@keyframes slide-top {
  0% {
    -webkit-transform: translateY(0);
    transform: translateY(0);
  }
  100% {
    -webkit-transform: translateY(-40px);
    transform: translateY(-40px);
  }
}






/* .card .title-box {
  content: "";
  height: 100px;
  position: absolute;
  transform: translatey(50px);
  transition: 0.3s ease;
  left: 0;
  bottom: 0;
  background: linear-gradient(to bottom, rgba(0, 0, 0, 0), black);
  width: 100%;
  z-index: 1;
} */
/* 고령딸기체 제목 */
/* .card .name {
  font-size: 15px;
  font-family: GoryeongStrawberry;
  position: absolute;
  width: 100%;
  bottom: 10px;
  color: #fff;
  transform: translatey(100px);
  padding: 10px;
  z-index: 10;
  transition: .3s ease;
  cursor: default;
} */
/* .card:hover .name,
.card:hover .title-box {
  transform: translatey(0);
} */
</style>