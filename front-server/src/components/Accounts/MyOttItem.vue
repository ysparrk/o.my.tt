<template>
  <div class="btn">

      <img :src="require(`@/assets/${ott.initial}.png`)"
      style="width: 70px; height: 70px; padding: 0; margin: 20px;"
      @click="saveMyOtt(ott.id)"
      v-bind:class="{btn_selected: is_selected}">

  </div>
</template>

<script>
export default {
  name: 'MyOttItem',
  props: {
    ott: Object
  },
  data () {
    return{
      is_selected: true
    }
  },
  computed: {
    myOtts() {
      return this.$store.state.myOtts
    },
    myFirstOtts() {
      return this.$store.state.myFirstOtts
    }
  },
  created() {
    this.checkMyOtt()
  },
  methods: {
    saveMyOtt(input) {
      const myOtt = input
      this.is_selected = !this.is_selected
      this.$store.dispatch('saveMyOtt', myOtt)
    },
    // user가 이미 가지고 있는 ott 체크
    checkMyOtt() {
      console.log('check 함수 실행')
      // console.log(this.myFirstOtts)
      const ottId = this.ott.id
    
      for (let i = 0; i < this.myFirstOtts.length; i++) {
        // console.log(this.myOtts[i])
        if (this.myFirstOtts[i].id === ottId) {
          this.is_selected = false;
          break
        }
      }
    }
  }
}
</script>

<style scoped>
div {
  display: inline;
}
.btn {
  border: none;
}
.btn:focus {
	border: none;
	outline: none;
}
.btn_selected {
  opacity: 0.5;
  transform: scale(1.05);
  animation: jello-horizontal infinite;
}
.jello-horizontal {
  -webkit-animation: jello-horizontal 0.9s both;
  animation: jello-horizontal 0.9s both;
}
@keyframes jello-horizontal {
0% {
  -webkit-transform: scale3d(1, 1, 1);
  transform: scale3d(1, 1, 1);
}
30% {
  -webkit-transform: scale3d(1.25, 0.75, 1);
  transform: scale3d(1.25, 0.75, 1);
}
40% {
  -webkit-transform: scale3d(0.75, 1.25, 1);
  transform: scale3d(0.75, 1.25, 1);
}
50% {
  -webkit-transform: scale3d(1.15, 0.85, 1);
  transform: scale3d(1.15, 0.85, 1);
}
65% {
  -webkit-transform: scale3d(0.95, 1.05, 1);
  transform: scale3d(0.95, 1.05, 1);
}
75% {
  -webkit-transform: scale3d(1.05, 0.95, 1);
  transform: scale3d(1.05, 0.95, 1);
}
100% {
  -webkit-transform: scale3d(1, 1, 1);
  transform: scale3d(1, 1, 1);
}
}
</style>