#this code was inspire on: https://readthedocs.org/projects/selenium-python/downloads/pdf/latest/ (the python selenium docs)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")

assert "Python" in driver.title
# O assert existe na maioria das linguagens de programação e tem sempre a mesma função, garantir uma condição para continuar a execução do código. Caso a condição não seja atendida, uma exceção é disparada, e a execução é interrompida.
 
elem = driver.find_element_by_name("q") #pega uma caixa de pesquisa, você pode confrontar isso utilizando JavaScript no console com o comando document.getElementByName('q')
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.ENTER)

assert "No results found." not in driver.page_source

driver.close()