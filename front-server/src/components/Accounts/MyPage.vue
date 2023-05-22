<template>
  <div>
    <p>my page입니다</p>
    <MyMovies />
    <MyOffer />
  </div>
</template>

<script>
import MyMovies from '@/components/Accounts/MyMovies'
import MyOffer from '@/components/Accounts/MyOffer'

export default {
  name: 'MyPage',
  components: {
    MyMovies,
    MyOffer
  }
}
</script>

<style>

</style>