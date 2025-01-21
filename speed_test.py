import speedtest

test = speedtest.Speedtest()

print('Performing download speed test...')
download_result = test.download()
print(f'Download Speed: {download_result/1024/1024:.2f} mb/s')
print('Performing Upload speed test...')
upload_result = test.upload()
print(f'Upload Speed: {upload_result/1024/1024:.2f} mb/s')
print('Performing ping test...')
ping_result = test.results.ping
print(f'Ping: {ping_result} ms')

#print(f'Download Speed: {download_result/1024/1024:.2f} mb/s')
#print(f'Upload Speed: {upload_result/1024/1024:.2f} mb/s')
#print(f'Ping: {ping_result} ms')
