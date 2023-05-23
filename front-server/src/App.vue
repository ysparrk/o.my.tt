<template>
  <div id="app">

    <!-- <router-link :to="{ name: 'SignUpView' }">Sign-Up Page</router-link> | -->
    <div>
      <button class="login"><router-link :to="{ name: 'LogInView' }">Login Page</router-link></button>
    </div>

    <!-- <router-link v-if="!loggedIn" :to="{ name: 'LogInView' }" class="button">
      Login
    </router-link>
    <router-link v-else type="button" class="logoutButton" @click="logout">
      LogOut
    </router-link> -->

    <nav>
      <router-link :to="{ name: 'MovieView' }">Movie List</router-link> |
      <router-link :to="{ name: 'RecommendView'}">Recommend</router-link> |
      <router-link :to="{ name: 'AccountsView' }">MyPage</router-link>
    </nav>

    <div>
      <!-- <img :src="require(`@/assets/logo.png`)" style="width:400px; height:auto" alt="MainLogo"> -->
      <h1 class="brand">o . my . tt</h1>
    </div>

    <router-view/>
  </div>

</template>

<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #F7F7F7;
  position: relative;
  background: #20262E;
  width: 100vw;
}

button.login {
  position: absolute;
  top: 0;
  right: 0;
  /* margin-left: 100%; */
  /* margin-inline-end: 0%; */
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: white;
}

nav a.router-link-exact-active {
  color: #9CFF2E;
}

@font-face {
    font-family: 'Tenada';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2210-2@1.0/Tenada.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
}

.brand {
  font-size: 70px;
  text-align: center;
  font-family: cursive;
  color: #fff;
  text-shadow: 0 0 50px #F8FFDB, 0 0 100px #F8FFDB, 0 0 20px #9CFF2E, 0 0 20px #9CFF2E, 0 0 20px #F0FF42, 0 0 20px #F0FF42, 0 0 20px #F0FF42;
  /* text-shadow: 0 0 50px #fff, 0 0 10px #fff, 0 0 15px #9CFF2E, 0 0 20px #9CFF2E, 0 0 25px #F0FF42, 0 0 30px #F0FF42, 0 0 35px #F0FF42; */
}
</style>
