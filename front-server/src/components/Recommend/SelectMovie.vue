<template>
  <div>
    <p>선호하는 영화를 선택하세요</p>
    <button @click="sendIds">제출하기</button>
    <!-- <h2>선택 영화 :
      <span v-for="id in selectedId" v-bind:key="id">
        {{ id }}
      </span>
    </h2> -->

    
    <div v-if="finalRecommend">
      <h2>추천하는 Ott는 : {{ finalRecommend.name }}</h2>
      
      <a v-bind:href="finalRecommend.signup">가입하기</a>
      <!-- <ul>  리스트로..?
        <li v-for="ott in receivedData" :key="ott.id">{{ name }}</li>
      </ul> -->
    </div>
    
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
      selectedId: [],
      finalRecommend: null,
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
        this.finalRecommend = res.data  // 요청받은 ott 데이터 가져오기
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