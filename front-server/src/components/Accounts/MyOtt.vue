<template>
  <div>
    <p>내가 가지고 있는 ott</p>


    <button type="button" variant="primary" class="m-2 btn btnEvent" v-for="ott in otts" :key="ott.id" @click="saveMyOtt(ott.id)">
      <img :src="require(`@/assets/${ott.initial}.png`)" style="width:50px; height:50px" alt="btnImages" class="btnImages">
    </button>
    <button @click="sendMyOtt">저장</button>

  </div>
</template>

<script>
export default {
  name: 'MyProfile',
  computed: {
    otts() {
      return this.$store.state.otts
    },
    myOtts() {
      return this.$store.state.myOtts
    }
  },
  methods: {
    saveMyOtt(input) {
      const myOtt = input
      this.$store.dispatch('saveMyOtt', myOtt)
    },
    sendMyOtt() {
      this.$store.dispatch('sendMyOtt', this.myOtts)
    }
  } 
}
</script>

<style>

</style>