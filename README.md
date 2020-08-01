<h1>
    <div align='center'>Teste WebJump - Analista de QA</div>
</h1>
<div align='center'>
    <img src="http://img.shields.io/static/v1?label=python%20&message=3.8.3&color=yellow&logo=python"/>
    <img src="http://img.shields.io/static/v1?label=VS Code%20&message=1.47.3&color=blue&logo=visual-studio-code"/>
    <img src="http://img.shields.io/static/v1?label=status%20&message=concluded&color=-green"/>
</div>
</br>

### Índice
- Ferramentas
- Instalação do Selenium WebDriver
- Download e Armazenamento ChromeDriver
- Executando os Testes
- Links

### Ferramentas :wrench:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Para o desenvolvimento desse software, foram utilizadas as ferramentas listadas a seguir:


- Windows 10 Home Single Language
- [Visual Studio Code 1.47.3](https://code.visualstudio.com/download)
- [Python 3.8.3](https://www.python.org/downloads/)
- [ChromeDriver 84.0.4147.30](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- [Selenium WebDriver](https://selenium-python.readthedocs.io/installation.html#)

##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Obs: Clicando sob cada item que contém hiperlink, você será redirecionado para a página de download.

### Instalação do Selenium WebDriver :computer:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Na programação, foi utilizada a biblioteca Selenium WebDriver, pois com ela é possível identificar e manipular os elementos dentro da página. Segue abaixo informações referente à instalação do framework e sua documentação:
- [Selenium WebDriver](https://selenium-python.readthedocs.io/)
O Selenium WebDriver pode ser instalado de diversas maneiras. O método utilizado nesse caso foi seguindo os passos abaixo:
1. Acesse o prompt de comando `'win'` + `'r'`
2. Digite o seguinte comando: `py -m pip install selenium`

##### Obs: Para esse comando funcionar, é necessário que o usuário já tenha instalado em sua máquina o Python 3.8.3

### Executando os Testes :arrow_forward:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Para executar os testes é muito simples, primeiro de tudo, baixe todos os arquivos e armazene-os na mesma pasta. Feito isso, siga os passos a seguir:

1. Instale o Python 3.8.3, para poder executar o programa;
   <div align='center'>
    <img src='DownloadPython.JPG' width=75% height= 75%>
   <div>
2. Instale o Visual Studio Code 1.47.3 no seu computador, para a edição do código;
   <div align='center'>
    <img src='DownloadVSCode.JPG' width=75% height= 75%>
   <div>
3. Abra o arquivo "QA-WebJump.py" com "Visual Studio Code";
   <div align='center'>
    <img src='Etapa3.jpg' width=75% height= 75%>
   <div>
4. Vá até as últimas linhas do código e realize as tarefas conforme comentado.
   ###### Para a realização dos testes, deve-se descomentar a classe e seu respectivo "executa cenário"

    4.1. Para executar o teste 1: 
    ```(Python)
    CB = ClickButtons() #CLASSE DO CENÁRIO 1 
    #CIF = ClickIFrameButtons() #CLASSE DO CENÁRIO 2
    #LS = LastScene() #CLASSE DO CENÁRIO 3
    CB.run() #EXERCUTA CENÁRIO 1
    #CIF.run() #EXECUTA CENÁRIO 2
    #LS.run() #EXECUTA CENÁRIO 3
    ```

    4.2. Para executar o teste 2:
    ```(Python)
    #CB = ClickButtons() #CLASSE DO CENÁRIO 1 
    CIF = ClickIFrameButtons() #CLASSE DO CENÁRIO 2
    #LS = LastScene() #CLASSE DO CENÁRIO 3
    #CB.run() #EXERCUTA CENÁRIO 1
    CIF.run() #EXECUTA CENÁRIO 2
    #LS.run() #EXECUTA CENÁRIO 3
    ```

    4.3. Para executar o teste 3:
    ```(Python)
    #CB = ClickButtons() #CLASSE DO CENÁRIO 1 
    #CIF = ClickIFrameButtons() #CLASSE DO CENÁRIO 2
    LS = LastScene() #CLASSE DO CENÁRIO 3
    #CB.run() #EXERCUTA CENÁRIO 1
    #CIF.run() #EXECUTA CENÁRIO 2
    LS.run() #EXECUTA CENÁRIO 3
    ```


5. Após determinar qual teste será realizado, salve o arquivo "QA-WebJump.py", utilizando o comando `'ctrl'`+`'s'`;
6. Abra-o com o Python e veja o funcionamento do programa com o teste escolhido! 

   <div align='center'>
    <img src='Etapa6.jpg' width=75% height= 75%>
   <div>

### Links :link:

- Tutorial para instalação do Python: https://www.youtube.com/watch?v=UI2OKHxLWfg
- Tutorial para instalação do Visual Studio Code: https://www.youtube.com/watch?v=49K-Zxc8A7A
</br>
Documento desenvolvido em Markdown Markup Language.
