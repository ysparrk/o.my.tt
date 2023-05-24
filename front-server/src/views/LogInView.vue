<!------------------------------------------------------>

<!-- 수정 후 -->
<template>
  <div>
    <div class="background">
        <div class="shape"></div>
        <div class="shape"></div>
    </div>

    <form @submit.prevent="login">
      <h3>Login Here</h3>

      <label for="username">Username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password">

      <button><input class="check" type="submit" value="logIn"></button>
    </form>
  </div>
</template>-
<!------------------------------------------------------>

<!-- 수정 전 -->
<!--<template>
  <div>
    <form @submit.prevent="login">
      <label for="username">Username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>

      <input class="check" type="submit" value="logIn">
    </form>

  </div>
</template>-->

<!-- 수정 전
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
  /* font-family: "Poppins", sans-serif; */
}
h1 {
  cursor: default;
  user-select: none;
}
input {
  background: white;
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
-->

<script>
export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username, password
      }
      
      this.$store.dispatch('login', payload)
    },
  }
}
</script>

<style scoped>
*,
*:before,
*:after{
    box-sizing: border-box;
}
body {
    background-color: #080710;
}
.background {
    width: 430px;
    height: 520px;
    position: absolute;
    transform: translate(-50%,-50%);
    left: 50%;
    top: 50%;
}
.background .shape {
    height: 200px;
    width: 200px;
    position: absolute;
    border-radius: 50%;
}
.shape:first-child {
    background: linear-gradient(
        /* #1845ad,
        #23a2f6 */
        #ff512f,
        #f09819
    );
    left: -70px;
    top: 300px;
}
.shape:last-child {
    background: linear-gradient(
        to right,
        #ff512f,
        #f09819
    );
    right: -70px;
    bottom: -450px;
}
form {
    height: 520px;
    width: 400px;
    background-color: rgba(255,255,255,0.13);
    position: absolute;
    transform: translate(-50%,-50%);
    top: 400%;
    left: 50%;
    border-radius: 10px;
    backdrop-filter: blur(10px);
    border: 2px solid rgba(255,255,255,0.1);
    box-shadow: 0 0 40px rgba(8,7,16,0.6);
    padding: 50px 35px;
}
form * {
    font-family: 'Poppins',sans-serif;
    color: #ffffff;
    letter-spacing: 0.5px;
    outline: none;
    border: none;
}
form h3 {
    font-size: 32px;
    font-weight: 500;
    line-height: 42px;
    text-align: center;
}

label {
    display: block;
    margin-top: 30px;
    font-size: 16px;
    font-weight: 500;
}
input {
    display: block;
    height: 50px;
    width: 100%;
    background-color: rgba(254, 253, 253, 0.92);
    color: black;
    border-radius: 3px;
    padding: 0 10px;
    margin-top: 8px;
    font-size: 14px;
    font-weight: 300;
}
input.check {
  background-color: #9CFF2E;
  color: black;
}
button {
    margin-top: 50px;
    width: 100%;
    background-color: transparent;
    color: #080710;
    padding: 15px 0;
    font-size: 18px;
    font-weight: 600;
    border-radius: 5px;
    cursor: pointer;
}
input.check {
  background: #9CFF2E;
}

</style>