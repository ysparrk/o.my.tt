<template>
  <div>

    <div>
      <h1 class="brand">o . my . tt</h1>
    </div>

    <h3>this is {{ username }} page</h3>
    <MyPage />
  </div>
</template>

<script>
import MyPage from '@/components/Accounts/MyPage'

export default {
  name: 'AccountsView',
  components: {
    MyPage
  },
  computed: {
    username() {
      return this.$store.state.username
    }
  },
}
</script>

<style>

</style>