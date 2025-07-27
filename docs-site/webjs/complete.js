import { Realtime, CONNECTED } from "relayx-webjs"
import * as readline from 'readline';

const client = new Realtime({
  api_key: '$api_key',
  secret: '$secret'
})

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

client.init()

await client.on("$topic", (data) => {
    console.log(data);
})

client.on(CONNECTED, async () => {
  console.log("Connected to Relay!")

  console.log("Enter message: ")

  rl.on('line', async (input) => {
      if(input == "exit"){
        await client.close()
        return
      }

      var sent = await client.publish("$topic", {
          user_name: "John Doe",
          message: input
      });
    
      console.log("Message sent => " + sent);  
  });

  
})

client.connect()