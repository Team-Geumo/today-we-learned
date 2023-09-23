### 동기(Synchronous)와 비동기(Asynchronous)

- 동기
  
  - 순서에 맞추어 한 번에 하나의 작업을 수행

- 비동기
  
  - 요청을 보내고 응답에 관계없이 다음 작업을 수행

### Promise

- 비동기 처리를 위한 객체

- 3가지 상태
  
  - pending (대기)
    
    ```javascript
    new Promise();
    ```
  
  - fulfilled (이행)
    
    ```javascript
    const promise = new Promise((resolve, reject)=>{
        resolve();
    });
    ```
  
  - rejected (실패)
    
    ```javascript
    const promise = new Promise((resolve, reject)=>{
        reject();
    });
    ```

- 사용 예시
  
  ```javascript
  const promise = new Promise((resolve, reject)=>{
      resolve("성공");
  	reject(new Error('실패'));
  });
  
  promise
  	.then(value => console.log(value))  // resolve
  	.catch(err => console.log(err));  // reject
  ```

### async await

- async
  
  - new Promise 객체 사용하지 않고 Promise 반환

- await
  
  - async가 붙은 함수 내에서 사용 가능
  
  - 해당 함수가 실행을 끝낼 때까지 다음 코드 실행하지 않음

- 예시
  
  ```javascript
  async function 함수명() {
      await 비동기처리_메서드명()
    }
  ```
  
  ```typescript
  export default async function handler(
    req: NextApiRequest,
    res: NextApiResponse
  ) {
    const session = await getServerSession(req, res, authOptions);
    if (req.method == "POST") {
      req.body = JSON.parse(req.body);
      const data = {
        content: req.body.comment,
        parent: new ObjectId(req.body._id),
        author: session?.user?.email,
      };
  
      const client = await connectDB;
      const db = client.db("forum");
      const result = await db.collection("comment").insertOne(data);
      res.status(200).json({});
    }
  }
  ```


