import asyncio
import sys
from relayx_py import Realtime

client = Realtime({
  "api_key": 'eyJ0eXAiOiJKV1QiLCJhbGciOiJlZDI1NTE5LW5rZXkifQ.eyJhdWQiOiJOQVRTIiwibmFtZSI6IjY5MDVjZDU4NDFkZjVmN2MxZGNjNmQ1ZiIsInN1YiI6IlVBWktKTldBSkpNSlJRQzdWUUJYWlVGVDY2TUk0NURFTEtBWExBUlpEUVZQT1pMU01OMlhPTEtQIiwibmF0cyI6eyJkYXRhIjotMSwicGF5bG9hZCI6LTEsInN1YnMiOi0xLCJwdWIiOnsiZGVueSI6WyI-Il19LCJzdWIiOnsiZGVueSI6WyI-Il19LCJvcmdfZGF0YSI6eyJvcmdfaWQiOiI2OGRiYjYxZjk2NjM4NzdkMzg5NTlkMDkiLCJvcmdfbmFtZSI6IlNwYWNlWCIsInZhbGlkaXR5X2tleSI6ImZlZjBiMjFlLTUzYzEtNDYxZi05ZjA5LWUyNTdiNTlmNWM5YSIsInJvbGUiOiJ1c2VyIiwicHJvamVjdF9pZCI6IjY5MDVjZDU4NDFkZjVmN2MxZGNjNmQ1ZiJ9LCJpc3N1ZXJfYWNjb3VudCI6IkFDSktNTUs2VFBJNUtYWDY0NExBSEpPVk9BRkNYWlRSS0dCVVcyQzQ0TkhESFRWTFo3T1ZKRDdLIiwidHlwZSI6InVzZXIiLCJ2ZXJzaW9uIjoyfSwiaXNzIjoiQUNKS01NSzZUUEk1S1hYNjQ0TEFISk9WT0FGQ1haVFJLR0JVVzJDNDROSERIVFZMWjdPVkpEN0siLCJpYXQiOjE3NjE5OTU1MTksImp0aSI6InAyTnpOWlpnNWdRdDFDTU1tZzBDTTY2M3J1ckpiZEs3c1BDbDlpaGxvL3VrU3NXdXFGMTRBeFNwc3JnZlQydFprRmorTWJReXBITWJRM045QXpnSmdnPT0ifQ.NnMl08SzpmA9q_CPVOh0GDyX2EJ3qUyWCMz08OQYI3XZ5_kXBrD6riNCvxXi6WsbUXhbVUV9kOXT58BHCTQxBQ',
  "secret": 'SUACG4GAH3OVX45X2COIK5UG46XG3TJXQCJZZGHOKZMCCPEFC2OXD6WQWU'
})

# client = Realtime({
#   "api_key": '$api_key',
#   "secret": '$secret'
# })

client.init()

def callback_fn(data):
    print("We got a message!")
    print(data)

    print()
    print("Ctrl + C to quit")

async def on_connected():
    type = sys.argv[1]
    topic = sys.argv[2]
    message = sys.argv[3]

    print("Connected to relayX!")

    if type == "pub":
        print("Sending message to topic => {}".format(topic))
        print()

        sent = await client.publish(topic, message)

        print(f"Message sent => {sent}")

        print()
        print("Ctrl + C to quit")
    elif type == "sub":
        print("Listening for messages on {}".format(topic))

        await client.on(topic, callback_fn)
    else:
        print("Invalid $type value!")
        print("--------------------------------------")

        print("Usage: node <file>.js <type> <topic> <message>")
        print("type = pub or sub")

async def main():
    if len(sys.argv) < 4:
        print("Usage: python <file name>.py <type> <topic> <message>")
        print("type = pub or sub")

        print()
        print("Ctrl + C to quit")

    type = sys.argv[1]
    topic = sys.argv[2]
    message = sys.argv[3]

    print("Type => {}".format(type))
    print("Topic => {}".format(topic))
    print("Message => {}".format(message))

    await client.on(Realtime.CONNECTED, on_connected)

    await client.connect() 

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())