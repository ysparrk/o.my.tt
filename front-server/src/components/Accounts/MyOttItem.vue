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
      is_selected: false
    }
  },
  computed: {
    myOtts() {
      return this.$store.state.myOtts
    }
  },
  methods: {
    saveMyOtt(input) {
      const myOtt = input
      this.is_selected = !this.is_selected
      this.$store.dispatch('saveMyOtt', myOtt)
    },
  }

}
</script>

<style>

</style>