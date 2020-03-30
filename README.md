# desafio-criptografia
Código utilizando Python para o desafio do Codenation para o programa Acelera Dev.

<h1>Desafio proposto</h1>

<ul>Acesse a página Codenation e obtenha token pessoal gerado pela plataforma;</ul>
<ul>Adicione o token pessoal no URL fornecido (https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=SEU_TOKEN), alterando o campo "SEU_TOKEN" para os caracteres obtidos anteriormente;</ul>
<ul>Faça o download do arquivo json com a mensagem criptografada e o número de algarismos de deslocamento;</ul>
<ul>Escreva um programa, em qualquer linguagem de programação, descriptografe o texto e atualize o arquivo JSON, no campo descriptografado.</ul>
<ul>Use uma função de hash criptográfico SHA-1 para gerar um resumo criptográfico;</ul>
<ul>Envie o arquivo atualizado para revisão via POST na API: https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=SEU_TOKEN</ul>

<h1>Regras</h1>

<ul>As mensagens serão convertidas em minúsculas para criptografia e descriptografia;</ul>
<ul>Os números e pontos serão mantidos.</ul>
<ul>A API espera que um arquivo seja enviado como dados de várias partes / formulário, como se fosse enviado por um formulário HTML, com um campo do tipo arquivo com o nome resposta.</ul>
<ul>O resultado da submissão será sua nota ou o erro correspondente. Você pode enviar quantas vezes for necessário, mas a API não permitirá mais de um envio por minuto.</ul>

<h1>Tecnologia e conhecimentos aplicados</h1> 
 
  <li>Python 3.8 e suas bibliotecas ( Requests, Json e Hashlib)</li> 
  <li>JSON</li> 
  <li>Tabela Unicode</li> 
  <li>Criptografia SHA1</li> 
