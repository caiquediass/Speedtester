import speedtest

test = speedtest.Speedtest()

print("Carregando a Lista de servidor...")
test.get_servers()
print("Escolhendo o melhor Servidor...")
best = test.get_best_server()

print(f"Encontrado: {best['host']} Localizado Em {best['host']}")

print("Otimizando O Teste De Download...")
download_result = test.download()
print("Otimizando O Teste De Upload...")
upload_result = test.upload()
ping_result = test.results.ping

print(f"Download Velocidade: {download_result / 1024 / 1024:.2f}Mbit/s")
print(f"Upload Velocidade: {upload_result / 1024 / 1024:.2f}Mbit/s")
print(f"Ping: {ping_result}ms")