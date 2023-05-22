<template>
  <div id="app">
      <router-link :to="{ name: 'SignUpView' }">Sign-Up Page</router-link> |
      <router-link :to="{ name: 'LogInView' }">Login Page</router-link>

      <router-link v-if="!loggedIn" to="/login" class="button">
        Login
      </router-link>
      <router-link v-else type="button" class="logoutButton" @click="logout">
        LogOut
      </router-link>

    <nav>
      <router-link :to="{ name: 'MovieView' }">Movie List</router-link> |
      <router-link :to="{ name: 'RecommendView'}">Recommend</router-link> |
      <router-link :to="{ name: 'SearchMovie'}">Search Movie</router-link> |
      <router-link :to="{ name: 'AccountsView' }">MyPage</router-link>
    </nav>
    <div>
      <img :src="require(`@/assets/logo.png`)" style="width:400px; height:auto" alt="MainLogo">
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
  color: #2c3e50;
  background-color: #66ff00;
}
nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
