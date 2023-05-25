<template>
  <div>
    <span class="commentTag"></span>
    <div class="comments">
      <MovieCommentItem
      v-for="comment in comments" 
      :key="comment.id"
      :comment="comment"/>
    </div>

    
    <form @submit.prevent="createComment">
      <input class="text-input" type="text" id="content" cols="50" rows="1.5" v-model="content" placeholder="댓글을 작성해주세요">
      '  '<input type="submit" id="submit" value="확인" class="button btnPush btnBlueGreen">
    </form>

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

<style scoped>
@font-face {
    font-family: 'SUITE-Regular';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2304-2@1.0/SUITE-Regular.woff2') format('woff2');
    font-weight: 400;
    font-style: normal;
}
.commentTag {
  font-family: 'Courier New', Courier, monospace;
  font-size: 20px;
  text-align: left;
}
.commentInput {
  font-family: 'SUITE-Regular';
}
.comments {
  padding: 5px 5px 0px 5px;
  width: 700px;
  margin-left: auto;
  margin-right: auto;
  border-radius: 6px;
}
.btnBlueGreen.btnPush {
  box-shadow: 0px 5px 0px 0px #007144;
}
.btnPush:hover {
  margin-top: 15px;
  margin-bottom: 5px;
}
.btnBlueGreen.btnPush:hover {
  box-shadow: 0px 0px 0px 0px #007144;
}
a.button {
  width: 10px;
  display: block;
  position: relative;
  float: left;
  width: 120px;
  padding: 0;
  margin: 10px 20px 10px 0;
  font-weight: 600;
  text-align: center;
  line-height: 50px;
  color: #FFF;
  border-radius: 5px;
  transition: all 0.2s ease-in-out;
}
.btnBlueGreen {
  background: #00AE68;
}
</style>
