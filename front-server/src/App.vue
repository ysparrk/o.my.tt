<template>
  <div id="app">
    <router-link v-if="isLogin" :to="{ name: 'MovieView', params: { id: $store.state.user } }" class="login-button"></router-link> 
    <!-- <router-link v-else to="/signup" class="login-button">Sign Up</router-link> -->
    <!-- <router-link v-if="!isLogin" to="/login" class="login-button" style="margin-right: 30px;">Login</router-link> -->

    <nav class="navbar navbar-expand bg-dark" data-bs-theme="dark">
      <div class="mx-auto">
        <span class="navbar-nav">
          <!-- <img :src="require(`@/assets/omytt.png`)" style="height: 40px; margin-top: auto; margin-bottom: auto;"> -->
          <router-link v-if="isLogin" :to="{ name: 'RecommendView'}" class="nav-link px-5">Recommend</router-link>
          <router-link v-if="isLogin" :to="{ name: 'MovieView' }" class="nav-link px-5">&nbsp;&nbsp;Home&nbsp;&nbsp;</router-link>
          <router-link v-if="isLogin" :to="{ name: 'AccountsView' }" class="nav-link px-5">&nbsp;&nbsp;My Page&nbsp;&nbsp;</router-link>
          <button v-if="isLogin" class="login-button" style="margin: 0 auto; background: transparent; border: none; color: gray;" @click="logout">Logout</button>
        </span>
      </div>
    </nav>


    <router-view/>

  </div>
</template>

<script>
export default {
  name: 'App',
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
    }
  }
}
</script>


<style>
body {
  height: 100vh;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #000000;
  /* position: relative; */
  background: #121212;
  width: 100vw;
  height: 100vh;
}
/* .spectrum-background {
  background:
    linear-gradient(red, transparent),
    linear-gradient(to top left, lime, transparent),
    linear-gradient(to top right, blue, transparent);
  background-blend-mode: screen;
} */

.logout-button {
  /* position: absolute;
  top: 0;
  right: 0;
  margin-left: 100%;
  margin-inline-end: 0%; */
}
nav {
  font-family: SUITE-Regular;
  font-size: 25px;
}
nav .nav-link.router-link-exact-hover {
  color: #ffffff;
  font-weight: 700;
  font-family: SUITE-Regular;
}
nav .nav-link.router-link-exact-active {
  color: #ffffff;
  font-weight: 700;
  font-family: SUITE-Regular;
}
.brand {
  font-size: 80px;
  /* text-align: center; */
  font-family: 'KCCChassam';
  color: #fff;
  text-shadow: 0 0 50px #ffff00, 0 0 100px #ffff00, 0 0 20px #ffff00, 0 0 20px #fdd750, 0 0 20px #fdd750, 0 0 20px #fdd750, 0 0 20px #fdd750;
  /* text-shadow: 0 0 50px #fff, 0 0 10px #fff, 0 0 15px #9CFF2E, 0 0 20px #9CFF2E, 0 0 25px #F0FF42, 0 0 30px #F0FF42, 0 0 35px #F0FF42; */
}
@import url('https://cdn.jsdelivr.net/font-iropke-batang/1.2/font-iropke-batang.css');

@font-face {
  font-family: 'Tenada';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2210-2@1.0/Tenada.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'HANAMDAUM';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-2@1.0/HANAMDAUM.woff2') format('woff2');
  font-weight: 400;
  font-style: normal;
}
@font-face {
  font-family: 'KCCChassam';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2302@1.0/KCCChassam.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'NanumSquareNeo-Variable';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_11-01@1.0/NanumSquareNeo-Variable.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'SUITE-Regular';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-2@1.0/SUITE-Regular.woff2') format('woff2');
  font-weight: 400;
  font-style: normal;
}
@font-face {
  font-family: 'KBO-Dia-Gothic_bold';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-2@1.0/KBO-Dia-Gothic_bold.woff') format('woff');
  font-weight: 700;
  font-style: normal;
}
@font-face {
  font-family: 'MBC1961M';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-01@1.0/MBC1961M.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'LINESeedKR-Bd';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_11-01@1.0/LINESeedKR-Bd.woff2') format('woff2');
  font-weight: 700;
  font-style: normal;
}
@font-face {
  font-family: 'Arita-buri-SemiBold';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/Arita-buri-SemiBold.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'GoryeongStrawberry';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-01@1.0/GoryeongStrawberry.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'omyu_pretty';
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-01@1.0/omyu_pretty.woff2') format('woff2');
  font-weight: normal;
  font-style: normal;
}
</style>
