<template>
  <div class="card">

    <router-link :to="{
      name: 'MovieDetail',
      params: { id: movie.id }}">
      <img :src="getMoviePoster(movie)" alt="Movie Poster">
    </router-link>
    <div class="title-box"></div>
    <div class="name">{{ movie.title }}</div> <!-- 영화 제목 표시 -->

  </div>
</template>
<script>

export default {
  name: 'MovieListItem',
  props: {
    movie: Object
  },
  methods: {
    getMoviePoster(movie) {
      if (movie.poster_path) {
        return 'https://image.tmdb.org/t/p/w300' + movie.poster_path
      }
    }
  }
}
</script>

<style scoped>
/* 고령딸기체 */
@font-face {
    font-family: 'GoryeongStrawberry';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-01@1.0/GoryeongStrawberry.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}
.card {
  margin: 10px;
  float: left;
  position: relative;
  background: linear-gradient(180deg, #ffffff 0%, #ffffff 100%);
  width: 13rem;
  overflow: hidden;
  box-shadow: 15px 15px 25px black;
  cursor: pointer;
}
.card img {
  display: inline-block;
  width: auto;
  height: 300px;
  overflow: hidden;
  object-fit: cover;
  transform: scale(1);
  transition: all 0.2s linear;
}
.card:hover img {
  opacity: 0.5;
  transform: scale(1.05);
  animation: flip-vertical-right 1s ease;
  animation-iteration-count: 2;
}
.card .title-box {
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
}
/* 고령딸기체 제목 */
.card .name {
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
}
.card:hover .name,
.card:hover .title-box {
  transform: translatey(0);
}

/* img {
  animation: flip-vertical-right 0.2s ease-in-out infinite;
} */

@keyframes flip-vertical-right {
  0% {
    -webkit-transform: rotateY(0);
            transform: rotateY(0);
  }
  100% {
    -webkit-transform: rotateY(180deg);
            transform: rotateY(180deg);
  }
}
</style>
