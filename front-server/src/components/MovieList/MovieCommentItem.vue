<template>
  <div class="commentBox">

    <hr style="color: white;"> <!-- 구분선 -->
    <div class="comment_user">
      <span class="comment_user">{{ comment.username }}</span>
    </div>

    <div class="comment">
      <span>{{ comment.content }}</span>
    </div>

    <hr style="color: white;"> <!-- 구분선 -->


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

<style scoped>
.comment_user {
  display: inline;
  float: left;
  margin-left: 10px;
  color:  rgb(255, 255, 255);
  font-weight: 700;
}
.comment {
  display: inline;
  color: white;
}
</style>