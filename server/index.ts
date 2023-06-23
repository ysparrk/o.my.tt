import express from 'express'

const app = express()

// root 디렉토리로 오면 200번
app.get('', (req, res, next) => {
  res.send(200)
})

// 웹 서버가 80번 포트를 듣겠다
app.listen(80, () => {
  console.log('listening...')
})