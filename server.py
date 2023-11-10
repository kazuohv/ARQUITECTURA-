if __name__=='__main__':
  sock=socket.socket(socket.AF_INET,sock.SOCK_STREAM)
  server_adress=('0.0.0.0',5000)
  print(f"Conectando a servidor {server_address[0]}:{server_address[1]}")
  sock.bind(server_address)
  sock.listen(1)
  while(true):
    print("Esperando conexiones")
    connection, adress=sock.accept
    t=thread(target=client_handler,args=(connection,client_adress))
    t.start
    print("cliente delegado")
