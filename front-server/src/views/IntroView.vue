<template>
  <div>
      <router-link to="/login" class="login-button"><h1 class="title brand-full-width">o . my . tt</h1></router-link>
  </div>
</template>

<script>
export default {
  name: 'IntroView'
}
</script>

<style scoped>
@keyframes text-pop-up-top {
  0% {
    -webkit-transform: translateY(0);
            transform: translateY(0);
    -webkit-transform-origin: 50% 50%;
            transform-origin: 50% 50%;
    text-shadow: none;
  }
  100% {
    -webkit-transform: translateY(-50px);
            transform: translateY(-50px);
    -webkit-transform-origin: 50% 50%;
            transform-origin: 50% 50%;
    text-shadow: 0 1px 0 #cccccc, 0 2px 0 #cccccc, 0 3px 0 #cccccc, 0 4px 0 #cccccc, 0 5px 0 #cccccc, 0 6px 0 #cccccc, 0 7px 0 #cccccc, 0 8px 0 #cccccc, 0 9px 0 #cccccc, 0 50px 30px rgba(0, 0, 0, 0.3);
  }
}
.title {
  font-size: 200px;
  /* text-align: center; */
  font-family: 'KCCChassam';
  color: #fff;
  text-shadow: 0 0 50px #ffff00, 0 0 100px #ffff00, 0 0 20px #ffff00, 0 0 20px #fdd750, 0 0 20px #fdd750, 0 0 20px #fdd750, 0 0 20px #fdd750;
  /* text-shadow: 0 0 50px #fff, 0 0 10px #fff, 0 0 15px #9CFF2E, 0 0 20px #9CFF2E, 0 0 25px #F0FF42, 0 0 30px #F0FF42, 0 0 35px #F0FF42; */
}
.brand-full-width {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin-top: -100px;
  animation: text-pop-up-top 1s;
}
.login-button {
  text-decoration: none; /* 밑줄 제거 */
}
</style>
