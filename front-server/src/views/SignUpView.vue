<template>
  <div>
    <h1>Welcome</h1>
    <form @submit.prevent="signUp">
      <table width ="1000" height="300" align = "center">
        <tr>
          <td><label for="username">username : </label></td>
          <td><input type="text" id="username" v-model="username"><br></td>
        </tr>
        <tr>
          <td><label for="password1"> password : </label></td>
          <td><input type="password" id="password1" v-model="password1"><br></td>
        </tr>
        <tr>
          <td><label for="password2"> password : </label></td>
          <td><input type="password" id="password2" v-model="password2"></td>
        </tr>
      </table>
      <p>
      <input class="check" type="submit" value="SignUp">
      </p>
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      // console.log('signup')
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }

      this.$store.dispatch('signUp', payload)

    }
  }
}
</script>

<style>
/* Import Poppins font: */
@import url("https://fonts.googleapis.com/css2?family=Poppins&display=swap");

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
  border-radius: 3rem;
  border: none;
  padding: 10px;
  text-align: center;
  outline: none;
  margin: 10px;
  width: 30%;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
  font-weight: 400;
}

input:hover {
  box-shadow: 0px 0px 8px -5px #000000;
}

input:active {
  box-shadow: 0px 0px 8px -5px #000000;
}

.button {
  cursor: pointer;
  user-select: none;
}

.check {
  background: #9CFF2E;
}
</style>