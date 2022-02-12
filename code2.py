# Encontrando elementos na página
### é importante destacar que os códigos desta seção não resultarão em resultados, eles são apenas um compilado de ações possíves que pode ser feitas acomponhados da sua explicação

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("http://www.python.org")

# imagine o html: <input type="text" name="passwd" id="passwd-id" />
### Formas de encontrar essa tag

element = driver.find_element_by_id("passwd-id")
element = driver.find_element_by_name("passwd")
element = driver.find_element_by_xpath("//input[@id='passwd-id']")
element = driver.find_element_by_css_selector("input#passwd-id")

### comandos úteis para o preenchimento de formulários
select = Select(driver.find_element_by_name('name'))
select.select_by_index('index')
select.select_by_visible_text("text")
select.select_by_value('value')

select = Select(driver.find_element_by_id('id'))
select.deselect_all() #desceleciona todas as opções em um formulário

select = Select(driver.find_element_by_xpath("//select[@name='name']"))
all_selected_options = select.all_selected_options #obtendo todas as opções selecionadas

driver.find_element_by_id("submit").click() #submetendo as opções do formulário marcadas, assumindo que o id delas é submit, ou de maneira mais simples use:
element.submit()



