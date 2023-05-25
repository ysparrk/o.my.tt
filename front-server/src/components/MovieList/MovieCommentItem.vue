<template>
  <div class="commentBox">
    <div class="comment_user">
      <span>{{ comment.username }}</span>
    </div>
    <hr>
    <div class="comment">
      <span>{{ comment.content }}</span>
    </div>
    <br>
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
@font-face {
    font-family: 'SUITE-Regular';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-2@1.0/SUITE-Regular.woff2') format('woff2');
    font-weight: 400;
    font-style: normal;
}
.commentBox {
    background-color: rgb(240, 240, 240, 0.4);
    box-sizing: border-box;
    padding: 0px 12px;
    border-radius: 6px;
    overflow: hidden;
    margin: 0px 0px 20px;
    color: black;
    font-family: 'SUITE-Regular';
}

.comment_user {
    position: relative;
    margin: 10px 0px 0px 10px;
    height: 10px;
    color:  black;
    /* font-weight: bold; */
    text-align: left;
    font-weight: 700;
}

.comment {
  height: auto;
  /* font-weight: bold; */
}
</style>