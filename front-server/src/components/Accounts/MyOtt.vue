<template>
  <div>
    <p>내가 가지고 있는 ott</p>


    <button type="button" variant="primary" class="m-2 btn btnEvent" v-for="ott in otts" :key="ott.id" @click="saveMyOtt(ott.id)">
      <img :src="require(`@/assets/${ott.initial}.png`)" style="width:50px; height:50px" alt="btnImages" class="btnImages">
    </button>
    <button @click="sendMyOtt">저장</button>
    <!-- <div>
        <h2>Select your OTT:</h2>
        <button @click="saveMyOtt">저장하기</button>
        <ul>
          <li v-for="ott in otts" :key="ott.id">
            <input type="checkbox" :id="ott.id" v-model="myOtts" :value="ott.id"> 
            <label :for="ott.id">{{ ott.name }}</label>
          </li>
        </ul>
      </div> -->
  </div>
</template>

<script>
export default {
  name: 'MyProfile',
  data() {
    return {
      // selectId: null,
    }
  },
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
      // console.log(input)
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