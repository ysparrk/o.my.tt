<template>
  <div>

    <div class="p-4">
      <h1 class="brand">o . my . tt</h1>
    </div>

    <div class="hi">{{ username }}님 안녕하세요. 회원가입이 완료되었습니다</div>
    <div class="hi-ott">가입하신 OTT를 선택해주세요</div>
    <!-- <button type="button" variant="primary" class="m-2 btn btnEvent" v-for="ott in otts" :key="ott.id" @click="saveMyOtt(ott.id)">
      <img :src="require(`@/assets/${ott.initial}.png`)" style="width:50px; height:50px" alt="btnImages" class="btnImages">
    </button> -->
    <div>
      <MyOttItem v-for="(ott, idx) in otts" :key="idx" :ott="ott"/>
    </div>
    <button class="btn-3d cyan m-4" style="color: black;" @click="sendMyOtt">완료</button>
    


  </div>
</template>

<script>
import MyOttItem from '@/components/Accounts/MyOttItem'


export default {
  name: 'MyFirstOttView',
  components: {
    MyOttItem
  },
  computed: {
    username() {
      return this.$store.state.username
    },
    otts() {
      return this.$store.state.otts
    },
    myOtts() {
      return this.$store.state.myOtts
    }
  },
  created() {
    this.getMyOtt()
  },
  methods: {
    getMyOtt() {
      this.$store.dispatch('getMyOtt')
      console.log("get 함수")
    },
    sendMyOtt() {
      this.$store.dispatch('sendMyOtt', this.myOtts)
      this.$router.push({name : 'MovieView'})
    }
    
  }
}
</script>

<style scoped>
.brand {
  animation: text-flicker-in-glow 2.5s;
}
.hi {
  font-family: NanumSquareNeo-Variable;
  font-size: 20px;
  color: white;
  margin-bottom: 20px;
  margin-top: 20px;
}
.hi-ott {
  font-family: NanumSquareNeo-Variable;
  font-size: 30px;
  color: white;
  margin-bottom: 20px;
}
.btn-3d {
  width: 80px;
  height: 40px;
  margin-bottom: 100px;
  position: relative;
  display: inline-block;
  color: white;
  border-radius: 6px;
  text-align: center;
  transition: top .01s linear;
  text-shadow: 0 1px 0 rgba(0,0,0,0.15);
  border: none;
}
.btn-3d.red:hover    {background-color: #e74c3c;}
.btn-3d.blue:hover   {background-color: #699DD1;}
.btn-3d.green:hover  {background-color: #80C49D;}
.btn-3d.purple:hover {background-color: #D19ECB;}
.btn-3d.yellow:hover {background-color: #F0D264;}
.btn-3d.cyan:hover   {background-color: #82D1E3;}

.btn-3d:active {
  top: 9px;
}
/* 3D button colors */
.btn-3d.red {
  background-color: #e74c3c;
  box-shadow: 0 0 0 1px #c63702 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 4px 0 0 #C24032,
        0 8px 0 1px rgba(0,0,0,0.4),
        0 8px 8px 1px rgba(0,0,0,0.5);
}
.btn-3d.red:active {
  box-shadow: 0 0 0 1px #c63702 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 0 0 1px rgba(0,0,0,0.4);
}
.btn-3d.blue {
  background-color: #6DA2D9;
  box-shadow: 0 0 0 1px #6698cb inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 8px 0 0 rgba(110, 164, 219, .7),
        0 8px 0 1px rgba(0,0,0,.4),
        0 8px 8px 1px rgba(0,0,0,0.5);
}
.btn-3d.blue:active {
  box-shadow: 0 0 0 1px #6191C2 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 0 0 1px rgba(0,0,0,0.4);
}
.btn-3d.green {
  background-color: #82c8a0;
  box-shadow: 0 0 0 1px #82c8a0 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 8px 0 0 rgba(126, 194, 155, .7),
        0 8px 0 1px rgba(0,0,0,.4),
        0 8px 8px 1px rgba(0,0,0,0.5);
}
.btn-3d.green:active {
  box-shadow: 0 0 0 1px #82c8a0 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 0 0 1px rgba(0,0,0,0.4);
}
.btn-3d.purple {
  background-color: #cb99c5;
  box-shadow: 0 0 0 1px #cb99c5 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 8px 0 0 rgba(189, 142, 183, .7),
        0 8px 0 1px rgba(0,0,0,.4),
        0 8px 8px 1px rgba(0,0,0,0.5);
}
.btn-3d.purple:active {
  box-shadow: 0 0 0 1px #cb99c5 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 0 0 1px rgba(0,0,0,0.4);
}
.btn-3d.cyan {
  background-color: #7fccde;
  box-shadow: 0 0 0 1px #7fccde inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 8px 0 0 rgba(102, 164, 178, .6),
        0 8px 0 1px rgba(0,0,0,.4),
        0 8px 8px 1px rgba(0,0,0,0.5);
}
.btn-3d.cyan:active {
  box-shadow: 0 0 0 1px #7fccde inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 0 0 1px rgba(0,0,0,0.4);
}
.btn-3d.yellow {
  background-color: #F0D264;
  box-shadow: 0 0 0 1px #F0D264 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 8px 0 0 rgba(196, 172, 83, .7),
        0 8px 0 1px rgba(0,0,0,.4),
        0 8px 8px 1px rgba(0,0,0,0.5);
}
.btn-3d.yellow:active {
  box-shadow: 0 0 0 1px #F0D264 inset,
        0 0 0 2px rgba(255,255,255,0.15) inset,
        0 0 0 1px rgba(0,0,0,0.4);
}
</style>
