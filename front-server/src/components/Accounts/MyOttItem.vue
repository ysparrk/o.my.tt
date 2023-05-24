<template>
  <div>
    <div :class="{card_selected : is_selected}">
      <button type="button" variant="primary" class="m-2 btn btnEvent" @click="saveMyOtt(ott.id)">
        <!-- <img :src="require(`@/assets/${ott.initial}.png`)" style="width:50px; height:50px" alt="btnImages" class="btnImages"> -->
        <img :src="require(`@/assets/${ott.initial}.png`)" style="width:50px; height:50px" alt="btnImages" class="btnImages">
      </button>
    </div>
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
      // this.is_selected = false
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
.card_selected {
  opacity: 0.5;
  transform: scale(1.05);
}
</style>