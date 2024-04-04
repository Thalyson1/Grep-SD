# Grep-SD
***Grep - Sistemas distribuidos*** 

Rodando o Script: 


1- Primeiro vá ao diretorio do arquivo




2- no Windows uso o seguinte comando:


```python
    python main.py "palavra que deseja buscar"
```
```python    
    python main.py "([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})" //Comando para pegar cpf
```   
```python
    python main.py "([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})$" //Comando para pegar email
```