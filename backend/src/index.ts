import * as express from 'express';
const app = express();
const port = 3000;

app.use(express.urlencoded());

app.get('/', (req,res)=>{
  res.sendFile('')
})

app.listen(port, () => {
  console.log(`Listening on port ${port}`);
})

