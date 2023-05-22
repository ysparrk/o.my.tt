<template>
  <div>
    <h4>{{ comment.username }}</h4>
    <h4>{{ comment.content }}</h4>
  </div>
</template>

<script>
export default {
  name: 'MovieCommentItem',
  props: {
    comment: Object,
  }
}
</script>

<style>

</style>