<template>
  <div>
    <h1>댓글 작성</h1>
    <form @submit.prevent="createComment">
      <textarea id="content" cols="30" rows="2" v-model="content"></textarea><br>
      <input type="submit" id="submit" value="작성">
    </form>

    <MovieCommentItem
    v-for="comment in comments" 
    :key="comment.id"
    :comment="comment"/>
  </div>
</template>

<script>
import MovieCommentItem from '@/components/MovieList/MovieCommentItem'

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieCommentCreate',
  components: {
    MovieCommentItem
  },
  data() {
    return {
      content: null, 
      user: null,
      comments: [],
    }
  },
  props:{
    movie: Object
  },
  created() {
    // 사용자 정보 가져오기
    this.user = this.$store.state.username
    this.getComments()
  },
  methods: {
    createComment() {
      const content = this.content
      const movieId = this.movie.id
      const userName = this.user

      console.log(userName)

      if (!content) {
        alert('댓글을 입력해주세요')
        return
      } 
      axios({
        method: 'post',
        url: `${API_URL}/movies/comment/${movieId}/`,
        data: {
          content: content,
          movie: movieId,
          username: userName
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
        console.log(res)
        this.content = null
        this.getComments()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getComments() {
      // console.log(this.movie.id)
      const movieId = this.movie.id
      axios({
        method: 'get',
        url: `${API_URL}/movies/comment/${movieId}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          this.comments = res.data // 댓글 목록 업데이트
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style>

</style>
