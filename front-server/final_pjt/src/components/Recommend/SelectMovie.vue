<template>
  <div>
    <p>선호하는 영화를 선택하세요</p>
    <button @click="sendIds">제출하기</button>
    <!-- <h2>선택 영화 :
      <span v-for="id in selectedId" v-bind:key="id">
        {{ id }}
      </span>
    </h2> -->
    
    <SelectMovieItem 
    v-for="select in selects"
    :key="select.id"
    :select="select"
    @item-to-list="selectId"/>

  </div>
</template>

<script>
import SelectMovieItem from '@/components/Recommend/SelectMovieItem'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'


export default {
  name: 'SelectMovie',
  components: {
    SelectMovieItem,
  },
  computed: {
    selects() {
      return this.$store.state.selects
    }
  },
  data() {
    return {
      selectedId: []
    }
  },
  methods: {
    selectId(input) {
      console.log('데이터 받음')
      if (!this.selectedId.includes(input)) {
        if (this.selectedId.length < 4) {  // 3개 까지 추가 가능
          this.selectedId.push(input)
        }
      }
      // 3개를 클릭했다면, django로 send 하기
      if (this.selectedId.length === 3) {
        alert("3개를 선택하셨습니다. 제출하기를 눌러주세요")
      }
      console.log(this.selectedId)
    },
    sendIds() {
      // console.log(selectedId)
      // const [id1, id2, id3] = this.selectedId
      // const payload = { id1, id2, id3 }
      const payload = this.selectedId
      axios({
        method: 'post',
        url: `${API_URL}/recommend/optimize_ott/`,
        data: {
          payload
        }
      })
      .then((res) => {
        console.log('response!!')
        console.log(res)
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