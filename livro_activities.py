#name = input("What is your name?\n") 
#print("oi "+ name)


# from logging import exception


# prompt = 'Qual a velocidade rasante de uma andorinha livre??\n' 

# try:
#      velocidade = input(prompt)
#     print(int(velocidade)*2)
# except:
#     print("NaN")
#comand barra para comentar
# 
# import random
# random.randint(5,11)

# import random
# t = [1,2,3,4,5,6,7]
# random.choice(t)


# def print_LetraDeMusica(): 
#     print("Eu sou um lenhador, e eu estou bem.")
#     print("Eu durmo a noite toda e trabalho o dia todo.")

# print_LetraDeMusica()

# def calculoPagamento(horas, TaxaHora):
#     pagamento= horas*TaxaHora
#     print (pagamento)

# calculoPagamento(45, 4.5)


# def computarNotas(nota):

#     if nota< 0.6:
#         print('E')
#     elif nota>= 0.6:
#          print('D') 
#         elif nota>= 0.7:    
#                  print('C') 
#         elif nota>= 0.8:
#                     print('B') 
#         elif nota >= 0.9:
#             print('A')           
#     else:print('erro') 
    
# computarNotas(0.8)


def computarNotas(nota):
 try:
       if nota >= 0.9:
           print('A')
      else: 
      if nota>= 0.8:
        print('B')
            else: 
             if nota>= 0.7:    
               print('C')
            else:
              if nota>= 0.6:
                print('D') 
             else:          
                      if nota< 0.6:
                        print('E')
                      else:print('erro') 
 except:
 print('nãon')
                  
    
computarNotas('no')






